import re

class Expression(object):
	def __init__(self, expression):
		self.expression = expression
		self.format_string = self.expression.replace('x', '({0})')
		self.__init_func()

	def __init_func(self):
		func_expression = self.expression.replace('^', '**')
		bad_coefficients = re.findall(re.compile("[0-9]+x"), self.expression)
		for b_c in bad_coefficients: 
			g_c = bytearray(b_c)
			g_c.insert(-1, '*')
			func_expression = func_expression.replace(b_c, str(g_c))
		self.func = eval("lambda x: " + func_expression)

	def __call__(self, x):
		return self.func(x)

	def __repr__(self):
		return "Expression({0})".format(self.expression)

	def __str__(self):
		return self.expression

	def substitute(self, x):
		return self.format_string.format(x)

def point_table(expression, lims):
	expression = Expression(expression)
	xs = range(*lims)
	ys = map(expression, xs)
	expressions = map(expression.substitute, xs)
	points = zip(xs, ys)
	lengths = [max(map(len, map(str, list_))+[3]) for list_ in [xs, expressions, ys, points]]
	format_string = '|'+'|'.join(" {"+":>{0}".format(length)+"} " for length in lengths)+'|'
	labels = format_string.format('x', expression, 'y', '(x, y)')
	sep = '-'*len(labels)

	print sep
	print labels
	print sep
	for i, x in enumerate(xs):
		print format_string.format(x, expressions[i], ys[i], points[i])
		print sep

def long_division(dividend, divisor):
	pass

if __name__=="__main__":
	point_table("x^2 + 1", [-2,3])