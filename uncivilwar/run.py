
import random
attackercount = 4;

defendercount = 10;


def generatePlanetName():
    First = ['Jur', 'Sel', 'Mon', 'Bel', 'Re', 'Or', 'Cro', 'Mer', 'Le', 'Ve']
    Middle = ['pit', 'rad', 'ink', 'flo', 'pus', 'mor', 'del', 'por', 'fit', 'ron']
    Suffix = ['los', 'ia', 'io' ' II']

    planetName = First[random.randint(0, len(First)-1)]
    for i in range(0, random.randint(0,2)):
        planetName += Middle[random.randint(0, len(Middle)-1)]
    for i in range(0, random.randint(0,1)):
        planetName += Suffix[random.randint(0, len(Suffix)-1)]
    return planetName;



class Planet:

   def __init__(self, name, defendercount):
      self.name = name
      self.defendercount = defendercount

      def getDefenders(self): return defendercount
      def setDefenders(defendercount): self.defendercount = defendercount
      def getName(self): return self.name

      def battle(attackers, objective, defenders):
         if objective == 0: #take the planet
             if attackercount <= defendercount*3:
                 print(str(defendercount) + " defenders prevailed against " + str(attackercount) + " attackers.")
             else:
                 print(str(defendercount) + " defenders failed against " + str(attackercount) + " attackers.")
         else: #destroy the planet
             if attackercount <= defendercount/3:
                 print(str(defendercount) + "defended against the concentrated attacks of " + str(attackercount) + " on the generators.  The planet is safe... for now.")
             if attackercount > defendercount/3:
                 print(str(defendercount) + " defenders could not defend against the concentrated attacks of " + str(attackercount) + " on the generators.  The planet is uninhabitable.")

      def survivors():
          return defendercount*0.5

generatePlanetName();
