# see https://dbxit.com/uploading-to-weatherunderground-using-http for all fields
# make this use cumulusmx to take the load off cumumulus and see if helps with station lockup
# this was used for actuald
#def create_wunderground_info(weather_info):
#    """
#    Perform necessary conversions to align to Wunderground API
#    :param weather_info:
#    :return:
#    """
#    wunderground_info = {}
#
#    wunderground_info['humidity'] = weather_info['humidity'] + '.0'
#    wunderground_info['baromin'] = round(float(weather_info['pressure']) * 0.030, 3)
#    wunderground_info['winddir'] = int(weather_info['wind_deg'])
#    wunderground_info['tempf'] = round(float(weather_info['temp']) * (9.0/5.0) + 32.0, 1)
#    wunderground_info['windspeedmph'] = round(float(weather_info['wind_speed']) * 1.151, 2)
#    wunderground_info['windgustmph'] = round(float(weather_info['wind_gust']) * 1.151, 1)
#    wunderground_info['dewptf'] = round(float(weather_info['dew_point']) * (9.0 / 5.0) + 32.0, 1)
#    wunderground_info['solarradiation'] = round(float(weather_info['lux']) * 0.0079, 2)
#    wunderground_info['UV'] = weather_info['uvi']
#    wunderground_info['rainin'] = float(weather_info['rain']) * 0.0393701
#    wunderground_info['weather'] = weather_info['weather_text_metar']
#    wunderground_info['clouds'] = weather_info['clouds_text']
#
#    return wunderground_info


def create_wunderground_request(wunderground_info, station_id, station_key):
    """

    :param wunderground_info:
    :param station_id:
    :param station_key:
    :return:
    """

    params_str = ""
    wu_url = 'https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?'
    wu_creds = 'ID=' + station_id + '&PASSWORD=' + station_key

    date_str = '&dateutc=now'
    action_str = '&action=updateraw'

    for param in wunderground_info:
        params_str += '&' + param + '=' + wunderground_info[param].__str__()

    uri = wu_url + wu_creds + date_str + params_str + action_str

    return uri
