from sop import SOP

def adjacent(exp1, exp2):
	''' determines if two expressions are adjacent'''
	# flag is set to True upon the first encounter of a differing term
	# upon the second encounter of a differing term, the function returns False
	flag = False
	for i in range(0, len(exp1)):
		# DC's must all match between adjacent expressions
		if (exp1[i] == '-' and exp2[i] != '-') or (exp1[i] != '-' and exp2[i] == '-'):
			return False
		# sets a flag if the current variable is off; if the flag has already been set, return False
		elif (exp1[i] == '0' and exp2[i] == '1') or (exp1[i] == '1' and exp2[i] == '0'):
			if not flag:
				flag = True
			else:
				return False
	return flag

def combine(exp1, exp2):
	''' takes two adjacent expressions and combines them
		NOTE: assumes the two expressions to be adjacent'''
	for i in range(0, len(exp1) - 1):
		if(exp1[i] == '0' and exp2[i] == '1') or (exp1[i] == '1' and exp2[i] == '0'):
			return exp1[:i] + '-' + exp1[i+1:]
	return exp1[:-1] + '-'

def expand(minterm):
	''' takes a boolean expression in the form of 1's, 0's, and -'s,
		constructs a list of included minterms
		e.g. expand('10-0') == ['1000', '1010']'''
	content = []
	# BASE CASE: if minterm represents a single input combination
	if '-' not in minterm:
		return [minterm]
	# STEP: if minterm represents multiple input combinations,
	#		divide and conquer, replacing the '-' with a '0' and a '1' in separate recursive calls
	else:
		for i in range(0, len(minterm)):
			if(minterm[i] == '-'):
				content += expand(minterm[:i] + '0' + minterm[i+1:])
				content += expand(minterm[:i] + '1' + minterm[i+1:])
	return content

