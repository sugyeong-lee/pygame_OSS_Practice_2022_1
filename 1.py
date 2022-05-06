import pygame
################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()     # 초기화

# 화면 크기 설정
screen_width = 1200   # 가로 크기
screen_height = 800   # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("C:\\Users\\653dl\\OneDrive\\바탕 화면\\oss\\pygame_basic\\background1.png")

# 화면 타이틀 설정
pygame.display.set_caption("게임 이름") # 게임 이름

# FPS
clock = pygame.time.Clock()
#################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))    # 배경 그리기
    pygame.display.update()

# 3. 게임 캐릭터 위치 정의
character = pygame.image.load("C:\\Users\\653dl\\OneDrive\\바탕 화면\\oss\\pygame_basic\\ch1.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴, rect(사각형)
character_width = character_size[0]         # 캐릭터의 가로 크기
character_height = character_size[1]        # 캐릭터의 세로 크기
character_x_pos = (screen_width / 5) - (character_width / 5)    # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - character_height              # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

    
    # 4. 충돌 처리
   
    # 5. 화면에 그리rl
    
pygame.quit()
