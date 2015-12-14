#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ryoma Suzuki"
__mail__="ryouma.suzuki.5c@stu.hosei.ac.jp"

from os import path
import sys
import sqlite3

# このプログラムの場所を取得
APP_ROOT = path.dirname( path.abspath( __file__ ) )

def main(hotel_name,pair_array):
    print("\tStart main")

    # DB接続
    con1 = sqlite3.connect(APP_ROOT+'/../db/hotelRecDB',isolation_level=None)
    con2 = sqlite3.connect(APP_ROOT+'/../db/emotionPolarityDB',isolation_level=None)

    # IDの取得
    sql3 = u"SELECT hotel_id FROM hotels WHERE hotel_name=='"+hotel_name+"';"
    cursor3 = con1.execute(sql3)
    val = cursor3.fetchone()
    if(val == None):
        print("\tNot exist : "+hotel_name)
        sys.exit()
    hotel_id = val[0]
    print("\tHOTEL ID : "+str(hotel_id))

    # データを取得
    f = open(APP_ROOT+'/../data/test3.txt')
    line = f.readline()

    # スコアをつける
    total_score = 0.0
    for pair in pair_array:
        str1 = pair[0]
        sql1 = u"SELECT * FROM location_dics WHERE word=='"+str1+"';"
        cursor = con1.execute(sql1)

        # 1つ目のデータが立地辞書にある場合
        val = cursor.fetchone()
        if (val != None):
            str2 = pair[1]
            sql2=u"SELECT * FROM words WHERE word=='"+str2+"';"
            cursor2 = con2.execute(sql2)

            # 2つ目のデータが感情極性表にある場合
            row = cursor2.fetchone()
            if (row != None):
                # 合計スコアに加算する
                total_score += row[4]

        line = f.readline()

    f.close()
    print("\tEvaluated score : "+str(total_score))

    sql3= u"UPDATE hotel_scores SET location_score="+str(total_score)+" WHERE hotel_id=="+str(hotel_id)+";"
    con1.execute(sql3)

    # DBを更新
    print("\tUpdate Score")

    # DB接続を解除
    con1.close()
    print("\tFinish!!")

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        main(sys.argv[1])
    else:
        print ("Please set single argment")
