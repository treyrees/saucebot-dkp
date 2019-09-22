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
                    loaded_player = Player(player['id'],player['name'],player['nick'],player['dkp'])
                    result.append(loaded_player)
                print('Loaded successfully')
                return result
        except(IOError,IndexError):
            print('Failed to load')
            
    def save_players(self):
        with open(self.filepath,'w') as f:
            nplayers = []
            for player in self.players:
                player_dict = player.__dict__
                nplayers.append(player_dict)
            if nplayers != []:
                json.dump(nplayers,f)
    
    def add_player(self,id,name,nick,dkp=0):
        new_player = Player(id,name,nick,dkp)
        self.players.append(new_player)
        self.save_players()
        return self
        
    def find_player(self,id):
        if  (isinstance(id, str)) and (id[2] == '!'):
            id = id[:2]+id[3:]
        elif (isinstance(id, str)):
            id = id
        else:
            id = ('<@'+str(id)+'>')
        for player in self.players:
            if player.id == id:
                return player
        return False