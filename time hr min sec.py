'''Time given a the seconds count'''

def returnTime(pSeconds, pIsMilitary):
	'''Returns a tupple containing Hour minute and second
        @Param pSeconds -> time in seconds format
        @Param pIsMilitary -> format the return into 24hr or 12hr'''

	second = pSeconds % 60
	minute = (pSeconds // 60) % 60
	hourMilitary = (pSeconds // 3600) % 24
	return (hourMilitary, minute, second)

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

