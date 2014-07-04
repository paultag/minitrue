from gi.repository import NetworkManager, NMClient

nmc = NMClient.Client.new()
devs = nmc.get_devices()


def ap_info(ap, active_bssid):
    frequency = ap.get_frequency()
    return {
        "ssid": ap.get_ssid(),
        "bssid": ap.get_bssid(),
        "frequency": frequency,
        "channel": NetworkManager.utils_wifi_freq_to_channel(frequency),
        "strength": ap.get_strength(),
        "associated": active_bssid == ap.get_bssid(),
    }


def probe():
    payload = []
    for dev in devs:
        if dev.get_device_type() == NetworkManager.DeviceType.WIFI:
            active_ap = dev.get_active_access_point()
            for ap in dev.get_access_points():
                payload.append(ap_info(ap, ap.get_bssid()))
    return payload
