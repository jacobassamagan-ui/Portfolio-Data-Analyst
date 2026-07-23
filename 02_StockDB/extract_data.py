"""
extract_data.py -- Extraction automatisee des donnees boursieres pour StockDB

Objectif
--------
Alimenter la base stockdb.sqlite (cf. create_schema.sql) a partir de donnees
de marche reelles, via l'API publique Yahoo Finance (librairie yfinance).

Ce script est concu pour tourner seul, de maniere recurrente (cron / tache
planifiee), sans intervention manuelle : c'est la piece qui transforme
StockDB d'un exercice ponctuel en un vrai pipeline de donnees.

Pourquoi deux fonctions d'extraction separees (fondamentaux vs cours) ?
------------------------------------------------------------------------
Les deux types de donnees n'ont pas la meme frequence de mise a jour utile :
- Les cours de cloture changent chaque jour de bourse -> extraction quotidienne.
- Les fondamentaux (P/E, dividende, capitalisation) changent lentement
  -> une extraction hebdomadaire ou mensuelle suffit, et sur-extraire ne fait
  qu'ajouter du bruit et des appels API inutiles.
Cette separation reflete directement le schema de StockDB, qui a deux tables
distinctes (cours et indicateurs_financiers) pour cette meme raison.

Usage
-----
    python extract_data.py --cours
    python extract_data.py --fondamentaux
    python extract_data.py --cours --fondamentaux
    python extract_data.py --tickers AAPL MSFT

Dependances
-----------
    pip install yfinance pandas

Planification recommandee (exemple crontab Linux, extraction quotidienne a 22h) :
    0 22 * * 1-5  cd /chemin/vers/projet && python extract_data.py --cours
    0 22 * * 1    cd /chemin/vers/projet && python extract_data.py --fondamentaux
"""

import argparse
import logging
import sqlite3
from datetime import date

import pandas as pd

try:
    import yfinance as yf
except ImportError:
    yf = None  # le script reste lisible/testable sans la dependance installee

DB_PATH = "stockdb.sqlite"

TICKERS_SUIVIS = {
    "AAPL": ("Apple Inc.", "Technologie", "US"),
    "MSFT": ("Microsoft Corp.", "Technologie", "US"),
    "TTE":  ("TotalEnergies", "Energie", "Europe"),
    "XOM":  ("Exxon Mobil", "Energie", "US"),
    "SAN":  ("Sanofi", "Sante", "Europe"),
    "JNJ":  ("Johnson & Johnson", "Sante", "US"),
    "BNP":  ("BNP Paribas", "Finance", "Europe"),
    "JPM":  ("JPMorgan Chase", "Finance", "US"),
    "MC":   ("LVMH", "Consommation", "Europe"),
    "KO":   ("Coca-Cola", "Consommation", "US"),
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def extraire_fondamentaux(tickers):
    """Recupere P/E, rendement du dividende et capitalisation pour chaque ticker.

    Une ligne par ticker, horodatee a la date d'extraction (date du jour).
    """
    if yf is None:
        raise RuntimeError("yfinance n'est pas installe : pip install yfinance")

    lignes = []
    aujourdhui = date.today().isoformat()

    for ticker in tickers:
        try:
            info = yf.Ticker(ticker).info
        except Exception as exc:
            logger.warning("Echec extraction fondamentaux pour %s : %s", ticker, exc)
            continue

        lignes.append({
            "ticker": ticker,
            "date_extraction": aujourdhui,
            "pe_ratio": info.get("trailingPE"),
            "dividende_rendement": info.get("dividendYield"),
            "capitalisation": info.get("marketCap"),
        })
        logger.info("Fondamentaux recuperes pour %s", ticker)

    return pd.DataFrame(lignes)


def extraire_cours(tickers, periode="5d"):
    """Recupere l'historique des cours de cloture et volumes, au format long
    (Date | Ticker | Cours_Cloture | Volume) -- meme convention que MarketPulse.

    periode : fenetre yfinance ("5d", "1mo", "6mo", "1y", "max"...).
    Une fenetre courte (ex. "5d") suffit pour une execution quotidienne :
    on ne recupere que les jours recents, la table SQL portant deja
    l'historique complet (cf. contrainte UNIQUE(ticker, date_cours) qui
    empeche les doublons en cas de chevauchement).
    """
    if yf is None:
        raise RuntimeError("yfinance n'est pas installe : pip install yfinance")

    lignes = []
    for ticker in tickers:
        try:
            hist = yf.Ticker(ticker).history(period=periode)
        except Exception as exc:
            logger.warning("Echec extraction cours pour %s : %s", ticker, exc)
            continue

        for idx, row in hist.iterrows():
            lignes.append({
                "ticker": ticker,
                "date_cours": idx.strftime("%Y-%m-%d"),
                "cours_cloture": round(float(row["Close"]), 2),
                "volume": int(row["Volume"]),
            })
        logger.info("Cours recuperes pour %s (%d jours)", ticker, len(hist))

    return pd.DataFrame(lignes)


def charger_dans_sqlite(df_cours, df_fond, db_path=DB_PATH):
    """Insere les nouvelles lignes dans stockdb.sqlite.

    INSERT OR IGNORE s'appuie sur les contraintes UNIQUE(ticker, date_cours) et
    UNIQUE(ticker, date_extraction) du schema : relancer le script plusieurs
    fois dans la meme journee ne cree jamais de doublons.
    """
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    if df_cours is not None and not df_cours.empty:
        cur.executemany(
            "INSERT OR IGNORE INTO cours (ticker, date_cours, cours_cloture, volume) "
            "VALUES (:ticker, :date_cours, :cours_cloture, :volume)",
            df_cours.to_dict("records"),
        )
        logger.info("Lignes de cours traitees : %d (doublons ignores automatiquement)", len(df_cours))

    if df_fond is not None and not df_fond.empty:
        cur.executemany(
            "INSERT OR IGNORE INTO indicateurs_financiers "
            "(ticker, date_extraction, pe_ratio, dividende_rendement, capitalisation) "
            "VALUES (:ticker, :date_extraction, :pe_ratio, :dividende_rendement, :capitalisation)",
            df_fond.to_dict("records"),
        )
        logger.info("Lignes de fondamentaux traitees : %d (doublons ignores automatiquement)", len(df_fond))

    conn.commit()
    conn.close()


def main():
    parser = argparse.ArgumentParser(description="Extraction StockDB (yfinance -> SQLite)")
    parser.add_argument("--cours", action="store_true", help="Extraire les cours du jour")
    parser.add_argument("--fondamentaux", action="store_true", help="Extraire les fondamentaux")
    parser.add_argument("--periode", default="5d", help="Fenetre yfinance pour les cours (defaut : 5d)")
    parser.add_argument(
        "--tickers", nargs="+", default=list(TICKERS_SUIVIS.keys()),
        help="Sous-ensemble de tickers a traiter (defaut : tous les tickers suivis)",
    )
    parser.add_argument("--db", default=DB_PATH, help="Chemin vers stockdb.sqlite")
    args = parser.parse_args()

    if not args.cours and not args.fondamentaux:
        parser.error("Preciser au moins --cours ou --fondamentaux")

    df_cours = extraire_cours(args.tickers, args.periode) if args.cours else None
    df_fond = extraire_fondamentaux(args.tickers) if args.fondamentaux else None

    charger_dans_sqlite(df_cours, df_fond, db_path=args.db)
    logger.info("Extraction terminee.")


if __name__ == "__main__":
    main()
