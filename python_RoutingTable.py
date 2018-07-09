#!/usr/bin/python

import HTML
import csv
from netmiko import ConnectHandler

routes = ['','','','','','']
	 
'''
Let's read the CSV file and connect to all devices listed in the CSV file
'''
with open("devices.csv") as f:
	reader = csv.reader(f)
	data = [r for r in reader]


'''
Let's iterate through the list , connect to each router and print out the # of routes
'''

htmlcode = HTML.Table(header_row=['Router','Total','Connected','Static','OSPF','BGP'])


for item in data:
	print item[1]

	routes[0] = item[0]

	'''
	Connect to Cisco IOS router
	'''
	connect = ConnectHandler(device_type='cisco_ios',ip=item[1],username='test',password='test')
	out = connect.send_command("show ip route", use_textfsm=True)

	'''
	Print out the Total number of routes (Excluding the L type of routes)
	'''
	fil = [elem for elem in out if elem['protocol'] != 'L']
	print "Total routes: " + str(len(fil))
	routes[1] = str(len(fil))

	'''
	Print out the number of Connected routes
	'''
	fil = [elem for elem in out if elem['protocol'] == 'C']
	print "Number of Connected routes: " + str(len(fil))
	routes[2] = str(len(fil))

	'''
	Print out the number of Static routes
	'''
	fil = [elem for elem in out if elem['protocol'] == 'S']
	print "Number of Static routes: " + str(len(fil))
	routes[3] = str(len(fil))

	'''
	Print out the number of OSPF routes
	'''
	fil = [elem for elem in out if elem['protocol'] == 'O']
	print "Number of OSPF routes: " + str(len(fil))
	routes[4] = str(len(fil))

	'''
	Print out the number of BGP routes
	'''
	fil = [elem for elem in out if elem['protocol'] == 'B']
	print "Number of BGP routes: " + str(len(fil))
	routes[5] = str(len(fil))

	###############################################################
	'''
	Let's write the output into HTML file 
	'''
	print routes
	#htmlcode.rows.append(routes)
	htmlcode.rows.append([routes[0],routes[1],routes[2],routes[3],routes[4],routes[5]])

htmlfile = 'Routing_table.html'
f = open(htmlfile,'w')
f.write(str(htmlcode))	 	

