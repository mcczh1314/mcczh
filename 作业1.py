import os,re
path="C:/Users/86740/Desktop/Python学习/第一阶段作业/task"
dirs=os.listdir(path)
for filename in dirs:
            txt=""
            file=open("C:/Users/86740/Desktop/Python学习/第一阶段作业/task/"+filename,"r" )            
            file_content=file.readlines()
            file.close()
            for line in file_content:
                        for character in line:
                                    if(character.isdigit()):
                                                character=character.replace(character,"")
                                    txt=txt+character
            
            print(txt)
            file=open("C:/Users/86740/Desktop/Python学习/第一阶段作业/task/"+filename,"w")
            file.write(txt)
            file.close()
