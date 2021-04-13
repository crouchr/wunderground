# API independent
def processActual(line):
    """
    Process a new entry taken from Actual Log
    Maintain the same units and names as used in SQL database i.e. API-agnostic
    :param line:
    :return:
    """
    weather_info = {}
    line = line.rstrip('\n')
    print(line)
    recs = line.split('\t')
    weather_info['pressure'] = recs[8]
    weather_info['temp'] = recs[9]
    weather_info['humidity'] = recs[10]
    weather_info['wind_deg'] = recs[11]
    weather_info['wind_speed'] = recs[12]
    weather_info['wind_gust'] = recs[13]
    weather_info['rain'] = recs[14]
    weather_info['snow'] = recs[15]
    weather_info['dew_point'] = recs[16]
    weather_info['feels_like'] = recs[17]
    weather_info['lux'] = recs[18]
    weather_info['uvi'] = recs[19]
    weather_info['main'] = recs[20]
    weather_info['synopsis_code'] = recs[21]
    # weather_info['coverage'] = recs[22]
    # weather_info['uuid'] = recs[23]

    return weather_info
