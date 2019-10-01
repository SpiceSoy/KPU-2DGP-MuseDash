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
    soy_debug.print_console('image_manager',f"Load Image {tag} at {image_url_dic[tag]} .")
    return pico2d.load_image(image_base_dir_url + image_url_dic[tag])


if __name__ =="__main__":
    pico2d.open_canvas()
    test_image = load_image('note-back-big')
    while True:
        events = pico2d.get_events()
        pico2d.clear_canvas()
        for evs in events:
            if evs.key == 27:
                exit()
        test_image.draw(100,100)
        pico2d.update_canvas()
        pico2d.delay(1/100)
        pass
