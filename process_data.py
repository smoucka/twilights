import csv, struct, copy

files = ['_daytime', '_civil_twilight', '_nautical_twilight', '_astronomical_twilight']
# city name prefix in twilight files
cities = ['miami']
	
# storage
times = []

def rise_set(tp):
	times.append(tp[0].split(' '))

def twilights(tp, day):
	times[day].insert(0, tp[0].split(' ')[0])
	times[day].append(tp[0].split(' ')[1])
		
def parse(iter_num, in_file):
	day_count = 0
	# field widths
	fieldwidths = [[-4,9],[-15,9],[-26,9],[-37,9],[-48,9],[-59,9],[-70,9],[-81,9],[-92,9],[-103,9],[-114,9],[-125,9]]
	head_lines = 9

	f = open('original_data/'+in_file+'.txt', 'rb')
	
	for col in fieldwidths:
		# reset 'f' location to beginning of file and skip header
		f.seek(0)
		for x in range(0,head_lines):
			f.readline()
		
		# fixed width parsing
		fmtstring = ' '.join('{}{}'.format(abs(c), 'x' if c < 0 else 's') for c in col)
		fieldstruct = struct.Struct(fmtstring)
		parse = fieldstruct.unpack_from
		
		for x in range(0,31):
			time_pair = parse(f.readline())
			if time_pair[0] <> '         ':
				if file_idx == 0:
					rise_set(time_pair)
				else:
					twilights(time_pair, day_count)
				day_count += 1

for city in cities:
	for file_idx, file in enumerate(files):
		city_file = city + file
		parse(file_idx, city_file)

	with open('parsed_data/' + city + '_times.csv', 'wb') as csvfile:
		csvwriter = csv.writer(csvfile)
		csv_head = ['astro_beg', 'naut_beg', 'civ_beg', 'rise', 'set', 'civ_end', 'naut_end', 'astro_end']
		csvwriter.writerow(csv_head)
		for row in times:
			csvwriter.writerow(row)