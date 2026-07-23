# Scripts oraux — Présentation du portfolio en entretien

**Data Analyst spécialisé en Finance, Business Intelligence et Aide à la décision**

Ces scripts sont des trames, pas des textes à réciter mot pour mot. Le but : que tu retiennes la structure et les chiffres clés, puis que tu les dises avec tes propres mots. Un recruteur sent immédiatement un texte appris par cœur — ce qui inspire confiance, c'est de sentir que tu comprends ce que tu racontes.

**Règle commune aux trois scripts :** toujours finir par une limite ou une nuance, jamais par un chiffre qui sonne comme une promesse. C'est la marque de fabrique de tout ce portfolio.

---

## Pitch d'ouverture (30 secondes, si on te demande de te présenter)

> "Je suis en formation Data Analyst, et je me suis spécialisé sur un axe précis : Finance, Business Intelligence et aide à la décision. Plutôt que de faire des projets isolés, j'ai construit un portfolio de trois projets qui se répondent : un outil de suivi de portefeuille en Excel et Power BI, un screener d'actions automatisé en SQL et Python, et un projet de Machine Learning qui teste honnêtement si on peut vraiment prédire les cours de bourse. Je peux vous montrer celui qui vous intéresse le plus, ou vous les présenter dans l'ordre — comme vous préférez."

Cette dernière phrase est volontaire : elle redonne la main au recruteur plutôt que de dérouler un monologue de 6 minutes sans respiration.

---

## 1. MarketPulse (Excel, Power BI, DAX)

**Durée cible : 2 à 3 minutes**

> "Le premier projet part d'un cas concret : un investisseur particulier qui gère son portefeuille lui-même, dans un Excel basique, sans vraie visibilité sur trois choses — est-ce que son portefeuille est trop concentré, est-ce que le risque qu'il prend est compensé par le rendement, et est-ce qu'il fait mieux qu'un simple indice comme le CAC 40.
>
> J'ai construit un classeur Excel structuré — données brutes, calculs, synthèse — avec les indicateurs qu'on utilise en finance : rendement annualisé, volatilité, ratio de Sharpe, bêta, corrélations entre positions. Ensuite j'ai maquetté un dashboard Power BI en quatre pages, avec les mesures DAX qui vont derrière, et j'ai terminé par un rapport de synthèse et une présentation, comme si je livrais vraiment cette mission à un client.
>
> Sur les données que j'ai utilisées pour la démonstration, le portefeuille affichait un rendement de +21,9 % contre +2,3 % pour le CAC 40 — mais avec une volatilité plus élevée, ce que j'ai bien mis en avant : une surperformance ne veut rien dire si on ne dit pas à quel prix en risque. Et surtout, un tiers du portefeuille reposait sur un seul secteur, la technologie — c'est le genre de risque qu'on ne voit pas dans un suivi Excel classique, mais qui saute aux yeux dès qu'on structure l'analyse.
>
> Ce que je voulais montrer avec ce projet, c'est que je ne me contente pas de faire des graphiques : je pars d'une vraie question métier, et je finis par des recommandations concrètes, chiffrées, qu'un client peut utiliser pour décider."

**Si on te demande "pourquoi Power BI et pas juste Excel ?" :**
> "Excel me sert à construire et vérifier les calculs, mais Power BI permet à un client de filtrer lui-même par action ou par période sans dépendre de moi à chaque question — les mesures DAX se recalculent automatiquement selon ses filtres, alors qu'en Excel le chiffre reste figé au moment du calcul."

---

## 2. StockDB (SQL, Python)

**Durée cible : 2 à 3 minutes**

> "Le deuxième projet part d'un problème différent, plus opérationnel : un investisseur qui suit une trentaine d'actions et qui passe des heures chaque semaine à vérifier, action par action, si certaines sont devenues intéressantes — un P/E bas, un dividende correct, une bonne dynamique récente.
>
> J'ai construit un pipeline complet : un schéma de base de données relationnelle avec quatre tables, un script Python qui va chercher les données via l'API Yahoo Finance et qui est pensé pour tourner seul, automatiquement, via une tâche planifiée. Et ensuite des requêtes SQL qui répondent à des vraies questions : quelles sont les meilleures actions de chaque secteur sur le dernier mois, quelles actions sont sous-évaluées avec un bon dividende, comment évolue une action jour après jour.
>
> Ce que je veux mettre en avant sur ce projet, ce sont deux choses. D'abord, la modélisation : j'ai séparé les cours, qui changent tous les jours, des données fondamentales comme le P/E, qui changent beaucoup moins souvent — ça évite de sur-extraire inutilement. Ensuite, les requêtes elles-mêmes utilisent des fonctions de fenêtrage — ROW_NUMBER, RANK, LAG — donc pas de simples SELECT basiques, mais des requêtes qui répondent vraiment à des questions d'analyse temporelle.
>
> Sur mes données de test, le screener a identifié en une seule requête quatre actions sous-évaluées avec un bon dividende — un travail qui, fait à la main, prendrait facilement une heure chaque semaine."

