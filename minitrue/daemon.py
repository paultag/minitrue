from .log import log
from .submit import submit

import datetime as dt
import importlib
import time

CONFIG = {"wifi": "minitrue.plugins.wifi",
          "battery": "minitrue.plugins.battery",}


def run():
    modules = {
        x: importlib.import_module(y) for x, y in CONFIG.items()
    }

    while True:
        payload = {}
        for class_, m in modules.items():
            log("Probing {}".format(class_))
            payload[class_] = m.probe()
            log("Probed  {}".format(class_))
        log("Submitting")
        submit({
            "time": int(dt.datetime.utcnow().timestamp()),
            "data": payload
        })
        time.sleep(3)
