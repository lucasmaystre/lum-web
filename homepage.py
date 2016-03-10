#!/usr/bin/env python
from flask import Flask, render_template, redirect


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


if __name__ == '__main__':
    app.run()
