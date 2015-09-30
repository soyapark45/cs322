# Author: Soya Park <soya@kaist.ac.kr>
# Date: 9/28/2015

import ConfigParser
import sys

class Mealy(object):
	def __init__(self, inCfg):
		Config = ConfigParser.ConfigParser()
		Config.read(inCfg)
		
		self.states = self.parse(Config.get('Mealy', 'States'))
		self.symbols = self.parse(Config.get('Mealy', 'Symbols'))
		self.delta = self.parseDelta(Config.get('Mealy', 'Delta'))
		self.lam = self.parseDelta(Config.get('Mealy', 'Lambda'))
		self.initial = Config.get('Mealy', 'Initial')
		self.phi = Config.get('Mealy', 'Phi')

		if self.initial not in self.states:
			raise(Exception("Error! initial is not among states"))
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
				raise(Exception("ERROR! Incorrect input format"))

			dic[(tup[0],tup[1])] = tup[2]

		return dic

	# Return phi if given string is part of Mealy language.
	def printPhi(self, inStr):
		cur = self.initial
		phi = ""

		for s in inStr:
			if s not in self.symbols:
				raise(Exception("ERROR! Invalid symbol"))

			# what if transition is not existing!
			if self.delta.get((cur,s)) is None:
				raise(Exception("ERROR! Invalid transition"))

			cur = self.delta[(cur,s)]

			if self.lam.get((cur,s)) is None:
				raise(Exception("ERROR! Invalid lambda"))

			phi += self.lam[(cur,s)]
			
		return phi

if __name__ == '__main__':
	if len(sys.argv) == 1:
		raise(Exception("ERROR! String is not provided!"))

	d =Mealy("Mealy.cfg")
	print("################")
	print "Output string for " + sys.argv[1]
	print(d.printPhi(sys.argv[1]))
