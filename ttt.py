from random import *

# define functions

#making deivider for column
def prRow(box1, box2, box3):
    print(" " + box1 + " | " + box2 + " | " + box3)

#making devider for column
def prBrd(box11, box12, box13, box21, box22, box23, box31, box32, box33):
    " ""Prints the entire board" ""
    divider = "---+---+---"
    prRow(box11, box12, box13)
    print(divider)
    prRow(box21, box22, box23)
    print(divider)
    prRow(box31, box32, box33)


# condition to win
def checkWin(box11, box12, box13, box21, box22, box23, box31, box32, box33):
    winner = False
    if box11 == box12 == box13 != " " or box21 == box22 == box23 != " " or box31 == box32 == box33 != " " or box11 == box21 == box31 != " " or box12 == box22 == box32 != " " or box13 == box23 == box33 != " " or box11 == box22 == box33 != " " or box13 == box22 == box31 != " ":
        winner = True
    return winner


row1col1 = " "
row1col2 = " "
row1col3 = " "
row2col1 = " "
row2col2 = " "
row2col3 = " "
row3col1 = " "
row3col2 = " "
row3col3 = " "

prBrd(row1col1, row1col2, row1col3, row2col1, row2col2, row2col3, row3col1, row3col2, row3col3)
list = ['box11', 'box12', 'box13', 'box21', 'box22', 'box23', 'box31', 'box32', 'box33']


while True:
    move = input('make your move(box11,12,...):')
    while not move in list:
        move = input('where')
    if move == 'box11':
        row1col1= 'x'
        list.remove('box11')
    elif move == 'box12':
        row1col2= 'x'
        list.remove('box12')
    elif move== 'box13':
        row1col3 ='x'
        list.remove('box13')
    elif move == 'box21':
        row2col1 ='x'
        list.remove('box21')
    elif move == 'box22':
        row2col2 ='x'
        list.remove('box22')
    elif move == 'box23':
        row2col3='x'
        list.remove('box23')
    elif move == 'box31':
        row3col1 = 'x'
        list.remove('box31')
    elif move == 'box32':
        row3col2 = 'x'
        list.remove('box32')
    elif move == 'box33':
        row3col3 = 'x'
        list.remove('box33')
    if checkWin(row1col1, row1col2, row1col3, row2col1, row2col2, row2col3, row3col1, row3col2, row3col3):
        prBrd(row1col1, row1col2, row1col3, row2col1, row2col2, row2col3, row3col1, row3col2, row3col3)
        print('player win')
        break
    if list ==[] and checkWin(row1col1, row1col2, row1col3, row2col1, row2col2, row2col3, row3col1, row3col2, row3col3) == False:
        print('The game is draw')
        break


    pmove = choice(list)
    if pmove == 'box11':
        row1col1= 'o'
        list.remove('box11')
    elif pmove == 'box12':
        row1col2= 'o'
        list.remove('box12')
    elif pmove== 'box13':
        row1col3 ='o'
        list.remove('box13')
    elif pmove == 'box21':
        row2col1 ='o'
        list.remove('box21')
    elif pmove == 'box22':
        row2col2 ='o'
        list.remove('box22')
    elif pmove == 'box23':
        row2col3='o'
        list.remove('box23')
    elif pmove == 'box31':
        row3col1 = 'o'
        list.remove('box31')
    elif pmove == 'box32':
        row3col2 = 'o'
        list.remove('box32')
    elif pmove == 'box33':
        row3col3 = 'o'
        list.remove('box33')

    prBrd(row1col1, row1col2, row1col3, row2col1, row2col2, row2col3, row3col1, row3col2, row3col3)
    if checkWin(row1col1, row1col2, row1col3, row2col1, row2col2, row2col3, row3col1, row3col2, row3col3):
        print('computer win')
        break


