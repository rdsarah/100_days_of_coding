import colorgram, random
import turtle as t

# rgb_colors = []
# colors = colorgram.extract('day18_HirstPainting/hirst.jpg', 25)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

tur = t.Turtle()
t.colormode(255)
tur.speed("fastest")
tur.hideturtle()

def hirst():
    for i in range(10):
        tur.penup()
        tur.goto(-250, -200 + i*50)
        for i in range(10):
            tur.penup()
            tur.dot(20, random.choice(color_list))
            tur.forward(50)
            tur.pendown()
    
hirst()
t.Screen()
t.exitonclick()
