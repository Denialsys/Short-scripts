import math
error_marker = '[Main Error]================================>'
value_to_search = '0.0000471' ## For searching the precise increment in distance covered

def read_log_lines(filename):
    """Read each line in the log file then print the distance between each in meters"""

    current_data = ''
    try:
        log_lines = []
        prev_lat = 0
        prev_lng = 0

        ## Open the log file
        with open(filename, 'r') as gps_logs:
            log_lines = gps_logs.readlines()

        ## Iterate through the log file
        for idx,i in enumerate(log_lines):
            current_data = i
            log_line = i.replace('\n', '').split(',')

            ## Error marker was found in the log
            ## Skip calculation in this line,
            ## (proly due to loss of satelite signal or initialization error)
            if i == error_marker:
                continue
            
            ## If currently on the beginning of the loop
            if idx == 0:
                prev_lat = float(log_line[1])
                prev_lng = float(log_line[2])
                continue

            lat = float(log_line[1])
            lng = float(log_line[2])
            distance = '{:.7f}'.format(math.dist((prev_lat, prev_lng), (lat, lng)))
            distance_m = distance_between(prev_lat, prev_lng, lat, lng)
            print (f'lattitude: {lat}, longitude: {lng}, distance: {distance}, distance in meters {distance_m}')
            # if distance == value_to_search:
            #     print (f'matching distance was: {log_line}')
            #     break
            prev_lat = lat
            prev_lng = lng

        print('loop search has ended')

    except Exception as e:
        print(f'Error occured {current_data}')


def distance_between (lat1, long1, lat2, long2):
    """Given the two points (Latitude and longitude),
    determine the distance in meters between.
    Currently using the GPS module that is inaccurate, The equation
    is the closest approximate given that the earth is not perfectly round"""

    delta = math.radians(long1 - long2)
    sdlong = math.sin(delta)
    cdlong = math.cos(delta)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    slat1 = math.sin(lat1)
    clat1 = math.cos(lat1)
    slat2 = math.sin(lat2)
    clat2 = math.cos(lat2)
    delta = (clat1 * slat2) - (slat1 * clat2 * cdlong)
    delta = pow(delta, 2)
    delta += pow(clat2 * sdlong, 2)
    delta = math.sqrt(delta)
    denom = (slat1 * slat2) + (clat1 * clat2 * cdlong)
    delta = math.atan2(delta, denom)
    return delta * 6372795


read_log_lines('LogFile-22.txt')
