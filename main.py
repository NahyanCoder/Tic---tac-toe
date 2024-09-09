#define tic-toc board
board = {
    '7': ' ','8': ' ','9': ' ',
    '4': ' ','5': ' ','6': ' ',
    '1': ' ','2': ' ','3': ' '
}
#funtion to display the code
def show_board(b):
    print(b['7'] + '|' + b['8']+ '|' + b['9'])
    print('-+-+-')
    print(b['4'] + '|' + b['5']+ '|' + b['6'])
    print('-+-+-')
    print(b['1'] + '|' + b['2']+ '|' + b['3'])
    
    #function to check for a win
def check_winner(b,player):
    win_patterns=[
        ('7','8','9'),('4','5','6'),('1','2','3'),
        ('7','4','1'),('8','5','2'),('9','6','3'),
        ('7','5','3'),('1','5','9')
        ]
    return any(b[a]==b[b_]==b[c]==player for a,b_,c in win_patterns)
def play_game():
    player='X'
    moves=0
    while moves<9:
        show_board(board)
        move=input(f"player {player},choose a position(1-9):")
        if board[move]==' ':
            board[move]=player
            moves+=1
        else:
            print("Position already taken!")
            continue
        if moves>=5 and check_winner(board,player):
            show_board(board)
        player = 'O' if player == 'X' else 'X'
    if moves == 9:
        print("It's a tie")
    
play_game()
    
    
    
    
    
    
    
    
    
    
    
    
    