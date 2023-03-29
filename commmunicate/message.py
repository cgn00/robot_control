import serial
import time

def send_message(message, port='USB0', baudrate=9600):
    """
    Send the message by serial port
    
    Args:
    ---
    message: str = the message to send
    port: str = the port where is connected the serial device, by deffault is 'USB0'. Also could be 'USB1' or 'ACM0'
    baudrate: int 
    """
    
    port = '/dev/tty' + port
    
    ser = serial.Serial(port, baudrate, timeout=1)
    ser.reset_input_buffer()

    message = message + '\n'
    
    ser.write(message.encode('utf-8'))
    #line = ser.readline().decode('utf-8').rstrip()
    #print(line)
    