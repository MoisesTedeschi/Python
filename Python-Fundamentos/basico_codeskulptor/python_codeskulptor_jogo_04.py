import simplegui
import random

largura = 600
altura = 400
pos_x = 200
pos_y = 200
tempo = 1000
score = 0

def timer_handler():
    global pos_x, pos_y
    pos_x = random.randint(0, largura)
    pos_y = random.randint(0, altura)
    

def mouse_handler(position):
    pass
    

def draw_handler(canvas):
    canvas.draw_circle([pos_x, pos_y], 10, 20, 'Red')


frame = simplegui.create_frame('Jogo', largura, altura)
label_score = frame.add_label('Score: ' + str(score))
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(mouse_handler)
frame.start()

timer = simplegui.create_timer(tempo, timer_handler)
timer.start()