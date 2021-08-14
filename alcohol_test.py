
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)
while True:
    #alcohol= float(5*(1023.0-chan.value)/float(chan.value))
    raw_adc = (chan.value & 0x0F) * 256 + chan1.value
    alcohol = (9.95 / 4096.0) * chan.value + 0.05
    print("Alcohol: ", alcohol)
#print("Raw ADC volt: ", chan.voltage)

'''`

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(0)

# ADC121C_MQ3 address, 0x50(80)
# Read data back from 0x00(00), 2 bytes
# raw_adc MSB, raw_adc LSB
data = bus.read_i2c_block_data(0x50, 0x00, 2)

# Convert the data to 12-bits
raw_adc = (data[0] & 0x0F) * 256 + data[1]
concentration = (9.95 / 4096.0) * raw_adc + 0.05

# Output data to screen
print ("Alcohol Concentration : %.2f mg/l" %concentration)'''