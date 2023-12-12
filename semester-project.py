"""
Author: Arianna Bikombe
Date: December 11, 2023
Purpose: Simulation of packet transfer between two devices
"""

import random

#  The options for fictional devices that the user can choose from will originate from different cities, and the program will choose the best router to transfer data between the devices, this being the closest and therefore most efficient router between the two cities/devices.

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
router1 = "";
router2 = "";

# Send packets (user input for which city they are in (randomly choose between 3 cities to assign to user's device) and which they are sending to (choose between 3 - 1 device in each city))
def connect():
	connect = input("Type [Y/N] to connect to the messaging server: ");
	if connect == "Y":
		source_device = random.choices(devices);
		source_city = random.choices(cities);
		print("Your device is a ", source_device, " in ", source_city);
		source_device_city = [source_device, source_city];
		return source_device_city;
	elif connect == "N":
		print("Goodbye.");
		return 0;
	else:
		print("Incorrect input.")
		return 0;
	

def send():
	chosen_device = input("Choose the device you'd like to send a message to: ");
	return chosen_device;

def receive(device, city):
	return 0;

source_device_city = connect();

if source_device_city != 0:
	dest_device = send();

	# If statement that connects device to respective city
	if dest_device == "Device 1":
		city = city1;
	elif dest_device == "Device 2":
		city = city2;
	elif dest_device == "Device 3":
		city = city3;

	receive(dest_device, city);