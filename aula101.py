x = 1

def escopo():
    global x
    x = 10

    def otra_funcao():
        #global x
        x = 11
        y = 2
        print(x, y)
    
    
    otra_funcao()    
    #print(x)    

#print(x)
escopo()
#print(x)

