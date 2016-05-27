import simplegui
import random
import math

largura = 600
altura = 400
pos_x = 200
pos_y = 200
tempo = 3000
score = 0
raio = 10

def timer_handler():
    global pos_x, pos_y
    pos_x = random.randint(0, largura)
    pos_y = random.randint(0, altura)
    

def mouse_handler(position):
    global score
    
    dist = math.sqrt((pos_x - position[0]) ** 2 + (pos_y - position[1])**2)
    
    # atualiza score
    if dist <= raio:
        score = score + 1
    else:
        if score > 0:
            score = score - 1
    

def draw_handler(canvas):
    label_score.set_text('Score: ' + str(score))
    canvas.draw_circle([pos_x, pos_y], raio, 20, 'Red')


frame = simplegui.create_frame('Jogo', largura, altura)
label_score = frame.add_label('Score: ' + str(score))
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(mouse_handler)
frame.start()

timer = simplegui.create_timer(tempo, timer_handler)
timer.start()