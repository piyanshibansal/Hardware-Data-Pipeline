import time
import math

def generate_sine_hex(step):
    # Create a smooth sine wave value between 0 and 255
    # math.sin needs radians. We scale it so it stays positive
    raw_value = int((math.sin(step * 0.5) + 1) * 127.5)
    
    # Convert to 8-bit Hex string
    hex_reading = hex(raw_value)[2:].upper().zfill(2)
    return hex_reading

print("Starting Realistic Wave Data Stream...")

with open("sensor_stream.txt", "w") as file:
    # Let's generate 40 data points this time to see the wave
    for step in range(40):
        data_point = generate_sine_hex(step)
        file.write(data_point + "\n")
        print(f"Step {step} | Generated Hex Wave Point: {data_point}")
        time.sleep(0.2)

print("Wave data successfully logged to sensor_stream.txt!")