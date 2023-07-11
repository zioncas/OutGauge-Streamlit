# OutGauge-Streamlit

# What is OutGauge
OutGauge is a vehicle-simulator-focused packet specification that was developed for the game Live For Speed. The BeamNG team has implemented it in their game as well, which is what this project targets. Source (https://github.com/fuelsoft/out-gauge-cluster)

# Tech Stack
This project uses Python for the backend and frontend.

# How to run
-------BeamNg's Side--------
1. Back up your current outgauge.lua file
2. Replace BeamNg's script with the modified one.
3. Run the game
4. Press esc and go to the settings
5. Navigate to other and enable Outgauge support
6. Leave the ip as 127.0.0.1 but ensure that the port matches the port in the python file

-------Python's Sise--------
1. Install Streamlit. Link: https://docs.streamlit.io/library/get-started/installation
2. open the CMD.exe from Anaconda (Reference streamlit installation)
3. Navigate to where you have dashbeam.py located
4. type "streamlit run dashbeam.py"
   *At this point the browser should open with the dashboard open*
