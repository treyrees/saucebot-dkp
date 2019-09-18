import json
from player import Player

class Players:
    def __init__(self, filepath):
        self.filepath = filepath
        
    def load_players(self):
        ##try:
            with open(self.filepath,'r') as f:
                players = json.load(f)
                result = []
                for player in players:
                    loaded_player = Player(player['id'],player['name'],player['dkp'])
                    result.append(loaded_player)
                print('Loaded successfully')
                return result
        ##except(IOError,IndexError):
        ##    print('Failed to load')
            
    def save_players(self):
        with open(self.filepath,'w') as f:
            nplayers: []
            for player in self.players:
                player_dict = player.__dict__
                nplayers.append(player_dict)
            json.dump(nplayers,f)
    
    def add_player(self,id,name,dkp=0):
        new_player = Player(id,name,dkp)
        self.players.append(new_player)
        ##self.save_players()
        return self
        
    def find_player(self,authorid):
        if str(authorid)[:2] == '<@':
            authorid = str(authorid)[2:-1]
        found = False
        for player in self.players:
            if player.id == ('<@'+str(authorid)+'>'):
                found = True
                break
        if found:
            return player
        else:
            return False
            
    def list_players(self):
        for player in self.players.players:
            print(str(player))