import subprocess

curl = 'curl "http://aa.usno.navy.mil/cgi-bin/aa_rstablew.pl" -H "Origin: http://aa.usno.navy.mil" -H "Accept-Encoding: gzip,deflate" -H "Accept-Language: en-US,en;q=0.8" -H "User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Cache-Control: max-age=0" -H "Referer: http://aa.usno.navy.mil/data/docs/RS_OneYear.php" -H "Connection: keep-alive" --data "FFX=2&xxy=2014&type=&place=&xx0=-1&xx1=0&xx2=0&yy0=1&yy1=&yy2=0&zz1=&zz0=-1&ZZZ=END" --compressed'

table_type = ['0','2','3','4']

for lat in range(90,-95,-5):
	lat_val = str(abs(lat))
	if lat<0:
		name = lat_val + 'S'
		curl = curl.replace('yy0=1', 'yy0=-1')
	else:
		name = lat_val + 'N'
	
	for tab in table_type:
		command = curl.replace('type=', 'type=' + tab).replace('place=', 'place=' + name).replace('yy1=', 'yy1=' + lat_val)
		
		subprocess.call(command)