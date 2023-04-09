import os,time

def getSystemDetails(p_SystemEntity="cpu"):
    CONST_DRIVERS = "sysdriver"
    CONST_CPU = "cpu"
    #Get all the available entity names
    c_EntityList = os.popen("wmic " + p_SystemEntity + " get caption").read().strip().split('\n')

    ##initiate the limit of how many entities we wan to ID
    c_Num = 0
    for c_Entity in c_EntityList[2:]:

        if c_Entity:    #check if the entity has values
            
            c_Entity = c_Entity.strip()
            c_PropertyListRaw = os.popen("wmic " + p_SystemEntity + " where caption='" + c_Entity + "' get *").read().strip().split("\n")
            c_PropertyList = [c_Values for c_Values in c_PropertyListRaw[0].split()]
            
            print("\n========")
            print(c_Entity)
            print("========")

            ##each entity has their own properties
            ##Iteratively display these properties one by one
            for c_Property in c_PropertyList:

                ##since the caption was displayed already, skip this one
                if c_Property != "Caption":
                    m_strCommand = "wmic " + p_SystemEntity + " where caption='" + c_Entity + "' get " + c_Property
                    m_EntityPropertyResult = os.popen(m_strCommand).read().strip().split('\n')
                    if len(m_EntityPropertyResult) == 3:
                        print(m_EntityPropertyResult[0].strip() + " : " + m_EntityPropertyResult[2])
                    else:
                        print(c_Property + ' : null')
                    
            ##Specify the number of iterations we want to make
            c_Num += 1  
            if c_Num >= 100:
                break

##c_EntityList = os.popen("C:\\Windows\\System32\\wbem\\wmic cpu get *").read().strip().split('\n')
##c_propertyList = [c_words for c_words in c_EntityList[0].split()]
##task = os.open('wmic cpu get ' +     
##    for c_property in c_propertyList:
##
##        strCommand = 'wmic cpu get ' + c_property
##        task = os.popen(strCommand).read().strip().split('\n')
##        
##        if len(task) == 3:
##            print(task[0].strip() + " : " + task[2])
##        else:
##            print(c_property + ' : null')


##c_task1 = os.popen("wmic sysdriver get caption").read().strip().split('\n')
##c_propertyList = [c_words for c_words in c_task1[0].split()]


##
##c_num = 0
##for c_property in c_propertyList:
##
##    strCommand = 'wmic sysdriver get ' + c_property
##    task = os.popen(strCommand).read().strip().split('\n')
##    
##    if len(task) == 3:
##        print(task[0] + ": " + task[2])
##    else:
##        print(c_property + ' : null')
##
