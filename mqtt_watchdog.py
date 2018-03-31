#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as paho   # pip install paho-mqtt
import time
import socket
import random
import json
import os

hostname = socket.gethostname()

clientid = 'jp-%s-%s' % (hostname, os.getpid())

mqttc = paho.Client(clientid, clean_session=False, userdata=None)
mqttc.connect("127.0.0.1", 1883, 60)

def payload():
	sinewave = [
	64,   66,   67,   69,   70,   72,   73,   75,
	76,   78,   79,   81,   82,   84,   85,   87,
	88,   90,   91,   92,   94,   95,   96,   98,
	99,  100,  102,  103,  104,  105,  106,  107,
	109,  110,  111,  112,  113,  114,  115,  116,
	116,  117,  118,  119,  120,  120,  121,  122,
	122,  123,  123,  124,  124,  125,  125,  125,
	126,  126,  126,  127,  127,  127,  127,  127,
	127,  127,  127,  127,  127,  127,  126,  126,
	126,  125,  125,  125,  124,  124,  123,  123,
	122,  122,  121,  120,  120,  119,  118,  117,
	116,  116,  115,  114,  113,  112,  111,  110,
	109,  107,  106,  105,  104,  103,  102,  100,
	99,   98,   96,   95,   94,   92,   91,   90,
	88,   87,   85,   84,   82,   81,   79,   78,
	76,   75,   73,   72,   70,   69,   67,   66,
	64,   62,   61,   59,   58,   56,   55,   53,
	52,   50,   49,   47,   46,   44,   43,   41,
	40,   38,   37,   36,   34,   33,   32,   30,
	29,   28,   26,   25,   24,   23,   22,   21,
	19,   18,   17,   16,   15,   14,   13,   12,
	12,   11,   10,    9,    8,    8,    7,    6,
	6,    5,    5,    4,    4,    3,    3,    3,
	2,    2,    2,    1,    1,    1,    1,    1,
	1,    1,    1,    1,    1,    1,    2,    2,
	2,    3,    3,    3,    4,    4,    5,    5,
	6,    6,    7,    8,    8,    9,   10,   11,
	12,   12,   13,   14,   15,   16,   17,   18,
	19,   21,   22,   23,   24,   25,   26,   28,
	29,   30,   32,   33,   34,   36,   37,   38,
	40,   41,   43,   44,   46,   47,   49,   50,
	52,   53,   55,   56,   58,   59,   61,   62,
	]

	for item in sinewave:
		#print(item)
		text = "Sinewave %s" % (item)
		data = {
		'host'      : hostname,
		'short_message' : text,
		'application': 'Sinewave',
		'value'   : item,
		}
		mqttc.publish('topic/test', json.dumps(data))


def run():
    while True:
        time.sleep(60)
        payload()

if __name__ == "__main__":
	run()