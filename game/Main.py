from CyberEscape.game.GameInitialization import *

pygame.mixer.music.load('resources/Music/power_bots.wav')
pygame.mixer.music.play(1000, 0.0)

def redraw_background(frame, bg_speed):
    game_window.blit(background[frame // bg_speed], (0, 0))
    for obj in objects:
        obj.draw(game_window)

collided_counter = 0
font = pygame.font.Font(None, 36)
while run:
    if game_over == True:
        pygame.quit()
        quit()
    redraw_background(frame_counter, bg_speed)
    for obj in objects:
        if obj.id != 0:
            if obj.collide(runner):
                print("Collided!")
                print(collided_counter)
                collided_counter+=1
                game_over = True
        obj.x -= 10
        if obj.x < obj.width * (-1):
            objects.pop(objects.index(obj))
    draw_runner()
    pygame.display.update()
    frame_counter += 1
    if frame_counter == 60 * bg_speed:
        frame_counter = 0
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
            pygame.quit()
            quit()
        if event.type == pygame.USEREVENT + 2:
            generator.obstacle = random.randrange(1,7)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                runner.jumping = True
            if event.key == pygame.K_DOWN:
                runner.sliding = True

