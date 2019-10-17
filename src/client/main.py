import json

from pip._vendor.distlib.compat import raw_input

# Client Request data
rfwId = -1  # 1. RFWID
benchmarkType = -1  # 2. Benchmark Type DVD or NDBench
workloadMetric = -1  # 3. CPU / NetworkIn
batchUnit = -1  # number of samples
batchId = -1  # 5th batch or 6th batch etc
batchSize = -1  # how many batches to return

# UI
optionStart = 1
userInput = ''

print(
    # f"What would you like to do?\n"
    f"Press {optionStart} : To send a request workload data from the server\n"
)

# The length of the input has to be 1 character for the program to work
while ~(userInput.isnumeric() and len(userInput) != 1):
    userInput = raw_input("Please enter your selection from the options listed above: ")
    userInput = userInput.lower()

    if userInput.isnumeric():
        # print(f"Test: Your input was {userInput}")
        rfwId = raw_input("Please enter RFW ID: ")
        benchmarkType = raw_input("Please enter Benchmark Type: ")
        workloadMetric = raw_input("Please enter Workload Metric: ")
        batchUnit = raw_input("Please enter Batch Unit: ")
        batchId = raw_input("Please enter Batch ID: ")
        batchSize = raw_input("Please enter Batch Size: ")

        request_json = {
            "rfwId": rfwId,
            "benchmarkType": benchmarkType,
            "workloadMetric": workloadMetric,
            "batchUnit": batchUnit,
            "batchId": batchId,
            "batchSize": batchSize
        }

        with open("client_data/client_request.json", 'w') as file:
            json.dump(request_json, file)

            # Save the JSON
            # file.write(output)

        break

# UI
