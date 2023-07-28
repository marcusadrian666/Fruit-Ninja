import pygame
import random
import sys

pygame.init()

# 游戏窗口尺寸
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Ninja")

# 颜色定义
WHITE = (255, 255, 255)

# 水果定义
fruits = ['apple', 'orange', 'banana', 'watermelon', 'grape', 'strawberry']
fruit_images = {fruit: pygame.image.load(f'images/{fruit}.png') for fruit in fruits}
fruit_rects = {fruit: fruit_images[fruit].get_rect() for fruit in fruits}

# 炸弹定义
bomb_image = pygame.image.load('images/bomb.png')
bomb_rect = bomb_image.get_rect()

# 游戏参数
score = 0
font = pygame.font.SysFont(None, 36)

def get_random_object():
    objects = fruits + ['bomb']
    return random.choice(objects)

def display_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, (10, 10))

def game_over():
    game_over_text = font.render("Game Over!", True, WHITE)
    window.blit(game_over_text, (WIDTH // 2 - 60, HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def main():
    global score
    clock = pygame.time.Clock()
    object_type = get_random_object()
    object_x, object_y = WIDTH // 2, HEIGHT
    object_speed = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if object_rect.collidepoint(mouse_x, mouse_y):
                    if object_type == 'bomb':
                        game_over()
                    else:
                        score += 1
                    object_type = get_random_object()
                    object_x, object_y = WIDTH // 2, HEIGHT

        window.fill((0, 0, 0))
        display_score()

        object_y -= object_speed
        if object_type == 'bomb':
            window.blit(bomb_image, (object_x - bomb_rect.width // 2, object_y))
            object_rect = bomb_rect
        else:
            window.blit(fruit_images[object_type], (object_x - fruit_rects[object_type].width // 2, object_y))
            object_rect = fruit_rects[object_type]
        
        if object_y < -object_rect.height:
            game_over()
            score = 0
            object_type = get_random_object()
            object_x, object_y = WIDTH // 2, HEIGHT

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
