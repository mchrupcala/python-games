import arcade
GAME_WIDTH = 600
GAME_HEIGHT = 600
arcade.open_window(GAME_WIDTH, GAME_HEIGHT, "A day at the beach")

arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()

x = 300
y = 100
width = 600
height = 200

arcade.draw_rectangle_filled(x, y, width, height, arcade.color.SAND)

x = 380
y = 140
radius = 20

arcade.draw_circle_filled(x, y, radius, arcade.color.RED)

x = 40
y = 580
radius = 60

arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

arcade.finish_render()

arcade.run()
