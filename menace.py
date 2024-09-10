from xoxo import Game,Player,GameOver

# To Add - argparse



def main():
    # instantiate the game
    g = Game()


    # instantiate a player
    x=Player('x',g)

    # instantiate a player
    o=Player('o',g)

    i = 0
    while i < 9:

        # loop unil complete
        try:
            x.move()
            i+=1
            o.move()
            i+=1
        except ValueError as e:
            print("ERROR",e)
        except GameOver as e:
            print("Complete",e)
            g.show()
            exit()

if __name__ == '__main__':
    main()