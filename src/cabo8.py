#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import CaboCha
from xml.etree.ElementTree import *

def cabo(sentence):
 c = CaboCha.Parser("")
 tree =  c.parse(sentence)

 xmlString = tree.toString(CaboCha.FORMAT_XML)
 return xmlString
 elem = fromstring(xmlString)
 

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

def start(check_word):
 f1 = open('2.txt')
 locate_dic = f1.read()  
 #f.close()
 location_dic = []
 location_dic = locate_dic.split(',') 
 print('立地辞書:'+str(location_dic))
 print("----------------------------------------")

 pair = []
 for i in range(1,3):
   f2 = open('test%s.txt'%(i),'r')
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
       x=(float(values[i]))
       if ( x > 0.0):
         pair.append([kakariset[i][0],kakariset[i][1],values[i]])
     
     hoteldata1 = f2.readline() 
 for j in pair :
   print (j[0]+","+j[1]+","+j[2])
 f1.close
 f2.close
 print("----------------------------------------")


 limitdata=[]
 for i in pair:
   kakarimoto = (",".join(i)).split(",")[0]
   print(str(kakarimoto))
   print(str(location_dic[0]))
   if(str(kakarimoto)==float(location_dic[i])):
     print("[match]")
   print("------")



   #if(kakarimoto == str(location_dic[i])):
    # limit += pair[i]
     #print(limit)
