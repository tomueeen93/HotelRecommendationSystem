#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ryoma Suzuki"
__mail__="ryouma.suzuki.5c@stu.hosei.ac.jp"

from os import path
import sys
import sqlite3

# このプログラムの場所を取得
APP_ROOT = path.dirname( path.abspath( __file__ ) )

def main():
    print("\tStarted main")
    con = sqlite3.connect(APP_ROOT+'/../db/hotelRecDB',isolation_level=None)

    # tableの削除
    sql1 = u"drop table if exists location_dics;"
    con.execute(sql1)
    print("\tDeleted exist table")

    # tableの作成
    sql2 = u"create table if not exists location_dics(location_dic_id integer primary key,word text);"
    con.execute(sql2)
    print("\tCreated table")

    # データの取得
    f1 = open(APP_ROOT+'/../data/location_dictionary.txt')
    line = f1.readline()
    rows = line.split(',')
    f1.close()
    print("\tLoaded File")

    # データの挿入
    count = 0
    total = len(rows)
    # m2 = str(total).decode('utf-8') # python 2.x
    m2 = str(total) # python 3.x
    for row in rows:
        count = count+1
        # val = row.decode("utf-8") # python 2.x
        val = row # python 3.x
        sql3 = u"insert into location_dics(word)  values('"+val+"');"
        con.execute(sql3)

        # 出力設定
        # m1 = str(count).decode('utf-8') # 2.x
        m1 = str(count) # python 3.x
        message = "\tNow inserting........."+m1+"/"+m2
        print message, "\r", # python 2.x
        # print(message, "\r", end="") # python 3.x
        sys.stdout.flush()

    con.close()
    print("")
    print("\tFinish!!")

if __name__ == '__main__':
    main()
