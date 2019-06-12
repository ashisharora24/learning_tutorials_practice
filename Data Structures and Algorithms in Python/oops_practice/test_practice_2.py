class UseProfile:
    count_number_of_profiles = 0

    def create_users(self, userid):
        UseProfile.count_number_of_profiles += 1
        #print("User profile created for : ", userid)

    def total_profile_created(self):
        print("total of ", UseProfile.count_number_of_profiles, " created.")


userid_list = ["a", "b", "c", "d"]
m = UseProfile()
for i in userid_list:
    m.create_users(i)
m.total_profile_created()

userid_list1 = ["a1", "1b", "c1", "d1"]
m1 = UseProfile()
for i1 in userid_list1:
    m1.create_users(i1)
m1.total_profile_created()
