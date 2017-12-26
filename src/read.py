from sht1x.Sht1x import Sht1x as SHT1x
dataPin = "P9_23"
clkPin = "P9_27"
sht1x = SHT1x(dataPin, clkPin)

temperature = sht1x.read_temperature_C()
humidity = sht1x.read_humidity()
dewPoint = sht1x.calculate_dew_point(temperature, humidity)

print("Temperature: {} Humidity: {} Dew Point: {}".format(temperature, humidity, dewPoint))  
