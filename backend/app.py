# backend/app.py
#python -m waitress --listen=0.0.0.0:5000 app:app

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from songs import mood_data
import os

# Install these if you haven'                                                                                                        
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import timedelta
from functools import wraps
from send_mail import send_contact_email

SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_secret_key')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Prefer DATABASE_URL from environment (Render sets this). Fallback to the existing value for local/dev.
database_url = os.environ.get('DATABASE_URL')
# SQLAlchemy expects postgresql://; some providers give postgres://
if database_url.startswith('postgresql://'):
    database_url = database_url.replace("postgresql://", "postgresql+psycopg://", 1)
    
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_premium = db.Column(db.Boolean, default=False)  # Premium status
    premium_until = db.Column(db.DateTime, nullable=True)  # Premium expiry
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship('User', backref=db.backref('playlists', lazy=True))

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    artist = db.Column(db.String(120))
    file_url = db.Column(db.String(255))
    mood = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PlaylistSong(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)

class RecentlyPlayed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    played_at = db.Column(db.DateTime, default=datetime.utcnow)

class LikedSong(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    liked_at = db.Column(db.DateTime, default=datetime.utcnow)

class SmartShuffleQueue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    position = db.Column(db.Integer, nullable=False)  # Order in the queue
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship('User', backref=db.backref('smart_shuffle_queue', lazy=True))
    song = db.relationship('Song', backref=db.backref('smart_shuffle_queues', lazy=True))

class SmartShuffleHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    played_at = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship('User', backref=db.backref('smart_shuffle_history', lazy=True))
    song = db.relationship('Song', backref=db.backref('smart_shuffle_histories', lazy=True))

# Serve static files (songs)
@app.route('/static/songs/<path:filename>')
def serve_song(filename):
    songs_dir = os.path.join(os.path.dirname(__file__), 'static', 'songs')
    return send_from_directory(songs_dir, filename)

@app.route('/api/moods', methods=['GET'])
def get_moods():
    return jsonify(mood_data["moods"])

@app.route('/api/songs/<mood_id>', methods=['GET'])
def get_songs_by_mood(mood_id):
    songs = mood_data["recommendedSongs"].get(mood_id, [])
    # Ensure each song has id, title, artist, file_url, and mood
    result = []
    for s in songs:
        # If s is a dict with id, use as is; else, map fields
        if isinstance(s, dict) and 'id' in s:
            result.append(s)
        else:
            # Try to find the song in the DB by file or title
            db_song = Song.query.filter_by(title=s.get('title')).first() if isinstance(s, dict) else None
            if db_song:
                result.append({
                    'id': db_song.id,
                    'title': db_song.title,
                    'artist': db_song.artist,
                    'file_url': db_song.file_url,
                    'mood': db_song.mood,
                    'copyright': s.get('copyright', ''),
                    'ncsLink': s.get('ncsLink', ''),
                    'ncsWatch': s.get('ncsWatch', '')
                })
            else:
                # fallback: include mood from mood_id
                result.append({
                    'id': None,
                    'title': s.get('title') if isinstance(s, dict) else str(s),
                    'artist': s.get('artist') if isinstance(s, dict) else '',
                    'file_url': s.get('file') if isinstance(s, dict) else '',
                    'mood': mood_id,
                    'copyright': s.get('copyright', ''),
                    'ncsLink': s.get('ncsLink', ''),
                    'ncsWatch': s.get('ncsWatch', '')
                })
    return jsonify(result)

@app.route('/api/songs', methods=['GET'])
def get_all_songs():
    songs = Song.query.all()
    result = []
    for s in songs:
        # Try to find the song in mood_data to get copyright info
        copyright_info = ''
        ncs_link = ''
        ncs_watch = ''
        
        for mood_songs in mood_data['recommendedSongs'].values():
            for mood_song in mood_songs:
                if isinstance(mood_song, dict) and mood_song.get('title') == s.title:
                    copyright_info = mood_song.get('copyright', '')
                    ncs_link = mood_song.get('ncsLink', '')
                    ncs_watch = mood_song.get('ncsWatch', '')
                    break
            if copyright_info:
                break
        
        result.append({
            'id': s.id,
            'title': s.title,
            'artist': s.artist,
            'file_url': s.file_url,
            'mood': s.mood,
            'copyright': copyright_info,
            'ncsLink': ncs_link,
            'ncsWatch': ncs_watch
        })
    return jsonify(result)

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username or not email or not password:
        return jsonify({'error': 'Missing fields'}), 400
    
    # Check for existing username
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error': 'Username already exists, choose a different one'}), 409
    
    # Check for existing email
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'error': 'Email already exists, choose a different one'}), 409
    
    password_hash = generate_password_hash(password)
    user = User(username=username, email=email, password_hash=password_hash)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

