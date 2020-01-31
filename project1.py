import time
import os
def start_menu():
    print('=== WELCOME ===')
    player1=input('Player 1 .Enter your name:\n')
    player2=input('Player 2 .Enter your name:\n')
    x_or_o = input(f'{player1}.Do you want to play with X or O?\n')
    option1 = x_or_o
    option1 = option1.upper()
    print(option1)
    option2 = ''
    while((option1!='X') & (option1!='O')):
        print('Try Again!! We only play with X or O')
        option1 = input(f'{player1} ,do you want to play with X or O ?')
        option1 = option1.upper()
    starting_list = [[player1,option1],[player2,option2]]
    print('--------------------')
    print(f'|  {"7"}  |  {"8"}   |  {"9"}  |\t')
    print('|     |      |     |')
    print('\n')
    print(f'|  {"4"}  |  {"5"}   |  {"6"}  |\t')
    print('|     |      |     |')
    print('\n')
    print(f'|  {"1"}  |  {"2"}   |  {"3"}  |\t')
    print('|     |      |     |')
    print('--------------------')
    return(starting_list)


def init_gui():
    
    my_dict = {'7': ' ','8':' ','9': ' ','4':' ','5':' ','6':' ','1': ' ','2': ' ','3':' '}
    print('--------------------')
    print(f'|  {my_dict["7"]}  |  {my_dict["8"]}   |  {my_dict["9"]}  |\t')
    print('|     |      |     |')
    print('\n')
    print(f'|  {my_dict["4"]}  |  {my_dict["5"]}   |  {my_dict["6"]}  |\t')
    print('|     |      |     |')
    print('\n')
    print(f'|  {my_dict["1"]}  |  {my_dict["2"]}   |  {my_dict["3"]}  |\t')
    print('|     |      |     |')
    print('--------------------')
    return(my_dict)


def update_gui(my_dict):
    print('--------------------')
    print(f'|  {my_dict["7"]}  |  {my_dict["8"]}   |  {my_dict["9"]}  |\t')
    print('|     |      |     |')
    print('\n')
    print(f'|  {my_dict["4"]}  |  {my_dict["5"]}   |  {my_dict["6"]}  |\t')
    print('|     |      |     |')
    print('\n')
    print(f'|  {my_dict["1"]}  |  {my_dict["2"]}   |  {my_dict["3"]}  |\t')
    print('|     |      |     |')
    print('--------------------')

def winner_checker_X(my_dict):
        if(((my_dict['7']=='X') & (my_dict['7'] == my_dict['8']) & (my_dict['8']==my_dict['9'])) | ( (my_dict['4']=='X') & (my_dict['4'] == my_dict['5']) & (my_dict['5']==my_dict['6'])) | ((my_dict['1']=='X') & (my_dict['1'] == my_dict['2']) & (my_dict['2']==my_dict['3'])) | ((my_dict['7']=='X') & (my_dict['7'] == my_dict['5']) & (my_dict['5']==my_dict['3'])) | ((my_dict['1']=='X') & (my_dict['1'] == my_dict['5']) & (my_dict['5']==my_dict['9'])) | ((my_dict['1']=='X') &(my_dict['1'] == my_dict['4']) & (my_dict['4']==my_dict['7'])) | ((my_dict['2']=='X') & (my_dict['2'] == my_dict['5']) & (my_dict['5']==my_dict['8'])) | ((my_dict['3']=='X') & (my_dict['3'] == my_dict['6']) & (my_dict['6']==my_dict['9']))):
                return(True)

def winner_checker_O(my_dict):
        if(((my_dict['7']=='O') & (my_dict['7'] == my_dict['8']) & (my_dict['8']==my_dict['9'])) | ( (my_dict['4']=='O') & (my_dict['4'] == my_dict['5']) & (my_dict['5']==my_dict['6'])) | ((my_dict['1']=='O') & (my_dict['1'] == my_dict['2']) & (my_dict['2']==my_dict['3'])) | ((my_dict['7']=='O') & (my_dict['7'] == my_dict['5']) & (my_dict['5']==my_dict['3'])) | ((my_dict['1']=='O') & (my_dict['1'] == my_dict['5']) & (my_dict['5']==my_dict['9'])) | ((my_dict['1']=='O') &(my_dict['1'] == my_dict['4']) & (my_dict['4']==my_dict['7'])) | ((my_dict['2']=='O') & (my_dict['2'] == my_dict['5']) & (my_dict['5']==my_dict['8'])) | ((my_dict['3']=='O') & (my_dict['3'] == my_dict['6']) & (my_dict['6']==my_dict['9']))):
                return(True)        
        
        
def decision(starting_list,my_dict):
    poslist = [] #For checking the available positions
    pos1 =0
    pos2 =0 
    flag = 0
    total = 0
    win = False
    while(True):
            
        if(flag == 0):    
                pos1 = input(f'{starting_list[0][0]} , give the position of {starting_list[0][1]} as you wish:')
                while(pos1 not in list(map(lambda x:str(x),list(range(0,10))))):
                                pos1 = input(f'Wrong position! {starting_list[0][0]} , give the position of {starting_list[0][1]} as you wish:')  
                while(pos1 in poslist):
                        print('The position is not available.Try again!')
                        pos1 = input(f'{starting_list[0][0]} , give the position of {starting_list[0][1]} as you wish:') 
                        while(pos1 not in list(map(lambda x:str(x),list(range(0,10))))):
                                pos1 = input(f'Wrong position! {starting_list[0][0]} , give the position of {starting_list[0][1]} as you wish:')     
                poslist.append(pos1)
                my_dict[pos1] =starting_list[0][1]
                update_gui(my_dict)
                win = winner_checker_X(my_dict)
                if(win == True):
                        print(f'Congrats {starting_list[0][0]} YOU WIN !!!')
                        return(1)
                total = total +1
                if(total==9):
                        return(1)
                flag=1
        if(flag == 1):
                pos2 = input(f'{starting_list[1][0]} , give the position of {starting_list[1][1]} as you wish:')
                while(pos2 not in list(map(lambda x:str(x),list(range(0,10))))):
                        pos2 = input(f'Wrong position! {starting_list[1][0]} , give the position of {starting_list[1][1]} as you wish:')
                while(pos2 in poslist):
                        print('The position is not available.Try again!')
                        pos2 = input(f'{starting_list[1][0]} , give the position of {starting_list[1][1]} as you wish:')
                        while(pos2 not in list(map(lambda x:str(x),list(range(0,10))))):
                                pos2 = input(f'Wrong position! {starting_list[1][0]} , give the position of {starting_list[1][1]} as you wish:')
                                
                poslist.append(pos2)
                my_dict[pos2] =starting_list[1][1]
                update_gui(my_dict)
                win = winner_checker_O(my_dict)
                if(win == True):
                        print(f'Congrats {starting_list[1][0]} YOU WIN !!!')
                        return(1)
                total = total +1
                if(total==9):
                        return(1)
                flag=0
                        


#Starting Menu
starting_list = start_menu()
status = 0
choice = ''
if(starting_list[0][1] == 'X'): 
        starting_list[1][1] = 'O'
if(starting_list[0][1]=='O'):
        starting_list[1][1]= 'X'   

#Initialize the graphics
time.sleep(1)
os.system('clear')
my_dict = init_gui() 
status=decision(starting_list,my_dict)
if(status == 1):
        while(True):       
                choice=input('Do you want to play again? yes or no\n')
                if(choice == 'yes'):
                        my_dict = init_gui()      
                        status=decision(starting_list,my_dict)
                else:
                        break
                                    