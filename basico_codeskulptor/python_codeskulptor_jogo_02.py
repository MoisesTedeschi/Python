import simplegui

largura = 600
altura = 400
pos_x = 200
pos_y = 200

def draw_handler(canvas):
    canvas.draw_circle([pos_x, pos_y], 10, 20, 'Red')


frame = simplegui.create_frame('Jogo', largura, altura)
frame.set_draw_handler(draw_handler)
frame.start()