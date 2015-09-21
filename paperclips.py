#Paperclip experiment from vsauce video "The Zipf Mystery"

import sys
import random
import argparse

class Paperclip:
	def __init__(self, id_):
		self.id_ = id_
		self.chain = [self]

	def __repr__(self):
		return str(self.id_) + " : " + self.print_chain()

	def print_chain(self):
		s = ""
		for paperclip in self.chain:
			s = s + str(paperclip.id_) + " "
		return s

	def get_chain_list(self):
		chain = []
		for paperclip in self.chain:
			chain.append(paperclip.id_)
		return chain

def pick(paperclips_list):
	return random.choice(paperclips_list)

def pick2(paperclips_list):
	paperclip1 = pick(paperclips_list)
	paperclip2 = pick(paperclips_list)

	while paperclip1.chain == paperclip2.chain:
		paperclip2 = pick(paperclips_list)

	# print "Got " + str(paperclip1.id_) + " and " + str(paperclip2.id_)

	return (paperclip1, paperclip2)

def link(clips, chain_list):
	paperclip1 = clips[0]
	paperclip2 = clips[1]

	chain_list.remove(paperclip1.get_chain_list())
	chain_list.remove(paperclip2.get_chain_list())

	paperclip1.chain.extend(paperclip2.chain)
	for paperclip in paperclip1.chain:
		paperclip.chain = paperclip1.chain

	chain_list.append(paperclip1.get_chain_list())

	# print "chain : " + str(paperclip1.get_chain_list())

	# print "New chain : " + paperclip1.print_chain()

def validate_input(num_paperclips, iterations):
	if num_paperclips < 1:
		print "addition paperclips required"
		print "(1st arg must be >0)"
		sys.exit(0)

	if iterations < 0:
		print "are you asking me to do this negative times? I can't even..."
		print "(2nd arg must be >=0)"
		sys.exit(0)

	if iterations >= num_paperclips:
		print "too many iterations, choose a number less than number of paperclips"
		sys.exit(0)

def run(num_paperclips, iterations):
	paperclips_list = []
	chain_list = []

	for id_ in range(0, num_paperclips):
		paperclip = Paperclip(id_)
		paperclips_list.append(paperclip)
		chain_list.append(paperclip.get_chain_list())

	for n in range(0, iterations):
		clips = pick2(paperclips_list)
		link(clips, chain_list)

		# for id_ in range(0, len(paperclips_list)):
		# 	print paperclips_list[id_]

		# print ""

	# if iterations == 0:
	# 	for id_ in range(0, len(paperclips_list)):
	# 		print paperclips_list[id_]

	chain_map = {}
	for chain in chain_list:
		key = len(chain)
		if key not in chain_map:
			chain_map[key] = []

		chain_map[key].append(chain)

	keys = sorted(chain_map.keys(), reverse=True)

	# print "Chains: "
	# print "keys : " + str(keys)

	results = {}

	print "length : frequency"


	for key in keys:
		results[key] = len(chain_map[key])
		print str(key) + " : " + str(len(chain_map[key]))




	# print "Chains: "
	# chain_list.sort(key = lambda l: len(l), reverse = True)
	# for chain in chain_list:
	# 	print chain
	return results


def main():



	if len(sys.argv) < 3:
		print "we require more arguments"
		print "(at least two)"
		return

	num_paperclips = int(sys.argv[1])
	iterations = int(sys.argv[2])
	if len(sys.argv) >= 4:
		num_tests = int(sys.argv[3])
	else:
		num_tests = 1

	print "num_paperclips : " + str(num_paperclips)
	print "iterations : " + str(iterations)
	print "num_tests : " + str(num_tests)
	

	validate_input(num_paperclips, iterations)

	sum_frequencies_map = {}

	for i in range(0, num_tests):
		print "--------------------"
		print "test #" + str(i+1)
		results = run(num_paperclips, iterations)
		for key in results.keys():
			if key in sum_frequencies_map:
				sum_frequencies_map[key] += results[key]
			else:
				sum_frequencies_map[key] = results[key]

	print "--------------------"			
	print "sums"
	for key in sorted(sum_frequencies_map.keys(), reverse=True):
		print str(key) + " : " + str(sum_frequencies_map[key])	


	mean_frequencies_map = {}
	for key in sum_frequencies_map.keys():
		mean_frequencies_map[key] = sum_frequencies_map[key] / float(num_tests)


	print "--------------------"
	print "mean"
	for key in sorted(mean_frequencies_map.keys(), reverse=True):
		print str(key) + " : " + str(mean_frequencies_map[key])	

	print "--------------------"
	print "expectation"
	for key in sorted(mean_frequencies_map.keys(), reverse=True):
		print str(key) + " : " + str(mean_frequencies_map[key] * key)	

if __name__ == "__main__":
    main()







