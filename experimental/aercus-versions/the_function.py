import time
import ast

from pprint import pprint

# NOTE : could not get the_function method to work
def _process_mqtt_msg(client, userdata, msg):
    """
    The function to run when a new MQTT message is read from the topic
    :param client:
    :param userdata:
    :param msg:
    :return:
    """
    print('---------------------------------')
    print('entered _process_mqtt_msg()')
    print(time.ctime() + ' : received MQTT msg via topic=' + msg.topic.__str__())
    mqtt_dict = ast.literal_eval(msg.payload.decode())
    pprint(mqtt_dict)

    weather_info = process_meteo_rec.create_wunderground_rec(mqtt_dict)

