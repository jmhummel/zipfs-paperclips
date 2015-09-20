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

def link(clips):
	paperclip1 = clips[0]
	paperclip2 = clips[1]
	paperclip1.chain.extend(paperclip2.chain)
	for paperclip in paperclip1.chain:
		paperclip.chain = paperclip1.chain
	print "New chain : " + paperclip1.print_chain()

def main():
	if len(sys.argv) < 3:
		print "we require more arguments"
		return

	num_paperclips = int(sys.argv[1])
	iterations = int(sys.argv[2])

	paperclips_list = []

	for id_ in range(0, num_paperclips):
		paperclips_list.append(Paperclip(id_))

	for n in range(0, iterations):
		clips = pick2(paperclips_list)
		link(clips)

		for id_ in range(0, len(paperclips_list)):
			print paperclips_list[id_]

		print ""

	

if __name__ == "__main__":
    main()







