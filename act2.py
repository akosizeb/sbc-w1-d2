from random import randint

player = input("FOLD OR UNFOLD? ")

print(f"PLAYER : {player} ")
C2 = randint(1,2)
if C2 == 1:
    print("C2 : FOLD")
else:
    print("C2 : UNFOLD")

C3 = randint(1,2)
if C3 == 1:
    print("C3 : FOLD")
else:
    print("C3 : UNFOLD")

        
if (player == "FOLD" and C2 == 1 and C3 == 1) or (player == "UNFOLD" and C2 == 2 and C3 == 2):
    print("ITS A DRAW")

elif (player == "FOLD" and C2 == 2 and C3 == 1) or (player == "UNFOLD" and C2 == 1 and C3 == 2):
    print("C2 wins")


elif (player == "FOLD" and C2 == 1 and C3 == 2) or (player == "UNFOLD" and C2 == 2 and C3 == 1):
    print("C3 wins")


elif (player == "UNFOLD" and C2 == 1 and C3 == 1) or (player == "FOLD" and C2 == 2 and C3 == 2):
    print("Player wins")

else:
    print("PLEASE TRY AGAIN!")