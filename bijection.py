# This file is part of Python-Bijection.
# Copyright 2016 Binary Birch Tree
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import struct

from Crypto.Cipher import AES
from Crypto.Hash import SHA256, SHAKE128


class Bijection(object):
    def __init__(self, seed):
        hash_input = seed.encode()
        self.key = SHA256.new(data=hash_input).digest()
        self.nonce = SHAKE128.new(data=hash_input).read(length=8)

    def _produce_cipher(self):
        return AES.new(key=self.key, mode=AES.MODE_CTR, nonce=self.nonce)

    def _convert_integer(self, format_string, input_value):
        return self.convert_bytes(
            input_value=struct.pack(format_string, input_value)
        )

    def _revert_integer(self, format_string, input_value):
        return struct.unpack(
            format_string,
            self.revert_bytes(input_value=input_value)
        )[0]

    def convert_bytes(self, input_value):
        """
        Converts a byte array.
        """
        return self._produce_cipher().encrypt(plaintext=input_value)

    def convert_string(self, input_value):
        """
        Converts a string.
        """
        return self.convert_bytes(input_value=input_value.encode())

    def convert_uint8(self, input_value):
        """
        Converts an unsigned 8-bit integer.
        """
        return self._convert_integer(
            format_string='=B',
            input_value=input_value
        )

    def convert_uint16(self, input_value):
        """
        Converts an unsigned 16-bit integer.
        """
        return self._convert_integer(
            format_string='=H',
            input_value=input_value
        )

    def convert_uint32(self, input_value):
        """
        Converts an unsigned 32-bit integer.
        """
        return self._convert_integer(
            format_string='=I',
            input_value=input_value
        )

    def convert_uint64(self, input_value):
        """
        Converts an unsigned 64-bit integer.
        """
        return self._convert_integer(
            format_string='=Q',
            input_value=input_value
        )

    def convert_int8(self, input_value):
        """
        Converts an signed 8-bit integer.
        """
        return self._convert_integer(
            format_string='=b',
            input_value=input_value
        )

    def convert_int16(self, input_value):
        """
        Converts an signed 16-bit integer.
        """
        return self._convert_integer(
            format_string='=h',
            input_value=input_value
        )

    def convert_int32(self, input_value):
        """
        Converts an signed 32-bit integer.
        """
        return self._convert_integer(
            format_string='=i',
            input_value=input_value
        )

    def convert_int64(self, input_value):
        """
        Converts an signed 64-bit integer.
        """
        return self._convert_integer(
            format_string='=q',
            input_value=input_value
        )

    def revert_bytes(self, input_value):
        """
        Reverts a byte array.
        """
        return self._produce_cipher().decrypt(ciphertext=input_value)

    def revert_string(self, input_value):
        """
        Reverts a string.
        """
        return self.revert_bytes(input_value=input_value).decode()

    def revert_uint8(self, input_value):
        """
        Reverts an unsigned 8-bit integer.
        """
        return self._revert_integer(
            format_string='=B',
            input_value=input_value
        )

    def revert_uint16(self, input_value):
        """
        Reverts an unsigned 16-bit integer.
        """
        return self._revert_integer(
            format_string='=H',
            input_value=input_value
        )

    def revert_uint32(self, input_value):
        """
        Reverts an unsigned 32-bit integer.
        """
        return self._revert_integer(
            format_string='=I',
            input_value=input_value
        )

    def revert_uint64(self, input_value):
        """
        Reverts an unsigned 64-bit integer.
        """
        return self._revert_integer(
            format_string='=Q',
            input_value=input_value
        )

    def revert_int8(self, input_value):
        """
        Reverts a signed 8-bit integer.
        """
        return self._revert_integer(
            format_string='=b',
            input_value=input_value
        )

    def revert_int16(self, input_value):
        """
        Reverts a signed 16-bit integer.
        """
        return self._revert_integer(
            format_string='=h',
            input_value=input_value
        )

    def revert_int32(self, input_value):
        """
        Reverts a signed 32-bit integer.
        """
        return self._revert_integer(
            format_string='=i',
            input_value=input_value
        )

    def revert_int64(self, input_value):
        """
        Reverts a signed 64-bit integer.
        """
        return self._revert_integer(
            format_string='=q',
            input_value=input_value
        )
