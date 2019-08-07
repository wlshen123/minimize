from sop import SOP
from sop_logic import *
from utility import *
from itertools import chain

##### main function #####
def quine_mccluskey(table):
	func = hpass(table)
	curr_groups = group(func)
	next_groups = []

	curr_groups = convert(curr_groups)

	# each iteration performs one stage of quine-mccluskey
	while curr_groups:

		for i in range(0, len(next(iter(curr_groups))) - 1):
			next_groups.append([])

			for minterm in curr_groups[i]:
				for other in curr_groups[i + 1]:
					if(adjacent(minterm, other)):
						next_groups[i].append(sop_combine(minterm, other))





# translates a list of 1's, 0's, and -'s, to a's, b's, and c's
def gate_translate(exps):
	expression = ""
	for exp in exps:
		for i in range(len(exp)):
			if exp[i] == '1':
				expression = expression + chr(97 + i)
			elif exp[i] == '0':
				expression = expression + chr(97 + i) + "\'"
		
		expression = expression + " + "
	
	return expression[:-3]

################ end of functions ################


func = {'0000': 0, '0001': 0, '0010': 0, '0011': 0,
		'0100': 0, '0101': 1, '0110': 0, '0111': 1,
		'1000': 0, '1001': 1, '1010': 0, '1011': 1,
		'1100': 0, '1101': 0, '1110': 0, '1111': 1}
