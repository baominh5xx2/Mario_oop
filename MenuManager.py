import pygame as pg

from LoadingMenu import LoadingMenu
from MainMenu import MainMenu

class MenuManager():
    """
    Lớp này cho phép dễ dàng quản lý các trạng thái của trò chơi. Tùy thuộc vào tình huống,
    nó sẽ cập nhật và vẽ các thành phần khác nhau.

    Thuộc tính:
        currentGameState (str): Trạng thái hiện tại của trò chơi (ví dụ: 'MainMenu', 'Loading', 'Game').
        oMainMenu (MainMenu): Đối tượng quản lý màn hình chính.
        oLoadingMenu (LoadingMenu): Đối tượng quản lý màn hình chờ.

    Phương thức:
        __init__(core): Khởi tạo đối tượng MenuManager, thiết lập trạng thái ban đầu và các menu.
        update(core): Cập nhật trạng thái của trò chơi dựa trên trạng thái hiện tại.
        render(core): Vẽ các thành phần của trò chơi dựa trên trạng thái hiện tại.
        start_loading(): Bắt đầu trạng thái 'Loading' và cập nhật thời gian bắt đầu.
    """
    def __init__(self, core):
        self.currentGameState = 'MainMenu'

        self.oMainMenu = MainMenu()
        self.oLoadingMenu = LoadingMenu(core)

    def update(self, core):
        if self.currentGameState == 'MainMenu':
            pass
        elif self.currentGameState == 'Loading':
            self.oLoadingMenu.update(core)
        elif self.currentGameState == 'Game':
            core.get_map().update(core)

    def render(self, core):
        if self.currentGameState == 'MainMenu':
            core.screen.fill((0, 0, 0))  
            self.oMainMenu.render(core)
        elif self.currentGameState == 'Loading':
            self.oLoadingMenu.render(core)
        elif self.currentGameState == 'Game':
            core.get_map().render(core)
            core.get_map().get_ui().render(core)
        pg.display.update()

    def start_loading(self):
        self.currentGameState = 'Loading'
        self.oLoadingMenu.update_time()
