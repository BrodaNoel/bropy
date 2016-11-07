# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MS5611_01BXXX
# This code is designed to work with the MS5611_01BXXX_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Analog-Digital-Converters?sku=MS5611-01BXXX_I2CS_A01#tabs-0-product_tabset-2
# Taken form https://github.com/ControlEverythingCommunity/MS5611-01BXXX/blob/master/Python/MS5611_01BXXX.py
# Code modified by Broda Noel (@BrodaNoel in all social networks)

import smbus
import time
import sys

# Get I2C bus
bus = smbus.SMBus(1)
address = 0x77

# MS5611_01BXXX address, 0x77(118)
#		0x1E(30)	Reset command
bus.write_byte(address, 0x1E)

time.sleep(0.5)

# Read 12 bytes of calibration data
# Read pressure sensitivity
data = bus.read_i2c_block_data(address, 0xA2, 2)
C1 = data[0] * 256 + data[1]

# Read pressure offset
data = bus.read_i2c_block_data(address, 0xA4, 2)
C2 = data[0] * 256 + data[1]

# Read temperature coefficient of pressure sensitivity
data = bus.read_i2c_block_data(address, 0xA6, 2)
C3 = data[0] * 256 + data[1]

# Read temperature coefficient of pressure offset
data = bus.read_i2c_block_data(address, 0xA8, 2)
C4 = data[0] * 256 + data[1]

# Read reference temperature
data = bus.read_i2c_block_data(address, 0xAA, 2)
C5 = data[0] * 256 + data[1]

# Read temperature coefficient of the temperature
data = bus.read_i2c_block_data(address, 0xAC, 2)
C6 = data[0] * 256 + data[1]

# MS5611_01BXXX address, 0x77(118)
#		0x40(64)	Pressure conversion(OSR = 256) command
bus.write_byte(address, 0x40)

time.sleep(0.5)

# Read digital pressure value
# Read data back from 0x00(0), 3 bytes
# D1 MSB2, D1 MSB1, D1 LSB
value = bus.read_i2c_block_data(address, 0x00, 3)
D1 = value[0] * 65536 + value[1] * 256 + value[2]

# MS5611_01BXXX address, 0x77(118)
#		0x50(64)	Temperature conversion(OSR = 256) command
bus.write_byte(address, 0x50)

time.sleep(0.5)

# Read digital temperature value
# Read data back from 0x00(0), 3 bytes
# D2 MSB2, D2 MSB1, D2 LSB
value = bus.read_i2c_block_data(address, 0x00, 3)
D2 = value[0] * 65536 + value[1] * 256 + value[2]

dT = D2 - C5 * 256
TEMP = 2000 + dT * C6 / 8388608
OFF = C2 * 65536 + (C4 * dT) / 128
SENS = C1 * 32768 + (C3 * dT) / 256
T2 = 0
OFF2 = 0
SENS2 = 0

if TEMP >= 2000 :
	T2 = 0
	OFF2 = 0
	SENS2 = 0
else :
	T2 = (dT * dT) / 2147483648
	OFF2 = 5 * ((TEMP - 2000) * (TEMP - 2000)) / 2
	SENS2 = 5 * ((TEMP - 2000) * (TEMP - 2000)) / 4
	if TEMP < -1500 :
		OFF2 = OFF2 + 7 * ((TEMP + 1500) * (TEMP + 1500))
		SENS2 = SENS2 + 11 * ((TEMP + 1500) * (TEMP + 1500)) / 2

TEMP = TEMP - T2
OFF = OFF - OFF2
SENS = SENS - SENS2
pressure = ((((D1 * SENS) / 2097152) - OFF) / 32768.0) / 100.0
cTemp = TEMP / 100.0
altitude = (1 - (pressure / 1013.25)**0.190284) * 44307.69396

# Output data to screen
# PRESSURE: mbars
# TEMPERATURE: Celsius
# ALTITUDE: Meters
sys.stdout.write('{"pressure": ' + str(pressure) + ', "temperature": ' + str(cTemp) + ', "altitude": ' + str(altitude) + '}')
