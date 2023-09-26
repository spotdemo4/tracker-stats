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

FILENAMES = ['aither.txt', 'alpharatio.txt', 'animez.txt', 'anthelion.txt', 'avistaz.txt', 'cinemaz.txt', 'filelist.txt', 'iptorrents.txt', 'myanonamouse.txt', 'orpheus.txt', 'torrentleech.txt']

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
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and file.filename in FILENAMES:
            file.save('./cookies/' + file.filename)
            flash('File uploaded successfully')
            return redirect(request.url)
        else:
            flash('Invalid file')
            return redirect(request.url)
    return render_template('upload.html', filenames=FILENAMES, user_agent=request.headers.get('User-Agent'), user_agent_file=getUserAgent())

@app.route('/aither')
def aither():
    if os.path.isfile('./cookies/aither.txt'):
        aither = Aither()
        try:
            aither.get_stats(parseCookieFile('./cookies/aither.txt'), {'User-Agent': getUserAgent()})
            return json.dumps(aither.__dict__)
        except Exception as e:
            return json.dumps({'error': str(e)})
    else:
        return json.dumps({'error': 'No cookie file found for Aither'})

@app.route('/alpharatio')
def alpharatio():
    if os.path.isfile('./cookies/alpharatio.txt'):
        alpharatio = AlphaRatio()
        try:
            alpharatio.get_stats(parseCookieFile('./cookies/alpharatio.txt'), {'User-Agent': getUserAgent()})
            return json.dumps(alpharatio.__dict__)
        except Exception as e:
            return json.dumps({'error': str(e)})
    else:
        return json.dumps({'error': 'No cookie file found for AlphaRatio'})

@app.route('/animez')
def animez():
    if os.path.isfile('./cookies/animez.txt'):
        animez = AnimeZ()
        try:
            animez.get_stats(parseCookieFile('./cookies/animez.txt'), {'User-Agent': getUserAgent()})
            return json.dumps(animez.__dict__)
        except Exception as e:
            return json.dumps({'error': str(e)})
    else:
        return json.dumps({'error': 'No cookie file found for AnimeZ'})

@app.route('/anthelion')
def anthelion():
    if os.path.isfile('./cookies/anthelion.txt'):
        anthelion = Anthelion()
        try:
            anthelion.get_stats(parseCookieFile('./cookies/anthelion.txt'), {'User-Agent': getUserAgent()})
            return json.dumps(anthelion.__dict__)
        except Exception as e:
            return json.dumps({'error': str(e)})
    else:
        return json.dumps({'error': 'No cookie file found for Anthelion'})

@app.route('/avistaz')
def avistaz():
    if os.path.isfile('./cookies/avistaz.txt'):
        avistaz = AvistaZ()
        try:
            avistaz.get_stats(parseCookieFile('./cookies/avistaz.txt'), {'User-Agent': getUserAgent()})
            return json.dumps(avistaz.__dict__)
        except Exception as e:
            return json.dumps({'error': str(e)})
    else:
        return json.dumps({'error': 'No cookie file found for AvistaZ'})

@app.route('/cinemaz')
def cinemaz():
    if os.path.isfile('./cookies/cinemaz.txt'):
        cinemaz = CinemaZ()
        try:
            cinemaz.get_stats(parseCookieFile('./cookies/cinemaz.txt'), {'User-Agent': getUserAgent()})
            return json.dumps(cinemaz.__dict__)
        except Exception as e:
            return json.dumps({'error': str(e)})
    else:
        return json.dumps({'error': 'No cookie file found for CinemaZ'})

@app.route('/filelist')
def filelist():
    if os.path.isfile('./cookies/filelist.txt'):
        filelist = FileList()
        try:
            filelist.get_stats(parseCookieFile('./cookies/filelist.txt'), {'User-Agent': getUserAgent()})
            return json.dumps(filelist.__dict__)
        except Exception as e:
            return json.dumps({'error': str(e)})
    else:
        return json.dumps({'error': 'No cookie file found for FileList'})

@app.route('/myanonamouse')
def myanonamouse():
    if os.path.isfile('./cookies/myanonamouse.txt'):
        myanonamouse = MyAnonamouse()
        try:
            myanonamouse.get_stats(parseCookieFile('./cookies/myanonamouse.txt'), {'User-Agent': getUserAgent()})
            return json.dumps(myanonamouse.__dict__)
        except Exception as e:
            return json.dumps({'error': str(e)})
    else:
        return json.dumps({'error': 'No cookie file found for MyAnonamouse'})

@app.route('/iptorrents')
def iptorrents():
    if os.path.isfile('./cookies/iptorrents.txt'):
        iptorrents = IPTorrents()
        try:
            iptorrents.get_stats(parseCookieFile('./cookies/iptorrents.txt'), {'User-Agent': getUserAgent()})
            return json.dumps(iptorrents.__dict__)
        except Exception as e:
            return json.dumps({'error': str(e)})
    else:
        return json.dumps({'error': 'No cookie file found for IPTorrents'})

@app.route('/orpheus')
def orpheus():
    if os.path.isfile('./cookies/orpheus.txt'):
        orpheus = Orpheus()
        try:
            orpheus.get_stats(parseCookieFile('./cookies/orpheus.txt'), {'User-Agent': getUserAgent()})
            return json.dumps(orpheus.__dict__)
        except Exception as e:
            return json.dumps({'error': str(e)})
    else:
        return json.dumps({'error': 'No cookie file found for Orpheus'})

@app.route('/torrentleech')
def torrentleech():
    if os.path.isfile('./cookies/torrentleech.txt'):
        torrentleech = TorrentLeech()
        try:
            torrentleech.get_stats(parseCookieFile('./cookies/torrentleech.txt'), {'User-Agent': getUserAgent()})
            return json.dumps(torrentleech.__dict__)
        except Exception as e:
            return json.dumps({'error': str(e)})
    else:
        return json.dumps({'error': 'No cookie file found for TorrentLeech'})

if __name__ == '__main__':
    serve(app, listen='*:5000')