class Game:
    def __init__(self, title):
        self.title = title
        
    @property
    def title(self):
        return self._title 
    
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title) > 0 and not hasattr(self,'_title'):
            self._title=new_title
        else:
            print('title must be string > 0 chars')

    def results(self):
        result_list = []
        for result in Result.all:
            if result.game is self:
                result_list.append(result)
        return result_list

    def players(self):
        pass

    def average_score(self, player):
        pass

class Player:
    def __init__(self, username):
        self.username = username
        
    @property
    def username(self):
        return self._username
        
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2<=len(new_username)<=16:
            self._username = new_username
        else:
            print('error username')

    def results(self):
        result_list = []
        for result in Result.all:
            if result.player is self:
                result_list.append(result)
        return result_list

    def games_played(self):
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

class Result:
    all = []
    
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if hasattr(self, '_score'):
            print('score has already been set')
            return
        
        if not isinstance(new_score, int):
            print('score must be int')
            return
        
        if not 1 <= new_score <=5000:
            print('score must be between 1 and 5000')
            return
        
        self._score = new_score
        
        @property
        def player(self):
            return self._player
        
        @player.setter
        def player(self, new_player):
            if isinstance(new_player, Player):
                self._player = new_player
            else:
                print('invalid player')
                
        @property
        def game(self):
            return self._game
        
        @game.setter
        def game(self, new_game):
            if isinstance(new_game, Game):
                self._game = new_game
            else:
                print('invalid game')
                
        def __repr__(self) -> str:
            return f'<Result {self.score}, {self.game.title}, {self.player.username}>'