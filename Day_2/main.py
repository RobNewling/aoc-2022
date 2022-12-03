class Player:
    score = 0
    planned_moves = []
    turn_outcomes = [] # (play, outcome)

    def add_move(self, move):
        self.planned_moves.append(move)

class Game:
    opponent_player = Player()
    my_player = Player()
    num_of_turns = 0

    def add_moves(self, player1, player2):
        self.opponent_player.add_move(player1)
        self.my_player.add_move(player2)
        self.num_of_turns += 1

    def play_turns(self):
        for turn in range(self.num_of_turns):
            opponent_move = self.opponent_player.planned_moves[turn]
            my_move = self.my_player.planned_moves[turn]

    def game_logic(self, p1_move, p2_move):
        # paper > rock > scissors > paper
        if p1_move == 'paper':
            if p2_move == 'paper':
                return 'draw'
            if p2_move == 'rock':
                return 'p1 wins'
            if p2_move == 'scissors':
                return 'p2 wins'

    def translate_move(self, input):
        return 'todo'


def process_input(filename):
    game = Game()

    with open(filename, 'r') as input_file:
        for line in input_file:
            game.add_moves(*line.split())


if __name__ == '__main__':
    process_input('input.txt')
