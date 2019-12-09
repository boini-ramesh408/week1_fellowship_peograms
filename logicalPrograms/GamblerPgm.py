from com.bridgelabz.python.utility.pythonUtil import gambler
try:
    stake=int(input("enter stake value:"))# investment
    goal=int(input("enter goal to win:"))#winning amount
    trials=int(input("enter trials to play the game:"))#number of times
    gambler(stake,goal,trials)
except ValueError:
    print("enter only numbers.....")




