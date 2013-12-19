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

RIGHT = ">"
LEFT = "<"
CENTER = "^"

class Table(object):
	def __init__(self, data, uniform=False, columnwise=True, align=">", min_width=3):
		"""Data is an object that iterates over the rows of the Table"""
		self.data = data
		if columnwise: #each column has a uniform width
			lens = [max([len(str(datum)) for datum in column]+[min_width]) for column in zip(*data)]
			self.format_string = "|"+"|".join("{"+":"+align+"{}".format(n)+"}" for n in lens)+"|"

	def __str__(self):
		rows = [self.format_string.format(*row) for row in self.data]
		sep = "-"*len(rows[0])
		return "\n".join([sep]+sum([[row, sep] for row in rows], []))

def point_table(expression, *lims):
	expression = Expression(expression)
	xs = range(*lims)
	ys = map(expression, xs)
	expressions = map(expression.substitute, xs)
	points = zip(xs, ys)
	xs, expressions, ys, points = ["x"]+xs, [str(expression)]+expressions, ["y"]+ys, ["(x, y)"]+points
	table = Table(zip(xs, expressions, ys, points))
	print str(table)


if __name__=="__main__":
	point_table("x^2 + 1", -2,3)