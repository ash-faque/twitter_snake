from draw_game import draw_game

apple = ()
snake = [()]
turn_to = 0





# get diresction from insta
def get_direction():

    # get likes and retweets of old tweet
    
    likes, retweets = 0, 0

    global turn_to

    if likes > retweets:

        turn_to = -1

    elif retweets > likes:

        turn_to = +1

    else:
        turn_to = 0 

################################


# recalculate the snake n apple
def recalculate():

    global apple, snake

    apple = ()
    snake = [()]


################################




# post game
def post_game():
    instagram = 0


################################




# get_snake()
# get_direction()
# recalculate()
# draw_game()
# post_game()