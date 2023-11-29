"""Forms for playlist app."""
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'veryveryVERY_secretkey'  # Change this to a random secret key


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField('Name of Playlist', 
                       validators=[DataRequired(), 
                        Length(max=50)])
    description = StringField('Description', 
                       validators=[Length(max=255)])
    submit = SubmitField('Create Playlist')


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField('Title of Song',
                        validators=[DataRequired(), 
                        Length(max=50)])
    artist = StringField('Artist',
                        validators=[Length(max=50)])
    album = StringField('Name of Album',
                        validators=[Length(max=100)])
    submit = SubmitField('Create Song')


class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""
    song = SelectField('Song To Add', coerce=int)
    submit = SubmitField("Add Song To Playlist")
