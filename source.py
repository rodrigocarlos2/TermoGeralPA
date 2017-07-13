
a1 = input('Write the first name: ')

r = input('Write the reason: ')

n = input('Write the wished element number: ')

an = a1+(n-1)*r

print(an)

while a1<=an:
	print(a1),
	a1 += r
