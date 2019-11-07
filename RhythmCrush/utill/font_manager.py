import pico2d
import enum


class FontType(enum.Enum):
    NanumSquare = 0
    NexonLv1 = 1
    NexonLv2 = 2
    NexonFootball = 3
    Fixedsys = 4


class FontStyle(enum.Enum):
    Regular = 0
    Bold = 1


class FontManager:
    font_dir = {
        (FontType.NanumSquare, FontStyle.Regular): "Resource/Font/NanumSquareR.ttf",
        (FontType.NanumSquare, FontStyle.Bold): "Resource/Font/NanumSquareB.ttf",
        (FontType.NexonLv1, FontStyle.Regular): "Resource/Font/NEXONLv1GothicRegular.ttf",
        (FontType.NexonLv1, FontStyle.Bold): "Resource/Font/NEXONLv1GothicBold.ttf",
        (FontType.NexonLv2, FontStyle.Regular): "Resource/Font/NEXON Lv2 Gothic.ttf",
        (FontType.NexonLv2, FontStyle.Bold): "Resource/Font/NEXON Lv2 Gothic Bold.ttf",
        (FontType.NexonFootball, FontStyle.Regular): "Resource/Font/NEXONFootballGothicL.ttf",
        (FontType.NexonFootball, FontStyle.Bold): "Resource/Font/NEXONFootballGothicL.ttf",
        (FontType.Fixedsys, FontStyle.Regular): "Resource/Font/fixedsys.ttf",
        (FontType.Fixedsys, FontStyle.Bold): "Resource/Font/fixedsys.ttf",
    }
    loaded_font = {}

    @staticmethod
    def load(type: FontType, style: FontStyle, size: int):
        if (type, style, size) not in FontManager.loaded_font:
            FontManager.loaded_font[(type, style, size)] = pico2d.Font(FontManager.font_dir[(type, style)], size)
        return FontManager.loaded_font[(type, style, size)]