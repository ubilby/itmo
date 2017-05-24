def func(**d):
	print(d)
	for i in d:
		print("{0} => {1}".format(i, d[i]), end = " ")
func(a=1, b=2, c=3)
print()
form1 = "{:<10} {:>10} {:^10}".format(7, 8, 9)
print(form1)