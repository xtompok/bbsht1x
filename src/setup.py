from setuptools import setup, find_packages

setup(
    name = 'rpiSht1x',
    version = '1.3',
    author = 'Luca Nobili',
    author_email = 'lunobiliAT_MARKyahooDOTit',
    packages = find_packages(),
    license = 'LICENSE.txt',
    description = 'Reads Humidity and Temperature from a Sensirion SHT1x sensor.',
    long_description = open('README.txt').read(),
    keywords = "Raspberry Pi RaspberryPi SHT15 SHT11 SHT1x Humidity Temperature GPIO",
    url = "https://bitbucket.org/lunobili/rpisht1x/overview",
    install_requires = "RPi.GPIO>=0.5.9",
)
