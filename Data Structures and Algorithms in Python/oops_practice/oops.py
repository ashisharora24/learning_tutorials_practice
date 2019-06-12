import os,sys
class TOPS:
    pass

class UserProfile(TOPS):
    def __init__(self,user_id):
        self.user_id=user_id
    def create_user_id(self,username,email_id):
        os.mkdir("./UserProfile/"+self.user_id)
        f=open("./UserProfile/"+self.user_id+"/password.txt",'w')
        f.write("tops@123")
        f.close()
        f=open("./UserProfile/"+self.user_id+"/username.txt",'w')
        f.write(username)
        f.close()
        f=open("./UserProfile/"+self.user_id+"/email_id.txt",'w')
        f.write(email_id)
        f.close()

    def credential_verification(self,password):
        self.__password=password


class Module(TOPS):

    loading_counts=1

    def __str__(self):
        return "This is Module class, where we take care of all the modules info"

    def __init__(self,module_name,user_id):
        self.module_name=module_name
        self.user_id=user_id

    def check_if_module_already_exist(self):
        if os.path.isfile("./module_name_list/"+self.module_name+".txt"):
            return True
        return False

    def create_new_module(self):
        f=open("./module_name_list/"+self.module_name+".txt",'w')

    def loading_count(self):
        Module.loading_counts+=1


class Module_Run_Utitlity(Module):

    def __init__(self):
        super().__init__("Run_Utitlity")

    def load_details(self):
        self.loading_count()



print("*******************************************************")
print("******Welcome to Command Prompt version of TOPS********")
print("*******************************************************")

print("Do you want to login to TOPS")
print("Press 1 for login to TOPS")
print("Press 2 for create New user for TOPS")
user_input = int(input("Please enter your response : "))
if user_input==1:
    pass
elif user_input==2:
    li=["user_id","username","email_id"]
    user_input=[]
    for i in li:
        user_input.append(input("please enter the "+i+" : "))
    print("The details entered are as follows : ",*user_input)
    m = UserProfile(user_input[0])
    m.create_user_id(user_input[1],user_input[2])
else:
    pass
