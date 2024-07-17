#!/usr/bin/python3

import sys
from security import safe_requests

domoticzserver = "192.168.1.36"
idx_temp = "52"

val_temp = sys.argv[3]  # change to sys.argv[5] for calibrated
val_hum = sys.argv[4]
val_bat = sys.argv[6]

val_comfort = "0"
if float(val_hum) < 40:
    val_comfort = "2"
elif float(val_hum) <= 70:
    val_comfort = "1"
elif float(val_hum) > 70:
    val_comfort = "3"

res = safe_requests.get("http://"
    + domoticzserver
    + "/json.htm?type=command&param=udevice&idx="
    + idx_temp
    + "&nvalue=0&svalue="
    + val_temp
    + ";"
    + val_hum
    + ";"
    + val_comfort
    + "&battery="
    + val_bat
)

