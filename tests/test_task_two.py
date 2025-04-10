from lib.task_two import *
"""
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to 
and see a list of them. 


Name: Tracker
Parameters: song name as string
Return: List of songs
"""

def test_empty_track_added():
    tracker = Tracker()
    result = tracker.return_track_list()
    assert result == []

def test_one_track_added():
    tracker = Tracker()
    tracker.add_track('A good song')
    result = tracker.return_track_list()
    assert result == ['A good song']

def test_two_track_added():
    tracker = Tracker()
    tracker.add_track('A good song')
    tracker.add_track('A bad song')
    result = tracker.return_track_list()
    assert result == ['A good song', 'A bad song']

def test_two_identical_tracks_added():
    tracker = Tracker()
    tracker.add_track('A good song')
    tracker.add_track('A good song')
    result = tracker.return_track_list()
    assert result == ['A good song']