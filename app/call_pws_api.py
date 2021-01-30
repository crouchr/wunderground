# PWS cloud independent
import requests
import traceback
import time

import creds


# add some exception handling
def update_pws_api(pws_name, pws_request):
    """


    :return:
    """
    try:
        max_attempts = 3    # attempts to access the PWS API
        attempt = 0

        while True:
            response = requests.get(pws_request)
            print('API request sent to ' + pws_name)
            if response.status_code != 200:
                attempt += 1
                print('Error : attempt=' + attempt.__str__() + ' accessing ' + pws_name + ' API, status_code=' + response.status_code.__str__())
                if attempt >= max_attempts:
                    break
                backoff_secs = int(attempt * 30)    # 30
                print('Backing off for ' + backoff_secs.__str__() + ' seconds...')
                time.sleep(backoff_secs)      # back off for x seconds
                continue
            else:
                print('Updated '+ pws_name + ' via API access OK, status_code=' + response.status_code.__str__())
                break

        if attempt == max_attempts:
            print('Error : Failed to update via ' + pws_name + ' API after ' + attempt.__str__() + ' attempts')

        return response.status_code

    # something really bad
    except Exception as e:
        traceback.print_exc()
        return response.status_code
