# -*- coding: utf-8 -*-

"""Python library module for LIS3MDL magnetometer.
This module for the Raspberry Pi computer helps interface the LIS3MDL
magnetometer.The library makes it easy to read the raw magnetometer
through I²C interface.

The datasheet for the LIS3MDL is available at
[https://www.pololu.com/file/download/LIS3MDL.pdf?file_id=0J1089]
"""

from i2c import I2C
from constants import *


class LIS3MDL(I2C):
    """ Set up and access LIS3MDL magnetometer.
    """

    # Output registers used by the magnetometer
    magnetometer_registers = [
        LIS3MDL_OUT_X_L,  # low byte of X value
        LIS3MDL_OUT_X_H,  # high byte of X value
        LIS3MDL_OUT_Y_L,  # low byte of Y value
        LIS3MDL_OUT_Y_H,  # high byte of Y value
        LIS3MDL_OUT_Z_L,  # low byte of Z value
        LIS3MDL_OUT_Z_H,  # high byte of Z value
    ]

    def __init__(self, bus_id=2):
        """ Set up I2C connection and initialize some flags and values.
        """

        super(LIS3MDL, self).__init__(bus_id)
        self.is_magnetometer_enabled = False

    def __del__(self):
        """ Clean up. """
        try:
            # Power down magnetometer
            self.write_register(LIS3MDL_ADDR, LIS3MDL_CTRL_REG3, 0x03)
            super(LIS3MDL, self).__del__()
        except:
            pass
	
    def enable(self, temp_sens_active=False):
        """ Enable and set up the the magnetometer and determine
            whether to auto increment registers during I2C read operations.
        """

        # Disable magnetometer and temperature sensor first
        self.write_register(LIS3MDL_ADDR, LIS3MDL_CTRL_REG1, 0x00)
        self.write_register(LIS3MDL_ADDR, LIS3MDL_CTRL_REG3, 0x03) # Power-down mode

        # Enable device in continuous conversion mode
        self.write_register(LIS3MDL_ADDR, LIS3MDL_CTRL_REG3, 0x00)

        # Initial value for CTRL_REG1 (wo temperature sensor)
        ctrl_reg1 = 0x00
        
        self.is_temperature_sensor_enable = False
        if temp_sens_active:
            # Initial value for CTRL_REG1 (w temperature sensor)
			 # binary value -> 10000000b, hex value -> 0x80
             ctrl_reg1 = 0x80
             self.is_temperature_sensor_enable = True

        # Ultra-high-performance mode for X and Y
        # Output data rate 10Hz
        # binary value -> 01110000b, hex value -> 0x70
        ctrl_reg1 += 0x70

        # +/- 4 gauss full scale
        self.write_register(LIS3MDL_ADDR, LIS3MDL_CTRL_REG2, 0x00)

        # Ultra-high-performance mode for Z
        # binary value -> 00001100b, hex value -> 0x0c
        self.write_register(LIS3MDL_ADDR, LIS3MDL_CTRL_REG4, 0x0c)

        self.is_magnetometer_enabled = True

        # Write calculated value to the CTRL_REG1 register
        self.write_register(LIS3MDL_ADDR, LIS3MDL_CTRL_REG1, ctrl_reg1)

    def get_magnetometer_raw(self):
        """ Return 3D vector of raw magnetometer data.
        """
        # Check if magnetometer has been enabled
        if not self.is_magnetometer_enabled:
            raise(Exception('Magnetometer is not enabled'))

        return self.read_3d_sensor(LIS3MDL_ADDR, self.magnetometer_registers)
        
    def get_termometer_raw(self):
        """ Return temerature raw value (-40 / + 80)
        """
        # Check if termometer has been enabled
        if not self.is_temperature_sensor_enable:
            raise(Exception('Termometer is not enabled'))
		
        temp_lo_byte = self.read_register(LIS3MDL_ADDR, LIS3MDL_TEMP_OUT_L)
        temp_hi_byte = self.read_register(LIS3MDL_ADDR, LIS3MDL_TEMP_OUT_H)
        return self.combine_signed_lo_hi(temp_lo_byte, temp_hi_byte)		
    
