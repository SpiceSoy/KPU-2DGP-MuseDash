import pico2d
import soy_debug

image_base_dir_url = "Resource/Image/"

image_url_dic =  {
        'note-back-big' : "Note/taikobigcircle.png",
        'note-front-big' : "Note/taikobigcircleoverlay.png",
        'note-back' : "Note/taikohitcircle.png",
        'note-front' : "Note/taikohitcircleoverlay.png",
    }

soy_debug.print_console('image_manager',"Image Manager Init")

def load_image(tag):
    complete_url = image_base_dir_url + image_url_dic[tag]
    soy_debug.print_console('image_manager',f"Load Image {tag} at {complete_url} .")
    return pico2d.load_image(complete_url)
