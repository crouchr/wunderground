# PWS cloud independent
import requests
import traceback
import time


# add some exception handling
# Works for any online API
# This function works but needs more testing to verify is network is down
# how to increase backoff period in requests ?
def update_pws_api(pws_name, pws_request):
    """


    :return:
    """
    try:
        max_attempts = 3    # attempts to access the PWS API
        attempt = 0

        while True:
            print('API request for ' + pws_name + ' is ' + pws_request.__str__())
            print('send request to API...')
            response = requests.get(pws_request)    # if network down, this will trigger an exception ?

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
                print('Updated ' + pws_name + ' via API access OK, status_code=' + response.status_code.__str__())
                break

        if attempt == max_attempts:
            print('Error : Failed to update via ' + pws_name + ' API after ' + attempt.__str__() + ' attempts')

        return response.status_code

    # something really bad
    except Exception as e:
        print(f'update_pws_api() : exception {e}')
        traceback.print_exc()
        return None     # if network unreachable, there will not even be a stats code value
