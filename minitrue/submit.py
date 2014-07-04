import requests
from requests.exceptions import ConnectionError

import os
import glob
import json
from itertools import chain

from .core import load_config
from .log import log

config = load_config()
API_BASE = "http://{host}/v1/devices/{name}/"
CACHE_ROOT = "/var/lib/minitrue/"
GLOB = "{}/*json".format(CACHE_ROOT)


def submit(data):
    try:
        update(chain(backlog(), [data]))
        purge_cache()
    except (ConnectionError, ValueError):
        cache(data)


def purge_cache():
    for fp in glob.glob(GLOB):
        log("Removing: {}".format(fp))
        os.unlink(fp)


def update(datas):
    response = requests.post(
        API_BASE.format(**config),
        data={
            "upload": json.dumps(list(datas)),
            "config": json.dumps(config),
        },
    )
    if int(response.status_code) != 200:
        print(response.text)
        log("Bad status: {}".format(response.status_code))
        raise ValueError("Badstatus.")


def cache(data):
    log("Caching: {}".format(data['time']))
    with open("{}/{}.json".format(
        CACHE_ROOT,
        data['time']
    ), 'w') as fd:
        fd.write(json.dumps(data))


def backlog():
    for fp in glob.glob(GLOB):
        with open(fp, 'r') as fd:
            yield json.load(fd)
