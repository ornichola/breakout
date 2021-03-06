import colors

background_image = 'images/background.jpg'
ball_color = colors.GREEN
ball_radius = 8
ball_speed = 3
brick_width = 60
brick_height = 20
brick_color = colors.RED1
button_hover_back_color = colors.INDIANRED2
button_normal_back_color = colors.INDIANRED1
button_pressed_back_color = colors.INDIANRED3
button_text_color = colors.WHITE
font_name = 'Arial'
font_size = 20
frame_rate = 90
effect_duration = 20
initial_lives = 3
lives_right_offset = 85
menu_button_h = 50
menu_button_w = 80
menu_offset_x = 20
menu_offset_y = 300
message_duration = 2
offset_y = brick_height + 10
paddle_width = 80
paddle_height = 20
paddle_color = colors.ALICEBLUE
paddle_speed = 6
row_count = 6
score_offset = 5
screen_width = 800
screen_height = 600
sounds_effects = dict(
    brick_hit='sound_effects/brick_hit.wav',
    effect_done='sound_effects/effect_done.wav',
    paddle_hit='sound_effects/paddle_hit.wav',
    level_complete='sound_effects/level_complete.wav',
)
status_offset_y = 5
text_color = colors.YELLOW1

lives_offset = screen_width - lives_right_offset
