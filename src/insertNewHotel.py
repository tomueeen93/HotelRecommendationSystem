#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ryoma Suzuki"
__mail__="ryouma.suzuki.5c@stu.hosei.ac.jp"

from os import path
import sys
import sqlite3

# このプログラムの場所を取得
APP_ROOT = path.dirname( path.abspath( __file__ ) )

def main(hotel_name):
    print("\tStart main")
    con = sqlite3.connect(APP_ROOT+'/../db/hotelRecDB',isolation_level=None)

    sql1 = u"INSERT INTO hotels(hotel_name) values('"+hotel_name+"');"
    con.execute(sql1)

    sql2 = u"SELECT hotel_id FROM hotels WHERE hotel_name=='"+hotel_name+"';"
    cursor = con.execute(sql2)

    row = cursor.fetchone();
    if(row != None):
        sql3 = u"INSERT INTO hotel_scores(hotel_id) VALUES("+str(row[0])+");"
        con.execute(sql3)

    con.close()
    print("\tFinish!!")

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        main(sys.argv[1])
    else:
        print ("\tError! Please set single argment")
