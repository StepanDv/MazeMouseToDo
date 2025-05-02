import settings
import pygame
from maze import Maze
from tasks import tasks
from ui import events
from ui import graphics
from ui import screen
from maze import mice
from maze import cheese


FPS = 60
running = True
clock = events.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('freesansbold.ttf', 30)
text1 = font.render("Левой кнопкой мыши нажмите в место, где хотите, чтобы появилась мышь.", True, (255, 0, 0))
text2 = font.render("Правой кнопкой мыши нажмите в место, где хотите, чтобы появился сыр.", True, (255, 0, 0))
text3 = font2.render("Мышь нашла сыр!", True, (255, 0, 0))

while running:
    for event in events.get_event_queue():
        if tasks.handle_event(event):
            continue
        if event.type == events.QUIT:
           running = False
        if event.type == events.MOUSEBUTTONDOWN:

            if event.button == 1:
                Maze.add_mouse((event.pos[0] - settings.view_left_top[0]) / settings.tile_size[0], (event.pos[1] - settings.view_left_top[1]) / settings.tile_size[1])

            if event.button == 3:
                Maze.add_cheese((event.pos[0] - settings.view_left_top[0]) / settings.tile_size[0], (event.pos[1] - settings.view_left_top[1]) / settings.tile_size[1])

    graphics.fill("black")

    # рисуем лабиринт
    Maze.draw()
    if Maze.mouse and Maze.mouse.check():
        screen.blit(text3, (270, 80))
    else:
        screen.blit(text1, (65, 70))
        screen.blit(text2, (65, 100))
    tasks.check_tasks()
    graphics.flip()
    clock.tick(FPS)
    # обновляем весь лабиринт
    Maze.update(1 / FPS)
