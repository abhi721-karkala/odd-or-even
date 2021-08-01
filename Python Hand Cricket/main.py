import utils
import random

teams= ["CSK","RCB","MI","KKR","KXIP","RR","SRH","DC"]
print("It is the odd or even cricket tournament")
print("Please select your team:\n0.CSK\n1.RCB\n2.MI\n3.KKR\n4.KXIP\n5.RR\n6.SRH\n7.DC\n")
team= int(input("Please select your team number:"))
cteam = random.randint(0,7)
if teams[team]==teams[cteam]:
    cteam= cteam+1
    if cteam==8:
        cteam= cteam-3
print("Hello friend!")
print("It's the match between"+" "+teams[team]+" "+"and"+" "+teams[cteam])
print("It's the toss time")
dec = int(input("Select: 1.odd 2.even:"))
cnum = random.randint(1, 6)
if dec==1:
    cons=utils.odd(team,cteam)
else:
    cons=utils.even(team,cteam)

if cons==0:
    utils.bat(team,cteam)
else:
    utils.bowl(team,cteam)
