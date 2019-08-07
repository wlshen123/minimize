def group(items):
	''' initiates the quine-mccluskey algorithm
		groups boolean expressions by number of 1's'''
	mgroup = []
	for i in range (0, len(items[0])):
		mroup.append([])
	for i in range (0, len(items)):
		num_ones = items[i].count('1')
		mgroup[num_ones].append(items[i])
	return mgroup

def hpass(table):
	''' forms a list from only elements in the input dictionary that have value 1'''
	return [x for x in table if (table[x] == 1)]

def convert(input):
	''' converts a list of minterms to a list of SOP objects
		returns the list of SOP objects'''
	sop_group = []
	for item in input:
		sop_group.append(SOP(item))
	return sop_group
