debug_flag = {
    'all': True,
    'image_manager': False,
    'parse_file': False,
    'note': False,
    'note-calc': False
   }


def print_console(name, content):
    if debug_flag[name]:
        print(name + " : " + content)


print_console('all', "Debug Layer Enable")