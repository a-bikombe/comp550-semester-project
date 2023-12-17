# COMP550 Semester Project

## DESCRIPTION

My semester project is a Python program simulating the packet transfer between two devices. The options for fictional devices that the user can choose from will originate from different cities, and the program will choose the best router to transfer data between the devices, this being the closest and therefore most efficient router between the two cities/devices.

1. User chooses to connect to fictional messaging server.
2. Server randomly assigns user a device and their source city.
3. User chooses one of three options for devices to send a message to.
4. Without typing in message, server determines order of router(s) to send message depending on the source and destination locations.
5. Server acknowledges successfully sent message.

## TESTS

### TEST 1:
`Type [Y/N] to connect to the messaging server: Y`
`Your device is a smartphone in San Francisco, CA`
`Choose the device you'd like to send a message to [1, 2, 3]: 1`
`San Francisco, CA  => First hop:  Phoenix, AZ  => Second hop:  Nashville, TN  =>  Manchester, NH`
`Message successfully sent`

### TEST 2:
`Type [Y/N] to connect to the messaging server: Y`
`Your device is a PC in Austin, TX`
`Choose the device you'd like to send a message to [1, 2, 3]: 2`
`Austin, TX  => First hop:  Phoenix, AZ  =>  San Francisco, CA`
`Message successfully sent`

### TEST 3:
`Type [Y/N] to connect to the messaging server: Y`
`Your device is a PC in San Francisco, CA`
`Choose the device you'd like to send a message to [1, 2, 3]: 3`
`San Francisco, CA  => First hop:  Phoenix, AZ  =>  Austin, TX`
`Message successfully sent`

### TEST 4:
`Type [Y/N] to connect to the messaging server: N`
`Goodbye.`