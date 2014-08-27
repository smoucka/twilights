import csv, struct

def alternate(a):
	return a[::1]

fieldwidths = (-4, 4, -1, 4, -2, 4, -1, 4, -2, 4, -1, 4, -2, 4, -1, 4, -2, 4, -1, 4, -2, 4, -1, 4, -2, 4, -1, 4, -2, 4, -1, 4, -2, 4, -1, 4, -2, 4, -1, 4, -2, 4, -1, 4, -2, 4, -1, 4)

fmtstring = ' '.join('{}{}'.format(abs(fw), 'x' if fw < 0 else 's') for fw in fieldwidths)
fieldstruct = struct.Struct(fmtstring)
parse = fieldstruct.unpack_from

# storage
time_dict = {'jan':[], 'feb':[], 'mar':[], 'apr':[], 'may':[], 'jun':[], 'jul':[], 'aug':[], 'sep':[], 'oct':[], 'nov':[], 'dec':[]}
sunrise = []
sunset = []

f = open('original_data/rise-set.txt', 'rb')
head_lines = 9
# skip header
for x in range(0,head_lines):
	f.readline()
'''	
for x in range(0,31):
	for times in parse(f.readline()):
		sunrise.append(alternate(times))
'''
for x in range(0,31):
	for times in parse(f.readline()):
		print times

print sunrise

'''
test_line = '01  0729 1633  0713 1710  0634 1747  0540 1824  0451 1859  0421 1930  0422 1941  0448 1919  0522 1832  0555 1739  0632 1649  0709 1624'
out = parse(test_line)
print out
'''