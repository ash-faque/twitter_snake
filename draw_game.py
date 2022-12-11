from PIL import Image, ImageDraw

# game drawer
def draw_game(apple, snake):

    game_bord_width = 1000
    game_board_bg = (30, 30, 50)

    game_board_size = 10
    game_cell_size = (game_bord_width / game_board_size)

    # init new image
    game = Image.new('RGB', (game_bord_width, game_bord_width), game_board_bg)
    draw = ImageDraw.Draw(game)

    # draw background
    for i in range(game_board_size):
        i+=1
        draw.line((0, (i * game_cell_size), game_bord_width, (i * game_cell_size)), fill=(200, 200, 200), width=1)
        draw.line(((i * game_cell_size), 0, (i * game_cell_size), game_bord_width), fill=(200, 200, 200), width=1)

    # drwa aple 
    draw.rectangle((apple[0] * game_cell_size + 10, apple[1] * game_cell_size + 10, apple[0] * game_cell_size + game_cell_size - 10, apple[1] * game_cell_size + game_cell_size - 10), fill=(255, 0, 0))

    # draw snake
    for count, (x, y) in enumerate(snake):
        count += 10
        if count >= 30: count = 30
        draw.rectangle((x * game_cell_size + count, y * game_cell_size + count, x * game_cell_size + game_cell_size - count, y * game_cell_size + game_cell_size - count), fill=(0, 180, 0))

    # save img
    game.save('game.jpg', quality=95)
