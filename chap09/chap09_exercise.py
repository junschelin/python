from user import User

class Admin(User):
    def __init__(self, privileges, first, last):
        super().__init__(first, last)
        self.privileges = privileges
    
    def show_privileges(self):
        print(self.privileges)

new_admin = Admin('can delete post', '존', '박')

new_admin.show_privileges()
new_admin.greet_user()