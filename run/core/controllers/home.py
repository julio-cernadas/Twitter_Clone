#!/usr/bin/env python3

from flask import Blueprint, render_template, request, session, redirect, url_for
from core.models.dashboard import user_info, all_tweets, record_tweet

controller = Blueprint('home',__name__,url_prefix='/home')

def info(username):
	if request.method == 'GET':
		if 'username' in session:
			username    = session['username']
			information = user_info(username)
			items = all_tweets()
			return render_template('home.html',username = username,
									information=information,items=items)

	elif request.method == 'POST':
		if 'username' in session:
			username = session['username']			
			tweet    = request.form['tweet']
			record_tweet(username,tweet,0)
			if tweet != None:
				return redirect(url_for('home.dashboard'))

@controller.route('/',methods=['GET','POST'])
def dashboard():
	return info(session['username'])
