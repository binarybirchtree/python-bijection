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

import sys
import unittest

import bijection as bijection_module


class TestBijection(unittest.TestCase):
    def test_converted_output_has_same_length_as_input(self):
        input_value = b'Test input'
        bijection = bijection_module.Bijection(seed='Test seed')
        converted = bijection.convert_bytes(input_value=input_value)

        self.assertEqual(len(converted), len(input_value))

    def test_roundtrip_conversion_with_different_seeds(self):
        input_value = b'Test input'

        bijection1 = bijection_module.Bijection(seed='Test seed 1')
        bijection2 = bijection_module.Bijection(seed='Test seed 2')

        converted = bijection1.convert_bytes(input_value=input_value)
        reverted = bijection2.revert_bytes(input_value=converted)

        self.assertNotEqual(reverted, input_value)

    def test_roundtrip_conversion_with_identical_seeds(self):
        input_value = b'Test input'
        seed = 'Test seed'

        bijection1 = bijection_module.Bijection(seed=seed)
        bijection2 = bijection_module.Bijection(seed=seed)

        converted = bijection1.convert_bytes(input_value=input_value)
        reverted = bijection2.revert_bytes(input_value=converted)

        self.assertEqual(reverted, input_value)

    def _test_roundtrip_conversion(self, conversion_type, input_value):
        bijection = bijection_module.Bijection(seed='Test seed')
        conversion_method = getattr(
            bijection,
            'convert_{type}'.format(type=conversion_type)
        )
        reversion_method = getattr(
            bijection,
            'revert_{type}'.format(type=conversion_type)
        )

        converted = conversion_method(input_value=input_value)
        reverted = reversion_method(input_value=converted)

        self.assertEqual(reverted, input_value)

    def test_roundtrip_conversion_for_empty_byte_array(self):
        self._test_roundtrip_conversion(
            conversion_type='bytes',
            input_value=b''
        )

    def test_roundtrip_conversion_for_non_empty_byte_array(self):
        self._test_roundtrip_conversion(
            conversion_type='bytes',
            input_value=b'Test input'
        )

    def test_roundtrip_conversion_for_empty_string(self):
        self._test_roundtrip_conversion(
            conversion_type='string',
            input_value=''
        )

    def test_roundtrip_conversion_for_non_empty_string(self):
        self._test_roundtrip_conversion(
            conversion_type='string',
            input_value='Test input'
        )

    def test_roundtrip_conversion_for_unsigned_8_bit_integers(self):
        for input_value in range(256):
            self._test_roundtrip_conversion(
                conversion_type='uint8',
                input_value=input_value
            )

    def test_roundtrip_conversion_for_unsigned_16_bit_integers(self):
        self._test_roundtrip_conversion(
            conversion_type='uint16',
            input_value=65535
        )

    def test_roundtrip_conversion_for_unsigned_32_bit_integers(self):
        self._test_roundtrip_conversion(
            conversion_type='uint32',
            input_value=4294967295
        )

    def test_roundtrip_conversion_for_unsigned_64_bit_integers(self):
        self._test_roundtrip_conversion(
            conversion_type='uint64',
            input_value=18446744073709551615
        )

    def test_roundtrip_conversion_for_signed_8_bit_integers(self):
        for input_value in range(-128, 128):
            self._test_roundtrip_conversion(
                conversion_type='int8',
                input_value=input_value
            )

    def test_roundtrip_conversion_for_signed_16_bit_integers(self):
        self._test_roundtrip_conversion(
            conversion_type='int16',
            input_value=-32768
        )

    def test_roundtrip_conversion_for_signed_32_bit_integers(self):
        self._test_roundtrip_conversion(
            conversion_type='int32',
            input_value=-2147483648
        )

    def test_roundtrip_conversion_for_signed_64_bit_integers(self):
        self._test_roundtrip_conversion(
            conversion_type='int64',
            input_value=-9223372036854775808
        )
