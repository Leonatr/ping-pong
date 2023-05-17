from pygame import *

#создай окно игры

window = display.set_mode((700, 500))
display.set_caption("Лабиринт")
background = transform.scale(image.load("gray.jpg"), (700, 500))
game = True

clock = time.Clock()
fps = 60
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        
        self.rect.x += self.speed
        self.rect.y += self.speed
        if  self.rect.y < 0 or self.rect.y > 450:
            self.speed *= -1
    
win_width = 700
win_height = 500
speed_x = 4
speed_y = 4
ball = Enemy('BALL1.png', 250, 250,3)
platform1 = Player('platform.png', -30, 250, 5)
platform2 = Player('platform.png', 670, 250, 5)
font.init()
font = font.Font(None, 50)
win1 = font.render('Игрок справа победил!', True, (255, 215, 0))
win2 = font.render('Игрок слева победил!', True, (255, 215, 0))
while game == True:
    window.blit(background, (0,0))
    ball.reset()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.y < 0 or ball.rect.y > 440:
        speed_y *= -1
    if sprite.collide_rect(platform1, ball) or sprite.collide_rect(platform2, ball):
        speed_x *= -1
    
    platform1.reset()
    platform1.update1()
    platform2.reset()
    platform2.update2()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if ball.rect.x < 0:
        window.blit(win1, (185, 250))
    if ball.rect.x > 700:
        window.blit(win2, (190, 250))
            
    
    clock.tick(fps)
    display.update()