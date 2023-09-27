from flask import Flask, flash, request, redirect, render_template
from waitress import serve
from utils import parseCookieFile, getUserAgent, setUserAgent
import json, os

from trackers.aither import Aither
from trackers.alpharatio import AlphaRatio
from trackers.animez import AnimeZ
from trackers.anthelion import Anthelion
from trackers.avistaz import AvistaZ
from trackers.cinemaz import CinemaZ
from trackers.filelist import FileList
from trackers.iptorrents import IPTorrents
from trackers.myanonamouse import MyAnonamouse
from trackers.orpheus import Orpheus
from trackers.torrentleech import TorrentLeech

app = Flask(__name__)
app.secret_key = os.urandom(24)

TRACKERS = {
    'aither': Aither,
    'alpharatio': AlphaRatio,
    'animez': AnimeZ,
    'anthelion': Anthelion,
    'avistaz': AvistaZ,
    'cinemaz': CinemaZ,
    'filelist': FileList,
    'iptorrents': IPTorrents,
    'myanonamouse': MyAnonamouse,
    'orpheus': Orpheus,
    'torrentleech': TorrentLeech
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            if request.form.get('user_agent'):
                setUserAgent(request.form.get('user_agent'))
                flash('User agent updated')
            else:
                flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        # If the file is valid, save it to the cookies folder
        if file and file.filename.split('.')[0] in TRACKERS:
            file.save('./cookies/' + file.filename)
            flash('File uploaded successfully')
            return redirect(request.url)
        
        # If the file is invalid, flash an error
        else:
            flash('Invalid file')
            return redirect(request.url)

    return render_template('upload.html', trackers=TRACKERS, user_agent=request.headers.get('User-Agent'), user_agent_file=getUserAgent())

@app.route('/<tracker>')
def tracker(tracker):
    if tracker in TRACKERS:
        if os.path.isfile('./cookies/' + tracker + '.txt'):
            try:
                tracker_class = TRACKERS[tracker]()
                tracker_class.get_stats(parseCookieFile('./cookies/' + tracker + '.txt'), {'User-Agent': getUserAgent()})
                return json.dumps(tracker_class.__dict__)
            except Exception as e:
                return json.dumps({'error': str(e)})
        else:
            return json.dumps({'error': 'No cookie file found for ' + tracker})
    else:
        return json.dumps({'error': 'Invalid tracker'})

if __name__ == '__main__':
    serve(app, listen='*:5000')