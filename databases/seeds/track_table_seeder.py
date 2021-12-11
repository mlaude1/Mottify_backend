"""TrackTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Track import Track

class TrackTableSeeder(Seeder):
    def run(self):
        Track.create({
            "title": "Poetic Justice",
            "artist": "Kendrick Lamar, Drake",
            "album": "good kid, m.A.A.d city",
            "albumCover": "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.killerhiphop.com%2Fwp-content%2Fuploads%2F2012%2F09%2Fkendrick-lamar-good-kid-maad-city-deluxe.jpg&f=1&nofb=1",
            "genre": "Hip-Hop, Rap",
            "trackLength": "5:00",
            "mp3Url": "https://res.cloudinary.com/asianboymandude/video/upload/v1639237324/Kendrick_Lamar_-_Poetic_Justice_feat_Drake_nmtklc.mp4"
        })
        Track.create({
            "title": "Leave The Door Open",
            "artist": "Bruno Mars, Anderson .Paak",
            "album": "An Evening With Silk Sonic",
            "albumCover": "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.soulinstereo.com%2Fwp-content%2Fuploads%2F2021%2F11%2Fan-evening-with-Silk-Sonic.jpg&f=1&nofb=1",
            "genre": "R&B, pop",
            "trackLength": "4:02",
            "mp3Url": "https://res.cloudinary.com/asianboymandude/video/upload/v1639237421/Bruno_Mars_-_Leave_The_Door_Open_y5u8tp.mp3"
        })
