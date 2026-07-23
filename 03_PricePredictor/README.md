# PricePredictor — Machine Learning appliqué à la prédiction de cours

**Data Analyst spécialisé en Finance, Business Intelligence et Aide à la décision**

> Ce projet répond à une question qu'un investisseur particulier se pose souvent face au marketing "l'IA prédit la bourse" : est-ce que ça marche vraiment, et à quel prix ?

## Le problème métier

Beaucoup de contenus vendent l'idée qu'un modèle de Machine Learning peut prédire fiablement les cours boursiers. Ce projet teste cette promesse avec rigueur plutôt que de la prendre pour acquise — et documente honnêtement ce qui marche, ce qui ne marche pas, et pourquoi.

## La démarche (3 notebooks séquentiels)

1. **`exploration.ipynb`** — test de stationnarité (ADF) et autocorrélation (ACF/PACF) sur les rendements journaliers : justifie pourquoi on modélise les rendements plutôt que les prix bruts.
2. **`modelisation.ipynb`** — comparaison d'une baseline naïve, d'une régression linéaire et d'un Random Forest, avec split temporel strict (jamais de mélange aléatoire sur une série temporelle).
3. **`backtest.ipynb`** — simulation d'une stratégie d'allocation basée sur les prédictions, frais de transaction inclus, comparée à un simple "acheter et garder".

## Résultats clés (sur données simulées, échantillon réduit)

| Étape | Résultat |
|---|---|
| Stationnarité | Cours brut non stationnaire (p = 0,696) ; rendements stationnaires (p < 0,0001) |
| Modélisation | Random Forest : RMSE légèrement meilleur que la baseline ; régression linéaire : moins bonne que la baseline |
| Backtesting (12 jours de test) | Stratégie Random Forest : +0,94 % frais inclus vs -0,99 % pour acheter-et-garder |

## Conclusion honnête

Un modèle simple peut capter un signal marginal sur des données financières, mais ce signal est faible, instable sur un petit échantillon, et sensible aux coûts de transaction. **L'intérêt de ce projet est méthodologique — savoir construire et évaluer un pipeline de prédiction correctement — plutôt qu'opérationnel.**

## Stack technique

`Python (statsmodels, scikit-learn)` · `Statistiques de séries temporelles` · `Machine Learning (régression, Random Forest)` · `Validation temporelle` · `Backtesting`

## Limites

- Échantillon simulé et réduit (79 jours de cours, 12 jours de test) — une vraie validation nécessiterait plusieurs années de données réelles et une validation croisée temporelle (walk-forward).
- Le backtest porte sur une seule fenêtre de 12 jours : aucune valeur de preuve statistique, valeur illustrative de méthode uniquement.
- Ce projet ne constitue en aucun cas un conseil en investissement ni une stratégie de trading prête à l'emploi.

## Fichiers

- `exploration.ipynb` — stationnarité, autocorrélation
- `modelisation.ipynb` — baseline, régression linéaire, Random Forest, évaluation
- `backtest.ipynb` — simulation de stratégie vs buy-and-hold, coûts de transaction

---

*Projet réalisé dans le cadre de la construction d'un portfolio Data Analyst — JACOBOFX · linkedin.com/in/jacobofx · jacobofx.carrd.co*
