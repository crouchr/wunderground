# client for subscribing to MQTT
import ast
from paho.mqtt import client as mqtt_client
from pprint import pprint
import time

# my funcs
import creds        # FIXME : set in environment
import wunderground
import process_meteo_rec
import call_pws_api


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

    wunderground_info = process_meteo_rec.create_wunderground_rec(mqtt_dict)
    pws_api_request = wunderground.create_wunderground_request(wunderground_info, creds.station_id, creds.station_key)
    status_code = call_pws_api.update_pws_api('Weather Underground', pws_api_request)



def connect_mqtt(broker_host, broker_port, client_id) -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker OK, waiting for messages...")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker_host, broker_port)

    return client


def subscribe_topic(client: mqtt_client, topic, called_function):
    """

    :param client:
    :param topic:
    :param called_function: function to call when a message is read from topic
    :return:
    """

    print('topic=' + topic.__str__())
    client.subscribe(topic)
    client.on_message = called_function
    print(f'Subscribed to topic={topic}')


if __name__ == '__main__':
    import random
    import time

    topic = "meteo/metrics"

    broker_host = 'j1900'
    broker_port = 1883

    # generate client ID with pub prefix randomly
    client_id = f'wunderground-{random.randint(0, 100)}'
    print('client_id=' + client_id.__str__())

    # Name of function to call when MQTT message is read from topic
    called_function = _process_mqtt_msg

    while True:
        try:
            client = connect_mqtt(broker_host, broker_port, client_id)
            subscribe_topic(client, topic, called_function)           # infinite loop
            client.loop_forever()
        except Exception as e:
            msg = 'main() : error=' + e.__str__()
            print(msg)
            time.sleep(5)
            continue
