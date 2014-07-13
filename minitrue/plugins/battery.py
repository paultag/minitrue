

def vread(end):
    def vread_f(what):
        return float(open("/sys/class/power_supply/%s/%s" % (
            end,
            what
        ), 'r').read())

    try:
        maxv = vread_f('charge_full')
        curv = vread_f('charge_now')
    except IOError:
        maxv = vread_f('energy_full')
        curv = vread_f('energy_now')

    return (curv / maxv) * 100


def probe():
    return [
        {"name": "BAT0",
         "value": vread("BAT0")},
    ]
