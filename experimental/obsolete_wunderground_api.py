import requests
import traceback
import time

import creds

# add some exception handling
def update_wunderground(wunderground_request):
    """

    :param wunderground_info:
    :return:
    """
    try:
        # params_str = ""
        # wu_url = 'https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?'
        # wu_creds = 'ID=' + creds.station_id + '&PASSWORD=' + creds.station_key
        # #wu_creds = 'ID=' + creds.station_id + '&PASSWORD=' + 'nopasswr232'
        # date_str = '&dateutc=now'
        # action_str = '&action=updateraw'
        #
        # for param in wunderground_info:
        #     params_str += '&' + param + '=' + wunderground_info[param].__str__()
        #
        # uri = wu_url + wu_creds + date_str + params_str + action_str
        print('accessing Wunderground API, wunderground_request : ' + wunderground_request)

        while True:
            response = requests.get(wunderground_request)
            if response.status_code != 200:
                print('error accessing Wunderground API, status_code=' + response.status_code.__str__() + ', sleeping...')
                time.sleep(10)
            else:
                print('API access OK, status_code=' + response.status_code.__str__())
                break

        return response.status_code

    # something really bad
    except Exception as e:
        traceback.print_exc()
        return response.status_code