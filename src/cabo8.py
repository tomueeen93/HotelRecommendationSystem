#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author 鈴木
# 立地に関連する辞書を最初に表示
# 次に係り受け解析のペアを表示 形式：[係元],[係先],[信頼度]
# 最後に立地辞書と単語のマッチを調べる出力

from os import path
import CaboCha # debug時はコメントアウト
from xml.etree.ElementTree import *

# このプログラムの絶対パスを取得
APP_ROOT = path.dirname( path.abspath( __file__ ) )

def cabo(sentence):
    c = CaboCha.Parser("")
    tree =  c.parse(sentence)

    xmlString = tree.toString(CaboCha.FORMAT_XML)
    return xmlString
    elem = fromstring(xmlString)

# 単語を取得する
def get_word(tree, chunk):
    surface = ''
    for i in range(chunk.token_pos, chunk.token_pos + chunk.token_size):
        token = tree.token(i)
        features = token.feature.split(',')
        if features[0] == '名詞':
            surface += token.surface
        elif features[0] == '形容詞':
            surface += features[6]
            break
        elif features[0] == '動詞':
            surface += features[6]
            break
    return surface

# 単語を取得する
def get_2_words(line):
    cp = CaboCha.Parser('-f1')
    tree = cp.parse(line)
    chunk_dic = {}
    chunk_id = 0
    for i in range(0, tree.size()):
        token = tree.token(i)
        if token.chunk:
            chunk_dic[chunk_id] = token.chunk
            chunk_id += 1

    tuples = []
    for chunk_id, chunk in chunk_dic.items():
        if chunk.link > 0:
            from_surface =  get_word(tree, chunk)
            to_chunk = chunk_dic[chunk.link]
            to_surface = get_word(tree, to_chunk)
            tuples.append((from_surface, to_surface))
    return tuples

# main (ここからスタート)
def start(check_word):
    print(APP_ROOT)
    # ファイルを取得
    f1 = open(APP_ROOT+'/../data/location_dictionary.txt')
    locate_dic = f1.read()
    #f.close()
    # 立地辞書の生成
    location_dic = []
    location_dic = locate_dic.split(',')
    print('立地辞書:')
    print (location_dic)
    print("----------------------------------------")


    pair = []
    reliability = 0.0;# どれくらい信頼性を担保するのか設定する
    # 係先ペアと点数の保存
    for i in range(1,3):
        # testデータを読み込み
        f2 = open(APP_ROOT+'/../data/test%s.txt'%(i),'r')
        hoteldata1 = f2.readline()
        while hoteldata1:
            xmlString = cabo(hoteldata1)
            elem = fromstring(xmlString)

            values = [] #係り値1.3
            for chunk in elem.findall(".//chunk"):
                values.append(chunk.get("score"))

                kakariset = [] #料理-->美味しい
                tuples = get_2_words(hoteldata1)
            for t in tuples:
                kakariset.append([t[0],t[1]]) #pair = []#kakarisetとvaluesを一組

            for i in range(len(kakariset)) :
                # 係値をxに保存
                x=(float(values[i]))
                if ( x > reliability):
                    pair.append([kakariset[i][0],kakariset[i][1],values[i]])

            hoteldata1 = f2.readline()

    # 係先のデータを表示
    # 信頼度が＋のものだけを保存している
    for j in pair :
       print (j[0]+","+j[1]+","+j[2])
    f1.close
    f2.close
    print("----------------------------------------")
    

# コマンドラインからこのプログラムを読んだときだけこれを実行する
if __name__ == '__main__':
    # startメソッドの軌道
    start("")
