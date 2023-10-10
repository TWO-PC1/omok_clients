import pygame
import numpy as np
import time
import requests, json
import threading
import queue
import websocket
import time
import tkinter as tk






current_player=1

BOARD_SIZE = 15
board = np.zeros([BOARD_SIZE, BOARD_SIZE], dtype=str)

WIDTH, HEIGHT = 800, 800
STONE_SIZE = int(WIDTH / BOARD_SIZE)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (160, 90, 40)
GOLD = (255,215,0)
RED = (255,0,0)


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("오목 게임")
font = pygame.font.SysFont("arial",30,True,True)



def draw_board():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            pygame.draw.rect(screen, BLACK, (j*STONE_SIZE, i*STONE_SIZE, STONE_SIZE, STONE_SIZE), 2)
            if board[i][j] == '1':
                pygame.draw.circle(screen, BLACK, (j*STONE_SIZE+STONE_SIZE//2, i*STONE_SIZE+STONE_SIZE//2), STONE_SIZE//2-2)
            elif board[i][j] == '2':
                pygame.draw.circle(screen, WHITE, (j*STONE_SIZE+STONE_SIZE//2, i*STONE_SIZE+STONE_SIZE//2), STONE_SIZE//2-2)
            elif board[i][j] == 'w':
                pygame.draw.circle(screen, GOLD, (j*STONE_SIZE+STONE_SIZE//2, i*STONE_SIZE+STONE_SIZE//2), STONE_SIZE//2-2)
            elif board[i][j] == 'x':
               pygame.draw.line(screen, RED, (j*STONE_SIZE, i*STONE_SIZE), ((j+1)*STONE_SIZE, (i+1)*STONE_SIZE), 5)
               pygame.draw.line(screen, RED, ((j+1)*STONE_SIZE, i*STONE_SIZE), (j*STONE_SIZE, (i+1)*STONE_SIZE), 5)

                
                

def rule(player):
    if player ==1:
         pass
     
def cross():
    for i in range(BOARD_SIZE-4):
        for j in range(4, BOARD_SIZE):
            if board[i][j] != "" and \
            board[i][j] == board[i+1][j-1] and \
            board[i+1][j-1] == board[i+2][j-2] and \
            board[i+2][j-2] == board[i+3][j-3] and \
            board[i+3][j-3] == board[i+4][j-4]:

                board[i][j] = "w"
                board[i+1][j-1] = "w"
                board[i+2][j-2] = "w"
                board[i+3][j-3] = "w"
                board[i+4][j-4] = "w"
                print('역대각선 yes!')
                return True

    for i in range(4, BOARD_SIZE):
        for j in range(4, BOARD_SIZE):
            if board[i][j] != "" and \
            board[i][j] == board[i-1][j-1] and \
            board[i-1][j-1] == board[i-2][j-2] and \
            board[i-2][j-2] == board[i-3][j-3] and \
            board[i-3][j-3] == board[i-4][j-4]:
                board[i][j] = "w"
                board[i-1][j-1] = "w"
                board[i-2][j-2] = "w"
                board[i-3][j-3] = "w"
                board[i-4][j-4] = "w"







                print('정대각선yes!')
                return True

    for i in range(BOARD_SIZE):
        for j in range( BOARD_SIZE-4):
            if board[i][j]!= "" and \
            board[i][j] == board[i][j+1] and \
            board[i][j+1] == board[i][j+2] and \
            board[i][j+2] == board[i][j+3] and \
            board[i][j+3] == board[i][j+4]:
                board[i][j] = "w"
                board[i][j+1] = "w"
                board[i][j+2] = "w"
                board[i][j+3] = "w"
                board[i][j+4] = "w"
                print('가로yes!')
                return True
    for j in range(BOARD_SIZE):
        for i in range( BOARD_SIZE-4):
            if board[i][j]!= "" and \
            board[i][j] == board[i+1][j] and \
            board[i+1][j] == board[i+2][j] and \
            board[i+2][j] == board[i+3][j] and \
            board[i+3][j] == board[i+4][j]:
                board[i][j] = "w"
                board[i+1][j] = "w"
                board[i+2][j] = "w"
                board[i+3][j] = "w"
                board[i+4][j] = "w"






                print('세로yes!')
                return True
game = False
def button_click_action():
    global game
    print("게임 시작")
    game=True

def token():
    data = {
        'id': 'example',
        'pd':'example1' #임시데이터

    }
    headers={}
    url3='http://127.0.0.1:3000/signin'
    url2='http://127.0.0.1:3000/user'

    response = requests.post(url3, data=data, headers=headers)# 로그인 및 토큰 발급 과정
    print(response.text)
    response_data=json.loads(response.text)
    token = {'token':response_data.get('message')}

    print('ttttasdasd',token)
    response2 = requests.post(url2, json=data, headers=token)# 토큰 1차 검증 과정 
    print('dfdsf',response2.text)
    return token
    
def open_websocket_connection(token):
    # WebSocket 연결 열기
    data2={
#   'headers':'matching',
#   'id':'ysj',
'token':token

    }
    data3={
#   'headers':'matching',
#   'id':'ysj',
'headers':'matching'

}
    url = f'ws://127.0.0.1:3000'
    ws = websocket.create_connection(url)
    ws.send(json.dumps(data2))
    ws.send(json.dumps(data3))


    # 연결 반환
    return ws


button_width, button_height = 200, 50

button_x, button_y = (WIDTH - button_width) // 2, (HEIGHT - button_height) // 2
# Font settings
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 80)
button_text = font.render("game start", True, WHITE)
text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2+100))
button_text2 = font.render("multiplay", True, WHITE)
text_rect2 = button_text2.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2+200 ))  # Adjusted y-position
button_text4 = font2.render("THE Oooomok", True, WHITE)
text_rect4 = button_text4.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2 -180))

