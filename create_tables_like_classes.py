class Singer:
    def __init__(self, name):
        self.name=name


class Genre:
    def __init__(self, genre_name):
        self.genre_name=genre_name


class SingerGenre:
    def __init__(self, singer_id, genre_id):
        self.singer_id = singer_id
        self.genre_id = genre_id


class Album:
    def __init__(self, title, year_of_start, ratio):
        self.title = title
        self.year_of_start = year_of_start
        self.ratio = ratio


class Track:
    def __init__(self, track_title, duration, is_like, album_id):
        self.track_title = track_title
        self.duration = duration
        self.is_like = is_like
        self.album_id = album_id


class SingerAlbum:
    def __init__(self, singer_id, album_id):
        self.singer_id = singer_id
        self.album_id = album_id


class Collection:
    def __init__(self, collection_title, description, start_year):
        self.collection_title = collection_title
        self.description = description
        self.start_year = start_year

class TrackCollection:
    def __init__(self, collection_id, track_id):
        self.collection_id = collection_id
        self.track_id = track_id
