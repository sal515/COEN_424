import json
import math

NDBench_testing_json = "workload_data_json/NDBench-testing.json"
NDBench_training_json = "workload_data_json/NDBench-training.json"
DVD_testing_json = "workload_data_json/DVD-testing.json"
DVD_training_json = "workload_data_json/DVD-training.json"


def file_selector(benchmark_type_val):
    switcher = {
        1: NDBench_testing_json,
        2: NDBench_training_json,
        3: DVD_testing_json,
        4: DVD_training_json
    }
    return switcher.get(benchmark_type_val, "null")


def generate_batch_data_response(user_request):
    # Client Request data
    rfwId = user_request['rfwId']  # 1. RFWID
    benchmarkType = user_request['benchmarkType']  # 2. Benchmark Type DVD or NDBench
    workloadMetric = user_request['workloadMetric']  # 3. CPU / NetworkIn
    batchUnit = user_request['batchUnit']  # number of samples
    batchId = user_request['batchId']  # 5th batch or 6th batch etc
    batchSize = user_request['batchSize']  # how many batches to return

    data = -1
    response_start_line = -1
    response_end_line = -1
    response_lines_size = -1

    try:

        with open(file_selector(benchmarkType), 'r') as f:
            data = json.load(f)

            total_number_of_batches = {math.floor(len(data) / batchUnit)}
            length_of_json_data_files = len(data)
            response_start_line = (batchUnit * (batchId - 1))
            response_end_line = (batchUnit * ((batchId - 1) + batchSize) - 1)
            response_lines_size = (batchUnit * batchSize)
            end_batch_id = (batchId - 1) + batchSize

            # calculation_tester(data, batchId, end_batch_id, length_of_json_data_files, response_end_line,
            #                    response_lines_size, response_start_line, total_number_of_batches)

            f.close()

            try:
                with open("response_data/clientID_response.json", 'w') as file:
                    response_data = data[response_start_line:response_end_line + 1]
                    json.dump(response_data, file)

            except:
                print(f"Error writing response to file")

            # building response packet
            response_data = data[response_start_line:response_end_line + 1]
            response = [rfwId, end_batch_id, response_data]

        # send response packet to client
        return response

    except:
        print(f"Error reading json file")


def calculation_tester(data, batchId, end_batch_id, length_of_json_data_files, response_end_line, response_lines_size,
                       response_start_line, total_number_of_batches):
    print("")
    print(f"Length of json data file: {length_of_json_data_files}")
    print("")
    print(f"Starting batch unit: {batchId}")
    print(f"Ending batch unit: {end_batch_id}")
    print("")
    # Calculations done on the server side from request received client
    print(f"Total number of batches from 1 - {total_number_of_batches}")
    print(f"Starting line from batch unit (start is 0): {response_start_line}")
    print(f"Ending line from batch unit (start is 0): {response_end_line}")
    print(f"Total number of lines: {response_lines_size}")
    print("")

    print(data[response_start_line:response_end_line + 1])


# generate_batch_data()


def test_file(user_request):
    print("File executed")
    print(user_request)
    print(NDBench_testing_json)
    print(NDBench_training_json)
    print(DVD_training_json)
    print(DVD_testing_json)
