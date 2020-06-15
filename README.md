# DijkstraAlgo

Mise en place de l'algorithme de DijkstraAlgo

### Dataset:
Pour faire fonctionné l'algorithme, le code à besoin d'un dataset sous cette forme:
<code>
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
</code><br>
De manière à ce que pour chaque noeud il y est la liste des noeuds connectés et leurs longueurs.<br>

<code>
  "A": {
        "B": 9,
        "C": 20,
        "D": 17
    }
</code>
