import requests, os
from lxml import html

url = 'http://aa.usno.navy.mil/cgi-bin/aa_rstablew.pl'
payload = {'ID':'AA',
			'year':'2017',
			'task':'3',
			'place':None,
			'lon_sign':'-1',
			'lon_deg':'90',
			'lon_min':None,
			'lat_sign':None,
			'lat_deg':None,
			'lat_min':None,
			'tz':'6',
			'tz_sign':'-1'}

task_array = [{'name':'day', 'num':'0'},
				{'name':'civil', 'num':'2'},
				{'name':'naut', 'num':'3'},
				{'name':'astro', 'num':'4'}]

for lat in range(85,-90,-10):
	lat_val = str(abs(lat))
	payload['lat_deg'] = lat_val
	if lat<0:
		payload['lat_sign'] = '-1'
		ns = 'S'
	else:
		payload['lat_sign'] = '1'
		ns = 'N'
	
	for task in task_array:
		payload['task'] = task['num']

		r = requests.get(url, params=payload)
		tree = html.fromstring(r.content)
		
		fpath = '/path/to/dir/'
		fname = fpath + ns + lat_val + '_' + task['name'] + '.txt'

		with open(fname, 'w') as f:
			f.write(tree.xpath('//pre/text()')[0])

		print 'created file - ' + fname