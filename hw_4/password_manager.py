Passwords= ["Bibi","Tuleugalieva","Asylbekovna","Bibi23"]

class Password_manager:
    def __init__(self, exist_password):
        self.exist_password = Passwords

    def get_password(self):
        return Passwords[-1]

    def set_password(self):
        new_password =(input("New Password: " ))
        if new_password in Passwords:
            return "Choose new password"
        else:
            Passwords.append(new_password)
            return "New Password added.",Passwords[-1]

    def is_correct(self,pinkod):
        if pinkod == self.exist_password[-1]:
            return True
        else:
            return False

check  = Password_manager(Passwords)


print(check.is_correct("Bibi23"))
