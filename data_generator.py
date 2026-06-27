import time
import random

def generate_sensor_hex():
    decimal_reading = random.randint(0, 255)
    hex_reading = hex(decimal_reading)[2:].upper().zfill(2)
    return hex_reading

print("Starting Data Stream... Press Ctrl+C to stop.")

with open("sensor_stream.txt", "w") as file:
    for i in range(20):
        data_point = generate_sensor_hex()
        file.write(data_point + "\n")
        print(f"Generated Hex Data: {data_point}")
        time.sleep(0.5)

print("Data successfully logged to sensor_stream.txt!")