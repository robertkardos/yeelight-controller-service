#!/usr/bin/env python

from dasbus.connection import SessionMessageBus

bus = SessionMessageBus()
remote_object = bus.get_proxy(
    "org.example.YeelightBulbController", # The bus name
    "/org/example/YeelightBulbController", # The object path
    "org.example.YeelightBulbController" # The interface
)

remote_object.Toggle()
