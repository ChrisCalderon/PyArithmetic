import re

def point_table(expression, lims):
	func_expression = expression.replace('^', '**')
	bad_coefficients = re.findall(re.compile("[0-9]+x"), expression)
	for b_c in bad_coefficients:
		g_c = bytearay(b_c)
		g_c.insert(-2, '*')
		func_expression = func_expression.replace(b_c, str(g_c))
	eqfunc = eval("lambda x: " + func_expression)
	
	xs = range(*lims)
	ys = map(eqfunc, xs)
	xs, ys, = map(str, xs), map(str, ys)
	expressions = [expression.replace('x', '({0})').format(x) for x in xs]
	points = map(str, zip(xs, ys))
	lengths = [max(map(len, list_)) for list_ in [xs, expressions, ys, points]]
	lengths = [l if l > 3 else 3 for l in lengths]
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
