#!/bin/bash

# Copyright 2020 Adap GmbH. All Rights Reserved.
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
# ==============================================================================


# run as: ./run_pi_debian.sh --server_address=<YOUR_SERVER_ADDRESS> --cid=0 --model=Net

echo "ARGS: ${@}"

./build_image.sh --build-arg BASE_IMAGE_TYPE=cpu_debian

docker run --rm --platform linux/arm/v7 flower_client ${@}