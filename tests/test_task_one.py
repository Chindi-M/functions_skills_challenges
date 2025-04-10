from lib.task_one import *
"""
As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

Name: includes_todo
Parameters: String
Return: Bool (True/False)
"""

def test_empty_string_is_false():
    result = includes_todo('')
    assert result == False

def test_if_string_is_todo():
    result = includes_todo('#TODO')
    assert result == True

def test_if_string_includes_todo():
    result = includes_todo('Walk the dog #TODO')
    assert result == True

def test_if_string_does_not_include_todo():
    result = includes_todo('Wash the dishes')
    assert result == False

def test_string_includes_todo_no_hash():
    result = includes_todo('TODO today')
    assert result == False


