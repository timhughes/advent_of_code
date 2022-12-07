from enum import IntEnum

class Result(IntEnum):
    Win = 6
    Draw = 3
    Lose = 0

class Move(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3
    
winners = {
    Move.Rock: Move.Scissors,
    Move.Paper: Move.Rock,
    Move.Scissors: Move.Paper,
}

elf_decoder = {
    "A": Move.Rock,
    "B": Move.Paper,
    "C": Move.Scissors,
}
us_decoder = {
    "X": Move.Rock,
    "Y": Move.Paper,
    "Z": Move.Scissors,
}

q1 = "What would your total score be if everything goes exactly according to your strategy guide?"
def score(elf, us):
    elf_move = elf_decoder[elf]
    us_move = us_decoder[us]
    
    if elf_move == us_move:
        return Result.Draw + us_move
    elif elf_move == winners[us_move]:
        return Result.Win + us_move
    else:
        return Result.Lose + us_move
        
    
with open("./input_day02") as fh:
    data = [line.split() for line in fh]

print("%s : %s" % (q1, sum([score(*moves) for moves in data])))



q2 = (
    "Following the Elf's instructions for the second column, what "
    "would your total score be if everything goes exactly according to your strategy guide?"
)
desired_decoder = {
    "X": Result.Lose,
    "Y": Result.Draw,
    "Z": Result.Win,
}


def score2(elf, desired):
    elf_move = elf_decoder[elf]
    desired_result = desired_decoder[desired]
    
    if desired_result == Result.Draw:
        return elf_move + Result.Draw
    elif desired_result == Result.Lose:
        return winners[elf_move] + Result.Lose
    else:
        return winners[winners[elf_move]] + Result.Win
    
print("%s : %s" % (q2, sum([score2(*moves) for moves in data])))
