-- StockDB — Schéma relationnel
-- Base de données de suivi et screener d'actions
-- Compatible SQLite (fonctions de fenêtrage disponibles depuis SQLite 3.25+)

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS indicateurs_financiers;
DROP TABLE IF EXISTS cours;
DROP TABLE IF EXISTS entreprises;
DROP TABLE IF EXISTS secteurs;

-- Table de dimension : secteurs d'activité
CREATE TABLE secteurs (
    secteur         TEXT PRIMARY KEY,
    description     TEXT
);

-- Table de dimension : entreprises suivies
CREATE TABLE entreprises (
    ticker          TEXT PRIMARY KEY,
    nom             TEXT NOT NULL,
    secteur         TEXT NOT NULL,
    zone            TEXT NOT NULL,
    FOREIGN KEY (secteur) REFERENCES secteurs(secteur)
);

-- Table de faits : historique des cours (mise à jour quotidienne)
CREATE TABLE cours (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker          TEXT NOT NULL,
    date_cours      DATE NOT NULL,
    cours_cloture   REAL NOT NULL,
    volume          INTEGER,
    FOREIGN KEY (ticker) REFERENCES entreprises(ticker),
    UNIQUE(ticker, date_cours)
);

-- Table de faits : indicateurs fondamentaux (mise à jour peu fréquente)
CREATE TABLE indicateurs_financiers (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker                  TEXT NOT NULL,
    date_extraction         DATE NOT NULL,
    pe_ratio                REAL,
    dividende_rendement     REAL,
    capitalisation          REAL,
    FOREIGN KEY (ticker) REFERENCES entreprises(ticker),
    UNIQUE(ticker, date_extraction)
);

-- Index pour accélérer les requêtes fréquentes (filtrage par ticker/date)
CREATE INDEX idx_cours_ticker_date ON cours(ticker, date_cours);
CREATE INDEX idx_indic_ticker_date ON indicateurs_financiers(ticker, date_extraction);
