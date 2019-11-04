# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

# install grpc dependencies
# https://grpc.io/docs/quickstart/python/

from concurrent import futures
import logging

import json
import math

import grpc

import batch_request_pb2
import batch_request_pb2_grpc


class Batch(batch_request_pb2_grpc.batchServicer):

    def getBatch(self, request, context):
        request_json = {
            "rfwId": request.rfwId,
            "benchmarkType": request.benchmarkType,
            "workloadMetric": request.workloadMetric,
            "batchUnit": request.batchUnit,
            "batchId": request.batchId,
            "batchSize": request.batchSize
        }

        return batch_request_pb2.batch_response(
            response_batch=generate_batch_data_response(request_json))


def file_selector(benchmark_type_val):
    NDBench_testing_json = "workload_data_json/NDBench-testing.json"
    NDBench_training_json = "workload_data_json/NDBench-training.json"
    DVD_testing_json = "workload_data_json/DVD-testing.json"
    DVD_training_json = "workload_data_json/DVD-training.json"

    switcher = {
        1: NDBench_testing_json,
        2: NDBench_training_json,
        3: DVD_testing_json,
        4: DVD_training_json
    }
    return switcher.get(benchmark_type_val, "null")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    batch_request_pb2_grpc.add_batchServicer_to_server(Batch(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


def generate_batch_data_response(user_request):
    data = -1
    response_start_line = -1
    response_end_line = -1
    response_lines_size = -1

    # Client Request data
    rfwId = user_request['rfwId']  # 1. RFWID
    benchmarkType = user_request['benchmarkType']  # 2. Benchmark Type DVD or NDBench
    workloadMetric = user_request['workloadMetric']  # 3. CPU / NetworkIn
    batchUnit = user_request['batchUnit']  # number of samples
    batchId = user_request['batchId']  # 5th batch or 6th batch etc
    batchSize = user_request['batchSize']  # how many batches to return

    try:

        with open(file_selector(benchmarkType), 'r') as f:
            data = json.load(f)

            total_number_of_batches = {math.floor(len(data) / batchUnit)}
            length_of_json_data_files = len(data)
            response_start_line = (batchUnit * (batchId - 1))
            response_end_line = (batchUnit * ((batchId - 1) + batchSize) - 1)
            response_lines_size = (batchUnit * batchSize)
            end_batch_id = (batchId - 1) + batchSize

            f.close()

            # try:
            #     with open("response_data/clientID_response.json", 'w') as file:
            #         response_data = data[response_start_line:response_end_line + 1]
            #         json.dump(response_data, file)
            #
            # except:
            #     print(f"Error writing response to file")

            conv2str = json.dumps(data[response_start_line:response_end_line + 1])
            return conv2str

    except:
        print(f"Error reading json file")


if __name__ == '__main__':
    logging.basicConfig()
    serve()
