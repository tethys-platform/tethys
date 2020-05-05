# Copyright 2020 Konstruktor, Inc. All Rights Reserved.
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


class TethysException(Exception):
    pass


class TethysRuntimeError(RuntimeError, TethysException):
    pass


class TethysRONotFound(TethysException):
    pass


class TethysBadRepositoryObjectValue(TethysException):
    pass


class TethysInputNodesNotFound(TethysException):
    pass


class TethysSessionClosed(TethysException):
    pass


class TethysStreamInProcess(TethysException):
    pass


class TethysROFieldValidationError(TethysException):
    pass
