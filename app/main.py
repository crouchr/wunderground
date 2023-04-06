# client for subscribing to MQTT
import ast
from paho.mqtt import client as mqtt_client
from pprint import pprint

# my funcs
import creds        # FIXME : set in environment
import wunderground
import process_meteo_rec
import call_pws_api
import get_env_app


def _process_mqtt_msg(client, userdata, msg):
    """
    The function to run when a new MQTT message is read from the topic
    :param client:
    :param userdata:
    :param msg:
    :return:
    """

    try:
        print('--------------------------------------------------------------')
        print(time.ctime())
        print('entered _process_mqtt_msg()')
        print('received MQTT msg via topic=' + msg.topic.__str__())
        mqtt_dict = ast.literal_eval(msg.payload.decode())
        #pprint(mqtt_dict)

        wunderground_info = process_meteo_rec.create_wunderground_rec(mqtt_dict)
        pws_api_request = wunderground.create_wunderground_request(wunderground_info, creds.station_id, creds.station_key)
        status_code = call_pws_api.update_pws_api('Weather Underground', pws_api_request)

    except Exception as e:
        print(f'_process_mqtt_msg() : exception : {e}')


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

    broker_host = get_env_app.get_mqttd_host()
    broker_port = get_env_app.get_mqttd_port()

    # generate client ID with pub prefix randomly
    client_id = f'meteod-wunderground-{random.randint(0, 100)}'
    print('client_id=' + client_id.__str__())

    # name of function to call when MQTT message is read from topic
    called_function = _process_mqtt_msg

    while True:
        try:
            print(f'Connect to MQTT host {broker_host} on port {broker_port}...')
            client = connect_mqtt(broker_host, broker_port, client_id)
            subscribe_topic(client, topic, called_function)           # infinite loop
            client.loop_forever()
        except Exception as e:
            msg = 'main() : error=' + e.__str__()
            print(msg)
            time.sleep(5)
            continue
