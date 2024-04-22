#!/usr/bin/env python

from yeelight import discover_bulbs, Bulb

from dasbus.server.interface import dbus_interface
from dasbus.typing import Str


data = discover_bulbs()
ip = data[0]["ip"]
bulb = Bulb(ip)

print("==========================")
print("BULB found on IP: ", ip)
print("==========================")


@dbus_interface("org.example.HelloWorld")
class HelloWorld(object):

    def Hello(self, name: Str) -> Str:
        bulb.toggle()
        return "Hello {}!".format(name)

print(HelloWorld.__dbus_xml__)


from dasbus.connection import SessionMessageBus
bus = SessionMessageBus()
bus.publish_object("/org/example/HelloWorld", HelloWorld())
bus.register_service("org.example.HelloWorld")

from dasbus.loop import EventLoop
loop = EventLoop()
loop.run()

