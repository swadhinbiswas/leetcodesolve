def function(file:str):
    lite=list(file)
    listx=[]
    for i in lite:
        if i.isalpha():

            x=ord(i)+32
            listx.append(chr(x))
    print(listx)



text="cOdEfOrCeS"
function(text)


def function(str)->str:
    arrx=[]
    for 