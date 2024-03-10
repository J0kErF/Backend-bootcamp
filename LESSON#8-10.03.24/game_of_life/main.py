from game import Game

def main():
    rows = 8
    cols = 8
    game = Game(rows, cols)
    game.populate_board()
    num_rounds = int(input("Enter number of rounds: "))
    game.run_simulation(num_rounds)
    print("Simulation complete!")


main() 