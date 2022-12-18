
import serial ##serial communication with arduino
from threading import Thread
import logging
import time

g_switch = True
g_serial = serial.Serial("COM3", 9600)

def startReading():
    m_lastTimeRecord = ''
    while(g_switch):
##        if m_lastTimeRecord != time.strftime("%I:%M %p"):
        time.sleep(1)
        m_currentReading = g_serial.readline().decode().strip("Current average reading: ").strip("\r\n")
        print(m_currentReading, "-", time.strftime("%I:%M %p"))
        m_lastTimeRecord = time.strftime("%I:%M %p")
        raise

Thread(target = startReading).start()
