import pygame
import sys
from time import sleep 

###############################################
# 화면 크기 설정
screen_width = 1200  # 가로크기
screen_height = 800  # 세로크기

def drawObject(obj, x, y):   # 게임에 등장하는 객체 드로잉
    global screen      # 전역 변수 선언
    screen.blit(obj, (x, y))


def initGame():
    global screen, clock, background, character, teacher, shot1, shot2     # 전역 변수 선언
    pygame.init()  # 초기화 (반드시 필요)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("stage3")  # 게임 이름
    background = pygame.image.load("C:\\Users\\653dl\\KKLHY\\0_image\\Yang\\background.png")  # 배경
    character = pygame.image.load("C:\\Users\\653dl\\KKLHY\\0_image\\Yang\\character.png")  # 주인공 캐릭터
    shot1 = pygame.image.load("C:\\Users\\653dl\\KKLHY\\아이템\\shot.png")  # 주인공 총알
    shot2 = pygame.image.load("C:\\Users\\653dl\\KKLHY\\아이템\\shot.png")  # 보스 총알
    teacher = pygame.image.load("C:\\Users\\653dl\\KKLHY\\0_image\\Yang\\teacher.png")  # 보스 캐릭터
    clock = pygame.time.Clock() # FPS

def runGame():
    global screen, clock, background, character, teacher, shot1, shot2   # 전역 변수 선언
    
    # 주인공 캐릭터 크기 및 초기 위치
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = character_width
    character_y_pos = (screen_height / 2) - (character_height / 2)
    character_to_x, character_to_y = 0, 0  # 캐릭터 이동 방향
    character_speed = 20   # 캐릭터 이동 속도

    # 주인공 총알 좌표 리스트
    shotXY1 = []

    # 보스 총알 좌표 리스트
    shotXY2 = []
    
    # 보스 캐릭터 크기 및 초기 위치
    teacher_size = teacher.get_rect().size
    teacher_width = teacher_size[0]
    teacher_height = teacher_size[1]
    teacher_x_pos = screen_width - teacher_width
    teacher_y_pos= (screen_height / 2) - (teacher_height / 2)

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
                    shot1_x_pos = character_x_pos + character_width
                    shot1_y_pos = character_y_pos + character_height/2
                    shotXY1.append([shot1_x_pos, shot1_y_pos])
            if event.type in [pygame.KEYUP]:  # 방향키를 떼면 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    character_to_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    character_to_y = 0

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
        
        # 캐릭터 총알 움직임
        if len(shotXY1) != 0:
            for i, bxy in enumerate(shotXY1):
                bxy[0] += 10
                shotXY1[i][0] = bxy[0]
                drawObject(shot1, bxy[0], bxy[1])
                if bxy[0] >= screen_width:
                    shotXY1.remove(bxy)
        # 보스 총알 움직임
        if len(shotXY2) != 0:
            for i, kxy in enumerate(shotXY2):
                kxy[0] += 10
                shotXY2[i][0] = kxy[0]
                drawObject(shot2, kxy[0], kxy[1])
                if kxy[0] >= screen_width:
                    shotXY1.remove(kxy)

        drawObject(background, 0, 0)
        drawObject(character, character_x_pos, character_y_pos)
        drawObject(teacher, teacher_x_pos, teacher_y_pos)

        pygame.display.update()   # 화면에 다시 그리기
        clock.tick(60)  # 게임 화면의 초당 프레임 수를 설정

    pygame.quit()


initGame()
runGame()

        
