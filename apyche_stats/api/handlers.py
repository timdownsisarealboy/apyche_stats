from piston.handler import BaseHandler

class StatHandler( BaseHandler ):
    def read( self, request):
	f = open('/var/log/httpd/access_log', 'r')
        lines = f.readlines()
	f.close()
	# read in backwards so newest entries are first
	lines.reverse()
	ips = []
	ips_seen = {}
	for line in lines:
		data = line.split(" ")
		ip = data[0]
		if ip not in ips_seen:
			ips_seen[data[0]] = True
			line_data = {
				'time' : data[3][1:],
				'zone' : data[4][:-1],
				'method' : data[5],
				'resource' : data[6],
				'protocol' : data[7],
				'status_code' : data[8],
				'size' : data[9]
			}
			ips.append((data[0],line_data))
	return ips
