from game.GameInitialization import *
import pygameMenu
from game.GroundGenerator import *
from pygameMenu.locals import *

pygame.mixer.music.load('../resources/Music/power_bots.wav')
pygame.mixer.music.play(1000, 0.0)


def redraw_background():
    global frame_counter
    frame_counter += 1
    if frame_counter == 60 * bg_speed:
        frame_counter = 0
    game_window.blit(background[frame_counter // bg_speed], (0, 0))
    for obj in objects:
        obj.draw(game_window)


menu_flag = True


def toggle_menu_flag():
    global menu_flag
    menu_flag = not menu_flag
    return PYGAME_MENU_BACK


collided_counter = 0
font = pygame.font.Font(None, 72)


def game():
    global num_frames, collided_counter, before_fingers, finger_times_counter, fingers, objects
    game_over = False
    # print(objects)
    objects = []
    draw_init_objects(objects)
    generator = GroundGenerator(objects, screen_height)
    generator.start()
    while True:
        (grabbed, frame) = camera.read()
        frame = imutils.resize(frame, width=700)
        frame = cv.flip(frame, 1)
        clone = frame.copy()
        roi = frame[top:bottom, right:left]
        gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (7, 7), 0)
        hand = segment(gray)
        if hand is not None:
            (thresholded, segmented) = hand
            cv.drawContours(clone, [segmented + (right, top)], -1, (0, 0, 255))
            fingers = count_fingers(thresholded, segmented)
            cv.putText(clone, str(fingers), (70, 45), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)
        num_frames += 1
        cv.namedWindow("Video Feed", cv.WINDOW_NORMAL)
        cv.imshow("Video Feed", clone)
        cv.resizeWindow("Video Feed", 400, 300)
        # --------------------------------------------
        if game_over == True:
            game_over_text = font.render("Game Over", True, (255, 0, 0))
            game_window.fill((0, 0, 0))
            game_window.blit(game_over_text, dest=tuple(map(lambda x: x / 2, get_screen_size())))
            pygame.display.update()
            time.sleep(4)
            # camera.release()
            # cv.destroyAllWindows()
            # pygame.quit()
            # quit()
            break
        redraw_background()
        for obj in objects:
            if obj.id != 0:
                if obj.collide(runner):
                    print("Collided!")
                    print(collided_counter)
                    collided_counter += 1
                    game_over = True
            obj.x -= 10
            if obj.x < obj.width * (-1):
                objects.pop(objects.index(obj))
        draw_runner()
        pygame.display.update()
        clock.tick(speed)
        if fingers == 2:
            if before_fingers == 2:
                finger_times_counter += 1
            else:
                finger_times_counter = 0
            before_fingers = 2
        elif fingers == 3:
            if before_fingers == 3:
                finger_times_counter += 1
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
            if event.type == pygame.USEREVENT + 2:
                generator.obstacle = random.randrange(1, 7)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    runner.jumping = True
                if event.key == pygame.K_DOWN:
                    runner.sliding = True
    generator.stop()


def calibrate():
    for _ in range(30):
        (grabbed, frame) = camera.read()
        frame = imutils.resize(frame, width=700)
        frame = cv.flip(frame, 1)
        clone = frame.copy()
        roi = frame[top:bottom, right:left]
        gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (7, 7), 0)
        find_run_avg(gray, aWeight)
        cv.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)
        cv.namedWindow("Video Feed", cv.WINDOW_NORMAL)
        cv.imshow("Video Feed", clone)
        cv.resizeWindow("Video Feed", 400, 300)
    print("Calibrated")


menu = pygameMenu.Menu(game_window, *get_screen_size(), pygameMenu.fonts.FONT_8BIT, "Menu", bgfun=redraw_background,
                       menu_width=800)
menu.add_option("Start", game)
menu.add_option("Kalibracja kamery", calibrate)
menu.add_option("Wyjscie", PYGAME_MENU_EXIT)

redraw_background()
pygame.display.update()
calibrate()
events = pygame.event.get()
menu.mainloop(events)

cv.destroyAllWindows()
