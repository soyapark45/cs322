# Author: Soya Park <soya@kaist.ac.kr>
# Date: 9/21/2015

import configparser
import sys

class DFA(object):
	def __init__(self, inCfg):
		Config = configparser.ConfigParser()
		Config.read(inCfg)
		
		self.states = self.parse(Config.get('DFA', 'States'))
		self.symbols = self.parse(Config.get('DFA', 'Symbols'))
		self.delta = self.parseDelta(Config.get('DFA', 'Delta'))
		self.initial = Config.get('DFA', 'Initial')
		self.final = self.parse(Config.get('DFA', 'Final'))

		#print(self.delta)

	# parse config file of states, symbols and final states
	def parse(self, inStr):
		return inStr.split(',')

	# parse input of delta and build dict for each states accordingly
	def parseDelta(self, inStr):
		dic= {}

		for d in inStr.split(' '):
			tup = d[1:-1].split(",")
			if len(tup) != 3:
				raise(Exception("ERROR! Undefined transition"))

			dic[(tup[0],tup[1])] = tup[2]

		return dic

	# Return true if given string is part of DFA language. Otherwise return false
	def isAccepted(self, inStr):
		cur = self.initial

		for s in inStr:
			if s not in self.symbols:
				raise(Exception("ERROR! Invalid symbol"))

			cur = self.delta[(cur,s)]
			#print(cur)

		if cur in self.final:
			return True

		return False

if __name__ == '__main__':
	if len(sys.argv) == 1:
		raise(Exception("ERROR! String is not provided!"))

	d =DFA("DFA.cfg")
	print("################")
	print(d.isAccepted(sys.argv[1]))
