import json
from player import Player

class Players:
    def __init__(self, filepath):
        self.filepath = filepath
        
    def load_players(self):
        try:
            with open(self.filepath,'r') as f:
                players = json.load(f)
                result = []
                for player in players:
                    loaded_player = Player(player['id'],player['name'],player['dkp'])
                    result.append(loaded_player)
                return result
        except(IOError,IndexError):
            print('Failed to load')
            
    def save_players(self):
        with open(self.filepath,'w') as f:
            nplayers: []
            for player in self.players:
                player_dict = player.__dict__
                nplayers.append(player_dict)
            json.dump(nplayers,f)
    
    def add_player(self,id,name,dkp):
        new_player = Player(id,name,dkp)
        self.users.append(new_user)
        self.save_players
        return self