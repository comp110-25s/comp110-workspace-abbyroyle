"""Unit tests."""

__author__ = "730472123"

import pytest
from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


# -------- invert tests --------
def test_invert_edge_empty():
    """Invert an empty dictionary should return empty dictionary."""
    assert invert({}) == {}


def test_invert_use_case_1():
    """Invert a normal dictionary with unique values."""
    assert invert({"a": "z", "b": "y"}) == {"z": "a", "y": "b"}


def test_invert_raises_key_error():
    """Invert with duplicate values should raise KeyError."""
    with pytest.raises(KeyError):
        invert({"a": "x", "b": "x"})


# -------- count tests --------
def test_count_edge_empty():
    """Counting an empty list should return empty dict."""
    assert count([]) == {}


def test_count_use_case_1():
    """Counting multiple same items in list."""
    assert count(["a", "a", "b"]) == {"a": 2, "b": 1}


def test_count_use_case_2():
    """Counting all unique items."""
    assert count(["x", "y", "z"]) == {"x": 1, "y": 1, "z": 1}


# -------- favorite_color tests --------
def test_favorite_color_edge_empty():
    """Favorite color with empty dict returns None or raises."""
    with pytest.raises(ValueError):
        favorite_color({})


def test_favorite_color_use_case_1():
    """Most common color returned."""
    assert favorite_color({"a": "red", "b": "blue", "c": "red"}) == "red"


def test_favorite_color_tie():
    """In case of tie, return first encountered."""
    assert favorite_color({"a": "red", "b": "blue", "c": "blue", "d": "red"}) == "red"


# -------- bin_len tests --------
def test_bin_len_edge_empty():
    """Binning empty list returns empty dictionary."""
    assert bin_len([]) == {}


def test_bin_len_use_case_1():
    """Binning strings of varying lengths."""
    assert bin_len(["hi", "hello", "hey"]) == {2: {"hi"}, 5: {"hello"}, 3: {"hey"}}


def test_bin_len_duplicates():
    """Duplicate strings should not repeat in set."""
    assert bin_len(["a", "a", "ab"]) == {1: {"a"}, 2: {"ab"}}
