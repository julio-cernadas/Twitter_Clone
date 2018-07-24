#!/usr/bin/env python3

from flask import Blueprint, render_template, request, session, redirect, url_for
from core.models.dashboard import record_repost

controller = Blueprint('repost',__name__,url_prefix='/repost')

@controller.route('/',methods=['GET','POST'])
def dashboard():
    if request.method == 'GET':
        if 'username' in session:
            user    = request.args.get('usr')
            post_ID = request.args.get('id')
            record_repost(user,post_ID)
            return redirect(url_for('home.dashboard'))