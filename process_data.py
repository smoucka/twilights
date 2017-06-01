import csv, struct, copy

files = ['day', 'civil', 'naut', 'astro']
# city name prefix in twilight files
#cities = ['N85', 'N75', 'N65', 'N55']
fpath = 'original_data/files_by_latitude/'

twi_limit_lookup = {'----':['1200','1200'],
					'****':['0000','2400'],
					'====':['1200','1200'],
					'////':['0000','2400']}

def parse_times(tp, day):
	twi_times = tp[0].split(' ')
	# method to catch blank values, two in each twilight (and rise/set) type
	# split creates array with 6 items instead of 2, check position of blank
	# value (first or second) and replace with appropriate value
	if len(twi_times) != 2:
		if twi_times.index('') == 0:
			twi_times = twi_times[5:]
			twi_times.insert(0, '0000')
		else:
			twi_times = twi_times[:1]
			twi_times.append('2400')
	
	if twi_times[0] in twi_limit_lookup:
		twi_times = twi_limit_lookup[twi_times[0]]

	times[day].insert(0, twi_times[0])
	times[day].append(twi_times[1])
		
def parse_file(iter_num, in_file):
	day_count = 0
	# field widths
	fieldwidths = [[-4,9],[-15,9],[-26,9],[-37,9],[-48,9],[-59,9],[-70,9],[-81,9],[-92,9],[-103,9],[-114,9],[-125,9]]
	head_lines = 10

	f = open(fpath+in_file+'.txt', 'rb')
	
	for col in fieldwidths:
		# reset 'f' location to beginning of file and skip header
		f.seek(0)
		for x in range(0,head_lines):
			f.readline()
		
		# fixed width parsing
		fmtstring = ' '.join('{}{}'.format(abs(c), 'x' if c < 0 else 's') for c in col)
		fieldstruct = struct.Struct(fmtstring)
		parse_pair = fieldstruct.unpack_from
		
		for x in range(0,31):
			time_pair = parse_pair(f.readline())
			if time_pair[0] != '         ':

				if file_idx == 0:
					times.append([])
					parse_times(time_pair, day_count)
				else:
					parse_times(time_pair, day_count)
				day_count += 1

#for city in cities:

#process by latitude series
for n in range(85,-90,-10):
	lat_val = str(abs(n))
	if n<0:
		lat = 'S' + lat_val
	else:
		lat = 'N' + lat_val	
	
	# storage
	times = []

	for file_idx, file in enumerate(files):
		lat_file = lat + '_' + file
		parse_file(file_idx, lat_file)

	with open('parsed_data/' + lat + '_times.csv', 'wb') as csvfile:
		csvwriter = csv.writer(csvfile)
		csv_head = ['astro_beg', 'naut_beg', 'civ_beg', 'rise', 'set', 'civ_end', 'naut_end', 'astro_end']
		csvwriter.writerow(csv_head)
		for row in times:
			csvwriter.writerow(row)
