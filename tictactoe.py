import random

#tic tac toe

#         a1  a2    a3  b1    b2  b3    c1  c2   c3
board = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]

boardnames = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

def boardshower() :
    print("   1   2   3 ")
    print("  ___ ___ ___")
    print(f"A |{board[0]}| |{board[1]}| |{board[2]}|")
    print("  ___ ___ ___")
    print(f"B |{board[3]}| |{board[4]}| |{board[5]}|")
    print("  ___ ___ ___")
    print(f"C |{board[6]}| |{board[7]}| |{board[8]}|")

boardshower()

def placer(decision, xoro) :
    # a guy on discord helped me with this
    
    for i,(f, b) in enumerate(zip(board, boardnames)):
        if decision == b:
            if f == "0" or f == "X":
                if xoro == "X":
                    print("you cant place that there! somebody already placed something there...")
                #didhereally being short for did he really place his thing where somebody else had placed theirs
                global didhereally
                didhereally = True
            else:
                if xoro == "X":
                   board[i] = "X"
                   boardshower()
                   print("")
                   didhereally = False
                elif xoro == 0:
                   board[i] = "0"
                   boardshower()
                   print("")
                   didhereally = False

while True:
    while True:
        xlocation = input("where do you want to place an x?")
        placer(xlocation, "X")
        if didhereally == True:
            xlocation = input("Try not to place your X on an occupied square this time! Where do you want to place an x?")
        elif didhereally == False:
            break

    #win conditions    
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        print("X has won")
        break
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        print("X has won")
        break
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        print("X has won")
        break
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        print("X has won")
        break
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        print("X has won")
        break
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        print("X has won")
        break
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        print("X has won")
        break
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        print("X has won")
        break    
   
    #0 player is a robot
    while True:
        onumber = random.randint(0, 8)
        xlocation = boardnames[onumber]
    
        placer(xlocation, 0)
        if didhereally == True:
            onumber = random.randint(0, 8)
            xlocation = boardnames[onumber]
        else:
            break
        
    if board[0] == "0" and board[1] == "0" and board[2] == "0":
        print("0 has won")
        break
    elif board[2] == "0" and board[5] == "0" and board[8] == "0":
        print("0 has won")
        break
    elif board[6] == "0" and board[7] == "0" and board[8] == "0":
        print("0 has won")
        break
    elif board[0] == "0" and board[3] == "0" and board[6] == "0":
        print("0 has won")
        break
    elif board[3] == "0" and board[4] == "0" and board[5] == "0":
        print("0 has won")
        break
    elif board[1] == "0" and board[4] == "0" and board[7] == "0":
        print("0 has won")
        break
    elif board[0] == "0" and board[4] == "0" and board[8] == "0":
        print("0 has won")
        break
    elif board[2] == "0" and board[4] == "0" and board[6] == "0":
        print("0 has won")
        break    
