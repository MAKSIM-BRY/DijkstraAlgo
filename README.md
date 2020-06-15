# DijkstraAlgo

Mise en place de l'algorithme de DijkstraAlgo

### Dataset:
Pour faire fonctionné l'algorithme, le code à besoin d'un dataset sous cette forme:
```json
  {
    "A": {
        "B": 9,
        "C": 20,
        "D": 17
    },
    "B": {
        "E": 30
    },
    "C": {
        "F": 40
    },
    "D": {
        "G": 50
    },
    "E": {
        "F": 2
    },
    "F": {},
  }
```
De manière à ce que pour chaque noeud il y est la liste des noeuds connectés et leurs longueurs.<br> 
<img src="https://github.com/MAKSIM-BRY/DijkstraAlgo/blob/master/schema.png" alt="Schéma" width="100" height="100"><br>
```json
  "A": {
        "B": 9,
        "C": 20,
        "D": 17
    }
```

### Appel
Pour charger, executer et afficher le résultat:
```python
CDijkstra = Dijkstra();<br>
    #De Marseille jusqu'à Paris<br>
    CDijkstra.openJson('villes.json')<br>
    CDijkstra.pointToPoint("Marseille","Paris")<br>
    CDijkstra.parcourtab()<br>
    CDijkstra.printRecap()<br>
```
