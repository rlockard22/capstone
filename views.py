from flask import Blueprint, render_template
import sqlite3
from sqlite3 import Error
import visitor

from matplotlib import image

db_connection = sqlite3.connect('master.db', check_same_thread=False)
db_cursor = db_connection.cursor()

views = Blueprint(__name__, "views")
@views.before_request
def track_visitor():
    visitor.track_visitor()

@views.route("/")
def home():
    return render_template("eskenazi.html")

@views.route("/<page_name>")
def pages(page_name):
    artwork_name = page_name
    sql = "SELECT * FROM eskenazi WHERE name = ?"
    db_cursor.execute(sql, (artwork_name,))
    df = db_cursor.fetchone()
    artwork_name = df[2]
    artist_name = df[3]
    artwork_date = df[4]
    uri = df[6]
    print(uri[:1000])
    artwork_description = df[5]
    artwork_description = artwork_description.replace('\\','')
                                                      
    return render_template("the_studio.html", audio_filename="the_studio_audio.mp3", image_filename="the-studio.jpg", artwork_name=artwork_name, artist_name=artist_name, date=artwork_date, description=artwork_description)
    

@views.route("/the_studio")
def the_studio():
    artwork_name = 'The Studio'
    sql = "SELECT * FROM eskenazi WHERE name = ?"
    db_cursor.execute(sql, (artwork_name,))
    df = db_cursor.fetchone()
    artwork_name = df[2]
    artist_name = df[3]
    artwork_date = df[4]
    uri = df[6]
    print(uri[:1000])
    artwork_description = df[5]
    artwork_description = artwork_description.replace('\\','')
                                                      
    return render_template("the_studio.html", audio_filename="the_studio_audio.mp3", image_filename="the-studio.jpg", artwork_name=artwork_name, artist_name=artist_name, date=artwork_date, description=artwork_description)

@views.route("/portrait_of_lisa_bigelow")
def portrait_of_lisa_bigelow():
    artwork_name = 'Portrait of Lisa Bigelow'
    sql = "SELECT * FROM eskenazi WHERE name = ?"
    db_cursor.execute(sql, (artwork_name,))
    df = db_cursor.fetchone()
    artwork_name = df[2]
    artist_name = df[3]
    artwork_date = df[4]
    artwork_description = df[5]
                                                      
    return render_template("the_studio.html", audio_filename="portrait_lisa.mp3", image_filename="portrait_lisa.jpg", artwork_name=artwork_name, artist_name=artist_name, date=artwork_date, description=artwork_description)

@views.route("/madonna_and_child_with_apple_and_pear")
def madonna_and_child_with_apple_and_pear():
    artwork_name = 'Madonna and Child with Apple and Pears'
    sql = "SELECT * FROM eskenazi WHERE name = ?"
    db_cursor.execute(sql, (artwork_name,))
    df = db_cursor.fetchone()
    artwork_name = df[2]
    artist_name = df[3]
    artwork_date = df[4]
    artwork_description = df[5]
                                                      
    return render_template("the_studio.html", audio_filename="madonna_child_apple_pear.mp3", image_filename="madonna_child_apple_pears.jpg", artwork_name=artwork_name, artist_name=artist_name, date=artwork_date, description=artwork_description)

@views.route("/laborers_harvesting_bath_stone")
def laborers_harvesting_bath_stone():
    artwork_name = 'Laborers Harvesting Bath Stone'
    sql = "SELECT * FROM eskenazi WHERE name = ?"
    db_cursor.execute(sql, (artwork_name,))
    df = db_cursor.fetchone()
    artwork_name = df[2]
    artist_name = df[3]
    artwork_date = df[4]
    artwork_description = df[5]
                                                      
    return render_template("the_studio.html", audio_filename="laborers_harvesting_bath_stone.mp3", image_filename="laborers_harvesting_bath_stone.jpg", artwork_name=artwork_name, artist_name=artist_name, date=artwork_date, description=artwork_description)

