def fruits():
    fruitlist = ['mango','grapes','orange']
    fruitname = input("enter the fruit name:")
    if(fruitname== fruitlist[0]):
        print(fruitname,"is available")
        
    elif(fruitname== fruitlist[1]):
        print(fruitname,"is available")
    elif(fruitname== fruitlist[2]):
        print(fruitname,"is available")
    else:
        print(fruitname,"not available")
fruits()
