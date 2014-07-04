import configparser


def load_config():
    with open('/etc/minitrue.ini', 'r') as fd:
        cfg = configparser.ConfigParser()
        cfg.read_file(fd)
        config = cfg.items('minitrue')
    return dict(config)
