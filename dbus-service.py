#!/usr/bin/env python

from yeelight import discover_bulbs, Bulb
from dasbus.server.interface import dbus_interface
from dasbus.typing import Int

data = discover_bulbs()
print("==========================")
print("BULB data: ", data)
print("==========================")
ip = data[0]["ip"]
bulb = Bulb(ip)
print("==========================")
print("BULB found on IP: ", ip)
print("==========================")
bulbProperties = bulb.get_properties()
print("==========================")
print("BULB: ", bulbProperties)
print("==========================")

@dbus_interface("org.example.YeelightBulbController")
class YeelightBulbController(object):
	def Toggle(self):
		bulb.toggle()

	def ModifyBrightness(self, addBrightnessValue: Int):
		bulbProperties = bulb.get_properties()
		newBrightness = int(bulbProperties["bright"]) + addBrightnessValue
		print("modify brightness to ", newBrightness)
		bulb.set_brightness(newBrightness)

	def ModifyColorTemp(self, addColorTempValue: Int):
		bulbProperties = bulb.get_properties()
		newColorTemp = int(bulbProperties["ct"]) + addColorTempValue
		print("modify color temp to ", newColorTemp)
		bulb.set_color_temp(newColorTemp)

# print(YeelightBulbController.__dbus_xml__)

from dasbus.connection import SessionMessageBus
bus = SessionMessageBus()
bus.publish_object("/org/example/YeelightBulbController", YeelightBulbController())
bus.register_service("org.example.YeelightBulbController")

from dasbus.loop import EventLoop
loop = EventLoop()
loop.run()