win=None


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
        
        
                    # Check if the mouse click is within the button area
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_pos = pygame.mouse.get_pos()
            if game==True:
                x, y = event.pos
                j, i = int(x / STONE_SIZE), int(y / STONE_SIZE)
                print(i,j)
                if not i>BOARD_SIZE-1 and not j>BOARD_SIZE-1:
                    if board[i][j] == "":
                        board[i][j] = current_player
                        if cross():
                            print("플레이어 {} 승리!".format(current_player))
                            win = current_player
                            
                        current_player = 3 - current_player  # 1 -> 2, 2 -> 1
                        
                    else:
                        print('돌이 있는 자리입니다')
                else:
                    print('범위 초과')
            else:
                if text_rect.collidepoint(mouse_pos):
                    button_click_action()
                elif text_rect2.collidepoint(mouse_pos):
                    print("Multiplay button clicked!")
                elif text_rect4.collidepoint(mouse_pos):
                    print("THE Oooomok button clicked!")  

      # 화면 업데이트
    if game==True:
        screen.fill(BROWN)
        draw_board()
        pygame.display.update()
        if win!=None:
            if win==1:
                win='BLACK'
            else:
                win='WHITE'
            button_text3 = font.render(str(win)+" is win!", True, WHITE)
            text_rect3 = button_text3.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2 ))  
            pygame.draw.rect(screen, BLACK, (button_x, button_y, button_width, button_height))
            screen.blit(button_text3, text_rect3)
            pygame.display.update()
            time.sleep(3)
            board = np.zeros([BOARD_SIZE, BOARD_SIZE], dtype=str)
            game=False
            win=None
        
    else:
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (button_x - 100, button_y - 200, button_width*2, button_height*2))
        pygame.draw.rect(screen, BLACK, (button_x, button_y+100, button_width, button_height))
        pygame.draw.rect(screen, BLACK, (button_x, button_y +200, button_width, button_height))  # Adjusted y-position
        screen.blit(button_text, text_rect)
        screen.blit(button_text2, text_rect2)
        screen.blit(button_text4, text_rect4)
        pygame.display.flip()
    

cross()
time.sleep(2)
print(board)