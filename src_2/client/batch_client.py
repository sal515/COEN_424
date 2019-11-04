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
"""The Python implementation of the GRPC helloworld.Greeter client."""

# install grpc dependencies
# https://grpc.io/docs/quickstart/python/

from __future__ import print_function
import logging

import grpc

import batch_request_pb2
import batch_request_pb2_grpc

from time import sleep
import json


def batch_request(request_json_par):
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = batch_request_pb2_grpc.batchStub(channel)
        response = stub.getBatch(
            batch_request_pb2.batch_info(rfwId=request_json_par["rfwId"],
                                         benchmarkType=request_json_par["benchmarkType"],
                                         workloadMetric=request_json_par["workloadMetric"],
                                         batchUnit=request_json_par["batchUnit"],
                                         batchId=request_json_par["batchId"], batchSize=request_json_par["batchSize"]))
    return response.response_batch


if __name__ == '__main__':
    logging.basicConfig()

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
    # benchmarkType = input("Please enter Benchmark Type -> \n00 - DVD_Test, \n01 - DVD_Train, \n10 - NDBench_Test, \n11 - NDBench_Train: \nSelection -> ")
    # workloadMetric = input("Please enter Workload Metric: ")
    # batchUnit = input("Please enter Batch Unit: ")
    # batchId = input("Please enter Batch ID: ")
    # batchSize = input("Please enter Batch Size: ")
    # ------ input -------------

    # ------ delete -------------
    rfwId = "salman"
    benchmarkType = 1
    workloadMetric = 1
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
    print("woke up")
    # ------ delete -------------

    try:
        response_batch = batch_request(request_json)

        # https://www.w3schools.com/python/python_json.asp
        batch_data_2_json = json.loads(response_batch)

        batch_length = len(batch_data_2_json)

        counter = 0
        for x in batch_data_2_json:
            counter = counter + 1
            print(f"{counter} : {x}")

    except:
        print("Error: Could not call method in the server")

    # try:
    #     with open("client_data/client_request.json", 'w') as file:
    #         json.dump(request_json, file)
    #         # Save the JSON
    #         # file.write(output)
    #     # break
    # except:
    #     print("Error: Could not write to json file")
