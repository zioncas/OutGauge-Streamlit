import streamlit as st
import socket
import struct
import math

# Read outgauge data and store it in a dictionary
def read_outgauge_data():
    data, address = sock.recvfrom(96)
    
    # Your code to read the outgauge data and store it in a dictionary
    outgauge_data = {
        "speed": 100,
        "rpm": 5000,
        "turbo": 1.3,
        "engTemp": 100,
        "fuel":12.5,
        "oilPressure":10.0,
        "oilTemp":100.0,
        "throttle":13,
        "brake":13,
        "clutch":13,
    }
    
    #print(data)
    if data[:4] == b'\x00\x00\x00\x00':
    #     # Decode the data packet using the defined format
        packet = struct.unpack('sccffffffffffsi', data[4:56])
        outgauge_data["rpm"] = math.trunc(packet[5])
        outgauge_data["speed"] = math.trunc(packet[4]*2.237)
        outgauge_data["turbo"] = format((packet[6]/0.0689474), '.1f')
        outgauge_data["engTemp"] = format(((packet[7]*9/5)+ 32), '.1f')
        outgauge_data["fuel"] = format((packet[8]*100), '.2f')
        outgauge_data["oilPressure"] = format((packet[9]/0.0689474), '.1f')
        outgauge_data["oilTemp"] = format(((packet[10]*9/5)+ 32), '.1f')
        outgauge_data["throttle"] = math.trunc((packet[11]*100))
        outgauge_data["brake"] = math.trunc((packet[12]*100))
        #outgauge_data["clutch"] = math.trunc(packet[13]*100)
        
    
    return outgauge_data

# Streamlit dashboard
def streamlit_dashboard():
    st.title("Outgauge Data Dashboard")
    
    # Placeholder for speed and rpm values
    speed_placeholder = st.empty()
    rpm_placeholder = st.empty()
    turbo_placeholder = st.empty()
    engTemp_placeholder = st.empty()
    fuel_placeholder = st.empty()
    oilPressure_placeholder = st.empty()
    oilTemp_placeholder = st.empty()
    throttle_placeholder = st.empty()
    brake_placeholder = st.empty()
    clutch_placeholder = st.empty()
    
    
    # Update the data in real-time
    while True:
        outgauge_data = read_outgauge_data()
        
        # Update the placeholders with actual values
        speed_placeholder.text("Speed (Mph): " + str(outgauge_data.get("speed", "")))
        rpm_placeholder.text("RPM: " + str(outgauge_data.get("rpm", "")))
        turbo_placeholder.text("Boost (psi): " + str(outgauge_data.get("turbo", "")))
        engTemp_placeholder.text("Engine Temp (f): " + str(outgauge_data.get("engTemp", "")))
        fuel_placeholder.text("Fuel (%): " + str(outgauge_data.get("fuel", "")))
        oilPressure_placeholder.text("Oil Pressure (Psi): " + str(outgauge_data.get("oilPressure", "")))
        oilTemp_placeholder.text("Oil Temp (f): " + str(outgauge_data.get("oilTemp", "")))
        throttle_placeholder.text("Throttle (%): " + str(outgauge_data.get("throttle", "")))
        brake_placeholder.text("Brake (%): " + str(outgauge_data.get("brake", "")))
        clutch_placeholder.text("Clutch (%): " + str(outgauge_data.get("clutch", "")))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 8888))         
# Run the Streamlit dashboard
if __name__ == "__main__":
    streamlit_dashboard()