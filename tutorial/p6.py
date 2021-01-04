#context mangaers
# file = open ("test.txt","w")
# try :## use try and except such that the file closes properly even with errors.
#     file.write("Hello ")
# finally:
#     file.close()
# the above is same as
# with open("test.txt","w") as file:
#     file.write("Hello")
    # exit()
class File:
    def __init__(self, filename,method):
        self.file=open(filename,method)
    def __enter__(self):
        print("Enter")
        return self.file
    def __exit__(self,type,value,traceback):## the exception part
        print ("Exit")
        print(f"{type} - {value} - {traceback} ")
        self.file.close()
        return True # we gracefully handled the excpetion no crash
# with File("tutorial/test.txt","w") as f:
#     print("Middle")
    # f.write("hello")
from contextlib import contextmanager
@contextmanager # you could use this to do memorylock think deadlock

def file_non_class (filename,method):
    print("Enter")
    file=open(filename,method)
    yield file
    file.close()
    print("Exit")
with file_non_class("tutorial/test.txt","w") as f:
    print("Middle")
    f.write("hello")
    # raise Exception()
