from logic import expand

class SOP(object):
	def __init__(self, input = ''):
		''' optional argument: string representation of a minterm
			e.g '1--0', '1100', '-0-1' '''
		self.string = input
		self.contents = expand(input)
	
	def __str__(self):
		''' default string representation of SOP instances'''
		return self.string
