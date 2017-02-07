#!/usr/bin/env python3.4

import argparse
import pygeoip
import time

banner = '''By:

==================================================================
| ##   ## ######## ##   ##   ###### ########  ######## ########   |
| ##  ##  ##    ## ##   ##       #  ##    ##     ##          #    |
| ## ##   ##    ## ##   ##      ##  ##    ##     ##         #     |
| ## ##   ######   #######        # ######       ##       #       |
| ##  ##  ##   ##  ##   ##        # ##   ##      ##     #         |
| ##   ## ##    ## ##   ##   #####  ##    ##     ##    ########   |
|                                                                 |
|     Exploiting vulnerabilities, creating new ways through...    |
==================================================================
'''

class glocate ():

	def __init__ (self):
		pass

	def ip_info (self, ddaddr ):

		gloc = pygeoip.GeoIP ('database/GeoLiteCity.dat')
		
		try:
			
			addr_info 	= 	gloc.record_by_name (ddaddr)
			c_code		= 	addr_info ['country_code']
			country 	= 	addr_info ['country_name']
			city 		= 	addr_info ['city']
			region		= 	addr_info ['region_code']
			area_c		= 	addr_info ['area_code']
			zip_code 	= 	addr_info ['postal_code']
			time 		= 	addr_info ['time_zone']
			longitude 	= 	addr_info ['longitude']
			latitude 	= 	addr_info ['latitude']

			options = {
			'America':'http://maps.google.com/mapfiles/kml/paddle/grn-circle.png',		# America        -> 	Green
			'Africa':'http://maps.google.com/mapfiles/kml/paddle/ylw-circle.png',		# Africa         -> 	Yellow
			'Europe':'http://maps.google.com/mapfiles/kml/paddle/blu-circle.png',		# Europe         -> 	Blue
			'Asia':'http://maps.google.com/mapfiles/kml/paddle/red-circle.png',			# Asia           -> 	Red
			'Oceania':'http://maps.google.com/mapfiles/kml/paddle/wht-circle.png',		# Oceania        -> 	White
			'Antartic':'http://maps.google.com/mapfiles/kml/paddle/purple-circle.png',	# Antartic       -> 	Purple
			'None':'http://maps.google.com/mapfiles/kml/pushpin/pink-pushpin.png',		# None (default) -> 	Pink-pushpin
			}

			icon = ''
			for option in options:
				if option in str (time):
					icon = options[option]

			data = [icon, c_code, country, city, region, area_c, zip_code, time, longitude, latitude]

			return data

		except Exception as e:
			print (str (e))

	def placeMark (self, ddaddr):


		#data = [icon, c_code, country, city, region, area_c, zip, time, longitude, latitude]
		#			0		1		2		3	4		5		6		7		8		9

		try:
			data = self.ip_info (ddaddr)

			mark = (
				'<Placemark>\n'
				'<Style id="INFORMATION">\n'
	  			'<IconStyle>\n'
	  			'<Icon>\n'
	      		'<href>%s</href>\n'
	      		'<scale>1.0</scale>\n'
	    		'</Icon>\n'
	  			'</IconStyle>\n'
				'</Style>\n'
				'<name>%s</name>\n'
				'<description><![CDATA[<p>[+] Country Code: %s</p><p>[+] Country : %s</p><p>[+] City : %s</p><p>[+] Region Code: %s</p><p>[+] Area Code : %s</p><p>[+] Zip_code : %s</p><p>[+] Time : %s</p><p>[+] More: https://www.shodan.io/host/%s  https://censys.io/ipv4/%s</p>]]></description>\n'
				'<Point>\n'
				'<coordinates>%6f,%6f,0</coordinates>\n'
				'</Point>\n'
				'</Placemark>'
				)%(data[0], ddaddr, data[1], data[2], data[3], data[4], data[5], data[6], data [7], ddaddr, ddaddr, data[8],data [9])

			return mark

		except Exception as e:
			print (str (e))
			return 'Unregistered'

	def KML_FILE (self, addresses):

		info = ' '

		for addr in addresses:
			info = info + self.placeMark(addr)

		KML = (
			'<?xml version="1.0" encoding="UTF-8"?>\n'
			'<kml xmlns="http://www.opengis.net/kml/2.2">\n'
			'<Document>\n'
			'%s\n'
			'</Document>\n'
			'</kml>\n'
			)%(info)

		try:
			name = 'KML/glocate.kml'
			kml_out = open (name, 'w')
			kml_out.write (KML)
			kml_out.close ()

		except exception as e:

			print (str (e))

if __name__ == '__main__':

	parser = argparse.ArgumentParser(usage='usage:\n-F <file_with_hosts>\n'+banner)
	parser.add_argument ('-F', dest='addrs', type=argparse.FileType('r'), help='Hosts in dotted decimal notation (eg. 192.168.1.1)')
	args = parser.parse_args()
	if (args.addrs == None):
		print (parser.usage)
		exit (0)

	addrs = args.addrs
	targets = []

	for addr in addrs.readlines():
			host = addr.strip('\n')
			targets.append (host)
	kml = glocate ()
	kml.KML_FILE (targets)