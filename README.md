# Présentation 

Chaque année depuis 2016, l'Université de Lille publie l'enquête 'ODIF' sur l'insertion professionels de ses jeunes diplômés de master. 
A ce titre un sondage est réalisé plus d'un an après l'obtention du diplôme afin de récolter des informations sur les ex-étudiants. 
Ces données sont publiées et consultables librement sur le site https://odif.univ-lille.fr/repertoires-demplois/master/. 

L'objectif de ce projet est de travailler cette base très riche pour construire un modèle d'IA prédictive capable de répondre à la question suivante : 
"L'ex diplômé exerçant un emploi à temps plein perçoit-il un salaire supérieur à la médiane de référence pour l'année du sondage ?"

Ce modèle peut s'avérer très intéressant, notamment pour des étudiants qui envisageraient tel ou tel projet de carrière mais qui auraient du mal à se projeter 
sur le niveau de rémunération associé à cette dernière. 
Par exemple grâce à ce modèle, un étudiant qui envisage de faire le master X pour occuper l'emploi Y dans le secteur d'activité Z peut se projeter sur le niveau
de stabilité financière que permet ce projet. 

Ce modèle est construit dans le cadre du cours de Machine Learning en M2 SIAD Data sciences à l'Université de Lille. 
Les consignes de ce projet sont de : 

- Construire un modèle de classification en mobilisant nos compétences en Machine Learning
- Exploiter une base de donnée open source
- Répondre à une problématique innovante, encore jamais traité en Machine Learning (par ex en évitant les bases Kaggle)

## Généralités 

- Auteurs : Roman Delbare et Josue Kanteng-A-Mukoj 
- Source des donnnées : https://odif.univ-lille.fr/repertoires-demplois/master/ 
- Date de téléchargement : 15/11/2026 

## Dictionnaire de données 

- mention (string) : Intitulé général du diplôme ou du domaine d'études (ex. Arts, Histoire).
- parcours (string) : Spécialisation précise suivie au sein de la mention.
- promotion (int) : Année d'obtention du diplôme.
- situation (string) : Date de référence à laquelle la situation professionnelle est observée (ex. 1er décembre 2021).
- diplome (string) : Régime d'inscription du diplômé (FI : Formation Initiale ; FCRE : Formation Continue / Reprise d'études).
- n_interroges (int) : Nombre total de diplômés sollicités pour l'enquête au sein du parcours et de la promotion.
- taux_reponse (float) : Pourcentage de diplômés ayant répondu à l'enquête.
- n_total_repondants (int) : Nombre total de réponses exploitables recueillies pour la cohorte.
- n_en_emploi (int) : Nombre de répondants en activité professionnelle à la date d'observation.
- n_recherche_emploi (int) : Nombre de répondants en recherche active d'emploi.
- n_en_etudes (int) : Nombre de répondants en poursuite d'études.
- n_autre_situation (int) : Nombre de répondants dans une autre situation (inactivité, service civique, année sabbatique, etc.).
- n_emploi_stable (int) : Nombre de répondants occupant un emploi considéré comme stable (CDI, fonctionnaire, indépendant, etc.).
- n_emploi_non_stable (int) : Nombre de répondants occupant un emploi non stable (CDD, intérim, vacation, etc.).
- effectif_insuffisant (bool) : Indicateur signalant si le volume de répondants de la cohorte est jugé statistiquement trop faible pour être représentatif.
- intitule_emploi (string) : Libellé exact du poste occupé par le répondant.
- missions (string) : Description textuelle des tâches et responsabilités principales exercées dans le poste.
- categorie_emploi (string) : Catégorie socioprofessionnelle du poste (Cadre, Prof. interm., Employé ou ouvrier).
- type_emploi (string) : Qualification de la stabilité contractuelle du poste (Stable ou Non stable).
- emploi_stable (bool) : Équivalent booléen de type_emploi (True si emploi stable, False sinon).
- temps_partiel (bool) : Indique si l'emploi est exercé à temps partiel (True) ou à temps plein (False).
- revenu_net (float) : Rémunération mensuelle nette déclarée par le répondant (en euros).
- secteur_employeur (string) : Nature juridique de l'organisme employeur (Public, Privé, Associatif).
- activite_employeur (string) : Secteur d'activité économique de l'employeur (ex. Enseignement, Commerce, Administration publique).
- lieu_emploi (string) : Zone géographique d'exercice de l'activité professionnelle (ex. Métropole Européenne de Lille, Île-de-France, Étranger).
- autre_diplome (string) : Éventuel diplôme complémentaire obtenu ou préparé après la formation enquêtée.