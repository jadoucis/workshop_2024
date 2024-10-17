# workshop_2024 - CleanNet IA

## Description ##

CleanNet AI est une extension Chrome visant à améliorer l’expérience des utilisateurs sur les réseaux sociaux en floutant automatiquement les contenus problématiques, 
tels que les discours haineux, le cyberharcèlement et la désinformation.

## Fonctionnalités ##

- Détection automatique des contenus inappropriés.
- Floutage des textes jugés problématiques.
- Possibilité de visualiser le contenu flouté en cliquant sur un bouton.
- Personnalisation des niveaux de filtrage dans les options de l'extension.

## Installation ##

Pour installer l'extension CleanNet IA :

Clonez ou téléchargez le projet depuis GitHub :

git clone https://github.com/username/CleanNet-IA.git

Charger l'extension dans Chrome :

Allez sur chrome://extensions/.

Activez le mode développeur (coin supérieur droit).

Cliquez sur Charger l'extension non empaquetée et sélectionnez le dossier contenant les fichiers de l'extension.

L'extension sera maintenant visible dans la barre d'outils de votre navigateur.

## Utilisation ##

1 - Lancer un réseau social comme par exemple Facebook ou X etc.
2 - Si du contenu inapproprié est détecté, il sera automatiquement flouté.
3 - L’utilisateur peut cliquer sur un bouton “Afficher le contenu” pour voir le contenu flouté.

## Architecture de l'Extension ##

- manifest.json : Contient la configuration principale et les permissions nécessaires.
- contentScript.js : Script injecté dans les pages de réseaux sociaux pour analyser le contenu et appliquer le floutage.
- popup.js : Interface utilisateur du popup de l'extension, permettant de configurer les paramètres.


## Sécurité et Confidentialité ##

CleanNet IA prend la sécurité et la protection des données très au sérieux. L'extension suit les recommandations RGPD et ne stocke pas de données personnelles inutiles.

Les contenus analysés ne sont jamais stockés sur des serveurs tiers.

Toutes les communications entre l'extension et les APIs sont chiffrées.

## Technologies Utilisées ##

JavaScript (ES6) : Pour la logique principale de l'extension.

Chrome Extension API : Pour l'interaction avec les pages Web.

Bibliothèques NLP : Utilisation de modèles pré-entraînés pour analyser le contenu.

## Contribuer ##

Les contributions sont les bienvenues ! Voici comment vous pouvez aider :

Forkez le dépôt.

Créez une branche pour votre fonctionnalité ou correction de bug :

git checkout -b ma-branche-fonctionnalite

Soumettez une pull request une fois les modifications effectuées.

Merci de lire le fichier CONTRIBUTING.md avant de contribuer.

## Mises en Garde et Limites ##

CleanNet IA utilise des modèles de traitement du langage naturel pour détecter les contenus problématiques. Il peut y avoir des faux positifs ou des faux négatifs.

L’extension fonctionne uniquement sur des plateformes prises en charge, comme Facebook et Twitter.

## Licence ##

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

Contact

Pour toute question ou suggestion, n'hésitez pas à contacter l'équipe de développement :

Email : contact@cleannetia.com

GitHub Issues : 
