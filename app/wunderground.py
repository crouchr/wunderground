# see https://dbxit.com/uploading-to-weatherunderground-using-http for all fields
def create_wunderground_info(weather_info):
    """
    Perform necessary conversions to align to Wunderground API
    :param weather_info:
    :return:
    """
    wunderground_info = {}

    wunderground_info['humidity'] = weather_info['humidity'] + '.0'
    wunderground_info['baromin'] = round(float(weather_info['pressure']) * 0.030, 3)
    wunderground_info['winddir'] = int(weather_info['wind_deg'])
    wunderground_info['tempf'] = round(float(weather_info['temp']) * (9.0/5.0) + 32.0, 1)
    wunderground_info['windspeedmph'] = round(float(weather_info['wind_speed']) * 1.151, 2)
    wunderground_info['windgustmph'] = round(float(weather_info['wind_gust']) * 1.151, 1)
    wunderground_info['dewptf'] = round(float(weather_info['dew_point']) * (9.0 / 5.0) + 32.0, 1)
    wunderground_info['solarradiation'] = round(float(weather_info['lux']) * 0.0079, 2)
    wunderground_info['UV'] = weather_info['uvi']
    wunderground_info['rainin'] = float(weather_info['rain']) * 0.0393701

    return wunderground_info
