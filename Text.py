import pygame as pg

class Text():
    """
    Lớp này quản lý việc hiển thị văn bản trong trò chơi.

    Thuộc tính:
        font (Font): Phông chữ sử dụng để hiển thị văn bản.
        text (Surface): Bề mặt chứa văn bản đã được render.
        rect (Rect): Hình chữ nhật bao quanh văn bản để xác định vị trí hiển thị.

    Phương thức:
        __init__(text, fontsize, position, textcolor=(255, 255, 255)): Khởi tạo đối tượng Text với văn bản, kích thước phông chữ, vị trí và màu sắc văn bản.
        render(core): Vẽ văn bản lên màn hình trò chơi.
    """
    def __init__(self, text, fontsize, position, textcolor=(255, 255, 255)):
        self.font = pg.font.Font('fonts/emulogic.ttf', fontsize)
        self.text = self.font.render(text, False, textcolor)
        self.rect = self.text.get_rect(center=position)

    def render(self, core):
        core.screen.blit(self.text, self.rect)
