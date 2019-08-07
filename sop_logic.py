def sop_adjacent(sop1, sop2):
	''' checks if two SOP objects are adjacent'''
	return adjacent(sop1.string, sop2.string)

def sop_combine(sop1, sop2):
	''' takes two adjacent SOP objects and combines them to form a new SOP object
		NOTE: assumes the two SOP objects to be adjacent'''
	result = SOP(combine(sop1, sop2))
	return result
