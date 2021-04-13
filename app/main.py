import traceback
import os
import time

import definitions
import process_actuald_rec
import creds
import call_pws_api

# only code specific to a PWS Cloud service
import wunderground


def main_loop():
    try:
        actuald_log_filename = definitions.WEATHER_INFO_DIR + 'actuald.tsv'
        fileActual = open(actuald_log_filename, 'r')

        debug = False
        if debug:
        # fixme : temp debugging code
            import sys
            lineActual = fileActual.readlines()
            weather_info = process_actuald_rec.processActual(lineActual[0])
            wunderground_info = wunderground.create_wunderground_info(weather_info)
            pws_api_request = wunderground.create_wunderground_request(wunderground_info, creds.station_id, creds.station_key)
            status_code = call_pws_api.update_pws_api('Weather Underground', pws_api_request)
            sys.exit('debugging so exit')

        st_resultsActual = os.stat(actuald_log_filename)
        st_sizeActual = st_resultsActual[6]
        fileActual.seek(st_sizeActual)
        print("Seek to end of " + actuald_log_filename + ' ...')

        while True:
            whereActual = fileActual.tell()
            lineActual = fileActual.readline()
            if not lineActual:		# no data in feed
                fileActual.seek(whereActual)
            else:			        # new data has been added to log file
                print("*** NEW EVENT in " + actuald_log_filename + " to process")
                weather_info = process_actuald_rec.processActual(lineActual)
                wunderground_info = wunderground.create_wunderground_info(weather_info)
                pws_api_request = wunderground.create_wunderground_request(wunderground_info, creds.station_id, creds.station_key)
                status_code = call_pws_api.update_pws_api('Weather Underground', pws_api_request)

            time.sleep(10)          # time to wait until polling for another record

    except Exception as e:
        traceback.print_exc()


def main():
    print('started')
    main_loop()


if __name__ == '__main__':
    main()
