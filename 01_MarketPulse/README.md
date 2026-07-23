# MarketPulse — Suivi et aide à la décision pour un portefeuille boursier

**Data Analyst spécialisé en Finance, Business Intelligence et Aide à la décision**

> Un outil qui répond à une question simple qu'un investisseur particulier se pose rarement avec des chiffres à l'appui : *"Mon portefeuille est-il bien construit, ou est-ce que je prends des risques inutiles pour un rendement médiocre ?"*

---

## Le problème métier

Un investisseur particulier gère un portefeuille de ~45 000 € depuis plusieurs années, en suivant ses positions "au feeling" dans un tableau Excel basique. Il n'a aucune visibilité claire sur trois points :

- Son portefeuille est-il trop concentré sur certains secteurs ?
- Le risque qu'il prend est-il compensé par un rendement suffisant ?
- Fait-il mieux qu'un simple placement indiciel (CAC 40) ?

## La démarche

1. **Cadrage** — rédaction d'une note de cadrage simulant un vrai brief client, pour partir d'un besoin plutôt que d'un exercice technique.
2. **Excel** — construction d'un classeur structuré (données brutes → calculs → synthèse) avec Power Query et les indicateurs financiers clés : rendement annualisé, volatilité, ratio de Sharpe, drawdown maximum, bêta, matrice de corrélation.
3. **Power BI** — maquette de dashboard en 4 pages : vue d'ensemble, analyse du risque, zoom par actif, recommandations — avec les mesures DAX correspondantes (dont des mesures texte dynamiques pour générer les recommandations automatiquement).
4. **Recommandations** — traduction des chiffres en décisions concrètes, pas juste des graphiques.

## Résultats clés (sur données simulées)

| Indicateur | Valeur |
|---|---|
| Rendement annualisé du portefeuille | +21,9 % |
| Rendement CAC 40 (même période) | +2,3 % |
| Ratio de Sharpe du portefeuille | 0,79 |
| Concentration sectorielle maximale | Technologie, 29,9 % |
| Position la moins efficiente (Sharpe) | Sanofi (-2,37) |

**Recommandation générée automatiquement (extrait) :**
> "Le secteur Technologie représente 29,9 % du portefeuille, la plus forte concentration sectorielle. Une correction sur ce secteur aurait un impact disproportionné sur la valeur totale."

## Stack technique

`Excel (Power Query, fonctions financières avancées)` · `Power BI (DAX, Time Intelligence)` · `Statistiques descriptives` · `Modélisation de données (schéma en étoile simplifié)`

## Limites de l'analyse

- Les données de ce dépôt sont **simulées** (marche aléatoire calibrée par secteur) à des fins de démonstration — elles ne doivent jamais être présentées comme des cours réels.
- L'analyse s'appuie sur des données historiques ; elle ne prédit pas les performances futures.
- Le calcul de volatilité du portefeuille est une approximation pondérée (une version rigoureuse intégrerait la matrice de covariance complète).
- Ce projet ne constitue pas un conseil en investissement réglementé.

## Reproduire ce projet

1. Cloner ce dépôt
2. Ouvrir `MarketPulse_template.xlsx` — l'onglet `Positions` est le seul à modifier manuellement (cellules bleues sur fond jaune)
3. Remplacer les données de l'onglet `Cours_Bruts` par de vraies données (export Yahoo Finance ou script `yfinance`) en conservant le format long (`Date | Ticker | Cours_Cloture | Volume`)
4. Recalculer le classeur (Excel/LibreOffice) — tous les autres onglets se mettent à jour automatiquement
5. Connecter Power BI aux mêmes tables pour reproduire les 4 pages du dashboard

## Fichiers

- `MarketPulse_template.xlsx` — classeur complet (données, calculs, synthèse, recommandations)
- `dax_measures.md` — mesures DAX pour reproduire le dashboard Power BI
- `note_de_cadrage.md` — exemple de note de cadrage envoyée avant une mission

---

*Projet réalisé dans le cadre de la construction d'un portfolio Data Analyst — JACOBOFX · linkedin.com/in/jacobofx · jacobofx.carrd.co*
