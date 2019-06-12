from game.GameInitialization import *
from game.fingers import *
import pygameMenu
from pygameMenu.locals import *

pygame.mixer.music.load('../resources/Music/power_bots.wav')
pygame.mixer.music.play(1000, 0.0)

def redraw_background():
    game_window.blit(background[frame_counter // bg_speed], (0, 0))
    for obj in objects:
        obj.draw(game_window)

menu_flag = True

def toggle_menu_flag():
    print("Dupa")
    global menu_flag
    menu_flag = not menu_flag
    print(menu_flag)

collided_counter = 0
font = pygame.font.Font(None, 72)

first_run = 1
pygame.display.update()
menu = pygameMenu.Menu(game_window, *get_screen_size(), pygameMenu.fonts.FONT_8BIT, "Menu", dopause=False, menu_width=800)
menu.add_option("Start", toggle_menu_flag)
menu.add_option("Kalibracja kamery", lambda : print("Kalibracja"))

# print(tuple(map(lambda x: x/2, get_screen_size())))

while run:
    if menu_flag:
        events = pygame.event.get()
        menu.mainloop(events)
        redraw_background()
        menu.draw()
        pygame.display.update()
    #--------------------------------------
    else:
        if first_run:
            draw_init_objects()
            generator.start()
            first_run = 0
        (grabbed, frame) = camera.read()
        frame = imutils.resize(frame, width=700)
        frame = cv.flip(frame, 1)
        clone = frame.copy()
        roi = frame[top:bottom, right:left]
        gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (7, 7), 0)
        if num_frames < 30:
            find_run_avg(gray, aWeight)
        else:
            hand = segment(gray)
            if hand is not None:
                (thresholded, segmented) = hand
                cv.drawContours(clone, [segmented + (right, top)], -1, (0, 0, 255))
                fingers = count_fingers(thresholded, segmented)
                cv.putText(clone, str(fingers), (70, 45), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)
        num_frames += 1
        cv.imshow("Video Feed", clone)
        #--------------------------------------------
        if game_over == True:
            game_over_text = font.render("Game Over", True, (255, 0, 0))
            game_window.fill((0,0,0))
            game_window.blit(game_over_text, dest=tuple(map(lambda x: x/2, get_screen_size())))
            pygame.display.update()
            time.sleep(3)
            #camera.release()
            cv.destroyAllWindows()
            pygame.quit()
            quit()
        redraw_background()
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
        clock.tick(speed)
        if fingers == 2:
            if before_fingers == 2:
                finger_times_counter+=1
            else:
                finger_times_counter = 0
            before_fingers = 2
        elif fingers == 3:
            if before_fingers == 3:
                finger_times_counter+=1
            else:
                finger_times_counter = 0
            before_fingers = 3
        if finger_times_counter >= 10:
            if fingers == 2:
                runner.longer_jumping = True
                finger_times_counter = 0
            if fingers == 3:
                runner.sliding = True
                finger_times_counter = 0
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
    frame_counter += 1
    if frame_counter == 60 * bg_speed:
        frame_counter = 0
#camera.release()
cv.destroyAllWindows()
