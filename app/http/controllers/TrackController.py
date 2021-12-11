""" A TrackController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Track import Track


class TrackController(Controller):
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        id = self.request.param("id")
        return Track.find(id)

    def index(self):
        return Track.all()

    def create(self):
        title = self.request.input("title")
        artist = self.request.input("artist")
        album = self.request.input("album")
        albumCover = self.request.input("albumCover")
        genre = self.request.input("genre")
        trackLength = self.request.input("trackLength")
        mp3Url = self.request.input("mp3Url")
        track = Track.create({
            "title": title,
            "artist": artist,
            "album": album,
            "albumCover": albumCover,
            "genre": genre,
            "trackLength": trackLength,
            "mp3Url": mp3Url
        })
        return track


    def update(self):
        title = self.request.input("title")
        artist = self.request.input("artist")
        album = self.request.input("album")
        albumCover = self.request.input("albumCover")
        genre = self.request.input("genre")
        trackLength = self.request.input("trackLength")
        mp3Url = self.request.input("mp3Url")
        id = self.request.param("id")
        Track.where("id", id).update({
            "title": title,
            "artist": artist,
            "album": album,
            "albumCover": albumCover,
            "genre": genre,
            "trackLength": trackLength,
            "mp3Url": mp3Url
        })
        return Track.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        track = Track.where("id", id).get()
        Track.where("id", id).delete()
        return track