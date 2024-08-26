from main import *

def test_binary_to_decimal():
    assert binary_to_decimal("00000000") == 0
    assert binary_to_decimal("00000001") == 1
    assert binary_to_decimal("00000010") == 2
    assert binary_to_decimal("00001010") == 10
    assert binary_to_decimal("00001101") == 13
    assert binary_to_decimal("11111111") == 255
    assert binary_to_decimal("10000000") == 128
    assert binary_to_decimal("00000111") == 7
    assert binary_to_decimal("00010000") == 16
    assert binary_to_decimal("01111111") == 127

def test_decimal_to_binary():
    assert decimal_to_binary(0) == "00000000"
    assert decimal_to_binary(1) == "00000001"
    assert decimal_to_binary(2) == "00000010"
    assert decimal_to_binary(10) == "00001010"
    assert decimal_to_binary(13) == "00001101"
    assert decimal_to_binary(255) == "11111111"
    assert decimal_to_binary(128) == "10000000"
    assert decimal_to_binary(7) == "00000111"
    assert decimal_to_binary(16) == "00010000"
    assert decimal_to_binary(127) == "01111111"
