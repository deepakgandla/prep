def nthterm(input1, input2, input3):
	d = input2 - input1
	first = input1 - d
	nth = first + (input3-1) *d
	return nth
print(nthterm(1, 2, 10))