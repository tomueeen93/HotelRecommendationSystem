#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ryoma Suzuki"
__mail__="ryouma.suzuki.5c@stu.hosei.ac.jp"

from os import path
import sys
import sqlite3

# このプログラムの場所を取得
APP_ROOT = path.dirname( path.abspath( __file__ ) )

# 立地辞書に含まれている単語が、pairsの中に含まれていた場合に合計スコアに加算するテスト
def main():
    # 立地辞書の生成
    f1 = open(APP_ROOT+'/../data/EmotionalPolarityList.txt')
    line = f1.readline() # 1行を文字列として読み込む(改行文字も含まれる)

    location_dictionary = line.split(',')
    print_array = map(str,location_dictionary)
    f1.close
    print(",".join(print_array))

    score = 0.0

    f2 = open(APP_ROOT+'/../data/test3.txt')
    line=f2.readline()
    while line:
        print line
        line.split(',')
        line = f2.readline()
    f2.close

def insertData(hotel_name):
    print ("insert : "+hotel_name)

    # hotelRecDBをオートコミットモードで開く
    con = sqlite3.connect(APP_ROOT+'/../db/hotelRecDB',isolation_level=None)

    sql = u"insert into hotels(hotel_name) values('"+hotel_name+"')"

    print("SQL : "+sql)

    con.execute(sql)
    con.close()
    print ("INSERT Successed!!")

def viewTableData(table_name):
    print ("view table : "+table_name)

    # hotelRecDBをオートコミットモードで開く
    con = sqlite3.connect(APP_ROOT+'/../db/hotelRecDB',isolation_level=None)

    # SQL文の生成
    sql = u"select * from "+table_name

    # SQL文を実行し、cursorに保存
    cursor = con.execute(sql)

    # 結果を1行ずつ取り出して表示
    for row in cursor:
        print (row[0])
        print (row[1])

    # 接続を切る
    con.close()
    # 終了メッセージ
    print ("VIEW Successed!!")


if __name__=='__main__':
    if (len(sys.argv) > 1):
        viewTableData(sys.argv[1])
    else:
        print ("Please set single argment")
        main()
