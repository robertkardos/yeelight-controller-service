#!/usr/bin/env python

from dasbus.server.interface import dbus_interface
from dasbus.typing import Str

@dbus_interface("org.example.HelloWorld")
class HelloWorld(object):

    def Hello(self, name: Str) -> Str:
        return "Hello {}!".format(name)

print(HelloWorld.__dbus_xml__)


from dasbus.connection import SessionMessageBus
bus = SessionMessageBus()
bus.publish_object("/org/example/HelloWorld", HelloWorld())
bus.register_service("org.example.HelloWorld")

from dasbus.loop import EventLoop
loop = EventLoop()
loop.run()

