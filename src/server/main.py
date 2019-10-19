import json
import math

NDBench_testing_json = "workload_data_json/NDBench-testing.json"
NDBench_training_json = "workload_data_json/NDBench-training.json"
DVD_testing_json = "workload_data_json/DVD-testing.json"
DVD_training_json = "workload_data_json/DVD-training.json"

# Client Request data
rfwId = -1  # 1. RFWID
benchmarkType = -1  # 2. Benchmark Type DVD or NDBench
workloadMetric = -1  # 3. CPU / NetworkIn
batchUnit = 100  # number of samples
batchId = 5  # 5th batch or 6th batch etc
batchSize = 2  # how many batches to return

data = -1
response_start_line = -1
response_end_line = -1
response_lines_size = -1

try:
    data = -1
    response_start_line = (batchUnit * batchId) - 1
    response_end_line = (batchUnit * (batchId + batchSize) - 1)
    response_lines_size = (batchUnit * batchSize)

    with open(NDBench_testing_json, 'r') as f:
        data = json.load(f)
        # print(type(data))

        print(f"Length of json data file, 1 onwards: {len(data) + 1}")
        print(f"Starting batch unit: {batchId}")
        print(f"Ending batch unit: {batchId + batchSize}")

        # Request received from client
        print(f"Total number of batches from 1 - {math.floor(len(data) / batchUnit)}")
        print(f"Starting line from batch unit (start as 1): {batchUnit * batchId}")
        print(f"Ending line from batch unit (start as 1): {batchUnit * (batchId + batchSize)}")

        # Calculations done on the server side from request received client
        print(f"Length of json data file, 0 onwards: {len(data)}")
        print(f"Total number of batches from 1 - {math.floor(len(data) / batchUnit)}")
        print(f"Starting line from batch unit (start is 0): {response_start_line}")
        print(f"Ending line from batch unit (start is 0): {response_end_line}")
        print(f"Number of lines to be send in a response: {response_lines_size}")
        f.close()

except:
    print(f"Error reading json file")

try:
    with open("response_data/clientID_response.json", 'w') as file:
        response_data = data[response_start_line:response_end_line + 1]

        print(response_data)
        print(len(response_data))

        json.dump(response_data, file)

except:
    print(f"Error writing response to file")
