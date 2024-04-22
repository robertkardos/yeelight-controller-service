#!/usr/bin/env python

import dasbus

from dasbus.connection import SessionMessageBus
bus = SessionMessageBus()

# Create an object that will be a proxy for a particular remote object.
remote_object = bus.get_proxy(
    "org.example.HelloWorld",  # The bus name
    "/org/example/HelloWorld",  # The object path
    "org.example.HelloWorld" # The interface
)

# Call the Introspect method of the remote object.
print(remote_object.Hello("QWEQWE"))
