total = int(input('How much money do you have in your pocket\n'))

# YOUR CODE HERE
if total>100:
    print("Give me your money!")
elif 50<total<=100:
    print("Buy me some coffee you cheap!")
elif 0<total<=50:
    print("You are a poor guy, go away!")
else : print()