@views.route("/saint_eustace")
def saint_eustace():
    artwork_name = 'Saint Eustace'
    sql = "SELECT * FROM eskenazi WHERE name = ?"
    db_cursor.execute(sql, (artwork_name,))
    df = db_cursor.fetchone()
    artwork_name = df[2]
    artist_name = df[3]
    artwork_date = df[4]
    artwork_description = df[5]
                                                      
    return render_template("the_studio.html", audio_filename="saint_eustace.mp3", image_filename="saint_eustace.jpg", artwork_name=artwork_name, artist_name=artist_name, date=artwork_date, description=artwork_description)

@views.route("/holy_family_w_saint_john")
def holy_family_w_saint_john():
    artwork_name = 'Holy Family with Infant St. John'
    sql = "SELECT * FROM eskenazi WHERE name = ?"
    db_cursor.execute(sql, (artwork_name,))
    df = db_cursor.fetchone()
    artwork_name = df[2]
    artist_name = df[3]
    artwork_date = df[4]
    artwork_description = df[5]
                                                      
    return render_template("the_studio.html", audio_filename="holy_family_w_saint_john.mp3", image_filename="holy_family_w_saint_john.jpg", artwork_name=artwork_name, artist_name=artist_name, date=artwork_date, description=artwork_description)

@views.route("/judith_head_of_holofernes")
def judith_head_of_holofernes():
    artwork_name = 'Judith with the Head of Holofernes'
    sql = "SELECT * FROM eskenazi WHERE name = ?"
    db_cursor.execute(sql, (artwork_name,))
    df = db_cursor.fetchone()
    artwork_name = df[2]
    artist_name = df[3]
    artwork_date = df[4]
    artwork_description = df[5]
                                                      
    return render_template("the_studio.html", audio_filename="judith.mp3", image_filename="judith.jpg", artwork_name=artwork_name, artist_name=artist_name, date=artwork_date, description=artwork_description)

@views.route("/the_annunciation")
def the_annunciation():
    artwork_name = 'The Annunciation'
    sql = "SELECT * FROM eskenazi WHERE name = ?"
    db_cursor.execute(sql, (artwork_name,))
    df = db_cursor.fetchone()
    artwork_name = df[2]
    artist_name = df[3]
    artwork_date = df[4]
    artwork_description = df[5]
                                                      
    return render_template("the_studio.html", audio_filename="the_annunciation.mp3", image_filename="the_annunciation.jpg", artwork_name=artwork_name, artist_name=artist_name, date=artwork_date, description=artwork_description)

@views.route("/the_nativity")
def the_nativity():
    artwork_name = 'The Nativity'
    sql = "SELECT * FROM eskenazi WHERE name = ?"
    db_cursor.execute(sql, (artwork_name,))
    df = db_cursor.fetchone()
    artwork_name = df[2]
    artist_name = df[3]
    artwork_date = df[4]
    artwork_description = df[5]
                                                      
    return render_template("the_studio.html", audio_filename="the_annunciation.mp3", image_filename="the_nativity.jpg", artwork_name=artwork_name, artist_name=artist_name, date=artwork_date, description=artwork_description)

@views.route("/the_birth_of_the_virgin")
def the_birth_of_the_virgin():
    artwork_name = 'The Birth of the Virgin'
    sql = "SELECT * FROM eskenazi WHERE name = ?"
    db_cursor.execute(sql, (artwork_name,))
    df = db_cursor.fetchone()
    artwork_name = df[2]
    artist_name = df[3]
    artwork_date = df[4]
    artwork_description = df[5]
                                                      
    return render_template("the_studio.html", audio_filename="the_annunciation.mp3", image_filename="the_birth_of_the_virgin.jpg", artwork_name=artwork_name, artist_name=artist_name, date=artwork_date, description=artwork_description)



@views.route("/team")
def team():
    return render_template("team.html")
