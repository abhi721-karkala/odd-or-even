import random

string = ["Bat", "Bowl"]
teams = ["CSK", "RCB", "MI", "KKR", "KXIP", "RR", "SRH", "DC"]


def odd(hum, comp):
    hval = int(input("Please enter an odd number:"))
    cnum = random.randint(1, 6)
    if hval % 2 == 0:
        print("Please enter correct odd number")
        hval = int(input("Enter an odd number:"))
    sum = hval + cnum
    if not sum % 2 == 0:
        print(teams[hum] + " " + "have won the toss what would you decide:")
        print("0.Bat\n1.Ball\n")
        wal = int(input("Please choose:"))
        print(teams[hum] + " " + "have won the toss and decided to" + " " + string[wal] + " "+ "first")
        return wal

    else:
        thu = random.randint(0, 1)
        print(teams[comp] + " " + "have won the toss and choose to" + " " + string[thu] + " " + "first")
        if thu == 1:
            return 0
        else:
            return 1


def even(hum, comp):
    hval = int(input("Please enter an even number:"))
    cnum = random.randint(1, 6)
    if hval % 2 != 0:
        print("Please enter correct even number")
        hval = int(input("Enter an even number:"))
    sum = hval + cnum
    if sum % 2 == 0:
        print("You have won the toss what would you decide:")
        print("0.Bat\n1.Ball\n")
        wal = int(input("Please choose:"))
        print(teams[hum] + " " + "have won the toss and decided to" + " " + string[wal] + " " + "first")
        return wal

    else:
        thu = random.randint(0, 1)
        print(teams[comp] + " " + "have won the toss and choose to" + " " + string[thu] + " " + "first")
        if thu == 1:
            return 0
        else:
            return 1


def bat(team1, cteam1):
    add1 = 0
    add2 = 0
    print("Hello folks!")
    while 1:
        play = int(input("Respond through values:"))
        oppo = random.randint(1, 6)
        print("opponent:" + str(oppo))
        if play == oppo:
            print(teams[team1] + " " + "are all-out,it's opponents turn")
            print(teams[cteam1] + " " + "need" + " " + str(int(add1) + 1) + " " + "to win")
            add1 = add1 + 12
            break

        else:
            add1 = add1 + play

    while 1:
        play = int(input("Respond through values:"))
        oppo = random.randint(1, 6)
        add2 = add2 + oppo
        print("opponent:" + str(oppo))
        if play == oppo:
            print("OUT!")
            print("congratulations" + " " + teams[team1] + " " + "have won the match!")
            break
        if add2 >= add1:
            print("congratulations" + " " + teams[cteam1] + " " + "have won the match")
            break
        else:
            add2 = add2 + oppo

    return


def bowl(team1, cteam1):
    add1 = 0
    add2 = 0
    print("Hello folks!")
    while 1:
        play = int(input("Respond through values:"))
        oppo = random.randint(1, 6)
        print("opponent:" + str(oppo))
        if play == oppo:
            print("OUT!")
            print(teams[cteam1] + " " + "are all-out,it's opponents turn")
            print(teams[team1] + " " + "need" + " " + str(int(add1) + 1) + " " + "to win")
            add1 = add1+1
            break

        else:
            add1 = add1 + oppo

    while 1:
        play = int(input("Respond through values:"))
        oppo = random.randint(1, 6)
        print("opponent:" + str(oppo))
        if play == oppo:
            print("congatulations" + " " + teams[cteam1] + " " + "have won the match!")
            break
        elif add2 >= add1:
            print("congratulations" + " " + teams[team1] + " " + "have won the match")
            break
        else:
            add2 = add2 + play
    return
