import copy
import pico2d
from RhythmCrush import debug
from ..component.image_controller import *
from . import ResourceData

debug.print_console('image_manager', "Init")


# 동기적 작업
def load_image(tag):
    if tag in ResourceData.image_url_dic:
        if ResourceData.image_url_dic[tag] in ResourceData.image_cache:
            debug.print_console('image_manager', f"Load Image {tag} at Cache .")
            ret_image = ResourceData.image_cache[ResourceData.image_url_dic[tag]]
        else:
            complete_url = ResourceData.image_base_dir_url + ResourceData.image_url_dic[tag]
            debug.print_console('image_manager', f"Load Image {tag} at {complete_url} .")
            ret_image = pico2d.load_image(complete_url)
            ResourceData.image_cache[ResourceData.image_url_dic[tag]] = ret_image
        return ret_image
    else:
        debug.print_console('image_manager', f"Image Dic has NOT Image {tag}")


def load_animator(tag):
    if tag in ResourceData.animators:
        return copy.copy(ResourceData.animators[tag])
    else:
        return None


def get_image_controller(tag, randomize_csr=False, randomize_time=False):
    result = ImageController(load_image(tag))
    result.add_animator(load_animator(tag))
    if randomize_csr:
        result.animator.randomize_frame_csr()
    if randomize_time:
        result.animator.randomize_frame_time()
    return result
