from ipaddress import ip_address
import sqlite3
from flask import request
import sys


def track_visitor():
    try:
        
        print("hello", file=sys.stderr)
        print(request.url, file=sys.stderr)
        print(request.url_root, file=sys.stderr)
        ip_address = request.remote_addr
        requested_url = request.url
        user_agent = request.user_agent.string
        if requested_url == request.url_root:
            return
            
        db_connection = sqlite3.connect('master.db', check_same_thread=False)
        db_cursor = db_connection.cursor()
        sql = "INSERT into user_info (ip_address, requested_url, user_agent) VALUES (?,?,?)"
        db_cursor.execute(sql, (ip_address, requested_url, user_agent))
        db_connection.commit()
        #db_connection.close()
        if "the_studio" in requested_url:
            db_connection = sqlite3.connect('master.db', check_same_thread=False)
            db_cursor = db_connection.cursor()
            artwork_name = "The Studio"
            sql = "SELECT * FROM page_views WHERE page_name = ?"
            db_cursor.execute(sql, (artwork_name,))
            df = db_cursor.fetchone()
            print(df[2], file=sys.stderr)
            no_page_views = df[2]
            no_page_views = no_page_views + 1
            sql = "UPDATE page_views SET number_of_views = ? WHERE page_name = ?"
            db_cursor.execute(sql, (no_page_views, artwork_name))
            db_connection.commit()
            db_connection.close()
            
        elif "portrait_of_lisa_bigelow" in requested_url:
            db_connection = sqlite3.connect('master.db', check_same_thread=False)
            db_cursor = db_connection.cursor()
            artwork_name = "Portrait of Lisa Bigelow"
            sql = "SELECT * FROM page_views WHERE page_name = ?"
            db_cursor.execute(sql, (artwork_name,))
            df = db_cursor.fetchone()
            print(df[2], file=sys.stderr)
            no_page_views = df[2]
            no_page_views = no_page_views + 1
            sql = "UPDATE page_views SET number_of_views = ? WHERE page_name = ?"
            db_cursor.execute(sql, (no_page_views, artwork_name))
            db_connection.commit()
            db_connection.close()
            
        elif "madonna_and_child_with_apple_and_pear" in requested_url:
            db_connection = sqlite3.connect('master.db', check_same_thread=False)
            db_cursor = db_connection.cursor()
            artwork_name = "Madonna and Child with Apple and Pears"
            sql = "SELECT * FROM page_views WHERE page_name = ?"
            db_cursor.execute(sql, (artwork_name,))
            df = db_cursor.fetchone()
            print(df[2], file=sys.stderr)
            no_page_views = df[2]
            no_page_views = no_page_views + 1
            sql = "UPDATE page_views SET number_of_views = ? WHERE page_name = ?"
            db_cursor.execute(sql, (no_page_views, artwork_name))
            db_connection.commit()
            db_connection.close()
            
        elif "laborers_harvesting_bath_stone" in requested_url:
            db_connection = sqlite3.connect('master.db', check_same_thread=False)
            db_cursor = db_connection.cursor()
            artwork_name = "Laborers Harvesting Bath Stone"
            sql = "SELECT * FROM page_views WHERE page_name = ?"
            db_cursor.execute(sql, (artwork_name,))
            df = db_cursor.fetchone()
            print(df[2], file=sys.stderr)
            no_page_views = df[2]
            no_page_views = no_page_views + 1
            sql = "UPDATE page_views SET number_of_views = ? WHERE page_name = ?"
            db_cursor.execute(sql, (no_page_views, artwork_name))
            db_connection.commit()
            db_connection.close()
            
        elif "saint_eustace" in requested_url:
            db_connection = sqlite3.connect('master.db', check_same_thread=False)
            db_cursor = db_connection.cursor()
            artwork_name = "Saint Eustace"
            sql = "SELECT * FROM page_views WHERE page_name = ?"
            db_cursor.execute(sql, (artwork_name,))
            df = db_cursor.fetchone()
            print(df[2], file=sys.stderr)
            no_page_views = df[2]
            no_page_views = no_page_views + 1
            sql = "UPDATE page_views SET number_of_views = ? WHERE page_name = ?"
            db_cursor.execute(sql, (no_page_views, artwork_name))
            db_connection.commit()
            db_connection.close()
            
        elif "holy_family_w_saint_john" in requested_url:
            db_connection = sqlite3.connect('master.db', check_same_thread=False)
            db_cursor = db_connection.cursor()
            artwork_name = "Holy Family with Infant St. John"
            sql = "SELECT * FROM page_views WHERE page_name = ?"
            db_cursor.execute(sql, (artwork_name,))
            df = db_cursor.fetchone()
            print(df[2], file=sys.stderr)
            no_page_views = df[2]
            no_page_views = no_page_views + 1
            sql = "UPDATE page_views SET number_of_views = ? WHERE page_name = ?"
            db_cursor.execute(sql, (no_page_views, artwork_name))
            db_connection.commit()
            db_connection.close()
            
        elif "judith_head_of_holofernes" in requested_url:
            db_connection = sqlite3.connect('master.db', check_same_thread=False)
            db_cursor = db_connection.cursor()
            artwork_name = "Judith with the Head of Holofernes"
            sql = "SELECT * FROM page_views WHERE page_name = ?"
            db_cursor.execute(sql, (artwork_name,))
            df = db_cursor.fetchone()
            print(df[2], file=sys.stderr)
            no_page_views = df[2]
            no_page_views = no_page_views + 1
            sql = "UPDATE page_views SET number_of_views = ? WHERE page_name = ?"
            db_cursor.execute(sql, (no_page_views, artwork_name))
            db_connection.commit()
            db_connection.close()
            
        elif "the_annunciation" in requested_url:
            db_connection = sqlite3.connect('master.db', check_same_thread=False)
            db_cursor = db_connection.cursor()
            artwork_name = "The Annunciation"
            sql = "SELECT * FROM page_views WHERE page_name = ?"
            db_cursor.execute(sql, (artwork_name,))
            df = db_cursor.fetchone()
            print(df[2], file=sys.stderr)
            no_page_views = df[2]
            no_page_views = no_page_views + 1
            sql = "UPDATE page_views SET number_of_views = ? WHERE page_name = ?"
            db_cursor.execute(sql, (no_page_views, artwork_name))
            db_connection.commit()
            db_connection.close()
            
        elif "the_nativity" in requested_url:
            db_connection = sqlite3.connect('master.db', check_same_thread=False)
            db_cursor = db_connection.cursor()
            artwork_name = "The Nativity"
            sql = "SELECT * FROM page_views WHERE page_name = ?"
            db_cursor.execute(sql, (artwork_name,))
            df = db_cursor.fetchone()
            print(df[2], file=sys.stderr)
            no_page_views = df[2]
            no_page_views = no_page_views + 1
            sql = "UPDATE page_views SET number_of_views = ? WHERE page_name = ?"
            db_cursor.execute(sql, (no_page_views, artwork_name))
            db_connection.commit()
            db_connection.close()
            
        elif "the_birth_of_the_virgin" in requested_url:
            db_connection = sqlite3.connect('master.db', check_same_thread=False)
            db_cursor = db_connection.cursor()
            artwork_name = "The Birth of the Virgin"
            sql = "SELECT * FROM page_views WHERE page_name = ?"
            db_cursor.execute(sql, (artwork_name,))
            df = db_cursor.fetchone()
            print(df[2], file=sys.stderr)
            no_page_views = df[2]
            no_page_views = no_page_views + 1
            sql = "UPDATE page_views SET number_of_views = ? WHERE page_name = ?"
            db_cursor.execute(sql, (no_page_views, artwork_name))
            db_connection.commit()
            db_connection.close()
            
        else:
            db_connection.close()
            return
           
    except:
        return
    
    