import turtle 
wn = turtle.Screen()


graph = turtle.Turtle()
graph.hideturtle() 
graph.speed(0) 

graph.forward(250)
graph.penup()
graph.goto(250,5)
graph.write('x',font=('Cambria',12,'italic'))
graph.goto(0,0)
graph.pendown()
graph.backward(250)
graph.forward(250)


graph.left(90)
graph.forward(250)
graph.penup()
graph.goto(5,250)
graph.write('y',font=('Cambria',12,'italic'))
graph.goto(0,0)
graph.pendown()
graph.backward(250)
graph.forward(250)

def f(x):
    '''f(x) -> float
    generic function to be graphed'''
    return x**2

def decrease_to_fit(zoom):
    '''decrease_to_fit(zoom) -> tup
    decreases x to fit the graph'''
    minX = -250/zoom
    maxX = 250/zoom
    
    while abs(f(minX)) > 250/zoom:
        minX += 0.5/zoom
    
    while f(maxX) > 250/zoom:
        maxX -= 0.5/zoom
    
    return (minX,maxX)
    
def graph_function(t,zoom=10):
    '''graph_function(t,zoom) -> none
    draws the graph of a function using turtle t
    and is zoomed in to zoom'''
    t.pensize(2)
    
    x,maxX = decrease_to_fit(zoom)
    t.penup()
    t.goto(x*zoom,f(x)*zoom)
    t.pendown()
    
    while x <= maxX:
        x += 0.01
        t.goto(x*zoom,f(x)*zoom)

graph_function(graph,100)
        
wn.mainloop()

