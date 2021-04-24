import speedtest
import json
import time


def open_file(mode):
    return open("../shared/data.json", mode)


# load previous json data into memory
speed_file = open_file("r")
speed_json = speed_file.read()
speed_dict = json.loads(speed_json)
speed_file.close()

# get current network speed
speedTester = speedtest.Speedtest()
speed_mbps = speedTester.download() / 1000000

# save network speed to file
speed_file = open_file("w")
speed_dict['data'].append({'time': time.time(), 'speed': speed_mbps})
speed_json = json.dumps(speed_dict)
speed_file.write(speed_json)
