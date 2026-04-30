class Song:
    def __init__(self, name, artist, length):
        self.name = name
        self.artist = artist
        self.length = length  # en minutes

    def get_length_in_seconds(self):
        return self.length * 60