class F1:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.member = {}
        self.wins = 0
    

class Team(F1):
    def __init__(self, name, color):
        super().__init__(name, color)
    
    def add_player(self, name, wins):
        self.wins += wins
        self.member[name] = wins
        
    def remove_player(self, name):
        self.wins -= self.member[name]
        self.member.pop(name)


ferrari = Team("Ferrari", "Red")

ferrari.add_player("Carlos", 2)
ferrari.add_player("Charles", 5)

ferrari.remove_player("Carlos")

ferrari.add_player("Lewis", 105)

print(ferrari.wins)