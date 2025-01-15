class Solve:
    def countCGPA():
        for i in range(int(input())):
            p=f=g=0
            for j in [1]*int(input()):
                m,c=map(float,input().split());p+=c
                if m<40:f+=1
                elif m>=80:g+=4*c
                else:g+=c*(m//5)/4
            print("Case %d: %s"%(i+1,('%.2f'%(g/p),'Sorry, you have failed in %d course%s!'%(f,('s','')[f<2]))[f>0]))




if __name__ == '__main__':
    Solve.countCGPA()
