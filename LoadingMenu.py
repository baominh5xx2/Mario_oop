import pygame as pg

from const import *
from Text import Text

class LoadingMenu():
    """
    Class quản lý màn hình chờ của trò chơi.

    Thuộc tính:
        iTime (int): Thời gian hiện tại khi khởi tạo màn hình chờ.
        loadingType (bool): Kiểu tải hiện tại.
        bg (Surface): Bề mặt nền của màn hình chờ.
        text (Text): Đối tượng Text để hiển thị văn bản 'Loading...'.

    Phương thức:
        __init__(core): Khởi tạo màn hình chờ.
        update(core): Cập nhật trạng thái màn hình chờ.
        set_text_and_type(text, type): Thiết lập văn bản và kiểu tải.
        render(core): Vẽ màn hình chờ.
        update_time(): Cập nhật thời gian hiện tại.
    """
    def __init__(self, core):
        self.iTime = pg.time.get_ticks()
        self.loadingType = True
        self.bg = pg.Surface((WINDOW_W, WINDOW_H))
        self.text = Text('Loading...', 32, (WINDOW_W / 2, WINDOW_H / 2))

    def update(self, core):
        if pg.time.get_ticks() >= self.iTime + (5250 if not self.loadingType else 2500):
            if self.loadingType:
                core.oMM.currentGameState = 'Game'
            else:
                core.oMM.currentGameState = 'MainMenu'
            self.set_text_and_type('Loading...', True)

    def set_text_and_type(self, text, type):
        self.text = Text(text, 32, (WINDOW_W / 2, WINDOW_H / 2))
        self.loadingType = type

    def render(self, core):
        core.screen.blit(self.bg, (0, 0))
        self.text.render(core)

    def update_time(self):
        self.iTime = pg.time.get_ticks()

# File: Text.py
import pygame as pg

class Text():
    """
    Class quản lý việc hiển thị văn bản trong trò chơi.

    Thuộc tính:
        text (str): Nội dung văn bản.
        font_size (int): Kích thước phông chữ.
        pos (tuple): Vị trí hiển thị văn bản.
        font (Font): Phông chữ sử dụng để hiển thị văn bản.
        surface (Surface): Bề mặt chứa văn bản đã được render.

    Phương thức:
        __init__(text, font_size, pos): Khởi tạo đối tượng Text.
        render(core): Vẽ văn bản lên màn hình.
    """
    def __init__(self, text, font_size, pos):
        self.text = text
        self.font_size = font_size
        self.pos = pos
        self.font = pg.font.Font(None, font_size)
        self.surface = self.font.render(text, True, (255, 255, 255))

    def render(self, core):
        rect = self.surface.get_rect(center=self.pos)
        core.screen.blit(self.surface, rect)

# File: const.py
WINDOW_W = 800
WINDOW_H = 600
FPS = 60

# File: MenuManager.py
class MenuManager():
    """
    Class quản lý các menu trong trò chơi.

    Thuộc tính:
        core (Core): Đối tượng Core của trò chơi.
        currentGameState (str): Trạng thái trò chơi hiện tại.

    Phương thức:
        __init__(core): Khởi tạo đối tượng MenuManager.
        start_loading(): Bắt đầu màn hình chờ.
        update(core): Cập nhật trạng thái menu.
        render(core): Vẽ menu lên màn hình.
    """
    def __init__(self, core):
        self.core = core
        self.currentGameState = 'MainMenu'
        self.loadingMenu = LoadingMenu(core)

    def start_loading(self):
        self.currentGameState = 'Loading'
        self.loadingMenu.update_time()

    def update(self, core):
        if self.currentGameState == 'Loading':
            self.loadingMenu.update(core)
        # Các trạng thái khác sẽ được xử lý ở đây

    def render(self, core):
        if self.currentGameState == 'Loading':
            self.loadingMenu.render(core)
        # Các trạng thái khác sẽ được vẽ ở đây
