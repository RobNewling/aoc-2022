class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.planned_moves = []
        self.round_outcomes = []  # (play, outcome, round score)

    def add_move(self, move):
        self.planned_moves.append(move)

    def add_round_outcome(self, play, outcome):
        # play = 'rock', 'paper', 'scissors'
        # outcome = 'win', 'lose', 'draw'
        score = self.round_score(play, outcome)
        self.round_outcomes.append((play, outcome, score))
        #print(self.round_outcomes)
        self.total_score += score
        #print(self.total_score)

    def round_score(self, play, outcome):
        score = 0
        match play:
            # play = 'rock', 'paper', 'scissors'
            case 'rock':
                score += 1
            case 'paper':
                score += 2
            case 'scissors':
                score += 3

        match outcome:
            # outcome = 'win', 'lose', 'draw'
            case 'lose':
                pass # 0 score
            case 'draw':
                score += 3
            case 'win':
                score += 6

        return score


class Game:
    opponent_player = Player('opponent')
    my_player = Player('me')
    num_of_turns = 0

    def game_final_report(self):
        print('Game over!')
        print('Total rounds played: ' + str(self.num_of_turns))
        print('Opponent score: ' + str(self.opponent_player.total_score))
        print('Your score: ' + str(self.my_player.total_score))

    def add_moves(self, player1, player2):
        self.opponent_player.add_move(player1)
        self.my_player.add_move(player2)
        self.num_of_turns += 1

    def play_rounds(self):
        for turn in range(self.num_of_turns):
            opponent_move = self.translate_move(self.opponent_player.planned_moves[turn])
            desired_outcome = self.translate_outcome(self.my_player.planned_moves[turn])
            my_move = self.calcualte_move_for_desired_result(opponent_move, desired_outcome)

            match self.game_logic(opponent_move, my_move):
                case 'draw':
                    self.opponent_player.add_round_outcome(opponent_move, 'draw')
                    self.my_player.add_round_outcome(my_move, 'draw')
                case 'p1 wins':
                    self.opponent_player.add_round_outcome(opponent_move, 'win')
                    self.my_player.add_round_outcome(my_move, 'lose')
                case 'p2 wins':
                    self.opponent_player.add_round_outcome(opponent_move, 'lose')
                    self.my_player.add_round_outcome(my_move, 'win')


    def game_logic(self, p1_move, p2_move):
        # paper > rock > scissors > paper
        outcomes = ['draw', 'p1 wins', 'p2 wins']
        if p1_move == 'paper':
            if p2_move == 'paper':
                return outcomes[0]
            if p2_move == 'rock':
                return outcomes[1]
            if p2_move == 'scissors':
                return outcomes[2]
        if p1_move == 'rock':
            if p2_move == 'paper':
                return outcomes[2]
            if p2_move == 'rock':
                return outcomes[0]
            if p2_move == 'scissors':
                return outcomes[1]
        if p1_move == 'scissors':
            if p2_move == 'paper':
                return outcomes[1]
            if p2_move == 'rock':
                return outcomes[2]
            if p2_move == 'scissors':
                return outcomes[0]

    def translate_move(self, encrypted_move):
        match encrypted_move:
            case 'A' | 'X':
                return 'rock'
            case 'B' | 'Y':
                return 'paper'
            case 'C' | 'Z':
                return 'scissors'

    def translate_outcome(self, encrypted_outcome):
        match encrypted_outcome:
            case 'X':
                return 'lose'
            case 'Y':
                return 'draw'
            case 'Z':
                return 'win'

    def calcualte_move_for_desired_result(self, opponent_move, desired_result):
        move_list = ['paper', 'rock', 'scissors']
        opponent_index = move_list.index(opponent_move)
        match desired_result:
            case 'lose':
                return move_list[(opponent_index + 1) % 3]
            case 'draw':
                return move_list[opponent_index]
            case 'win':
                return move_list[(opponent_index - 1) % 3]


def process_input(filename):
    game = Game()

    with open(filename, 'r') as input_file:
        for line in input_file:
            game.add_moves(*line.split())

    game.play_rounds()
    game.game_final_report()


if __name__ == '__main__':
    process_input('input.txt')
