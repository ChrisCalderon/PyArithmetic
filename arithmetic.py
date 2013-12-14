def point_table(expression, eqfunc, lims):
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
