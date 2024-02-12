print("Welcome to the darts calculator! I will keep track of your game of darts.")
score = int(input("What is the start score of the game?\n"))
round = 1
sum = score
flag = False
while flag == False:
    print()
    roundsum = sum
    print("Enter the results of your throws for round ", round, ":", sep='')
    value = int(input("Throw 1: "))
    sum = sum - value
    value = int(input("Throw 2: "))
    sum = sum - value
    value = int(input("Throw 3: "))
    sum = sum - value
    if sum == 0:
        flag = True
        print("You have 0 points remaining.")
        print("You have won the game after ", round, " rounds. Congratulations!", sep='')
    elif sum < 0 or sum == 1:
        print("You have reduced your score to ", sum, ". Score resetting to the initial score of the round.", sep='')
        sum = roundsum
        print("You have ", sum, " points remaining.", sep='')
        round = round + 1
    elif sum > 1:
        print("You have ", sum, " points remaining.", sep='')
        round = round + 1

