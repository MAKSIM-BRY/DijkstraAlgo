import json

class Dijkstra:
    def __init__(self):
        self.routes = {}
        self.start = ""
        self.end = ""
        self.lenghtFromStartToEnd = 0
        self.pathFromNodes = []

    def openJson(self, file):
        with open(file) as f:
            self.routes = json.load(f)
    
    def pointToPoint(self, start, end):
        self.start = start
        self.end = end

    def parcourtab(self):
        incrementedValue = 0
        lastPoint = self.start
        lastValue = 0
        alreadyPass = [self.start]
        while lastPoint != self.end:
            addedValue, lastPoint = self.chooseMinimalPath(lastPoint, alreadyPass)
            lastValue += addedValue
        self.lenghtFromStartToEnd = lastValue
        self.pathFromNodes = alreadyPass
    
    def chooseMinimalPath(self, lastPoint, alreadyPass):
        minimalValue = -1
        minimalAttrib = ""
        cproutes = self.routes[lastPoint]
        for node in alreadyPass:
            try:
                del cproutes[node]
            except:
                pass
        for attr, value in self.routes[lastPoint].items():
            if minimalValue == -1 or minimalValue > value:
                minimalValue = value
                minimalAttrib = attr
        alreadyPass.append(minimalAttrib)
        return minimalValue, minimalAttrib

    def printRecap(self):
        print(f'Pour aller de {self.start} à {self.end}, {self.pathFromNodes}, on parcours {self.lenghtFromStartToEnd} étapes.')

if __name__ == "__main__" :
    CDijkstra = Dijkstra();
    #De Marseille jusqu'à Paris
    CDijkstra.openJson('villes.json')
    CDijkstra.pointToPoint("Marseille","Paris")
    CDijkstra.parcourtab()
    CDijkstra.printRecap()
    
    # Avec le premier data set
    #CDijkstra.openJson('data.json')
    #CDijkstra.pointToPoint("A","F")
    #CDijkstra.parcourtab()
    #CDijkstra.printRecap()
    #CDijkstra.pointToPoint("D","F")
    #CDijkstra.parcourtab()
    #CDijkstra.printRecap()
    ## Avec le second data set
    #CDijkstra.openJson('data2.json')
    #CDijkstra.pointToPoint("D","G")
    #CDijkstra.parcourtab()
    #CDijkstra.printRecap()