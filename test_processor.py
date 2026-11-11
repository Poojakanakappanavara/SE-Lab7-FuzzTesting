import pytest

from hypothesis import given, strategies as st
from processor import (
    parse_int_list,
    calculate_average,
    validate_age
)


# TEST 1: Parse comma-separated integers
@given(st.lists(st.integers(), min_size=0, max_size=50))
def test_parse_int_list(numbers):
    input_string = ",".join(map(str, numbers))
    assert parse_int_list(input_string) == numbers


def test_parse_int_list_invalid_input():
    assert parse_int_list(None) == []


# TEST 2: Calculate average
@given(st.lists(st.floats(
    allow_nan=False,
    allow_infinity=False,
    width=32
), min_size=1, max_size=50))
def test_calculate_average(numbers):
    result = calculate_average(numbers)
    expected = sum(numbers) / len(numbers)
    assert result == pytest.approx(expected)


def test_calculate_average_empty_list():
    assert calculate_average([]) == 0.0


# TEST 3: Validate age
@given(st.integers(min_value=0, max_value=120))
def test_validate_age_valid(age):
    assert validate_age(age) is True


@given(st.booleans())
def test_validate_age_rejects_boolean(age):
    assert validate_age(age) is False
