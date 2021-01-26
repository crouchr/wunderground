import requests
import creds

# add some exception handling
def update_wunderground(wunderground_info):
    """

    :param wunderground_info:
    :return:
    """

    params_str = ""
    wu_url = 'https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?'
    wu_creds = 'ID=' + creds.station_id + '&PASSWORD=' + creds.station_key
    date_str = '&dateutc=now'
    action_str = '&action=updateraw'

    for param in wunderground_info:
        params_str += '&' + param + '=' + wunderground_info[param].__str__()

    uri = wu_url + wu_creds + date_str + params_str + action_str
    print('wunderground_uri : ' + uri)

    response = requests.get(uri)

    return response.status_code
