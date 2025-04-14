---
layout: post
date: 2025-04-14
title: "Splunk et les TCD"
categories:
    - quicky
    - splunk
    - SIEM
    - SOC
---
Quand on a un Splunk comme puits de logs, il est parfois utile de faire des tableaux croisés dynamiques (TCD) pour 
analyser rapidement les données.
On va voir ici un exemple de TCD sur Splunk, mais il y a plein d'autres outils qui permettent de faire des TCD,
comme Excel, Google Sheets, etc.


## Exemple de TCD sur Splunk :

```splunk
index=main RequestPath NOT  ("/realpath" OR "/authentication") | where RequestPath !="/" | stats count by 
HttpStatus, RequestPath, ip | xyseries HttpStatus,  RequestPath, count
```

## Explication

Ici, on va chercher dans l'index main, toutes les requêtes qui ne contiennent pas `"/realpath"` ou 
`"/authentication"`, et qui ne sont pas la racine (`"/"`). Ensuite, on va compter le nombre de requêtes par statut HTTP, chemin de la requête et
adresse IP. Enfin, on va transformer le résultat en un tableau croisé dynamique (TCD) avec `xyseries`, où les statuts
HTTP seront sur l'axe des abscisses, les chemins de requête sur l'axe des ordonnées et le nombre de requêtes sera la
valeur dans le tableau.

et ca donne cela : 
![img.png]({{home}}/assets/img/tcdsplunk.png)

