# common environment non-specific to this app
# This file can be used in other metminiwx projects
import os

# Use j1900 for live
def get_mqttd_host():
    """
    Determine the hostname that hosts the MQTT Daemon
    :return:
    """
    if 'STAGE' in os.environ and os.environ['STAGE'] == 'PRD':
        mqttd_host = 'mqttd'    # name of container
    else:
        mqttd_host = 'j1900'    # IP of mqttd

    return mqttd_host


def get_mqttd_port():
    mqttd_port = 1883

    return mqttd_port


