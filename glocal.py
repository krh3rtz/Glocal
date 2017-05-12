'''
  Glocal.py
  
 * Author Krhertz 2017
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
  
'''
#!/usr/bin/env python3.4

import argparse
import pygeoip
import time

banner = '''By:

									
	 ██ ▄█▀ ██▀███   ██░ ██ ▓█████  ██▀███  ▄▄▄█████▓▒███████▒	
 	 ██▄█▒ ▓██ ▒ ██▒▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒▓  ██▒ ▓▒▒ ▒ ▒ ▄▀░	
	▓███▄░ ▓██ ░▄█ ▒▒██▀▀██░▒███   ▓██ ░▄█ ▒▒ ▓██░ ▒░░ ▒ ▄▀▒░ 	
	▓██ █▄ ▒██▀▀█▄  ░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  ░ ▓██▓ ░   ▄▀▒   ░	
	▒██▒ █▄░██▓ ▒██▒░▓█▒░██▓░▒████▒░██▓ ▒██▒  ▒██▒ ░ ▒███████▒	
	▒ ▒▒ ▓▒░ ▒▓ ░▒▓░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░  ▒ ░░   ░▒▒ ▓░▒░▒	
	░ ░▒ ▒░  ░▒ ░ ▒░ ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░    ░    ░░▒ ▒ ░ ▒	
	░ ░░ ░   ░░   ░  ░  ░░ ░   ░     ░░   ░   ░      ░ ░ ░ ░ ░	
	░  ░      ░      ░  ░  ░   ░  ░   ░                ░ ░    	
	                                                 ░        	
									
	__"Exploiting vulnerabilities, creating new ways through"__	
'''

glocalb = '''

			 ██████╗ ██╗      ██████╗  ██████╗ █████╗ ██╗     
			██╔════╝ ██║     ██╔═══██╗██╔════╝██╔══██╗██║     
			██║  ███╗██║     ██║   ██║██║     ███████║██║     
			██║   ██║██║     ██║   ██║██║     ██╔══██║██║     
			╚██████╔╝███████╗╚██████╔╝╚██████╗██║  ██║███████╗
			 ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝
			
			 	A public IPv4 Geolocalization Tool
			 		  By: Krhertz

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

			print ('----------------HOST '+ddaddr+'---------------')
			print ('[+] Country Code: ' + data[1])
			print ('[+] Country : ' + data[2])
			print ('[+] City : ' + data[3])
			print ('[+] Region Code: ' + data[4])
			print ('[+] Area Code : '+ str(data[5]))
			print ('[+] Zip_code : ' + str(data[6]))
			print ('[+] Time : ' + data[7])
			print ('[+] Latitude: '+ str(data [9]))
			print ('[+] Longitude: '+ str(data [8]))
			print ('[+] More:\nhttps://www.shodan.io/host/'+ ddaddr+'\nhttps://censys.io/ipv4/'+ ddaddr)

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

	parser = argparse.ArgumentParser(usage='usage:\n-F <file_with_hosts>\n'+glocalb)
	parser.add_argument ('-F', dest='addrs', type=argparse.FileType('r'), help='Hosts in dotted decimal notation (eg. 192.168.1.1)')
	parser.add_argument ('-H', dest='host', type=argparse.FileType('r'), help='Hosts in dotted decimal notation (eg. 192.168.1.1)')
	args = parser.parse_args()
	if (args.addrs == None and args.host == None):
		print (parser.usage)
		exit (0)
	print (glocalb)
	
	targets = []
	
	if host == None:
		addrs = args.addrs		
		for addr in addrs.readlines():
				ip = addr.strip('\n')
				targets.append (ip)
		kml = glocate ()
		kml.KML_FILE (targets)
	else:
		host = args.host
		targets.append (host)
		
		kml  = glocate ()
		kml.KML_FILE (targets)
		
	print ('\n\n\n[+] KML file under \'KML/\'\n')
	print (banner)
