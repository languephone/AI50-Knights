from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave), # A is a knight or a knave
    Not(And(AKnight, AKnave)), # A is not both a knight and a knave
    Or(
        And(AKnight, And(AKnight, AKnave)), # If A is a knight, then A is both knight and knave
        And(AKnave, Not(And(AKnight, AKnave))) # If A is a knave, then A is not both a knight and knave
    ), 
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave), # A is a knight or a knave
    Or(BKnight, BKnave), # B is a knight or a knave
    Not(And(AKnight, AKnave)), # A is not both a knight and a knave
    Not(And(BKnight, BKnave)), # B is not both a knight and a knave
    Or(
        And(AKnight, AKnave, BKnave), # If A is a knight then A & B are knaves
        And(AKnave, Or(Not(AKnave), Not(BKnave))), # If A is a knave then A & B are not both knaves 
    )
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
