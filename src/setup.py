from setuptools import setup, find_packages

setup(
    name = 'bbSht1x',
    version = '1.3',
    author = 'Luca Nobili and Tomas \'Jethro\' Pokorny',
    author_email = 'xtompokAT_MARKgmailDOTcom',
    packages = find_packages(),
    license = 'LICENSE.txt',
    description = 'Reads Humidity and Temperature from a Sensirion SHT1x sensor.',
    long_description = open('README.txt').read(),
    keywords = "BeagleBone Black SHT15 SHT11 SHT1x Humidity Temperature GPIO",
    url = "",
    install_requires = "Adafruit_BBIO.GPIO>=1.0.0",
)
