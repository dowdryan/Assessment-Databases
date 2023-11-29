"""Models for Playlist app."""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    _tablename_ = 'playlist'
    id = db.Column(db.Integer, 
                   primary_key=True)
    name = db.Column(db.String(255),
                     nullable=False)
    description = db.Column(db.String(255))
    songs = db.relationship('PlaylistSong',
                            backref="playlists")

class Song(db.Model):
    """Song."""
    _tablename_ = 'song'
    song_id = db.Column(db.Integer, 
                        primary_key=True)
    title = db.Column(db.String(255), 
                      nullable=False,
                      unique=True)
    artist = db.Column(db.String(255), 
                       nullable=False)
    album = db.Column(db.String(255))
    def to_dict(self): 
        return {
            "id": self.song_id,
            "title": self.title,
            "artist": self.artist if self.artist else "Unknown Artist",
            "album": self.album,
        }

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    _tablename_ = 'playlistsongs'
    playlist_id = db.Column(db.Integer, 
                            db.ForeignKey("playlist.id"), 
                            primary_key=True)
    song_id = db.Column(db.Integer, 
                        db.ForeignKey("song.song_id"), 
                        primary_key=True)
    def __repr__(self):
        ps = self
        return f"PlaylistSong<playlist_id={ps.playlist_id}, song_id={ps.song_id}>"


def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)