class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def display(self):
        pass

class Image(File):
    def __init__(self, name,size):
        self.name = name
        self.size = size

class User:
    def __init__(self, username,password):
        self.username = username
        self.password = password
    def post(self, thread, content):
        pass
    def login():
        pass
    def make_thread(self, title, content):
        pass

class Moderator(User):
    def __init__(self, username,password):
        self.username = username
        self.password = password
    def edit(self, post, content):
        pass
    def delete(self, thread, post):
        pass

class Post:
    def __init__(self, user,time_posted, content):
        self.user=user
        self.time_posted=time_posted
        self.content=content
    def display(self):
        pass

class FilePost(Post):
    def __init__(self, user,time_posted, content, file):
        self.user=user
        self.time_posted=time_posted
        self.content=content
        self.file=file

class Thread:
    def __init__(self, title):
        self.title=title
