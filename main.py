from flask import Flask, Response, flash, request, redirect, render_template
from waitress import serve
from utils import parseCookieFile, parseCookieFileExp, getUserAgent, setUserAgent
from dotenv import load_dotenv
from datetime import datetime
import json, os, humanize

from trackers.aither import Aither
from trackers.alpharatio import AlphaRatio
from trackers.animez import AnimeZ
from trackers.anthelion import Anthelion
from trackers.avistaz import AvistaZ
from trackers.blutopia import Blutopia
from trackers.cathoderaytube import CathodeRayTube
from trackers.cinemaz import CinemaZ
from trackers.filelist import FileList
from trackers.iptorrents import IPTorrents
from trackers.myanonamouse import MyAnonamouse
from trackers.nebulance import Nebulance
from trackers.oldtoonsworld import OldToonsWorld
from trackers.orpheus import Orpheus
from trackers.privatehd import PrivateHD
from trackers.reelflix import ReelFliX
from trackers.torrentleech import TorrentLeech
from trackers.torrentseeds import TorrentSeeds
from trackers.uhdbits import UHDBits

load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(24)

TRACKERS = {
    'aither': Aither,
    'alpharatio': AlphaRatio,
    'animez': AnimeZ,
    'anthelion': Anthelion,
    'avistaz': AvistaZ,
    'blutopia': Blutopia,
    'cathoderaytube': CathodeRayTube,
    'cinemaz': CinemaZ,
    'filelist': FileList,
    'iptorrents': IPTorrents,
    'myanonamouse': MyAnonamouse,
    'nebulance': Nebulance,
    'oldtoonsworld': OldToonsWorld,
    'orpheus': Orpheus,
    'privatehd': PrivateHD,
    'reelflix': ReelFliX,
    'torrentleech': TorrentLeech,
    'torrentseeds': TorrentSeeds,
    'uhdbits': UHDBits
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
    
    cookiefiles = {}
    for file in os.listdir('./cookies'):
        if file.endswith('.txt') and file != 'useragent.txt':
            name = file.split('.')[0]
        
            exps = parseCookieFileExp('./cookies/' + file)
            cookies = []
            for exp in exps:
                exp_delta = datetime.fromtimestamp(int(exps[exp])) - datetime.now()
                if datetime.fromtimestamp(int(exps[exp])) < datetime.now():
                    cookies.append({'name': exp, 'exp': 'expired'})
                else:
                    cookies.append({'name': exp, 'exp': humanize.precisedelta(exp_delta, minimum_unit='minutes')})
            
            cookiefiles[name] = cookies

    return render_template('upload.html', trackers=TRACKERS, cookiefiles=cookiefiles, user_agent=request.headers.get('User-Agent'), user_agent_file=getUserAgent())

@app.route('/<tracker>')
def tracker(tracker):
    if tracker in TRACKERS:
        tracker_class = TRACKERS[tracker]()
        if os.path.isfile('./cookies/' + tracker + '.txt'):
            try:
                tracker_class.get_stats(parseCookieFile('./cookies/' + tracker + '.txt'), {'User-Agent': getUserAgent()})
                return Response(json.dumps(tracker_class.__dict__), mimetype='application/json')
            except Exception as e:
                return Response(json.dumps({'error': str(e)}), mimetype='application/json')
        else:
            return Response(json.dumps({'error': 'No cookie file found for ' + tracker}), mimetype='application/json')
    else:
        return Response(json.dumps({'error': 'Invalid tracker'}), mimetype='application/json')

if __name__ == '__main__':
    serve(app, listen='*:5000')