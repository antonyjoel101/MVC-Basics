from model import createfile
from view import user_input1, user_input2,display
filename_c=user_input1()
content_c=user_input2()

obj1=createfile(filename_c,content_c)
obj1.create()
obj1.write()
result_c=obj1.read()
display(result_c)




