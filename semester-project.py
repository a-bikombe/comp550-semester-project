"""
Author: Arianna Bikombe
Date: December 11, 2023
Purpose: Simulation of packet transfer between two devices
"""

#  The options for fictional devices that the user can choose from will originate from different cities, and the program will choose the best router to transfer data between the devices, this being the closest and therefore most efficient router between the two cities/devices.

# Cities
city1 = "Manchester, NH";
city2 = "San Francisco, CA";
city3 = "Austin, TX";

# Devices
device1 = "PC";
device2 = "desktop computer";
device3 = "smartphone";

# Routers
router1 = 0;
router2 = 0;

# Send packets (user input for which city they are in (randomly choose between 3 cities to assign to user's device) and which they are sending to (choose between 3 - 1 device in each city))


def send():
	# "Y/N to connect to server"
	# Acknowledgement print: "Your device is a [device1/2/3] in [city1/2/3]"
	chosen_device = input("Choose the device you'd like to send a message to: ");
	return chosen_device;

def receive(device, city):

	return 0;

dest_device = send();

# If statement that connects device to respective city
if dest_device == "Device 1":
	city = city1;
elif dest_device == "Device 2":
	city = city2;
elif dest_device == "Device 3":
	city = city3;

receive(dest_device, city);