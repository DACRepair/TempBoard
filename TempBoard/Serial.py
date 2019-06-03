import serial
from .Config import Config
from bitstring import BitArray
from io import BytesIO


class Serial:
    _buffer = BytesIO()
    _sepr = b'\x91'
    _delim = b'\x92'
    _term = b'\x23'

    def __init__(self, port: str = None, baud: int = None):
        self._port = port or Config.get('serial', 'port') or 'COM1'
        self._baud = baud or Config.get('serial', 'baud') or 115200

    def get_port(self):
        return serial.Serial(self._port, self._baud)

    def parse_buffer(self):
        data = self._buffer.getvalue().replace(self._term, b'').rstrip(self._delim).split(self._delim)
        sensor_data = []
        for sensor_raw in data:
            address, temp = sensor_raw.split(self._sepr)
            address = "".join([char for char in ["%02X" % char for char in address] if char != '00'])
            temp = BitArray(bytes([char for char in temp])).uint / 128
            sensor_data.append({"sensor": address, "temp": round(temp, 2)})
        self._buffer.truncate(0)
        self._buffer.seek(0)
        return sensor_data

    def poll(self, write_callable: callable = print):
        with self.get_port() as port:
            while port.is_open:
                chunk = port.read()
                self._buffer.write(chunk)
                if self._buffer.getvalue().endswith(self._term):
                    write_callable(self.parse_buffer())
