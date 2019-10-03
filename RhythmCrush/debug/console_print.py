debug_flag = {
    'all': True,
    'image_manager': True
   }


def print_console(name, content):
    if debug_flag[name]:
        print(name + " : " + content)


print_console('all', "Debug Layer Enable")