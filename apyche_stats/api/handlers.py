from piston.handler import BaseHandler

class StatHandler( BaseHandler ):
    def _get_line_data(self, data):
	return {
		'time' : data[3][1:],
		'zone' : data[4][:-1],
		'method' : data[5][1:],
		'resource' : data[6],
		'protocol' : data[7],
		'status_code' : data[8],
		'size' : data[9]
	}
    
    def read( self, request):
	params = request.GET
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
		if params.get("all","false") == "false":
			if ip not in ips_seen:
				line_data = self._get_line_data(data)
				if params.get("resource",None) != None:
					if line_data["resource"] == params.get("resource"):
						ips_seen[data[0]] = True
						ips.append((data[0],line_data))
				else:
					ips_seen[data[0]] = True
					ips.append((data[0],line_data))
		else:
			line_data = self._get_line_data(data)
			if params.get("resource",None) != None:
				if line_data["resource"] == params.get("resource"):
					ips.append((data[0],line_data))
					ips_seen[data[0]] = True
			else:
				ips.append((data[0],data))
				ips_seen[data[0]] = True
	
	if params.get("ip_list","false") == "true":
		ip_list = []
		for ip in ips:
			ip_list.append(ip[0])
		return ip_list
	else:
		return ips

