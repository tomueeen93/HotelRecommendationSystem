#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
import tkinter.messagebox 
import cabo8


root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

#ラベル
Static1 = tkinter.Label(text=u'ホテル推薦',foreground='black',bg='skyblue')
Static1.place(x=0,y=0)
Static2 = tkinter.Label(text=u'あなたの嗜好にあったホテルを推薦します',bg='skyblue')
Static2.place(x=100,y=200)
Static3 = tkinter.Label(text=u'重要視するキーワードを一つ選択してください',bg='skyblue')
Static3.place(x=93,y=220)
#print("root.cofigure(width = 400, height=300,bg='skyblue')")
root.configure(width = 400, height=300,bg='skyblue')
Static4 = tkinter.Label(text=u'選択項目',bg='skyblue')
Static4.pack()
Static5 = tkinter.Label(text=u'     ',bg='skyblue')
Static5.pack()


#Static1.place(x=0,y=0)
#自動的に位置を揃えてウィンドウ上に配置
#Static1.pack()

#エントリー
#EditBox = tkinter.Entry(width=50)
#EditBox.insert(tkinter.END,"重要視するキーワード入力")
#EditBox.pack()

#
# チェックボックスのチェック状況を取得する
#
def check(event):
    global Val1
    global Val2
    global Val3
    global Val4
    global Val5
    global Val6
    global Val7
#add
    text = ""
    check_word = ""

    if Val1.get() == True:
        text += "サービスはチェックされています\n"
        check_word += "サービス,"
    else:
        text += "サービスはチェックされていません\n"

    if Val2.get() == True:
        text += "料理はチェックされています\n"
        check_word += "料理,"
    else:
        text += "料理はチェックされていません\n"

    if Val3.get() == True:
        text += "お風呂はチェックされています\n"
    else:
        text += "お風呂はチェックされていません\n"
        
    if Val4.get() == True:
        text += "ネット環境はチェックされています\n"
    else:
        text += "ネット環境はチェックされていません\n"
        
    if Val5.get() == True:
        text += "価格はチェックされています\n"
    else:
        text += "価格はチェックされていません\n"
        
    if Val6.get() == True:
        text += "景色はチェックされています\n"
    else:
        text += "景色はチェックされていません\n"
        
    if Val7.get() == True:
        text += "立地はチェックされています\n"
    else:
        text += "立地はチェックされていません\n"
        

    cabo8.start(check_word)
    tkinter.messagebox.showinfo('info',text)
   

#
# チェックボックスの各項目の初期値
#
Val1 = tkinter.BooleanVar()
Val2 = tkinter.BooleanVar()
Val3 = tkinter.BooleanVar()
Val4 = tkinter.BooleanVar()
Val5 = tkinter.BooleanVar()
Val6 = tkinter.BooleanVar()
Val7 = tkinter.BooleanVar()

Val1.set(False)
Val2.set(False)
Val3.set(False)
Val4.set(False)
Val5.set(False)
Val6.set(False)
Val7.set(False)

CheckBox1 = tkinter.Checkbutton(text=u"サービス", variable=Val1,bg='skyblue')
CheckBox1.pack()

CheckBox2 = tkinter.Checkbutton(text=u"料理", variable=Val2,bg='skyblue')
CheckBox2.pack()

CheckBox3 = tkinter.Checkbutton(text=u"お風呂", variable=Val3,bg='skyblue')
CheckBox3.pack()

CheckBox4 = tkinter.Checkbutton(text=u"ネット環境", variable=Val4,bg='skyblue')
CheckBox4.pack()

CheckBox5 = tkinter.Checkbutton(text=u"価格", variable=Val5,bg='skyblue')
CheckBox5.pack()

CheckBox6 = tkinter.Checkbutton(text=u"景色", variable=Val6,bg='skyblue')
CheckBox6.pack()

CheckBox7 = tkinter.Checkbutton(text=u"立地", variable=Val7,bg='skyblue')
CheckBox7.pack()


button1 = tkinter.Button(root, text=u'検索',width=30)
button1.bind("<Button-1>",check)
button1.pack()

root.mainloop()
