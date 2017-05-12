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

import os

def requ ():
	try:
		requiFile = 'requirements'
		command = 'pip3 install -r '+requiFile
		os.system (command)
		return 1

	except Exception as e:
		return '[!] An error ocurred while installing requirements -> '+ str(e)  
		pass

def main ():
	DBlink = 'http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz'
	print ('[+] Dowloading and extracting Database \n')

	
	command = 'wget '+ DBlink +' ; gunzip GeoLiteCity.dat.gz; mv GeoLiteCity.dat database/; rm -rf GeoLiteCity.dat.gz'
	os.system (command)
	
	result = requ ()

	if result == 1:
		print ('[+] Requirements correctly installed')
	else:
		print (str (result))
	print  ('By Krh3rtz')

if __name__ == '__main__':
	main ()
