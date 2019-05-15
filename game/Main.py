from CyberEscape.game.GameInitialization import *

#pygame.mixer.music.load('resources/Music/power_bots.wav')
#pygame.mixer.music.play(1000, 0.0)

def redraw_background(frame, bg_speed):
    game_window.blit(background[frame // bg_speed], (0, 0))
    for obj in objects:
        obj.draw(game_window)


while run:
    redraw_background(frame_counter, bg_speed)
    for obj in objects:
        if obj.id != 0:
            if obj.collide(runner):
                print("Collided!")
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
            generator.obstacle = random.randrange(3,4)

