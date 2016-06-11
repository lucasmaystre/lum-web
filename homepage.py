#!/usr/bin/env python
import json
import requests

from flask import Flask, render_template, redirect, request


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/projects')
def projects():
    return render_template('projects.html', home_link=True)


@app.route('/vim')
def vim():
    return render_template('vim.html', home_link=True)


@app.route('/arb')
def ref_assignments():
    return redirect('https://www.clubcorner.ch/')


@app.route('/nips15')
def nips15():
    return render_template('nips15.html', home_link=True)

@app.route('/kickoffai', methods=['GET', 'POST'])
def kickoff_ai():
    url = "https://nqwxwb9jr2.execute-api.eu-central-1.amazonaws.com/beta/game"
    res=None
    if request.form.get('submitted'):
        payload = {
            'gameId': int(request.form['gameId']),
            'scoreHome': int(request.form['scoreHome']),
            'scoreAway': int(request.form['scoreAway']),
        }
        headers = {'x-api-key': request.form['apiKey']}
        res = requests.post(url, headers=headers, data=json.dumps(payload))
    return render_template('kickoffai.html', res=res)


if __name__ == '__main__':
    app.run()
