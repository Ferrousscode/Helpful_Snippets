import snap7
import time as clock

import logging
logging.basicConfig(level=logging.INFO)

Logo7=True

plc = snap7.logo.Logo()

logger = logging.getLogger(__name__)

try:
    plc.connect("xxx.xxx.xxx.xxx",0x0300,0x0200) #Fill in IP address
    print("¤¤ Connected ¤¤")
except:
    print("¤¤ Connection failed at init ¤¤")
    logger.info("Connection failed at init")


#Digital Variables

Switch_Manual_Auto = "V528.1"
Switch_Stairs_West_East_North = "V529.0"
Switch_Ramp_West = "V529.1"
Switch_Ramp_East = "V529.2"

OK_Signal_Stairs_West = "V528.2"
OK_Signal_Stairs_Easst = "V528.3"
OK_Signal_Stairs_North = "V528.4"
OK_Signal_Ramp_West = "V528.5"
OK_Signal_Ramp_East = "V528.6"

#Analogue Variables

Temp_Outside_Air = "VW101"
Humidity_Outside_Air = "VW102"
Temp_Ground_1 = "VW103"
Power_Stairs_West = "VW104"
Power_Ramp_West = "VW105"
Power_Ramp_East = "VW106"
Power_Stairs_North = "VW107"
Power_Ramp_East = "VW108"


if plc.get_connected():
    logger.info("Connected")

    plc.read(Temp_Outside_Air)
    plc.write(Switch_Manual_Auto, 1)
    clock.sleep(5)
    plc.write(Switch_Manual_Auto, 0)
    
    
else:
    print("¤¤ Could not connect to PLC ¤¤")
    logger.info("Could not connect to PLC")


plc.disconnect()

if plc.get_connected():
    logger.info("Disconnection failed")
else:
    logger.info("Disconnected from PLC")
    
plc.destroy()
