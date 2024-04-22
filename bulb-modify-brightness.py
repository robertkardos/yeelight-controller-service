#!/usr/bin/env python

import sys
from dasbus.connection import SessionMessageBus

bus = SessionMessageBus()
remote_object = bus.get_proxy(
	"org.example.YeelightBulbController", # The bus name
	"/org/example/YeelightBulbController", # The object path
	"org.example.YeelightBulbController" # The interface
)

remote_object.ModifyBrightness(int(sys.argv[1]))
