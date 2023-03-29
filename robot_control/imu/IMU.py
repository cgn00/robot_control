from mpu6050 import mpu6050
from time import sleep
import threading
from commmunicate import message

def get_measurement(address):
    sensor = mpu6050(address=address)
    accelerometer_data = sensor.get_accel_data()
    gyroscope_data = sensor.get_gyro_data()
    measurement = dict(accele=accelerometer_data, giros=gyroscope_data)
    return measurement
    
def run(timer = 3, address = 0x68):
    """Execute in a thread the measurement of the MPU6050 Sensor every timer value in seconds

    Args:
        timer (int): The value of the sampling time. Defaults to 1 second.
        address (int): The addres of the I2C MPU6050. Defaults to 0x68
    """
        
    thread = threading.Timer(timer, run) # wait 1 second to execute the thread 
    thread.start()
    
    measurement = get_measurement(address).__str__()
    message.send_message(message=measurement)
    #print(measurement)

