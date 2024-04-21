#!/usr/bin/env python

import dasbus

from dasbus.connection import SessionMessageBus
bus = SessionMessageBus()

# Create an object that will be a proxy for a particular remote object.
remote_object = bus.get_proxy(
    "org.freedesktop.Notifications",  # The bus name
    "/org/freedesktop/Notifications",  # The object path
    # "org.freedesktop.DBus.Introspectable" # The interface
    "org.freedesktop.Notifications" # The interface
)

# Call the Introspect method of the remote object.
print(remote_object.Notify("asdasd", 0, "important", "Notification title!!!", "get nofitied scrub", [], [], 0))


# <method name="Notify">
#       <arg type="s" name="arg_0" direction="in">
#       </arg>
#       <arg type="u" name="arg_1" direction="in">
#       </arg>
#       <arg type="s" name="arg_2" direction="in">
#       </arg>
#       <arg type="s" name="arg_3" direction="in">
#       </arg>
#       <arg type="s" name="arg_4" direction="in">
#       </arg>
#       <arg type="as" name="arg_5" direction="in">
#       </arg>
#       <arg type="a{sv}" name="arg_6" direction="in">
#       </arg>
#       <arg type="i" name="arg_7" direction="in">
#       </arg>
#       <arg type="u" name="arg_8" direction="out">
#       </arg>
#     </method>