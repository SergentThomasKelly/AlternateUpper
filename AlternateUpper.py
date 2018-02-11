##Coded by SergentThomasKelly

# ================= IMPORTING MODULE AND SETTING VARIABLES =================== #
from tkinter import *
import os
startLetter = 0

# =============================== FUNCTIONS ================================== #
# >>> Update start letter value >>>
def updatePair(x):
    global startLetter
    startLetter = int(x)

# >>> Transform the text >>>
def Alternate():
    global label, startLetter
    listText=[]
    for letter in TextToTransform.get():
        listText.append(letter.lower())
    for i in range(startLetter,len(listText),2):
        listText[i] = listText[i].upper()
    listText = "".join(listText)
    label["text"] =str(listText)

# ========================== WINDOW AND MAIN OPTIONS ========================= #
root = Tk()
root.title("Alternate upper and lower")
root.resizable(width=False, height=False)
root.configure(background='lavender')
if os.path.isfile('iconUpperLower.ico') == True:
    root.iconbitmap('iconUpperLower.ico')
mainLabel = Label(root, 
                text='Here you can type some text and make it "MoRe LiKe ThAt"', 
                bg='lavender').pack()
TextToTransform = StringVar()
entryText = Entry(root, textvariable=TextToTransform, width = 65).pack()
pairScale = Scale(root, orient='horizontal', from_=0, to=1, resolution=1,
                tickinterval=1, length=390, label='Start at letter ',
                command=updatePair, bg='lavender').pack()
TransformButton = Button(root, text="TRANSFORM", command=Alternate, 
                bg='chartreuse').pack()
label = Label(root, text="", bg= 'lavender')
label.pack()
root.mainloop()