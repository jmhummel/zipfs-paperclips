#Paperclip experiment from vsauce video "The Zipf Mystery"

import sys
import random

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

def pick(paperclips_list):
	return random.choice(paperclips_list)

def pick2(paperclips_list):
	paperclip1 = pick(paperclips_list)
	paperclip2 = pick(paperclips_list)

	while paperclip1.chain == paperclip2.chain:
		paperclip2 = pick(paperclips_list)

	print "Got " + str(paperclip1.id_) + " and " + str(paperclip2.id_)

	return (paperclip1, paperclip2)

def link(clips, chain_list):
	paperclip1 = clips[0]
	paperclip2 = clips[1]

	chain_list.remove(paperclip1.chain)
	chain_list.remove(paperclip2.chain)

	paperclip1.chain.extend(paperclip2.chain)
	for paperclip in paperclip1.chain:
		paperclip.chain = paperclip1.chain

	chain_list.append(paperclip1.chain)

	print "New chain : " + paperclip1.print_chain()

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


def main():
	if len(sys.argv) < 3:
		print "we require more arguments"
		print "(at least two)"
		return

	num_paperclips = int(sys.argv[1])
	iterations = int(sys.argv[2])

	print "num_paperclips : " + str(num_paperclips)
	print "iterations : " + str(iterations)
	print "--------------------"

	validate_input(num_paperclips, iterations)

	paperclips_list = []
	chain_list = []

	for id_ in range(0, num_paperclips):
		paperclip = Paperclip(id_)
		paperclips_list.append(paperclip)
		chain_list.append(paperclip.chain)

	for n in range(0, iterations):
		clips = pick2(paperclips_list)
		link(clips, chain_list)

		for id_ in range(0, len(paperclips_list)):
			print paperclips_list[id_]

		print ""

	if iterations == 0:
		for id_ in range(0, len(paperclips_list)):
			print paperclips_list[id_]

	print chain_list


if __name__ == "__main__":
    main()







