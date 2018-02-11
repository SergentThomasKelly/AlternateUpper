##Coded by SergentThomasKelly

# =================== MAIN CODE ================================ #

# >>> Ask text to transform >>>
text=str(input('Type your text here : '))
listText=[]

# >>> Transform every letter to lower case >>>
for letter in text:
    listText.append(letter.lower())

# >>> Alternate the upper cases >>>
for i in range(1,len(listText),2):
    listText[i] = listText[i].upper()

# >>> Join the letters and print result >>>
listText = "".join(listText)
print(listText)
