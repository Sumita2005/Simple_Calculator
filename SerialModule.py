import serial

def initConnection(port, baudrate):
  
    try:
        ser = serial.Serial(port, baudrate)
        print("Device connected successfully.")
        return ser
    except :
        print("Failed to connect to the device.")

if __name__ == "__main__":

    ser = initConnection("/dev/ttyACM0", 9600)
