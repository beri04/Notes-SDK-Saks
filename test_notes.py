import json
import os
import pytest
from notes_sdk.notes import Notes

# file_name = "test_notes.json"
@pytest.fixture
def sdk():
    # if os.path.exists(file_name):
    #     os.remove(file_name)
        
        return Notes()


def test_create(sdk):
    # sdk = Notes()
    result = sdk.create("","eggs,sex,bro")
    assert "created" in result
    assert sdk.read("") == "eggs,sex,bro"

def test_create(sdk):
    # sdk = Notes()
    result = sdk.create("Bro","yzzzz")
    assert "created" in result
    assert sdk.read("Bro") == "yzzzz"

def test_read(sdk):
    # sdk = Notes()
    sdk.create("Todo","Study")
    assert "Study" in sdk.read("Todo")
    assert "doesn't" in sdk.read("Nothing") 

def test_update(sdk):
    # sdk = Notes()
    sdk.create("Todo", "Study")
    result = sdk.update("Todo","Study + practice")
    assert "updated" in result
    assert sdk.read("Todo") == "Study + practice" 


def test_delete(sdk):
    # sdk = Notes()
    sdk.create("Saks","Bath + Breakfast")
    result = sdk.delete("Saks")
    assert "deleted" in result
    result1 = sdk.delete("Saks")
    assert "Nothing to delete" in result1

def test_get_all(sdk):
    # sdk = Notes()
    # sdk.create("Bro","Study + Bath + Breakfast")
    result = sdk.get_all()
    assert result == {'Bro': 'yzzzz', 'Todo': 'Study + practice'}