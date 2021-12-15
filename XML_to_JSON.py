def convertToJson(contents):
   jid='"id": '
   jname='"name": '
   jposts='"posts": '
   jpost='"post": '
   jbody='"body": '
   jtopics='"topics": '
   jtopic='"topic": '
   jfollowers='"followers": '
   jfollower='"follower": '
   json_file='{\n  "users": {\n    "user": '
   json_indet="\n      " # 6 double spaces
   unit_indent="  "        # double space
   contents=contents.replace("  " ,"")                     # remove all double spaces Not space to keep the names separated     (Ahmed Ali NOT AhmedAli)
   contents=contents.replace("\n","")        
   user_list=contents.split("<user>")                      # split the file according to <user> to deal with single user at a time 
   user_list=user_list[1:]                                 # first element is not counted (<users>)
   if len(user_list)==1:                                   # for one user we put only { after user
      json_file+="{"
   else:                                                   # for more than one user we put [ after user
      json_file+="["

   for userx in user_list:                                 # loop through user_list to perform the body on each user       
      if len(user_list)>=2:                                # for more than one user , each user start {  
         json_file+=json_indet+"{"
         json_indet+=unit_indent
      post_list=userx.split("<post>")                      # make list of post to loop through
      follower_list=userx.split("<follower>")
      follower_list=follower_list[1:]                      # first element is not counted (all the string before first follower)

      id_name=post_list[0]                                 # id_name = post_list[0] =<id>1</id><name>Ahmed Ali</name><posts>
      index2=id_name.find("</id>")
      json_file+=json_indet+jid
      json_file +=id_name[4:index2]+","                    # len("<id>") = 4
      
      index1=id_name.find("<name>")
      index2=id_name.find("</name>")
      json_file+=json_indet+jname
      json_file +='"'+id_name[index1+6:index2]+'",'        # len("<name>") = 6
      
      json_file+=json_indet+jposts
      
      post_list=post_list[1:]                              # first element is not counted (<posts>)
      if(len(post_list)==0) :                              #empty post list
         json_file+="null"
      else:                                                # one or more (post)s
         json_file+="{"
         json_indet+=unit_indent
         json_file+=json_indet+jpost
         if len(post_list)==1:                             #  one post
            json_file+="{"
         else:                                             # two or more (post)s
            json_file+="["
            json_indet+=unit_indent
      
      for postx in post_list:                              #  uncomment this line
         if len(post_list)>=1:
            json_file+=json_indet+"{"
         json_indet+=unit_indent
         json_file+=json_indet+jbody
         index2=postx.find("</body>")
         json_file+='"'+postx[6:index2]+'",'               # len("<body>") = 6
         
         json_file+=json_indet+jtopics

         topic_list=postx.split("<topic>")
         topic_list=topic_list[1:]

         if(len(topic_list)==0) :                          # empty topic list
            json_file+="null"
         else:                                             # one or more (topic)s
            json_file+="{"
            json_indet+=unit_indent
            json_file+=json_indet+jtopic
            if len(topic_list)>=2:                         # two or more (topic)s
               json_file+="["
               json_indet+=unit_indent
         
         for topicx in topic_list:                         # uncomment this line
            index2=topicx.find("</topic>")
            if len(topic_list)==1:
               json_file+='"'+topicx[0:index2]+'",'            
            else:
               json_file+=json_indet+'"'+topicx[0:index2]+'",'
         json_file=json_file[:-1]
         if len(topic_list)>=2:                            # line 15 
            json_indet=json_indet[:-2]
            json_file+=json_indet+"]"
         if len(topic_list)>=1:                            # topics not null
            json_indet=json_indet[:-2]
            json_file+=json_indet+"}"                      # line 16 in json sample    close topics
         
         json_indet=json_indet[:-2]
         json_file+=json_indet+"},"                        # line 17
      json_file=json_file[:-1]                             # remove the comma after the last post block (last block is after post_list for loop) 
      if len(post_list)>=2:                                # line 24
         json_indet=json_indet[:-2]
         json_file+=json_indet+"]"
      
      if len(post_list)>=1:                                # posts not null
         json_indet=json_indet[:-2]
         json_file+=json_indet+"}"                         # line 25 the comma is exist in line 117

      json_file+=","+json_indet+jfollowers
      
      if(len(follower_list)==0) :                          # empty follower list
         json_file+="null"
      else:                                                # one or more (follower)s
         json_file+="{"
         json_indet+=unit_indent
         json_file+=json_indet+jfollower
         if len(follower_list)==1:                         # two or more (follower)s
            json_file+="{"
         else:
            json_file+="["
         json_indet+=unit_indent

      for followerx in follower_list:
         index2=followerx.find("</id>")
         if len(follower_list)==1:
            json_file+=json_indet+jid+followerx[4:index2]  # len("<id>") = 4
            json_indet=json_indet[:-2]
            json_file+=json_indet+"}"
         else:
            json_file+=json_indet+"{"
            json_file+=json_indet+unit_indent+jid+followerx[4:index2]     
            json_file+=json_indet+"},"
   
      if len(follower_list)>=2:
         json_file=json_file[:-1]                          # delete the comma added each loop (in else)
         json_indet=json_indet[:-2]
         json_file+=json_indet+"]"
      if len(follower_list)>=1:                            # followers not null
         json_indet=json_indet[:-2]
         json_file+=json_indet+"}"                         # close followers block

      json_indet=json_indet[:-2]
      json_file+=json_indet+"},"                           # close { of each user

   json_file=json_file[:-1]                                # delete the comma after user (for the last user)
   if len(user_list)>=2:
      json_indet=json_indet[:-2]
      json_file+=json_indet+"]"                            # close [  of user

   json_indet=json_indet[:-2]
   json_file+=json_indet+"}"                               # close {  of users

   json_indet=json_indet[:-2]
   json_file+=json_indet+"}"                               # close { at the start of the file

   return json_file
