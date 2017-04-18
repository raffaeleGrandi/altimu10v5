# -*- coding: utf-8 -*-

"""This module contains constants used by the library
"""

# I2C device addresses
LIS3MDL_ADDR = 0x1e      # Magnetometer
LPS25H_ADDR = 0x5d      # Barometric pressure sensor
LSM6DS33_ADDR = 0x6b      # Gyrometer / accelerometer

# LSM6DS33 gyroscope and accelerometer control registers
LSM6DS33_WHO_AM_I = 0x0F  # Returns 0x69 (read only)
LSM6DS33_CTRL1_XL = 0x10  # Acceleration sensor control
LSM6DS33_CTRL2_G = 0x11  # Angular rate sensor (gyroscope) control
LSM6DS33_CTRL3_C = 0x12  # Device/communication settings
LSM6DS33_CTRL4_C = 0x13  # Bandwith/sensor/communication settings
LSM6DS33_CTRL5_C = 0x14  # Rounding/self-test control
LSM6DS33_CTRL6_C = 0x15  # Gyroscope settings
LSM6DS33_CTRL7_G = 0x16  # Gyroscope settings
LSM6DS33_CTRL8_XL = 0x17  # Acceleration sensor settings
LSM6DS33_CTRL9_XL = 0x18  # Acceleration sensor axis control
LSM6DS33_CTRL10_C = 0x19  # Gyroscope axis control / misc. settings

# LSM6DS33 Gyroscope and accelerometer output registers
LSM6DS33_OUTX_L_G = 0x22  # Gyroscope pitch axis (X) output, low byte
LSM6DS33_OUTX_H_G = 0x23  # Gyroscope pitch axis (X) output, high byte
LSM6DS33_OUTY_L_G = 0x24  # Gyroscope roll axis (Y) output, low byte
LSM6DS33_OUTY_H_G = 0x25  # Gyroscope roll axis (Y) output, high byte
LSM6DS33_OUTZ_L_G = 0x26  # Gyroscope yaw axis (Z) output, low byte
LSM6DS33_OUTZ_H_G = 0x27  # Gyroscope yaw axis (Z) output, high byte
LSM6DS33_OUTX_L_XL = 0x28  # Accelerometer pitch axis (X) output, low byte
LSM6DS33_OUTX_H_XL = 0x29  # Accelerometer pitch axis (X) output, high byte
LSM6DS33_OUTY_L_XL = 0x2A  # Accelerometer roll axis (Y) output, low byte
LSM6DS33_OUTY_H_XL = 0x2B  # Accelerometer roll axis (Y) output, high byte
LSM6DS33_OUTZ_L_XL = 0x2C  # Accelerometer yaw axis (Z) output, low byte
LSM6DS33_OUTZ_H_XL = 0x2D  # Accelerometer yaw axis (Z) output, high byte

# Control registers for magnetometer
# Enable device, set operating modes and rates for X and Y axes
LIS3MDL_CTRL_REG1 = 0x20
LIS3MDL_CTRL_REG2 = 0x21   # Set gauss scale
LIS3MDL_CTRL_REG3 = 0x22   # Set operating/power modes
LIS3MDL_CTRL_REG4 = 0x23   # Set operating mode and rate for Z-axis

# Output registers for magnetometer
LIS3MDL_OUT_X_L = 0x28   # X output, low byte
LIS3MDL_OUT_X_H = 0x29   # X output, high byte
LIS3MDL_OUT_Y_L = 0x2A   # Y output, low byte
LIS3MDL_OUT_Y_H = 0x2B   # Y output, high byte
LIS3MDL_OUT_Z_L = 0x2C   # Z output, low byte
LIS3MDL_OUT_Z_H = 0x2D   # Z output, high byte

# Gyroscope dps/LSB for 1000 dps full scale
GYRO_GAIN = 35.0

# Accelerometer conversion factor for +/- 4g full scale
ACCEL_CONVERSION_FACTOR = 0.122
