class User:
    members = set()
    def __init__(self, name):
        self.name = name
    def sign_up(self):
        self.members.add(self.name)

# Change the code above so that the following lines work:
# 

sarah = User('sarah')
heather = User('heather')
cristina = User('cristina')
print(User.members)  # set()
heather.sign_up()
cristina.sign_up()
print(User.members)  # {'heather', 'cristina'}