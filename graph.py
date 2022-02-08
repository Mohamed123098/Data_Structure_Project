from userclass import user,node


def imp_graph(user_list):
    users_classes=[None]
    user_list=user_list.replace("  " ,"")                     # remove all double spaces Not space to keep the names separated     (Ahmed Ali NOT AhmedAli)
    user_list=user_list.replace("\n","")        
    user_list=user_list.split("<user>")                      # split the file according to <user> to deal with single user at a time 
    user_list=user_list[1:]
    
    for userx in user_list:
        users_classes.append([user(),None])    # array of users first element is a class contains user's data 

        post_list=userx.split("<post>")                      # make list of post to loop through
        post_list=post_list[1:]
        follower_list=userx.split("<follower>")
        follower_list=follower_list[1:]                      # first element is not counted (all the string before first follower)


        # set user name
        index1=userx.find("<name>")
        index2=userx.find("</name>")
        users_classes[-1][0].setName(userx[index1+6:index2])

        for postx in post_list:
            # extract the body of the post and store it in a dictionary
            index2=postx.find("</body>")
            postforclass={"body":postx[6:index2]}

            topic_list=postx.split("<topic>")
            topic_list=topic_list[1:]

            # make list contains all the topics
            topicforclass=[]
            for topicx in topic_list:
                index2=topicx.find("</topic>")
                topicforclass.append(topicx[0:index2])
            
            # store the list of topics in the dictionary
            # pass the dictionary to the class to be stored 
            postforclass["topix"]=topicforclass
            users_classes[-1][0].setPosts(postforclass)
    
        # make list of the followers ids 
        follower_ids=[]
        if(follower_list==0):
            users_classes[-1].setFollowers([None,None])
        else:
            for followerx in follower_list:
                index2=followerx.find("</id>")
                follower_ids.append(followerx[4:index2])

            # pass the list to be stored in the class
            users_classes[-1][0].setFollowers(follower_ids) 

            # make adjacency list it's head is the sceond element in the users_classes 
            p1=node(follower_ids[0])
            if(len(follower_ids)>1):
                p2=node(follower_ids[1])
                p1.setNext(p2)
                for id in follower_ids[2:]:
                    p=node(id-1)
                    p.setNext(id)
            users_classes[-1][1]=p1



    








#     for uc,p in users_classes[1:]:
#         print("\n\n")
#         print(uc.getId())
#         print(uc.getName())
#         print(uc.getPosts())
#         print(uc.getFollowers())
#         for i in range(len(uc.getFollowers())):
#             print(p.data)
#             p=p.next
     


# with open("D:/David/Data Structures and Algorithms/project/sample.xml",encoding='utf-8') as f:
#     XML_contents=f.read()

# imp_graph(XML_contents)


