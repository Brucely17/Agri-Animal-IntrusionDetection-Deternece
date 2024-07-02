
import serial 
import camSnap
import last
import time 
import datetime  # Import datetime module for timestamp
from pymongo import MongoClient
import mailing 
# Connect to MongoDB
client = MongoClient('mongodb+srv://purushoth170288:Bruce17@cluster0.yfliaq8.mongodb.net/?retryWrites=true&w=majority')
db = client['test']  # Replace 'your_database_name' with your actual database name
collection = db['animal']  # Replace 'your_collection_name' with your actual collection name

arduino = serial.Serial(port='COM11', baudrate=9600, timeout=.1) 
arduino.bytesize = 8   # Number of data bits = 8
arduino.parity = 'N'   # No parity
arduino.stopbits = 1   # Number of Stop bits = 1

# arduino.write(b'A')  

def write_read(): 
    data = arduino.readline() 
    return data 

while True: 
    value = write_read() 
    print(value.decode(), ':', value) # printing the value 
    if value != b'':
        data = {}
        data['angle'] = value.decode()
        data['area'] = 'left'
        data['timestamp'] = datetime.datetime.now()  # Add timestamp
        c = camSnap.camSnsapShot()  
        c = True
        if c:
            directory = r"C:\Users\vijay\OneDrive - SSN Trust\Documents"
            final_result = last.get_final_result(directory, num_files=4)
            print("Final Result:", final_result)
            if final_result == '0':
                data['trespasser'] = 'dog'
            elif final_result == '1':
                data['trespasser'] = 'Person'
            else:
                data['trespasser'] = 'Nothing'
            
            # Insert data into MongoDB collection
            collection.insert_one(data)

            # Encode final_result as string and send to Arduino
            arduino.write(str(final_result).encode())
            print("Encoded:", str(final_result).encode())
            mailing.main()
            # Reset value to empty string
            value = b''

            # Delay to allow Arduino to process the data
            time.sleep(1)
            break
