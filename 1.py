import pygame

pygame.init()     # 초기화
# 음향 속도 추가

# 불러오기 모듈? 찾기

# class 묶기 수정

# 화면 크기 설정
screen_width = 1200   # 가로 크기
screen_height = 800   # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game Name") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기 
background = pygame.image.load("C:\\Users\\653dl\\OneDrive\\바탕 화면\\oss\\pygame_basic\\background1.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\653dl\\OneDrive\\바탕 화면\\oss\\pygame_basic\\ch1.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴, rect(사각형)
character_width = character_size[0]         # 캐릭터의 가로 크기
character_height = character_size[1]        # 캐릭터의 세로 크기
character_x_pos = character_width - screen_width     # 화면 가로의 가장 왼쪽에 해당하는 곳에 위치 (가로)
character_y_pos = 0              # 화면 세로 크기에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 1 # 1이 가장 부드러움


# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()   # 현재 tick을 받아옴

# 이벤트 루프
running = True 
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임 진행 중이 아님
            
        if event.type == pygame.KEYDOWN:          # 키가 눌러졌는지 확인
            if event.key == pygame.K_UP:         # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:      # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP:     # 방향키를 떼면 멈춤
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt   # dt = 프레임값 보정
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

        # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))    # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update()  # 게임 화면을 다시 그리기!

# 잠시 대기
pygame.time.delay(2000)  # 2초 정도 대기 (ms)

# pygame 종료
pygame.quit()

print("2022 project")



# p_item
p_it1 = obj()
p_it2 = obj()
p_it3 = obj()
p_item1 = p_it1.img("/Users/ho/Git/KKLHY/아이템/아이템/p_it2.png")
p_item1 = p_it1.img("C:\\Users\\653dl\\KKLHY\\아이템\\p_it2.png")
p_item1_width, p_item1_height = p_it1.img_size(p_item1)  # 아이템의 가로, 세로 크기 설정
p_it1.x_pos, p_it1.y_pos = 1300, random.randint(0, screen_height - p_item1_height)  # 아이템 위치 설정(random)
p_it1.speed = 5
p_item2 = p_it2.img("/Users/ho/Git/KKLHY/아이템/아이템/p_it3.png")
p_item2 = p_it2.img("C:\\Users\\653dl\\KKLHY\\아이템\\p_it3.png")
p_item2_width, p_item2_height = p_it2.img_size(p_item2)  # 아이템의 가로, 세로 크기 설정
p_it2.x_pos, p_it2.y_pos = 1300, random.randint(0, screen_height - p_item2_height)  # 아이템 위치 설정(random)
p_it2.speed = 5
p_item3 = p_it3.img("/Users/ho/Git/KKLHY/아이템/아이템/p_it4.png")
p_item3 = p_it3.img("C:\\Users\\653dl\\KKLHY\\아이템\\p_it4.png")
p_item3_width, p_item3_height = p_it3.img_size(p_item2)  # 아이템의 가로, 세로 크기 설정
p_it3.x_pos, p_it3.y_pos = 1300, random.randint(0, screen_height - p_item3_height)  # 아이템 위치 설정(random)
p_it3.speed = 5
@@ -88,15 +88,15 @@ def show(self, k, a, b):
N_it1 = obj()
N_it2 = obj()
N_it3 = obj()
N_item1 = N_it1.img("/Users/ho/Git/KKLHY/아이템/아이템/n_it1.png")
N_item1 = N_it1.img("C:\\Users\\653dl\\KKLHY\\아이템\\n_it1.png")
N_item1_width, N_item1_height = N_it1.img_size(N_item1)  # 아이템의 가로, 세로 크기 설정
N_it1.x_pos, N_it1.y_pos = 1300, random.randint(0, screen_height - N_item1_height)  # 아이템 위치 설정(random)
N_it1.speed = 5
N_item2 = p_it1.img("/Users/ho/Git/KKLHY/아이템/아이템/n_it2.png")
N_item2 = p_it1.img("C:\\Users\\653dl\\KKLHY\\아이템\\n_it2.png")
N_item2_width, N_item2_height = N_it2.img_size(N_item2)  # 아이템의 가로, 세로 크기 설정
N_it2.x_pos, N_it2.y_pos = 1300, random.randint(0, screen_height - N_item2_height)  # 아이템 위치 설정(random)
N_it2.speed = 5
N_item3 = p_it1.img("/Users/ho/Git/KKLHY/아이템/아이템/n_it3.png")
N_item3 = p_it1.img("C:\\Users\\653dl\\KKLHY\\아이템\\n_it3.png")
N_item3_width, N_item3_height = N_it3.img_size(N_item3)  # 아이템의 가로, 세로 크기 설정
N_it3.x_pos, N_it3.y_pos = 1300, random.randint(0, screen_height - N_item3_height)  # 아이템 위치 설정(random)
N_it3.speed = 5


객체화 + 랜덤 수정 + 
