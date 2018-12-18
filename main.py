#!/usr/bin/python3
from os1 import OS1
from os1.utils import xyz_points


def handler(raw_packet):
    """Takes each packet and log it to a file as xyz points"""
    with open('points.csv', 'a') as f:
        x, y, z = xyz_points(raw_packet)
        #for coords in zip(x, y, z):
        #    f.write("{}\n".format(','.join(coords)))
        print(x, y, z)


os1 = OS1('192.168.0.101', '192.168.0.100')  # OS1 sensor IP and destination IP
# Inform the sensor of the destination host and reintialize it
os1.start()
# Start the loop which will handle and dispatch each packet to the handler
# function for processing
os1.run_forever(handler)
