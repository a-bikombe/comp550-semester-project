"""
Author: Arianna Bikombe
Date: December 11, 2023
Purpose: Simulation of packet transfer between two devices
"""

import random

# Cities
city1 = "Manchester, NH";
city2 = "San Francisco, CA";
city3 = "Austin, TX";
cities = [city1, city2, city3];

# Devices
device1 = "PC";
device2 = "desktop computer";
device3 = "smartphone";
devices = [device1, device2, device3];

# Routers
router1 = "Nashville, TN";
router2 = "Phoenix, AZ";
routers = [];

def connect():
	connect = input("Type [Y/N] to connect to the messaging server: ");
	if connect == "Y":
		source_device = str(random.choices(devices)).strip(" '[]");
		source_city = str(random.choices(cities)).strip(" '[]");
		print("Your device is a", source_device, "in", source_city);
		source_device_city = [source_device, source_city];
		return source_device_city;
	elif connect == "N":
		print("Goodbye.");
		return 0;
	else:
		print("Incorrect input.")
		return 0;

def send():
	chosen_device = input("Choose the device you'd like to send a message to [1, 2, 3]: ");
	return chosen_device;

def receive(source_device_city, city):
	source_city = str(source_device_city[1]).strip(" '[]");
	if source_city == city1:
		if city == city1 or city == city3:
			first_hop = router1;
			second_hop = 0;
		elif city == city2:
			first_hop = router1;
			second_hop = router2;
		else:
			return "Error: City 1";
	elif source_city == city2:
		if city == city1:
			first_hop = router2;
			second_hop = router1;
		elif city == city2 or city == city3:
			first_hop = router2;
			second_hop = 0;
		else:
			return "Error: City 2";
	elif source_city == city3:
		if city == city1:
			first_hop = router1;
			second_hop = 0;
		elif city == city2 or city == city3:
			first_hop = router2;
			second_hop = 0;
		else:
			return "Error: City 3";
	else:
		return "Error comparing to city";

	routers = [first_hop, second_hop];

	if second_hop == 0:
		print(source_city, " => First hop: ", first_hop, " => ", city)
	else:
		print(source_city, " => First hop: ", first_hop, " => Second hop: ", second_hop, " => ", city)
	return routers;

def acknowledgement():
	acknowledgement = "Message successfully sent";
	return acknowledgement;

source_device_city = connect();

if source_device_city != 0:
	dest_device = send();

	# If statement that connects device to respective city
	if dest_device == "1":
		city = city1;
	elif dest_device == "2":
		city = city2;
	elif dest_device == "3":
		city = city3;

	if receive(source_device_city, city):
		print(acknowledgement());
	else:
		print("Error sending message");