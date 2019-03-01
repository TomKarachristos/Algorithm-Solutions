import unittest
import StableMarriageProblem

manPreferns = {
  'abe': ['abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay'],
  'bob': ['cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay'],
  'col': ['hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan'],
  'dan': ['ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi'],
  'ed': ['jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay'],
  'fred': ['bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay'],
  'gav': ['gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay'],
  'hal': ['abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee'],
  'ian': ['hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve'],
  'jon': ['abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope']
}
womanPreferns = {
  'abi': ['bob', 'fred', 'jon', 'gav', 'ian', 'abe', 'dan', 'ed', 'col', 'hal'],
  'bea': ['bob', 'abe', 'col', 'fred', 'gav', 'dan', 'ian', 'ed', 'jon', 'hal'],
  'cath': ['fred', 'bob', 'ed', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
  'dee': ['fred', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ed'],
  'eve': ['jon', 'hal', 'fred', 'dan', 'abe', 'gav', 'col', 'ed', 'ian', 'bob'],
  'fay': ['bob', 'abe', 'ed', 'ian', 'jon', 'dan', 'fred', 'gav', 'col', 'hal'],
  'gay': ['jon', 'gav', 'hal', 'fred', 'bob', 'abe', 'col', 'ed', 'dan', 'ian'],
  'hope': ['gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ed', 'col', 'fred'],
  'ivy': ['ian', 'col', 'hal', 'gav', 'fred', 'bob', 'abe', 'ed', 'jon', 'dan'],
  'jan': ['ed', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'fred', 'dan']
}

manPreferns1 = {
  'boys0': ['girls0', 'girls1','girls2'],
  'boys1': ['girls1', 'girls2','girls0'],
  'boys2': ['girls2', 'girls0', 'girls1']
}

womanPreferns1 = {
  'girls0': ['boys0', 'boys1', 'boys2'],
  'girls1': ['boys1', 'boys2', 'boys0'],
  'girls2': ['boys2', 'boys0', 'boys1']
}
'''results :
92: boys0 is paired with girls0
93: boys1 is paired with girls1
94: boys2 is paired with girls2
'''


manPreferns2 = {
  'boys0': ['girls3', 'girls2','girls0','girls1'],
  'boys1': ['girls2', 'girls1','girls0','girls3'],
  'boys2': ['girls2', 'girls3', 'girls0','girls1'],
  'boys3': ['girls1', 'girls3', 'girls0','girls2']
}

womanPreferns2 = {
  'girls0': ['boys2', 'boys0', 'boys3','boys1'],
  'girls1': ['boys0', 'boys1', 'boys2','boys3'],
  'girls2': ['boys0', 'boys3', 'boys1', 'boys2'],
  'girls3': ['boys3', 'boys0', 'boys2','boys1']
}
'''results :
114: boys0 is paired with girls3
115: boys1 is paired with girls2
116: boys2 is paired with girls0
117: boys3 is paired with girls1
'''


class stable(unittest.TestCase):
  def test(self):
    result = StableMarriageProblem.stableMarriageProblem(manPreferns,womanPreferns)
    expectedResult = {"jan": "ed", "fay": "dan", "eve": "hal", "dee": "col", "gay": "gav", "abi": "jon", "cath": "bob", "bea": "fred", "ivy": "abe", "hope": "ian"}
    unmatched_item = set(result.items()) ^ set(expectedResult.items())
    self.assertEqual(len(unmatched_item), 0)
    result = StableMarriageProblem.stableMarriageProblem(manPreferns1, womanPreferns1)
    expectedResult = {"girls0": "boys0", "girls1": "boys1", "girls2": "boys2"}
    unmatched_item = set(result.items()) ^ set(expectedResult.items())
    self.assertEqual(len(unmatched_item), 0)
    result = StableMarriageProblem.stableMarriageProblem(manPreferns2, womanPreferns2)
    expectedResult = {"girls3": "boys0", "girls2": "boys1", "girls0": "boys2", "girls1": "boys3"}
    unmatched_item = set(result.items()) ^ set(expectedResult.items())
    self.assertEqual(len(unmatched_item), 0)