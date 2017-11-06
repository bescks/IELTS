import codecs
import re
import webbrowser
import tkinter as tk
from tkinter import ttk

word_list = None
words = []
words_index = None
f = None

win = tk.Tk()
win.title("IELTS")  # 添加标题
win.geometry('120x335')


def select_number(event):
    global word_list, words, words_index, f
    word_list = number.get()
    f = codecs.open(
        "/Users/gengdongjie/WorkSpace/PycharmProjects/2017-11-05-IELTS/text/world list " + word_list + ".html", 'r',
        'utf-8')
    pattern = re.compile("""^[<p class="]+normaltext1+[">]+[a-z]*[<sup class="suptext1">*</sup>]*[</p>]+$""")
    words = []
    words_index = 0
    line = f.readline()
    while line:
        if pattern.match(line):
            words.append(line.split(">")[1].split("<")[0])
        line = f.readline()
    f.close()
    text3.set(str(1) + " / " + str(len(words)))
    text4.set(words[words_index])
    b1.config(state="normal")
    b2.config(state="normal")
    b3.config(state="normal")
    b4.config(state="normal")
    cambridge()


def next_word():
    global words, words_index
    words_index += 1
    text3.set(str(words_index + 1) + " / " + str(len(words)))
    text4.set(words[words_index])


def cambridge():
    global words, words_index
    webbrowser.open('https://dictionary.cambridge.org/us/dictionary/english-chinese-simplified/' + words[words_index],
                    new=0)


def merriam():
    global words, words_index
    webbrowser.open('http://learnersdictionary.com/definition/' + words[words_index],
                    new=0)


def next_cam():
    global words, words_index
    next_word()
    webbrowser.open('https://dictionary.cambridge.org/us/dictionary/english-chinese-simplified/' + words[words_index],
                    new=0)


l1 = tk.Label(win, text='Word List', font='Arial 15 bold', background='white')
l1.pack()

number = tk.StringVar()
numberChosen = ttk.Combobox(win, font='Arial 18 normal', textvariable=number, background='white', state="readonly",
                            width=2)
num = []
for i in range(1, 49):
    num = num + [i]
numberChosen["values"] = num
numberChosen.pack()
numberChosen.bind("<<ComboboxSelected>>", select_number)

l2 = tk.Label(win, text='Count:', font='Arial 20 bold', background='white')
l2.pack()

text3 = tk.StringVar()
text3.set("-- / --")
tk.Label(win, textvariable=text3, font=('Arial 20 normal', 20), background='white').pack()

tk.Frame(win, height=1, width=120, bg="black").pack()

text4 = tk.StringVar()

tk.Label(win, textvariable=text4, font="Times 18 bold ", foreground='#271727').pack()

tk.Frame(win, height=1, width=120, bg="black").pack()

b1 = tk.Button(win, pady=10, text="Skip", font="Arial 20 bold", command=next_word, state='disabled')
b1.pack(fill=tk.BOTH)

b2 = tk.Button(win, padx=10, pady=10, text="Cambridge", font="Arial 22 bold", foreground='#248597', command=cambridge,
               state='disabled')
b2.pack(fill=tk.BOTH)

b3 = tk.Button(win, pady=10, text="Merriam", font="Arial 22 bold", foreground='#c21d23', command=merriam,
               state='disabled')
b3.pack(fill=tk.BOTH)

b4 = tk.Button(win, pady=10, text="Next-Cam", font="Arial 22 bold", foreground='#c21d23', command=next_cam,
               state='disabled')
b4.pack(fill=tk.BOTH)

win.mainloop()