**Si on te demande "pourquoi SQLite et pas une vraie base de production ?" :**
> "Pour un projet de portfolio, SQLite évite la complexité d'un serveur à maintenir, mais le schéma et les requêtes sont écrits pour être portables — je pourrais migrer vers PostgreSQL sans changer la logique, juste la connexion."

---

## 3. PricePredictor (Machine Learning)

**Durée cible : 3 minutes — c'est le projet qui demande le plus de nuance à l'oral**

> "Le troisième projet répond à une question qu'on entend beaucoup : est-ce que l'intelligence artificielle peut vraiment prédire la bourse ? Plutôt que de partir du principe que oui, j'ai voulu tester ça avec rigueur, en trois étapes.
>
> D'abord, une exploration statistique : j'ai vérifié si les rendements d'une action se comportent de façon stationnaire, avec un test ADF, et j'ai regardé leur autocorrélation. Résultat : sur mon échantillon, les rendements se comportent quasiment comme du bruit — il n'y a pas beaucoup de structure à exploiter, statistiquement parlant.
>
> Ensuite, j'ai quand même testé trois approches : une baseline naïve — je prédis que rien ne change —, une régression linéaire, et une random forest, avec des variables comme les rendements décalés, la volatilité récente et le volume. Résultat honnête : la régression linéaire fait moins bien que la baseline naïve. La random forest fait un peu mieux, mais sur un échantillon de seulement douze observations de test — donc rien de statistiquement solide.
>
> Enfin, j'ai fait un backtesting : est-ce que suivre les prédictions du modèle, frais de transaction inclus, aurait fait mieux qu'un simple 'acheter et garder' ? Sur cette fenêtre précise, oui, légèrement. Mais je le dis clairement dans mon rapport : un seul test sur douze jours ne prouve rien.
>
> Ma conclusion, et c'est celle que je veux vraiment faire passer : l'intérêt de ce projet est méthodologique, pas opérationnel. Je voulais montrer que je sais construire un pipeline de prédiction correctement — split temporel, comparaison à une baseline, backtesting avec les coûts — et surtout que je sais dire honnêtement quand un modèle n'apporte pas grand-chose de fiable, plutôt que de vendre un résultat qui sonne bien."

**Si on te demande "donc ça ne marche pas, ton modèle ?" :**
> "Il capte un signal marginal, mais sur un échantillon bien trop petit pour en tirer une conclusion fiable. Ce n'est pas un échec du projet — c'est exactement la conclusion attendue quand on modélise des rendements qui se comportent comme du bruit. Le vrai risque, ça aurait été de forcer un résultat impressionnant en surapprenant sur un petit échantillon."

**Si on te demande "qu'est-ce que tu ferais différemment avec plus de temps ou de vraies données ?" :**
> "Plusieurs années d'historique réel, une validation croisée temporelle plutôt qu'un split unique, et tester sur plusieurs titres et secteurs plutôt qu'une seule action — pour voir si le signal se retrouve ailleurs ou si c'était spécifique à ce cas."

---

## Questions transverses à anticiper (sur l'ensemble du portfolio)

**"Pourquoi des données simulées et pas de vraies données ?"**
> "Pour ce portfolio, je voulais pouvoir montrer une méthode complète et cohérente sans dépendre de la disponibilité ou de la licence de données réelles. Le script `extract_data.py` du projet StockDB est écrit pour se brancher directement sur des données réelles via l'API Yahoo Finance — la structure ne change pas, seule la source change."

**"Quel projet préfères-tu ?"**
> Réponds sincèrement, mais relie toujours ta préférence à une compétence : *"MarketPulse, parce que c'est celui qui se rapproche le plus d'une vraie mission client de bout en bout"* ou *"PricePredictor, parce qu'il m'a forcé à être rigoureux plutôt que de sortir un résultat flatteur."*

**"Es-tu disponible pour une mission courte ?"**
> C'est le moment de rebondir vers ton offre packagée et ta disponibilité — pas dans ce document, mais aie ta réponse prête (durée, tarif indicatif, disponibilité).

---

## Conseil final pour l'oral

Ne récite pas ces scripts. Entraîne-toi à voix haute 2-3 fois, puis pose le document et reformule avec tes mots — un recruteur retient beaucoup plus l'histoire et les chiffres clés (21,9 %, 29,9 %, les douze observations de test) que des phrases parfaites. Le naturel et l'honnêteté sur les limites comptent plus que la fluidité.
