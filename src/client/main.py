# required libraries:
# install requests library if needed:  pip install requests

import json
import requests

from time import sleep


# Client Request data
rfwId = -1  # 1. RFWID
benchmarkType = -1  # 2. Benchmark Type DVD or NDBench
workloadMetric = -1  # 3. CPU / NetworkIn
batchUnit = -1  # number of samples
batchId = -1  # 5th batch or 6th batch etc
batchSize = -1  # how many batches to return

# UI
# userInput = ''

# headers = {'Content-type': 'multipart/form-data'}
# with open("client_data/client_request.json", "r") as read_file:
#     data = json.load(read_file)
# files = {'client_data': data}
# r = requests.post(url, files=files, data=data, headers=headers)

print(
    f"Press {1} : To send a request workload data from the server\n"
    f"Press {2} : To exit application\n"
)


# def is_input_numeric(var, check_str):
#     while ~(var.isnumeric()):
#         var = input(f"Please enter {check_str}: ")


# The length of the input has to be 1 character for the program to work
while 1:

    # userInput = input("Please enter your selection from the options listed above: ")
    # userInput = userInput.lower()
    #
    # if userInput == "2":
    #     break
    #
    # rfwId = input("Please enter RFW ID: ")
    benchmarkType = input("Please enter Benchmark Type -> \n00 - DVD_Test, \n01 - DVD_Train, \n10 - NDBench_Test, \n11 - NDBench_Train: \nSelection -> ")
    # workloadMetric = input("Please enter Workload Metric: ")
    # batchUnit = input("Please enter Batch Unit: ")
    # batchId = input("Please enter Batch ID: ")
    # batchSize = input("Please enter Batch Size: ")

    request_json = {
        "rfwId": rfwId,
        "benchmarkType": benchmarkType,
        "workloadMetric": workloadMetric,
        "batchUnit": batchUnit,
        "batchId": batchId,
        "batchSize": batchSize
    }

    sleep(4)
    print("woke up")
    try:
        r = requests.post("http://127.0.0.1:5000/post_test", json=request_json)
    except:
        print("Error: Could not send post request to server")

    try:
        with open("client_data/client_request.json", 'w') as file:
            json.dump(request_json, file)
            # Save the JSON
            # file.write(output)
        # break
    except:
        print("Error: Could not write to json file")

