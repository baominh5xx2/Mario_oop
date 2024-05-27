from os import environ

import pygame as pg
from pygame.locals import *

from const import *
from MenuManager import MenuManager

class Core():
    """
    Lớp chính cho ứng dụng trò chơi Mario.

    Lớp này khởi tạo và quản lý vòng lặp chính của trò chơi, xử lý các sự kiện đầu vào,
    cập nhật trạng thái trò chơi và vẽ màn hình trò chơi. Đây là thành phần cốt lõi
    kết hợp các phần khác nhau của trò chơi, bao gồm hiển thị, âm thanh và quản lý menu.

    Thuộc tính:
        screen (Surface): Màn hình chính nơi trò chơi được vẽ.
        clock (Clock): Đối tượng Clock để giúp kiểm soát tốc độ khung hình của trò chơi.
        oMM (MenuManager): Một instance của lớp MenuManager để quản lý các menu của trò chơi.
        run (bool): Cờ để kiểm soát vòng lặp chính của trò chơi.

    Phương thức:
        __init__(): Khởi tạo trò chơi, bao gồm thiết lập hiển thị, âm thanh và quản lý menu.
        main_loop(): Vòng lặp chính của trò chơi, xử lý đầu vào, cập nhật và vẽ.
        input(): Xử lý các sự kiện đầu vào của người dùng.
        update(): Cập nhật trạng thái trò chơi.
        render(): Vẽ màn hình trò chơi.
    """
    def __init__(self):
        environ['SDL_VIDEO_CENTERED'] = '1'
        pg.mixer.pre_init(44100, -16, 2, 1024)
        pg.init()
        pg.display.set_caption('Mario Game')
        pg.display.set_mode((WINDOW_W, WINDOW_H))

        self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H))
        self.clock = pg.time.Clock()

        self.oMM = MenuManager(self)

        self.run = True

    def main_loop(self):
        while self.run:
            self.input()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def input(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False
            elif e.type == KEYDOWN:
                if e.key == K_RETURN:
                    self.oMM.start_loading()

    def update(self):
        self.oMM.update(self)

    def render(self):
        self.oMM.render(self)

