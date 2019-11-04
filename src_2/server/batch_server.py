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

import grpc

import batch_request_pb2
import batch_request_pb2_grpc


class batch(batch_request_pb2_grpc.batchServicer):

    def getBatch(self, request, context):
        return batch_request_pb2.batch_response(
            response_batch=f"param1: {request.rfwId} param2: {request.benchmarkType} param3: {request.workloadMetric}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    batch_request_pb2_grpc.add_batchServicer_to_server(batch(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