@app.route('/api/signup', methods=['OPTIONS'])
def signup_options():
    return '', 200

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'error': 'Missing fields'}), 400
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid credentials'}), 401
    # Generate JWT token
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(days=7)
    }, SECRET_KEY, algorithm='HS256')
    return jsonify({'token': token, 'username': user.username, 'email': user.email})

@app.route('/api/profile', methods=['GET'])
def profile():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Missing or invalid token'}), 401
    token = auth_header.split(' ')[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user = User.query.get(payload['user_id'])
        if not user:
            return jsonify({'error': 'User not found'}), 404
        return jsonify({
            'username': user.username, 
            'email': user.email,
            'is_premium': user.is_premium,
            'premium_until': user.premium_until.strftime('%Y-%m-%d') if user.premium_until else None
        })
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Missing or invalid token'}), 401
        token = auth_header.split(' ')[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user = User.query.get(payload['user_id'])
            if not user:
                return jsonify({'error': 'User not found'}), 404
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
    return decorated

@app.route('/api/playlists', methods=['POST'])
@token_required
def create_playlist(current_user):
    data = request.json
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Missing playlist name'}), 400
    playlist = Playlist(user_id=current_user.id, name=name)
    db.session.add(playlist)
    db.session.commit()
    return jsonify({'id': playlist.id, 'name': playlist.name}), 201

@app.route('/api/playlists', methods=['GET'])
@token_required
def get_playlists(current_user):
    playlists = Playlist.query.filter_by(user_id=current_user.id).all()
    result = []
    
    # Add Liked Songs playlist at the beginning
    liked_songs = (LikedSong.query
        .filter_by(user_id=current_user.id)
        .order_by(LikedSong.liked_at.desc())
        .all())
    liked_songs_list = []
    for ls in liked_songs:
        song = Song.query.get(ls.song_id)
        if song:
            liked_songs_list.append({'id': song.id, 'title': song.title, 'artist': song.artist, 'file_url': song.file_url, 'mood': song.mood})
    
    result.append({'id': 'liked_songs', 'name': 'Liked Songs', 'songs': liked_songs_list, 'is_liked_playlist': True})
    
    # Add regular playlists
    for p in playlists:
        songs = PlaylistSong.query.filter_by(playlist_id=p.id).all()
        song_list = []
        for ps in songs:
            song = Song.query.get(ps.song_id)
            if song:
                song_list.append({'id': song.id, 'title': song.title, 'artist': song.artist, 'file_url': song.file_url, 'mood': song.mood})
        result.append({'id': p.id, 'name': p.name, 'songs': song_list, 'is_liked_playlist': False})
    return jsonify(result)

@app.route('/api/playlists/<int:playlist_id>', methods=['PUT'])
@token_required
def rename_playlist(current_user, playlist_id):
    data = request.json
    new_name = data.get('name')
    playlist = Playlist.query.filter_by(id=playlist_id, user_id=current_user.id).first()
    if not playlist:
        return jsonify({'error': 'Playlist not found'}), 404
    if not new_name:
        return jsonify({'error': 'Missing new name'}), 400
    playlist.name = new_name
    db.session.commit()
    return jsonify({'id': playlist.id, 'name': playlist.name})

@app.route('/api/playlists/<int:playlist_id>', methods=['DELETE'])
@token_required
def delete_playlist(current_user, playlist_id):
    playlist = Playlist.query.filter_by(id=playlist_id, user_id=current_user.id).first()
    if not playlist:
        return jsonify({'error': 'Playlist not found'}), 404
    PlaylistSong.query.filter_by(playlist_id=playlist.id).delete()
    db.session.delete(playlist)
    db.session.commit()
    return jsonify({'message': 'Playlist deleted'})

@app.route('/api/playlists/<int:playlist_id>/songs', methods=['POST'])
@token_required
def add_song_to_playlist(current_user, playlist_id):
    data = request.json
    song_id = data.get('song_id')
    playlist = Playlist.query.filter_by(id=playlist_id, user_id=current_user.id).first()
    if not playlist:
        return jsonify({'error': 'Playlist not found'}), 404
    song = Song.query.get(song_id)
    if not song:
        return jsonify({'error': 'Song not found'}), 404
    if PlaylistSong.query.filter_by(playlist_id=playlist.id, song_id=song.id).first():
        return jsonify({'error': 'Song already in playlist'}), 409
    # Enforce 20-song limit for free users
    current_count = PlaylistSong.query.filter_by(playlist_id=playlist.id).count()
    if not current_user.is_premium and current_count >= 20:
        return jsonify({
            'error': 'Free users can only add up to 20 songs per playlist. Upgrade to Premium for unlimited playlists!',
            'limit_reached': True,
            'current_count': current_count,
            'limit': 20
        }), 403
    ps = PlaylistSong(playlist_id=playlist.id, song_id=song.id)
    db.session.add(ps)
    db.session.commit()
    return jsonify({'message': 'Song added'})

@app.route('/api/playlists/<int:playlist_id>/songs/<int:song_id>', methods=['DELETE'])
@token_required
def remove_song_from_playlist(current_user, playlist_id, song_id):
    playlist = Playlist.query.filter_by(id=playlist_id, user_id=current_user.id).first()
    if not playlist:
        return jsonify({'error': 'Playlist not found'}), 404
    ps = PlaylistSong.query.filter_by(playlist_id=playlist.id, song_id=song_id).first()
    if not ps:
        return jsonify({'error': 'Song not in playlist'}), 404
    db.session.delete(ps)
    db.session.commit()
    return jsonify({'message': 'Song removed'})

@app.route('/api/recently-played', methods=['GET'])
@token_required
def get_recently_played(current_user):
    recents = (RecentlyPlayed.query
        .filter_by(user_id=current_user.id)
        .order_by(RecentlyPlayed.played_at.desc())
        .limit(10)
        .all())
    result = []
    for rp in recents:
        song = Song.query.get(rp.song_id)
        if song:
            result.append({
                'id': song.id,
                'title': song.title,
                'artist': song.artist,
                'file_url': song.file_url,
                'mood': song.mood,
                'played_at': rp.played_at.strftime('%Y-%m-%d %H:%M:%S')
            })
    return jsonify(result)

@app.route('/api/recently-played', methods=['POST'])
@token_required
def add_recently_played(current_user):
    data = request.json
    song_id = data.get('song_id')
    if not song_id:
        return jsonify({'error': 'Missing song_id'}), 400
    # Remove if already exists (to re-add at top)
    old = RecentlyPlayed.query.filter_by(user_id=current_user.id, song_id=song_id).first()
    if old:
        db.session.delete(old)
        db.session.commit()
    # Add new
    rp = RecentlyPlayed(user_id=current_user.id, song_id=song_id)
    db.session.add(rp)
    db.session.commit()
    # Keep only 10
    recents = (RecentlyPlayed.query
        .filter_by(user_id=current_user.id)
        .order_by(RecentlyPlayed.played_at.desc())
        .all())
    for rp_extra in recents[10:]:
        db.session.delete(rp_extra)
    db.session.commit()
    return jsonify({'message': 'Added to recently played'})

# Liked Songs API endpoints
@app.route('/api/liked-songs', methods=['GET'])
@token_required
def get_liked_songs(current_user):
    liked_songs = (LikedSong.query
        .filter_by(user_id=current_user.id)
        .order_by(LikedSong.liked_at.desc())
        .all())
    result = []
    for ls in liked_songs:
        song = Song.query.get(ls.song_id)
        if song:
            result.append({
                'id': song.id,
                'title': song.title,
                'artist': song.artist,
                'file_url': song.file_url,
                'mood': song.mood,
                'liked_at': ls.liked_at.strftime('%Y-%m-%d %H:%M:%S')
            })
    return jsonify(result)

@app.route('/api/liked-songs/<int:song_id>', methods=['POST'])
@token_required
def like_song(current_user, song_id):
    song = Song.query.get(song_id)
    if not song:
        return jsonify({'error': 'Song not found'}), 404
    
    # Check if already liked
    existing_like = LikedSong.query.filter_by(user_id=current_user.id, song_id=song_id).first()
    if existing_like:
        return jsonify({'error': 'Song already liked'}), 409
    
    # Add to liked songs
    liked_song = LikedSong(user_id=current_user.id, song_id=song_id)
    db.session.add(liked_song)
    db.session.commit()
    return jsonify({'message': 'Song liked successfully'})

@app.route('/api/liked-songs/<int:song_id>', methods=['DELETE'])
@token_required
def unlike_song(current_user, song_id):
    liked_song = LikedSong.query.filter_by(user_id=current_user.id, song_id=song_id).first()
    if not liked_song:
        return jsonify({'error': 'Song not liked'}), 404
    
    db.session.delete(liked_song)
    db.session.commit()
    return jsonify({'message': 'Song unliked successfully'})

@app.route('/api/liked-songs/<int:song_id>/status', methods=['GET'])
@token_required
def check_liked_status(current_user, song_id):
    liked_song = LikedSong.query.filter_by(user_id=current_user.id, song_id=song_id).first()
    return jsonify({'liked': liked_song is not None})

# Smart Shuffle API endpoints
@app.route('/api/smart-shuffle/queue', methods=['GET'])
@token_required
def get_smart_shuffle_queue(current_user):
    """Get user's smart shuffle queue"""
    queue_items = (SmartShuffleQueue.query
        .filter_by(user_id=current_user.id)
        .order_by(SmartShuffleQueue.position)
        .all())
    
    result = []
    for item in queue_items:
        song = Song.query.get(item.song_id)
        if song:
            result.append({
                'id': song.id,
                'title': song.title,
                'artist': song.artist,
                'file_url': song.file_url,
                'mood': song.mood,
                'position': item.position,
                'added_at': item.added_at.strftime('%Y-%m-%d %H:%M:%S')
            })
    return jsonify(result)

@app.route('/api/smart-shuffle/queue', methods=['POST'])
@token_required
def add_to_smart_shuffle_queue(current_user):
    """Add song to smart shuffle queue"""
    data = request.json
    song_id = data.get('song_id')
    
    if not song_id:
        return jsonify({'error': 'Missing song_id'}), 400
    
    song = Song.query.get(song_id)
    if not song:
        return jsonify({'error': 'Song not found'}), 404
    
    # Check if song is already in queue
    existing = SmartShuffleQueue.query.filter_by(user_id=current_user.id, song_id=song_id).first()
    if existing:
        return jsonify({'error': 'Song already in queue'}), 409
    
    # Debug logging
    current_count = SmartShuffleQueue.query.filter_by(user_id=current_user.id).count()
    print(f"[DEBUG] User ID: {current_user.id}, is_premium: {current_user.is_premium}, current_count: {current_count}")
    
    # Premium check: Free users limited to 20 songs
    if not current_user.is_premium:
        if current_count >= 20:
            print(f"[DEBUG] LIMIT REACHED for user {current_user.id}")
            return jsonify({
                'error': 'Free users can only add up to 20 songs to Smart Shuffle. Upgrade to Premium for unlimited songs!',
                'limit_reached': True,
                'current_count': current_count,
                'limit': 20
            }), 403
    
    # Get next position
    max_position = db.session.query(db.func.max(SmartShuffleQueue.position)).filter_by(user_id=current_user.id).scalar()
    next_position = (max_position or 0) + 1
    
    # Add to queue
    queue_item = SmartShuffleQueue(user_id=current_user.id, song_id=song_id, position=next_position)
    db.session.add(queue_item)
    db.session.commit()
    
    return jsonify({'message': 'Song added to smart shuffle queue'})

@app.route('/api/smart-shuffle/queue/<int:song_id>', methods=['DELETE'])
@token_required
def remove_from_smart_shuffle_queue(current_user, song_id):
    """Remove song from smart shuffle queue"""
    queue_item = SmartShuffleQueue.query.filter_by(user_id=current_user.id, song_id=song_id).first()
    if not queue_item:
        return jsonify({'error': 'Song not in queue'}), 404
    
    # Get position of removed item
    removed_position = queue_item.position
    
    # Remove the item
    db.session.delete(queue_item)
    db.session.commit()
    
    # Reorder remaining items
    remaining_items = SmartShuffleQueue.query.filter_by(user_id=current_user.id).filter(SmartShuffleQueue.position > removed_position).all()
    for item in remaining_items:
        item.position -= 1
    db.session.commit()
    
    return jsonify({'message': 'Song removed from smart shuffle queue'})

@app.route('/api/smart-shuffle/queue', methods=['DELETE'])
@token_required
def clear_smart_shuffle_queue(current_user):
    """Clear entire smart shuffle queue"""
    SmartShuffleQueue.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    return jsonify({'message': 'Smart shuffle queue cleared'})

@app.route('/api/smart-shuffle/history', methods=['GET'])
@token_required
def get_smart_shuffle_history(current_user):
    """Get user's smart shuffle history"""
    history_items = (SmartShuffleHistory.query
        .filter_by(user_id=current_user.id)
        .order_by(SmartShuffleHistory.played_at.desc())
        .limit(50)
        .all())
    
    result = []
    for item in history_items:
        song = Song.query.get(item.song_id)
        if song:
            result.append({
                'id': song.id,
                'title': song.title,
                'artist': song.artist,
                'file_url': song.file_url,
                'mood': song.mood,
                'played_at': item.played_at.strftime('%Y-%m-%d %H:%M:%S')
            })
    return jsonify(result)

@app.route('/api/smart-shuffle/history', methods=['POST'])
@token_required
def add_to_smart_shuffle_history(current_user):
    """Add song to smart shuffle history"""
    data = request.json
    song_id = data.get('song_id')
    
    if not song_id:
        return jsonify({'error': 'Missing song_id'}), 400
    
    song = Song.query.get(song_id)
    if not song:
        return jsonify({'error': 'Song not found'}), 404
    
    # Add to history
    history_item = SmartShuffleHistory(user_id=current_user.id, song_id=song_id)
    db.session.add(history_item)
    db.session.commit()
    
    # Keep only last 50 items
    history_items = (SmartShuffleHistory.query
        .filter_by(user_id=current_user.id)
        .order_by(SmartShuffleHistory.played_at.desc())
        .all())
    
    for extra_item in history_items[50:]:
        db.session.delete(extra_item)
    db.session.commit()
    
    return jsonify({'message': 'Song added to smart shuffle history'})

@app.route('/api/premium/upgrade', methods=['POST'])
@token_required
def upgrade_to_premium(current_user):
    """Upgrade user to premium (demo endpoint)"""
    # In a real app, this would integrate with payment processing
    # For demo purposes, we'll just upgrade the user
    current_user.is_premium = True
    current_user.premium_until = datetime.utcnow() + timedelta(days=30)  # 30 days trial
    db.session.commit()
    
    return jsonify({
        'message': 'Successfully upgraded to Premium!',
        'is_premium': True,
        'premium_until': current_user.premium_until.strftime('%Y-%m-%d')
    })

@app.route('/api/premium/status', methods=['GET'])
@token_required
def get_premium_status(current_user):
    """Get user's premium status"""
    return jsonify({
        'is_premium': current_user.is_premium,
        'premium_until': current_user.premium_until.strftime('%Y-%m-%d') if current_user.premium_until else None
    })

@app.route('/api/contact', methods=['POST'])
def contact_us():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    if not name or not email or not message:
        return jsonify({'error': 'Missing fields'}), 400
    success = send_contact_email(name, email, message)
    if success:
        return jsonify({'message': 'Message sent successfully!'}), 200
    else:
        return jsonify({'error': 'Failed to send message. Please try again later.'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # --- Automatic Song Seeding ---
        from songs import mood_data
        if Song.query.count() == 0:
            for mood, songs in mood_data['recommendedSongs'].items():
                for s in songs:
                    db.session.add(Song(
                        title=s.get('title', ''),
                        artist=s.get('artist', ''),
                        file_url=s.get('file', ''),
                        mood=mood
                    ))
            db.session.commit()
            print('Seeded Song table from mood_data!')
    print('Database tables created!')
    app.run(debug=True, host='0.0.0.0', port=5000)
