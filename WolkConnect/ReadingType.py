#   Copyright 2017 WolkAbout Technology s.r.o.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import random
import string
from enum import Enum, unique

@unique
class DataType(Enum):
    """ Data types
    """
    NUMERIC = "NUMERIC"
    STRING = "STRING"
    BOOLEAN = "BOOLEAN"

@unique
class ReadingType(Enum):
    """ Reading types
    """
    def __init__(self, ref, dataType, minValue=None, maxValue=None, dataSize=1, dataDelimiter=""):
        self.ref = ref
        self.dataType = dataType
        self.minValue = minValue
        self.maxValue = maxValue
        self.dataSize = dataSize
        self.dataDelimiter = dataDelimiter

    def __str__(self):
        isScalar = " isScalar={0}".format(self.isScalar)
        dataSizeString = "" if self.dataSize == 1 else " dataSize={0}".format(self.dataSize)
        dataDelimiter = " dataDelimiter={0}".format(self.dataDelimiter) if dataSizeString else ""
        return self.ref + ":" + self.dataType.value + isScalar + dataSizeString + dataDelimiter

    def generateRandomValues(self):
        if self.dataType == DataType.NUMERIC:
            if self.minValue is None or self.maxValue is None:
                return None
            
            return [random.uniform(self.minValue, self.maxValue) for _ in range(self.dataSize)]
        elif self.dataType == DataType.BOOLEAN:
            return [bool(int(random.uniform(0, 1)))]

        rndValue = random.SystemRandom()
        return [''.join(rndValue.choice(string.ascii_uppercase + string.digits) for _ in range(10))]

    @property
    def isScalar(self):
        return self.dataSize == 1
