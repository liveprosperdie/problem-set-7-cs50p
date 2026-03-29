
from working import convert
import pytest

def test_valid():
    assert convert("9:00 AM to 5:00 PM")=="09:00 to 17:00"
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM")=="00:00 to 12:00"

def test_edge():
    assert convert("12:00 AM to 1:00 AM")=="00:00 to 01:00"
    assert convert("12:00 PM to 12:00 AM")=="12:00 to 00:00"

def test_late():
    assert convert("5:00 PM to 9:00 AM")=="17:00 to 09:00"

def test_invalid_min():
    with pytest.raises (ValueError):
        assert convert("9:60 AM to 5:00 PM")==ValueError

def test_invalid_hour():
    with pytest.raises (ValueError):    
        assert convert("13:00 AM to 5:00 PM")==ValueError

def test_invalid_format():
    with pytest.raises (ValueError):    
        assert convert("9am to 5pm")==ValueError