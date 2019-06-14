'''Active network connection identifier

    Checks the opened network ports then search
    for the applications that use that port'''


print('Importing the libraries')
from os import popen as ilPopen
from time import sleep as ilDelay
from re import sub as ilRegexReplace

print('Getting running tasks')
g_ActiveConnections = ilPopen('netstat -a').read().strip().split('\n')          ##get all the active network connections
g_ActiveApplicationList = ilPopen('tasklist').read().strip().split('\n')[2:]    ##get all the active application

print('Declaring containers')
g_ActiveConnectionList = []
g_AppsWithActiveConnection = []

g_portList = []                 ##opened ports that are currently in used
g_PIDList = []                  ##program ID list
g_applicationPIDDict = {}       ##Program name that corresponds to their ID (UNSORTED)

g_maxStrLength = 0

print('Starting the procedures\n')
##get all the active connections
print('Getting the active connections')
for t_line in g_ActiveConnections[2:]:
    g_ActiveConnectionList.append( ilRegexReplace('\s\s+', ',' ,t_line.strip()).split(',') )

##extract only the ports for each active connection
##rfind finds the last instance of a char in a str
print('Getting a list of active ports')
for t_connection in g_ActiveConnectionList[1:]:
    g_portList.append( t_connection[1][t_connection[1].rfind(':')+1:len(t_connection[1])] )

## get all the PID of the applications with active connections using the port
print('Finding the application ID')
for t_port in g_portList:   
    t_PID =  ilRegexReplace('\s\s+', ',', ilPopen('netstat -ano | findstr ' + t_port).read().strip()).split(',')[-1]
    g_PIDList.append(t_PID)

##this dictionary will be used for reference later
##create a dictionary out of the Application name and its PID

for t_task in g_ActiveApplicationList:
    t_key = ilRegexReplace('\s\s+', ',', t_task).split(',')[1].split(' ')[0]
    t_value = ilRegexReplace('\s\s+', ',', t_task).split(',')[0]
    g_applicationPIDDict[t_key] = t_value

##to atleast properly display the printout of application
for t_PID in g_PIDList:
    if len(t_PID) > 0:
        if g_maxStrLength < len( g_applicationPIDDict[t_PID] ): g_maxStrLength = len( g_applicationPIDDict[t_PID] )

del g_ActiveConnectionList[0] ##delete the headers of the g_ActiveConnectionList (not necessary for printing)

## begin displaying the applications
for t_index in range(len(g_PIDList)):
    if len( g_applicationPIDDict[g_PIDList[t_index]] ) < g_maxStrLength:
        t_space = ' '*(g_maxStrLength - len( g_applicationPIDDict[g_PIDList[t_index]]) ) + '\t'
    else:
        t_space = '\t'
        
    print(g_applicationPIDDict[g_PIDList[t_index]] +
          t_space + 
          g_ActiveConnectionList[t_index][1] +
          '\t' +
          g_ActiveConnectionList[t_index][2] +
          '\t' +
          g_PIDList[t_index])
    
    g_AppsWithActiveConnection.append(g_applicationPIDDict[g_PIDList[t_index]] +
          t_space + 
          g_ActiveConnectionList[t_index][1] +
          '\t' +
          g_ActiveConnectionList[t_index][2] +
          '\t' +
          g_PIDList[t_index])
