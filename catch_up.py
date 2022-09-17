from pygame import *
x1 = 233
x2 = 466
y2 = 250
y1 = 250
clock = time.Clock()
window = display.set_mode((700,500))
display.set_caption("Доганялки")
background = transform.scale(image.load("background.png"),(700,500))
sprite2 = transform.scale(image.load("sprite2.png"),(100,100))
sprite1 = transform.scale(image.load("sprite1.png"),(100,100))
game = True
while game:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))

    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP]:
        y2 -= 5
    if keys_pressed[K_DOWN]:
        y2 += 5
    if keys_pressed[K_RIGHT]:
        x2 += 5
    if keys_pressed[K_LEFT]:
        x2 -= 5 
    if keys_pressed[K_w]:
        y1 -= 5
    if keys_pressed[K_s]:
        y1 += 5
    if keys_pressed[K_d]:
        x1 += 5
    if keys_pressed[K_a]:
        x1 -= 5
    if keys_pressed[K_UP] and y2 < 10:
        y2 += 5
    if keys_pressed[K_w] and y1 < 10:
        y1 += 5
    if keys_pressed[K_DOWN] and y2 > 400:
        y2 -= 5
    if keys_pressed[K_s] and y1 > 400:
        y1 -= 5
    if keys_pressed[K_RIGHT] and x2 > 599:
        x2 -= 5
    if keys_pressed[K_LEFT] and x2 < 10:
        x2 += 5
    if keys_pressed[K_d] and x1 > 599:
        x1 -= 5
    if keys_pressed[K_a] and x1 < 10:
        x1 += 5
    
    clock.tick(60)
    display.update()
