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
    print("\tStart main")

    con = sqlite3.connect(APP_ROOT+'/../db/emotionPolarityDB',isolation_level=None)

    # tableの削除
    sql1 = u"drop table if exists words;"
    con.execute(sql1)
    print("\tDelete existed table")

    # tableの作成
    sql2 = u"create table if not exists words(word_id integer primary key,word text,hiragana text,type text,value real);"
    con.execute(sql2)
    print("\tCreated table")

    # データの取得
    f1 = open(APP_ROOT+'/../data/EmotionalPolarityList.txt')
    line = f1.readline()
    rows = line.split(' ')
    f1.close()
    print("\tLoaded file")

    # データの挿入
    count = 0
    total = len(rows)
    # m2 = str(total).decode('utf-8') # python2.x
    m2 = str(total) # python3.x

    for row in rows:
        count= count+1

        # print("insert : "+row) # 表示用
        cols = row.split(":")
        if(len(cols)<4):print ("----------Error!!------------")

        # python2.x
        # val0 = cols[0].decode('utf-8')
        # val1 = cols[1].decode('utf-8')
        # val2 = cols[2].decode('utf-8')
        # val3 = cols[3].decode('utf-8')
        # python3.x
        val0 = cols[0]
        val1 = cols[1]
        val2 = cols[2]
        val3 = cols[3]

        sql3 = u"insert into words(word,hiragana,type,value)  values('"+val0+"','"+val1+"','"+val2+"', "+val3+");"
        con.execute(sql3)

        # 出力設定
        # m1 = str(count).decode('utf-8') # python 2.x
        m1 = str(count) # python 3.x

        message = "\tNow inserting........."+m1+"/"+m2
        # print message, "\r", # python 2.x
        print(message, "\r", end="") # python 3.x
        sys.stdout.flush()

    con.close()

    print("")
    print("\tFinish!!")

if __name__=='__main__':
    main()
