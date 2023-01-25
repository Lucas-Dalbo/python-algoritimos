import pytest
from challenges.challenge_encrypt_message import encrypt_message


INVALID_KEY = '1'
INVALID_MESSAGE = 1453

VALID_KEY_EVEN = 2
VALID_KEY_ODD = 3
VALID_MESSAGE = 'ABCDE'
VALID_MESSAGE_2 = 'casablanca'

RESULT_NOT_FOUND = 'EDCBA'
RESULT_EVEN = 'EDC_BA'
RESULT_ODD = 'sac_acnalba'


def test_encrypt_message():
    _test_key_not_int()
    _test_message_not_sting()
    _test_key_not_found()
    _test_key_even()
    _test_key_odd()


def _test_key_not_int():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(VALID_MESSAGE, INVALID_KEY)


def _test_message_not_sting():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(INVALID_MESSAGE, VALID_KEY_EVEN)


def _test_key_not_found():
    result = encrypt_message(VALID_MESSAGE, 100)
    assert result == RESULT_NOT_FOUND


def _test_key_even():
    result = encrypt_message(VALID_MESSAGE, VALID_KEY_EVEN)
    assert result == RESULT_EVEN


def _test_key_odd():
    result = encrypt_message(VALID_MESSAGE_2, VALID_KEY_ODD)
    assert result == RESULT_ODD
