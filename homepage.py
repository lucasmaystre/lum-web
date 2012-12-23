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


@app.route('/lama')
def lama():
    """Grooveshark widget with music discovered through LAMA project."""
    return render_template('lama.html')


@app.route('/arb')
def ref_assignments():
    return redirect('http://www.football.ch/fr/SFV/SFV-Service/Schiedsrichter/'
                    'Recherche-darbitres.aspx/v-1191/sr-588481/')


if __name__ == '__main__':
    app.run()
