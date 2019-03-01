'''
  @Author Tom Karachristos
  Stable marriage problem
  Given an equal number of men and women to be paired for marriage,
  each man ranks all the women in order of his preference
  and each women ranks all the men in order of her preference.
  A stable set of engagements for marriage is one where no man prefers
  a women over the one he is engaged to, where that
  other woman also prefers that man over the one she is engaged to.
'''

def stableMarriageProblem(manPreferce, womanPreferce):
  persons = Preferences(manPreferce,womanPreferce)
  while persons.thereIsFreeMan() and persons.hasntProposeEveryWoman():
    man = persons.chooseAFreeMan()
    highestRankedWoman = persons.getHighestRankedWoman(man)
    if persons.isFree(highestRankedWoman):
      persons.engage(man,highestRankedWoman)
    else:
      if persons.isWomanPrefersMan(man,highestRankedWoman):
        persons.engage(man,highestRankedWoman)
    persons.removeWomanFromManPreference(man, highestRankedWoman)
  return persons.getEngages()


class Preferences:
  def __init__(self, manPreferce, womanPreferce):
    self.manPreferce = manPreferce
    self.womanPreferce = womanPreferce
    self.freeGuys = list(manPreferce.keys())
    self.engages = {}

  def thereIsFreeMan(self):
    return len(self.engages) < len(self.manPreferce)

  def hasntProposeEveryWoman(self):
    return len(self.manPreferce[self.freeGuys[0]])

  def getHighestRankedWoman(self,man):
    return self.manPreferce[man][0]

  def chooseAFreeMan(self):
    return self.freeGuys[0]

  def isFree(self,highestRankedWoman):
    return not (highestRankedWoman in self.engages)

  def isWomanPrefersMan(self, man, manHighWoman):
    return self.womanPreferce[manHighWoman].index(man) < \
           self.womanPreferce[manHighWoman].index(self.getManEngageToWoman(manHighWoman))

  def removeWomanFromManPreference(self, man, manHighWoman):
    self.manPreferce[man].remove(manHighWoman)
    return

  def engage(self,man,woman):
    if woman in self.engages:
      engageToWomanMan = self.getManEngageToWoman(woman)
      self.freeGuys.append(engageToWomanMan)
    self.engages[woman] = man
    self.freeGuys.remove(man)
    return

  def getManEngageToWoman(self,woman):
    return self.engages[woman]

  def getEngages(self):
    return self.engages