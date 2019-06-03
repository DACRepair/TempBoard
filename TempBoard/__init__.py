import datetime
import urllib3
from .Config import Config
from .Serial import Serial
from .InfluxDB import Influx
from .Middleware import sensor_name, c_to_f, filter_sensors


class App:
    def __init__(self):
        self.serial = Serial()
        self.influx = Influx()
        urllib3.disable_warnings()

    def process_data(self, data):
        points = []
        data = filter_sensors(data)
        for sensor in data:
            points.append(self.influx.generate_data(
                measurement="temperature",
                tags=dict(**{o: Config.get('influxtags', o) for o in Config.options('influxtags')},
                          name=sensor_name(sensor['sensor']), sid=sensor['sensor']),
                time=datetime.datetime.utcnow(),
                fields={
                    'fahrenheit': round(c_to_f(sensor['temp']), 2),
                    'celsius': sensor['temp']
                }
            ))
        if Config.getboolean('app', 'testing'):
            print(points)
        else:
            if Config.getboolean('app', 'debug'):
                print(points)
            self.influx.write_points(points)

    def run(self):
        self.serial.poll(self.process_data)
