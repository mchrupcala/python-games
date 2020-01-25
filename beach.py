import arcade

#CONSTANTS
GAME_WIDTH = 600
GAME_HEIGHT = 600
SCREEN_TITLE = "A day at the beach"


def draw_background():

    x = 300
    y = 100
    width = 600
    height = 200
    arcade.draw_rectangle_filled(x, y, width, height, arcade.color.SAND)

    x = 40
    y = 580
    radius = 60
    arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)


def draw_objects():
    x = 380
    y = 140
    radius = 20

    arcade.draw_circle_filled(x, y, radius, arcade.color.RED)

def draw_bird(x, y):
    arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(x+40, y, 20, 20, arcade.color.BLACK, 90, 180)

def main():

    arcade.open_window(GAME_WIDTH, GAME_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.SKY_BLUE)

    arcade.start_render()
    
    draw_background()
    draw_objects()
    draw_bird(420, 520)
    draw_bird(470, 550)

    arcade.finish_render()

    arcade.run()

if __name__ == "__main__":
    main()