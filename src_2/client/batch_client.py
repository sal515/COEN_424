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


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = batch_request_pb2_grpc.batchStub(channel)
        response = stub.getBatch(
            batch_request_pb2.batch_info(rfwId='Salman', benchmarkType=11, workloadMetric=11, batchUnit=1, batchId=2,
                                         batchSize=3))

        # response = stub.getBatch(
        #     batch_request_pb2.batch_info(rfwId='Salman', benchmarkType=))

    print("Batch client received: " + response.response_batch)


if __name__ == '__main__':
    logging.basicConfig()
    run()
