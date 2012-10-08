========
rpiSht1x
========
This modules reads Humidity and Temperature from a Sensirion SHT1x sensor. It has been tested
both with an SHT11 and an SHT15.

It is meant to be used in a Raspberry Pi and depends on this module (http://code.google.com/p/raspberry-gpio-python/).

The module raspberry-gpio-python requires root privileges, therefore, to run this module you need to run your script as root.

This a Python/Raspberry Pi port of this library: https://github.com/practicalarduino/SHT1x

Example Usage::

    from sht1x.Sht1x import Sht1x as SHT1x
    dataPin = 11
    clkPin = 7
    sht1x = Sht1x(dataPin, clkPin)
    print(sht1x.read_temperature_C())
    print(sht1x.read_humidity())