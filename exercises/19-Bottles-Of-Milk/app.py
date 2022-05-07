def number_of_bottles():
    for i in range(99, 0, -1):
        if (2<=i<=100):
            print(i, "bottles of milk on the wall, % s bottles of milk."% (i))
            print("Take one down and pass it around, % s bottles of milk on the wall."% (i-1))
            print("")
        elif(i==1):
            print(i, "bottle of milk on the wall, % s  bottle of milk."% (i))
            print("Take one down and pass it around, no more bottles of milk on the wall.")
            print("")
    print("No more bottles of milk on the wall, no more bottles of milk.")
    print("Go to the store and buy some more, 99 bottles of milk on the wall.")

number_of_bottles()