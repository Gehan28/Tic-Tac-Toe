from random import randint

# Players
pl1 = input('Player 1 enter your name : ')
pl2 = input('Player 2 enter your name : ')

# Game

ch = 'y'
while(ch == 'y'):
    # Toss
    pl = randint(0, 1)
    set_p = ('Player1 :'+pl1, 'Player2 :'+pl2)
    print(str(set_p[pl])+'----->starts with X')
    pl_dupli = pl
    # format
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # FUNCTIONS
    # print format of tic tac toe

    def print_format(l):
        print('\n')
        for i in range(0, 3):
            for j in range(0, 3):
                print(l[i][j], end='')
                if(j == 0 or j == 1):
                    print('|', end='')
            if(i == 0 or i == 1):
                print('\n'+'------')
        print('\n')
    print_format(l)

    def win_case(l):
        cases = [{1, 5, 9}, {1, 4, 7}, {1, 2, 3}, {
            2, 5, 8}, {3, 6, 9}, {3, 5, 7}, {4, 5, 6}]
        for x in cases:
            if x.intersection(l) == x:
                return(True)

    count = 9
    move1 = set()
    move2 = set()
    while(count != 0):
        move = set_p[pl]
        print('\n'+str(move)+' '+'Your Move')
        x = int(input())
        d = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (
            1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}
        i = d[x][0]
        j = d[x][1]
        if count % 2 != 0:
            l[i][j] = 'X'
            move1.add(x)
            if win_case(move1):
                print(str(set_p[pl])+' '+'Wins')
                print_format(l)
                break
        else:
            l[i][j] = 'O'
            move2.add(x)
            if win_case(move2):
                print(str(set_p[pl])+' '+'Wins')
                print_format(l)
                break
        print_format(l)

        pl = bool(pl)
        pl = not pl
        pl = int(pl)
        count = count-1
    if count==0:
    	print('Tie Game')
    ch = input('\nDo you want to continue?\n Yes-y No-n')
