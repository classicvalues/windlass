#
# (c) Copyright 2018 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#


class RetryableFailure(Exception):
    """Rasise this exception when you want to retry the task

    This will retry and task a fix number of time with a small
    time back off.
    """


class WindlassBuildException(Exception):
    pass


class WindlassPushPullException(RetryableFailure):
    pass
