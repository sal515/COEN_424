# required libraries:
# install requests library if needed:  pip install requests

import json
import requests

from time import sleep

post_request_url = "http://127.0.0.1:5000/post_test"

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


while 1:

    # Constraints
    # batchId > 0

    # ------ input -------------
    # userInput = input("Please enter your selection from the options listed above: ")
    # userInput = userInput.lower()
    #
    # if userInput == "2":
    #     break
    #
    # rfwId = input("Please enter RFW ID: ")
    # benchmarkType = input("Please enter Benchmark Type -> \n1 - DVD_Test, \n2 - DVD_Train, \n3 - NDBench_Test, \n4 - NDBench_Train: \nSelection -> ")
    # workloadMetric = input("Please enter Workload Metric -> \n1 - CPU, \n2 - NetworkIn, \n3 - NetworkOut, \n4 - Memory): \nSelection -> ")
    # batchUnit = input("Please enter Batch Unit: ")
    # batchId = input("Please enter Batch ID: ")
    # batchSize = input("Please enter Batch Size: ")
    # ------ input -------------

    # ------ delete -------------

    rfwId = 0
    benchmarkType = 1
    workloadMetric = 4
    batchUnit = 2
    batchId = 1
    batchSize = 3

    # ------ delete -------------

    request_json = {
        "rfwId": rfwId,
        "benchmarkType": benchmarkType,
        "workloadMetric": workloadMetric,
        "batchUnit": batchUnit,
        "batchId": batchId,
        "batchSize": batchSize
    }

    # ------ delete -------------
    sleep(6)
    # print("woke up")
    # ------ delete -------------

    try:
        r = requests.post(post_request_url, json=request_json)

        # print(r.json())
        response_batch_data_json = r.json()

        batch_length = len(response_batch_data_json)

        response_rfwId = response_batch_data_json[0]
        last_batch = response_batch_data_json[1]
        response_data = response_batch_data_json[2]

        print(f"request id: {response_rfwId}")
        print(f"last batch: {last_batch}")

        counter = 0
        for x in response_data:
            counter = counter + 1
            print(f"{counter} : {x}")




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
