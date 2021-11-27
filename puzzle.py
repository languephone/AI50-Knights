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
    Or( # A says "We are both knaves."
        And(AKnight, AKnave, BKnave), # If A is a knight then A & B are knaves
        And(AKnave, Or(Not(AKnave), Not(BKnave))), # If A is a knave then A & B are not both knaves 
    )
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave), # A is a knight or a knave
    Or(BKnight, BKnave), # B is a knight or a knave
    Not(And(AKnight, AKnave)), # A is not both a knight and a knave
    Not(And(BKnight, BKnave)), # B is not both a knight and a knave

    # A says "We are the same kind."
    Implication(AKnight, BKnight), # If A is a knight, then b is the same kind (knight)
    Implication(AKnave, Not(BKnave)), # If A is a knave, then b is not the same kind (knave)
    # B says "We are of different kinds."
    Implication(BKnight, AKnave),
    Implication(BKnave, Not(AKnight)),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave), # A is a knight or a knave
    Or(BKnight, BKnave), # B is a knight or a knave
    Or(CKnight, CKnave), # C is a knight or a knave
    Not(And(AKnight, AKnave)), # A is not both a knight and a knave
    Not(And(BKnight, BKnave)), # B is not both a knight and a knave
    Not(And(CKnight, CKnave)), # C is not both a knight and a knave
    Or( # A says either "I am a knight." or "I am a knave.", but you don't know which.
        Or(And(AKnight, Or(AKnight, AKnave))), # A is a knight and says either "I am a knight." or "I am a knave."
        Or(And(AKnave, Or(Not(AKnight), Not(AKnave)))),
    ),
    Or(
        And(BKnight, AKnight, BKnave), # B is a knight and A is a knight and B says "A said 'I am a knave'."
        And(BKnight, AKnave, Not(BKnave)), # B is a knight and A is a knave and B says "A said 'I am a knave'."
        And(BKnave, AKnight, Not(BKnave)), # B is a knave and A is a knight and B says "A said 'I am a knave'."
        And(BKnave, AKnave, Not(Not(BKnave))), # B is a knave and  A is a knave and B says "A said 'I am a knave'."
    ),
    Or(
        And(BKnight, CKnave), # B is a knight and says "C is a knave."
        And(BKnave, Not(CKnave)), # B is a knave and says "C is a knave."
    ),
    Or(
        And(CKnight, AKnight), # C is a knight and says "A is a knight."
        And(CKnave, Not(AKnight)), # C is a knave and says "A is a knight."
    ),
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
