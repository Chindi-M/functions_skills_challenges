class Tracker():
    def __init__(self):
        self.track_list = []
    def add_track(self, track):
        if track not in self.track_list:
            self.track_list.append(track)
    def return_track_list(self):
        return self.track_list
        