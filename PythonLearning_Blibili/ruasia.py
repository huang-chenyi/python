import pygame
import random

# 初始化pygame
pygame.init()

# 定义颜色
colors = [
    (0, 0, 0),
    (255, 85, 85),
    (100, 200, 115),
    (120, 108, 245),
    (255, 140, 50),
    (50, 150, 216),
    (146, 202, 73),
    (150, 161, 218)
]

# 创建游戏窗口
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('俄罗斯方块')

clock = pygame.time.Clock()
snake_block = 30

# 方块形状
shapes = [
    [[1, 1, 1, 1]],
    [[1, 1],
     [1, 1]],
    [[0, 1, 0],
     [1, 1, 1]],
    [[1, 0, 0],
     [1, 1, 1]],
    [[0, 0, 1],
     [1, 1, 1]],
    [[1, 1, 0],
     [0, 1, 1]],
    [[0, 1, 1],
     [1, 1, 0]]
]

# 游戏循环
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    shape = random.choice(shapes)
    color = random.choice(colors)

    while not game_over:

        while game_close:
            dis.fill(colors[0])
            font_style = pygame.font.SysFont("bahnschrift", 25)
            mesg = font_style.render("你输了! 按Q-退出 或者 C-继续", True, colors[1])
            dis.blit(mesg, [dis_width / 6, dis_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(colors[0])
        for i in range(len(shape)):
            for j in range(len(shape[0])):
                if shape[i][j]:
                    pygame.draw.rect(dis, color, [x1 + j*snake_block, y1 + i*snake_block, snake_block, snake_block])

        pygame.display.update()

        clock.tick(10)

    pygame.quit()
    quit()

gameLoop()