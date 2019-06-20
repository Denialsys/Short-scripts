'''Time given a the seconds count'''

def returnTime(pSeconds, pIsMilitary = True):
        '''Returns time tupple formatted in hours minutes and seconds
        @Param pSeconds -> time in seconds
        @Param pIsMilitary -> returns 24hr format if true 12hr otherwise'''
        
        second = pSeconds % 60
        minute = (pSeconds // 60) % 60
        hour = (pSeconds // 3600) % 24
        
        if pIsMilitary: return (hour, minute, second)
        else:
                
                meridiem = "AM"
                if hour == 0:hour = 12
                elif hour == 12: meridiem = "PM"
                elif hour > 12: hour -= 12


                return (hour, minute, second, meridiem)
