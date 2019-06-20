'''Time given a the seconds count'''

def returnTime(pSeconds, pIsMilitary):
	second = pSeconds % 60
	minute = (pSeconds // 60) % 60
	hourMilitary = (pSeconds // 3600) % 24
        if pIsMilitary:
                return (hourMilitary, minute, second)
        else:
                meridiem = "AM"
                if hourMilitary == 0:
                        hourStandard = 12
                elif hourMilitary > 12:
                        hourStandard = hourMilitary - 12
                        meridiem = "PM"
                else:
                        hourStandard = hourMilitary
                return (hourStandard, minute, second, meridiem)

##def returnTime(pSeconds, pIsMilitary):
##        second = pSeconds % 60
##        minute = (pSeconds // 60) % 60
##        hourMilitary = (pSeconds // 3600) % 24
##        if pIsMilitary:
##                return (hourMilitary, minute, second)
##        else:
##                meridiem = "AM"
##                if hourMilitary == 0:
##                        hourStandard = 12
##                elif hourMilitary > 12:
##                        hourStandard = hourMilitary - 12
##                        meridiem = "PM"
##                else:
##                        hourStandard = hourMilitary
##                return (hourStandard, minute, second, meridiem)
