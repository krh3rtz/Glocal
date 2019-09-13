# Glocal
A public IP addresses geo-localization script.

Glocal is a small application coded in Python 3.4, used to produce KML files
in order to geo locate ip addresses on the globe.

This application has been built using some great projects:

[+] Pygeoip (2014, Jennifer Ennis, William Tisäter. ):

-> pygeoip.readthedocs.io/en/v0.3.2/

[+] Maxmind GeoIp free database (2012-2017 MaxMind, Inc. All Rights Reserved.):

-> http://dev.maxmind.com/geoip/geoip2/geolite2/

NOTE: The database has changed. However I uploaded it to the "database" folder in
the project.

[+] Shodan.io (2013-2017, Shodan®):

-> https://www.shodan.io

[+] Censys.io (2016 Regents of the University of Michigan)

-> https://www.censys.io

[+] Special Thanks to Google.

------------------------------------------------------------------------------------------

[+] USAGE [+]

Glocal obtains information from public IP addresses and creates a KML extension file
that can be visualized on Google Earth.

To produce this KML file, Glocal uses a txt file which contains a list of public
IP addresses. The structure of this file is:

	eg.

	192.168.1.1
	192.168.1.1
	192.168.1.1
	192.168.1.1
	192.168.1.1

Once this file is specified you can start the script:

	sudo ./glocal.py -F addresses.txt


The output of this will be under "KML" folder so Don't Delete It.

One of the features that Glocal has is the seclusion of pin points by color. Depending
on the IPs continent it will show a specific color. These are:

	America        	-> 	Green
	Africa         	-> 	Yellow
	Europe         	-> 	Blue
	Asia           	-> 	Red
	Oceania        	-> 	White
	Antartic       	-> 	Purple
	None		->	Pink-pushpin

This helps to better identify IPs.

The information that is provided by Glocal is:

	country code
	country name
	city
	region code
	area code
	postal code
	time zone
	longitude
	latitude

[+] Added to it, it offers two direct links to 'Shodan.io' and 'Censys.oi' sites to provide
more information about the IP addresses.

------------------------------------------------------------------------------------------
[+] TROUBLE SHOOTING [+]


[!] If you need any help, type:
	
	sudo ./glocal.py --help

	or

	sudo ./glocal.py --usage

[!] This project has been developed  in Python 3.4, yet it also works on python 3.5.

[!] Make sure you have 'guzip' installed on your system.

[!] Make sure you run the 'configure.py' binary to install both the Python modules and the Database.

	eg.
	sudo ./configure.py
		
		or
		
	sudo python3.4 ./configure.py

[!] If you can't get the software to run, maybe you have other Python versions. Insuch a case specify the version of Python before calling the script:

	eg.

	sudo python3.4 glocal.py -F addresses.txt


PLEASE USE VIRTUALENV!

Created by:
									
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


    Happy hacking.
    
