# TempBoard
'TempBoard' is a program that polls a serial port for a custom OneWire multiplexer into an InfluxDB TSDB for metrics and reporting.

### Setup:
> This has been developed and tested on Python 3.6.x
> It should work fine on other versions, however this is the supported version.

Setup is done by installing python on your flavor of Linux or Windows, and cloning the repository to a location on a disk.

Once this has been done, all configuration is done via the `config.ini` file  located in the root of the application (the .default can be copied for reference).

config.ini:
```ini
[app]
testing = True  # Testing disables the sending of data to InfluxDB
debug = True    # Debug enables the sending of information to console. Only applys when testing is False

[serial]
port = COM1 or /dev/serial0 # This is set to whatever the serial port may be.
baud = 115200 # This should match the baud rate on the multiplexer

[influxdb]
host = 127.0.0.1 # InfluxDB host
port = 8086 # InfluxDB port
ssl = True # InfluxDB use ssl
verify = False # InfluxDB verify ssl (IE self signed)
username = admin 
password = admin
database = test
timeout = 300
retries = 3
use_udp = False # if UDP is yes, the "port" directive becomes the UDP port, default 4444

[influxtags]
region = homelab
host = temp-monitor

[sensors]
1234 = Intake
# This section maps the OneWire ID to a canonical name.
```

Once this has been configured, then execution is as simple as running `app.py`.

### Service
#### Linux:

I have included an example SystemD config in the extra folder that can be copied into `/etc/systemd/system/tempboard.service`.
This is designed to work the the Raspberry Pi, however this should work on most linux distros.

#### Windows:
I would use NSSM. You can get it here: https://nssm.cc/