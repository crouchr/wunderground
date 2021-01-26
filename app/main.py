import traceback
import os
import time
import definitions
import wunderground
import wunderground_api


def processActual(line):
    """
    Process a new entry taken from Actual Log
    Maintain the same units and names as used in SQL database i.e. API-agnostic
    :param line:
    :return:
    """
    weather_info = {}

    print(line.rstrip('\n'))
    recs = line.split('\t')
    weather_info['pressure'] = recs[8]
    weather_info['temp'] = recs[9]
    weather_info['humidity'] = recs[10]
    weather_info['wind_deg'] = recs[11]
    weather_info['wind_speed'] = recs[12]
    weather_info['wind_gust'] = recs[13]
    weather_info['dew_point'] = recs[16]
    weather_info['lux'] = recs[18]
    weather_info['uvi'] = recs[19]

    return weather_info


def main_loop():
    try:
        actuald_log_filename = definitions.WEATHER_INFO_DIR + 'actuald.tsv'
        fileActual = open(actuald_log_filename, 'r')

        # fixme : temp debugging code
        # lineActual = fileActual.readlines()
        # weather_info = processActual(lineActual[0])
        # wunderground_info = wunderground.create_wunderground_info(weather_info)
        # status_code = wunderground_api.update_wunderground(wunderground_info)

        st_resultsActual = os.stat(actuald_log_filename)
        st_sizeActual = st_resultsActual[6]
        fileActual.seek(st_sizeActual)
        print("Seek to end of " + actuald_log_filename)

        while True:
            whereActual = fileActual.tell()
            lineActual = fileActual.readline()
            if not lineActual:		# no data in feed
                # print("nothing in Actual Log to process...")
                fileActual.seek(whereActual)
            else:			        # new data has been added to log file
                print("*** NEW EVENT in Actual Log to process")
                weather_info = processActual(lineActual)
                wunderground_info = wunderground.create_wunderground_info(weather_info)
                status_code = wunderground_api.update_wunderground(wunderground_info)
                print('wunderground API status_code : ' + status_code.__str__())

            time.sleep(10)

    except Exception as e:
        traceback.print_exc()


def main():
    print('started')
    main_loop()


if __name__ == '__main__':
    main()
