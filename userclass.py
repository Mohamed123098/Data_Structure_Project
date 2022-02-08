class user():
    count=0
    __name=""
    __posts=[]
    __followers=0
    def __init__(self):
        user.count +=1
        self.__id=user.count
        
        
    
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getPosts(self):
        return self.__posts
    
    def getFollowers(self):
        return self.__followers
    
    def setId(self,id):
        self.__id=id 
    
    def setName(self,name):
        self.__name=name 
    
    def setPosts(self,post):
        self.__posts.append(post)
    
    def setFollowers(self,followers):
        self.__followers=followers

class node():
    def __init__(self,data):
        self.data=data
        self.next=None
    def setNext(self,next):
        self.next=next

# t=user()
# q=user()
# i=user()
# t.setName("pert")
# t.setPosts("weed")
# print(t.__posts)
# print(q.getId())
# print(i.getId())