# StockDB — Screener d'actions automatisé

**Data Analyst spécialisé en Finance, Business Intelligence et Aide à la décision**

> Un pipeline qui automatise une tâche que tout investisseur particulier suivant plusieurs actions fait manuellement : centraliser les cours et les fondamentaux dispersés sur plusieurs sites pour repérer rapidement les opportunités.

## Le problème métier

Un investisseur qui suit une trentaine d'actions passe des heures chaque semaine à consulter Yahoo Finance action par action pour vérifier si certaines sont devenues intéressantes (P/E bas, dividende correct, momentum positif). Aucun outil ne centralise ce suivi automatiquement.

## La démarche

1. **Modélisation** — schéma relationnel en 4 tables (`entreprises`, `secteurs`, `cours`, `indicateurs_financiers`), pensé pour refléter deux fréquences de mise à jour différentes (cours quotidiens vs fondamentaux mensuels).
2. **Extraction** — script Python (`extract_data.py`) réutilisable, conçu pour tourner seul via une tâche planifiée (cron), avec gestion des doublons et des échecs partiels.
3. **Requêtage** — 4 requêtes SQL couvrant des cas d'usage réels : classement sectoriel (fonctions de fenêtrage), screener multi-critères, suivi jour par jour (`LAG`), performance sectorielle (auto-jointure).
4. **Visualisation** — notebook Python avec graphiques commentés pour chaque requête.

## Résultats clés (sur données simulées)

| Requête | Résultat |
|---|---|
| Top performer secteur Énergie (30j) | Exxon Mobil (+14,9 %) |
| Screener P/E < 15 + dividende > 3 % | BNP Paribas, TotalEnergies, Sanofi, Exxon Mobil |
| Secteur le plus dynamique (30j) | Consommation (+4,2 %) |

## Stack technique

`SQL (SQLite — fenêtrage, CTE, LAG/RANK)` · `Python (yfinance, pandas)` · `Modélisation relationnelle` · `Automatisation (cron)`

## Limites

- Les données de ce dépôt sont simulées à des fins de démonstration — elles ne doivent jamais être présentées comme des cours réels.
- Le screener utilise deux critères simples (P/E, dividende) ; une version plus poussée croiserait dette, croissance du chiffre d'affaires et comparaison intra-sectorielle plutôt qu'absolue.
- Ce projet ne constitue pas un conseil en investissement réglementé.

## Reproduire ce projet

1. `sqlite3 stockdb.sqlite < create_schema.sql`
2. `pip install yfinance pandas` puis `python extract_data.py --cours --fondamentaux`
3. Ouvrir `requetes_analyse.ipynb` pour explorer les résultats

## Fichiers

- `create_schema.sql` — schéma relationnel (4 tables, contraintes d'unicité, index)
- `stockdb.sqlite` — base peuplée (données simulées, cohérentes avec MarketPulse)
- `extract_data.py` — script d'extraction réel (yfinance), prêt pour une tâche planifiée
- `requetes_analyse.ipynb` — 4 requêtes commentées + visualisations Python

---

*Projet réalisé dans le cadre de la construction d'un portfolio Data Analyst — JACOBOFX · linkedin.com/in/jacobofx · jacobofx.carrd.co*
