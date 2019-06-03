from TempBoard.Config import Config


def c_to_f(c: float):
    return c * 1.8 + 32


def sensor_name(sensor):
    if not Config.has_section('sensors'):
        Config.add_section('sensors')
    if not Config.has_option('sensors', sensor):
        Config.set('sensors', sensor, sensor)

    return Config.get('sensors', sensor) or sensor


def filter_sensors(sensors: list):
    ids = []
    retr = []
    for sensor in sensors:
        if sensor['sensor'] not in ids:
            ids.append(sensor['sensor'])
            retr.append(sensor)
    return retr
