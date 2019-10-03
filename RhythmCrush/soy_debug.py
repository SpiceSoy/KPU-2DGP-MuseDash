debug_flag = {
    'all' : True,
    'image_manager' : True 
   }

def print_console(name,str):
    if debug_flag[name] == True :
        print (name + " : " + str)

print_console('all',"Debug Layer Enable")