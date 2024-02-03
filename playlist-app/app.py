from flask import Flask, redirect, render_template, jsonify, url_for, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import PlaylistForm, SongForm, NewSongForPlaylistForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ryan:password@localhost/playlist-app'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///playlist_app?host=/var/run/postgresql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

with app.app_context():
    connect_db(app)
    db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
    # app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""
    return redirect("/playlists")


##############################################################################
# Playlist routes

@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""
    playlists = Playlist.query.order_by(Playlist.id).all()
    return render_template("playlists.html", 
                           playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    playlist = Playlist.query.get_or_404(playlist_id)
    # playlist = Playlist.query.join(Song).filter_by()
    return render_template("playlist.html",
                           playlist=playlist)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:
    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """
    form = PlaylistForm()
    if form.validate_on_submit():
        new_playlist = Playlist(
            name=form.name.data,
            description=form.description.data
        )
        db.session.add(new_playlist)
        db.session.commit()
        return redirect(url_for('show_all_playlists'))
    return render_template("new_playlist.html",
                           form=form)


##############################################################################
# Song routes

@app.route("/songs")
def show_all_songs():
    """Show list of songs."""
    songs = Song.query.all()
    return render_template("songs.html", 
                           songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""
    song = Song.query.get_or_404(song_id)
    return render_template("song.html",
                           song=song)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """
    form = SongForm()
    if form.validate_on_submit():
        new_song = Song(
            title=form.title.data,
            artist=form.artist.data,
            album=form.album.data
        )
        db.session.add(new_song)
        db.session.commit()
        return redirect(url_for('show_all_songs'))
    return render_template("new_song.html",
                           form=form)


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""
    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()
    curr_on_playlist = [song.song_id for song in playlist.songs]
    form.song.choices = [(song.song_id, f"{song.title}") for song in Song.query.filter(Song.song_id.notin_(curr_on_playlist)).all()]
    if form.validate_on_submit():
        selected_song_id = form.song.data
        if PlaylistSong.query.filter_by(playlist_id=playlist_id, song_id=selected_song_id).first():
            flash("Song is already in the playlist.", 'danger')
        else: 
            playlist_song = PlaylistSong(playlist_id=playlist_id, song_id=selected_song_id)
            db.session.add(playlist_song)
            db.session.commit()
        return redirect(f"/playlists/{playlist_id}")
    return render_template("add_song_to_playlist.html",
                             playlist=playlist,
                             form=form)

# ===================================================================
if __name__ == '__main__':
    app.run(debug=True)
