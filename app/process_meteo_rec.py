# API independent
from pprint import pprint


# wunderground takes your absolute pressure and adjusts it to sea-level
# it knows your elevation
def create_wunderground_rec(mqtt_dict):
    """
    :param mqtt_dict:
    :return:
    """

    wunderground_info = {}

    # Measured - Wunderground seems to want 'US' units, e.g. inches for pressure and Farenheit for temperatures
    wunderground_info['baromin'] = round(float(mqtt_dict['pressure_abs']) * 0.030, 3)   # inches
    wunderground_info['tempf'] = round(float(mqtt_dict['temp_c_smoothed']) * (9.0/5.0) + 32.0, 1)
    wunderground_info['humidity'] = mqtt_dict['humidity_smoothed']
    wunderground_info['solarradiation'] = round(float(mqtt_dict['lux']) * 0.0079, 2)

    # Derived
    wunderground_info['dewptf'] = round(float(mqtt_dict['dew_point']) * (9.0 / 5.0) + 32.0, 1)

    print('Data to be sent to Wunderground (Imperial format):')
    pprint(wunderground_info)

    return wunderground_info




    # wunderground_info['humidity'] = weather_info['humidity'] + '.0'
    # wunderground_info['baromin'] = round(float(weather_info['pressure']) * 0.030, 3)
    # wunderground_info['winddir'] = int(weather_info['wind_deg'])
    # wunderground_info['tempf'] = round(float(weather_info['temp']) * (9.0/5.0) + 32.0, 1)
    # wunderground_info['windspeedmph'] = round(float(weather_info['wind_speed']) * 1.151, 2)
    # wunderground_info['windgustmph'] = round(float(weather_info['wind_gust']) * 1.151, 1)
    # wunderground_info['dewptf'] = round(float(weather_info['dew_point']) * (9.0 / 5.0) + 32.0, 1)
    # wunderground_info['solarradiation'] = round(float(weather_info['lux']) * 0.0079, 2)
    # wunderground_info['UV'] = weather_info['uvi']
    # wunderground_info['rainin'] = float(weather_info['rain']) * 0.0393701
    # wunderground_info['weather'] = weather_info['weather_text_metar']
    # wunderground_info['clouds'] = weather_info['clouds_text']



    # weather_info['wind_deg'] = recs[11]
    # weather_info['wind_speed'] = recs[12]
    # weather_info['wind_gust'] = recs[13]
    # weather_info['rain'] = recs[14]
    # weather_info['snow'] = recs[15]

    # weather_info['uvi'] = recs[19]
    # weather_info['main'] = recs[20]
    # weather_info['synopsis_code'] = recs[21]
    # weather_info['coverage'] = recs[22]
    # weather_info['uuid'] = recs[23]

    # Hard-coded for the moment to check it is processed by weather underground
    # weather_info['weather_text_metar'] = '+RA'
    # weather_info['clouds_text'] = 'BKN'
    # weather_info['visibility'] = 1000

    return weather_info
