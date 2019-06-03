import datetime
from influxdb import InfluxDBClient
from .Config import Config


class Influx:
    def __init__(self, host: str = None, port: int = None, ssl: bool = False, verify_ssl: bool = False,
                 username: str = None, password: str = None, database: str = None, timeout: int = None,
                 retries: int = None, use_udp: bool = False):
        self._influx = InfluxDBClient(
            host=Config.get('influxdb', 'host') if Config.has_option('influxdb', 'host') else host or None,
            port=Config.getint('influxdb', 'port') if Config.has_option('influxdb', 'port') else port or None,
            ssl=Config.getboolean('influxdb', 'ssl') if Config.has_option('influxdb', 'ssl') else ssl or None,
            verify_ssl=Config.getboolean('influxdb', 'verify') if Config.has_option('influxdb',
                                                                                    'verify') else verify_ssl or None,
            username=Config.get('influxdb', 'username') if Config.has_option('influxdb',
                                                                             'username') else username or None,
            password=Config.get('influxdb', 'password') if Config.has_option('influxdb',
                                                                             'password') else password or None,
            database=Config.get('influxdb', 'database') if Config.has_option('influxdb',
                                                                             'database') else database or None,
            timeout=Config.getint('influxdb', 'port') if Config.has_option('influxdb', 'port') else timeout or None,
            retries=Config.getint('influxdb', 'retries') if Config.has_option('influxdb',
                                                                              'retries') else retries or None,
            use_udp=Config.getboolean('influxdb', 'use_udp') if Config.has_option('influxdb',
                                                                                  'use_udp') else use_udp or None,
            udp_port=Config.getint('influxdb', 'port') if Config.has_option('influxdb', 'port') else port or None
        )

    def generate_data(self, measurement: str, tags: dict, time: datetime.datetime, fields: dict):
        return {"measurement": measurement, "tags": tags, "time": time, "fields": fields}

    def write_points(self, points: list):
        return self._influx.write_points(points=points)
