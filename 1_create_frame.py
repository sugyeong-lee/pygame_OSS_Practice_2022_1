import pygame

pygame.init()     # 초기화

# 화면 크기 설정
screen_width = 800   # 가로 크기
screen_height = 600   # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 이벤트 루프
runing = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event in event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임 진행 중이 아님

# pygame 종료
pygame.quit()
