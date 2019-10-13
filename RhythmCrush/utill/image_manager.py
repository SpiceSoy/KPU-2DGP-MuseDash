import pico2d
from RhythmCrush import debug

image_base_dir_url = "Resource/Image/"

image_url_dic = {
        'note-back-big': "Note/taikobigcircle.png",
        'note-front-big': "Note/taikobigcircleoverlay.png",
        'note-back': "Note/taikohitcircle.png",
        'note-front': "Note/taikohitcircleoverlay.png",
        'player-trex': "Char/t_rex_sprite.png"
    }

image_cache = {}

debug.print_console('image_manager', "Init")


# 동기적 작업
def load_image(tag):
    if tag in image_url_dic:
        if tag in image_cache:
            debug.print_console('image_manager', f"Load Image {tag} at Cache .")
            ret_image = image_cache[tag]
        else:
            complete_url = image_base_dir_url + image_url_dic[tag]
            debug.print_console('image_manager', f"Load Image {tag} at {complete_url} .")
            ret_image = pico2d.load_image(complete_url)
            image_cache[tag] = ret_image
        return ret_image
    else:
        debug.print_console('image_manager', f"Image Dic has NOT Image {tag}")
