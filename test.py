# -*- coding: utf-8 -*-
import hunspell
hobj = hunspell.HunSpell('ml_IN.dic', 'ml_IN.aff')
tests  = [
  u"ജീവിതത്തെ",
  u"ജീവിതത്തിലെ",
  u"ജീവിതത്തിലേയ്ക്ക്",
  u"മുറ്റത്തെ",
  u"മുറ്റങ്ങള്‍",
  u"മുറ്റങ്ങള്‍ക്ക്",
  u"മുറ്റങ്ങളിലേയ്ക്ക്",
  u"മുറ്റത്തിലെ",
  u"മുറ്റത്തിലേയ്ക്കു്",
  u"മുറ്റത്തു്",
  u"അതു്",
  u"തിരമാല",
  u"തിരമാലകള്‍",
  u"തിരുമുറ്റങ്ങളിലേയ്ക്ക്",
  u"തിരക്കഥ",
  u"തിരക്കഥകള്‍",
  u"പൂമാല",
  u"നീലത്തിമിംഗലം",
  u"പ്രത്യയശാസ്ത്രം",
  u"പ്രത്യയശാസ്ത്രതിരക്കഥകള്‍",
  u"തിരക്കഥാശാസ്ത്രം",
  u"പവാദം",
  u"കഥാപവാദം"
]
for test in tests:
  result = hobj.spell(test.encode('utf8'))
  if not result:
    print "--------------"
    print test + " is wrong"
  else:
    continue
  suggestions = hobj.suggest(test.encode('utf8'))
  for suggestion in suggestions:
    print suggestion

