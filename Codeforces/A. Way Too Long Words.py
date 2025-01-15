class Solve:
    def toolong(word:str)->None:
        
        
        x:int=word.__len__()

        if x>10:
            finalword=f'{word[:1]}{x-2}{word[-1:]}'
            print(finalword)
        else:
           print(word)




if __name__ == '__main__':
    testcase:int=int(input())
    for i in range(testcase):
        word:str=str(input())
        Solve.toolong(word)
