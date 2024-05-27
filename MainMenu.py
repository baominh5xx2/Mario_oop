import pygame as pg

from const import *
from Text import Text

class MainMenu():
    """
    Class quản lý màn hình chính của trò chơi.

    Thuộc tính:
        mainImage (Surface): Hình ảnh chính của màn hình chính.
        toStartText (Text): Văn bản hiển thị yêu cầu người chơi nhấn ENTER để bắt đầu trò chơi.

    Phương thức:
        __init__(): Khởi tạo màn hình chính, tải hình ảnh chính và thiết lập văn bản hướng dẫn.
        render(core): Vẽ màn hình chính, bao gồm hình ảnh chính và văn bản hướng dẫn lên màn hình trò chơi.
    """
    def __init__(self):
        self.mainImage = pg.image.load(r'images\super_mario_bros.png').convert_alpha()
        self.toStartText = Text('Press ENTER to start', 16, (WINDOW_W - WINDOW_W * 0.72, WINDOW_H - WINDOW_H * 0.3))

    def render(self, core):
        core.screen.blit(self.mainImage, (50, 50))
        self.toStartText.render(core)
