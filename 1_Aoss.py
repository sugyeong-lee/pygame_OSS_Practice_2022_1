import pygame
import sys
from time import sleep 
import random


###############################################
# 화면 크기 설정
screen_width = 1200  # 가로크기
screen_height = 800  # 세로크기

def drawObject(obj, x, y):   # 게임에 등장하는 객체 드로잉
    global screen      # 전역 변수 선언
    screen.blit(obj, (x, y))


def initGame():
    global screen, clock, background, character, shot, teacher, ball    # 전역 변수 선언
    pygame.init()  # 초기화 (반드시 필요)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("stage3")  # 게임 이름
    background = pygame.image.load("C:\\Users\\653dl\\KKLHY\\0_image\\Yang\\background.png")  # 배경
    character = pygame.image.load("C:\\Users\\653dl\\KKLHY\\0_image\\Yang\\character.png")  # 주인공 캐릭터
    shot = pygame.image.load("C:\\Users\\653dl\\KKLHY\\0_image\\Yang\\shot.png")  # 주인공 공격
    teacher = pygame.image.load("C:\\Users\\653dl\\KKLHY\\0_image\\Yang\\teacher.png")  # 보스 캐릭터
    ball = pygame.image.load("C:\\Users\\653dl\\KKLHY\\0_image\\Yang\\ball.png")  # 아이템
    clock = pygame.time.Clock() # FPS

def runGame():
    global screen, clock, background, character, shot, teacher, ball  # 전역 변수 선언
    
    # 주인공 캐릭터 크기 및 초기 위치
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = character_width
    character_y_pos = (screen_height / 2) - (character_height / 2)
    character_to_x, character_to_y = 0, 0  # 캐릭터 이동 방향
    character_speed = 20   # 캐릭터 이동 속도

    # 총알 좌표 리스트
    shotXY = []

    
    # 보스 캐릭터 크기 및 초기 위치
    teacher_size = teacher.get_rect().size
    teacher_width = teacher_size[0]
    teacher_height = teacher_size[1]
    teacher_x_pos = screen_width - teacher_width
    teacher_y_pos= (screen_height / 2) - (teacher_height / 2)

    # 아이템 크기 및 초기 위치
    ball_size = ball.get_rect().size
    ball_width = ball_size[0]
    ball_height = ball_size[1]
    ball_x_pos = screen_width - teacher_width
    ball_y_pos = screen_height/2 - ball_height/2
    
    onGame = False  # 게임이 진행중인가?
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:   # 게임 프로그램 종료
                pygame.quit()
                sys.exit()
        
            if event.type in [pygame.KEYDOWN]:  # 키가 눌러졌는지 확인
                if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                    character_to_x -= character_speed
                elif event.key == pygame.K_RIGHT:
                    character_to_x += character_speed
                elif event.key == pygame.K_UP:
                    character_to_y -= character_speed
                elif event.key == pygame.K_DOWN:
                    character_to_y += character_speed
                elif event.key == pygame.K_SPACE:
                    shot_size = shot.get_rect().size
                    shot_width = shot_size[0]
                    shot_height = shot_size[1]
                    shot_x_pos = character_x_pos - character_width
                    shot_y_pos = character_y_pos + character_height/2
                    shot_to_x, shot_to_y = 0, 0
                    shot_x_pos += shot_to_x
                    shot_y_pos += shot_to_y
                    shotXY.append([shot_x_pos, shot_y_pos])
            if event.type in [pygame.KEYUP]:  # 방향키를 떼면 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    character_to_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    character_to_y = 0

        drawObject(background, 0, 0)

        drawObject(character, character_x_pos, character_y_pos)
        # 3. 주인공 캐릭터 위치 재정의
        character_x_pos += character_to_x
        character_y_pos += character_to_y
        if character_x_pos < 0:
            character_x_pos = 0
        elif character_y_pos < 0:
            character_y_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width
        elif character_y_pos > screen_height - character_height:
            character_y_pos = screen_height - character_height
        
        if len(shotXY) != 0:
            for i, shot_to_xy in enumerate(shotXY):
                 shot_to_xy[0] -= 10
                 shotXY[1][i] = shot_to_xy[0]
                 if shot_to_xy[0] <= 0:
                    try:
                        shotXY.remove(shot_to_xy)
                    except:
                        pass
        if len(shotXY) != 0:
            for shot_to_x, shot_to_y in shotXY:
                drawObject(shot, shot_x_pos, shot_y_pos)


        drawObject(teacher, teacher_x_pos, teacher_y_pos)

        pygame.display.update()   # 화면에 다시 그리기
        clock.tick(60)  # 게임 화면의 초당 프레임 수를 설정

    pygame.quit()


initGame()
runGame()
