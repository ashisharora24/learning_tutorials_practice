class Module:

    def __str__(self):
        return "This is Module class, where we take care of all the modules info"

    def __init__(self):
        self.module_name = module_name

    def check_if_module_already_exist(self):
        path="./module_name_list/"+self.module_name+".txt"
        import os,sys
        if os.path.isfile(path):
            return True
        return False

class Module_Run_Utitlity(Module):
    def __init__(self,module_name):
        super().__init__(module_name)


M=Module_Run_Utitlity("Run_Utitlity")
print(M.check_if_module_already_exist())
