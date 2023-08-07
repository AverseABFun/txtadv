"""Sending multiplayer events"""

from txtadv.multiplayer import SERVER
import txtadv
import requests
import json

def SendEvent(event: txtadv.Event) -> bool:
    if not event==txtadv.Event:
        raise TypeError("event is incorrect type, expected txtadv.Event")
    data = requests.post(SERVER + "/event/" + event.__name__)
    return json.loads(data).response
