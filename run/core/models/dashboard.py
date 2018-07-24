#!/usr/bin/env python3
import datetime

from core.mappers.Connections import Select, Insert

def user_info(username):
    info = Select().select_user_info(username)
    return {
        'first': info[0][0],
        'posts': info[0][1],
        'reposts': info[0][2],
        'followers': info[0][3],
        'following': info[0][4]
    }

def all_tweets():
    items = Select().select_all_posts()
    x = []
    for i in reversed(items):
        tweet = {
            'username': i[0],
            'date'    : i[1],
            'tweet'   : i[2],
            'reposts' : i[3],
            'id'      : i[4],
            'repost'  : repost_counter(i[4])
        }
        x.append(tweet)
    return x

def user_tweets(username):
    items = Select().select_all_user_posts(username)
    x = []
    for i in reversed(items):
        tweet = {
            'username': i[0],
            'date'    : i[1],
            'tweet'   : i[2],
            'reposts' : i[3],
            'id'      : i[4],
            'repost'  : repost_counter(i[4])
        }
        x.append(tweet)
    return x


def record_tweet(username,tweet,reposts):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Insert().insert_tweet(username,date,tweet,reposts)
    count = Select().select_post_user(username)
    Insert().insert_post_user(username,count)


def record_repost(username,post_ID):
    check = Select().select_repost(username,post_ID)
    if check == None:
        Insert().insert_repost(username,post_ID)
        count = Select().select_repost_user(username)
        Insert().insert_repost_user(username,count)
    else:
        pass

def repost_counter(post_ID):
    count = Select().select_repost_counter(post_ID)
    return count
