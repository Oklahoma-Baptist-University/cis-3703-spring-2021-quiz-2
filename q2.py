import graphics
import math

def q2_graphic():
    win = graphics.GraphWin("Quiz 2", 500, 500)
    
    pt1 = win.getMouse()
    pt2 = win.getMouse()
    pt3 = win.getMouse()
    
    
    circ = graphics.Circle(pt1, 20)
    circ.setFill("red")
    circ.draw(win)
    
    square = graphics.Rectangle(graphics.Point(pt2.getX() - 10, pt2.getY() - 10), 
                                graphics.Point(pt2.getX() + 10, pt2.getY() + 10))
    square.setFill("blue")
    square.draw(win)
    
    l1 = graphics.Line(pt1, pt2)
    l1.draw(win)
    lengthText = graphics.Text(l1.getCenter(), "Length = " + str(math.sqrt((pt2.getX()-pt1.getX()) ** 2 + (pt2.getY() - pt1.getY()) ** 2)))
    lengthText.draw(win)

    
    l2 = graphics.Line(pt2, pt3)
    l2.draw(win)
    lengthText = graphics.Text(l2.getCenter(), "Length = " + str(math.sqrt((pt3.getX()-pt2.getX()) ** 2 + (pt3.getY() - pt2.getY()) ** 2)))
    lengthText.draw(win)
    
    l3 = graphics.Line(pt3, pt1)
    l3.draw(win)
    lengthText = graphics.Text(l3.getCenter(), "Length = " + str(math.sqrt((pt3.getX()-pt1.getX()) ** 2 + (pt3.getY() - pt1.getY()) ** 2)))
    lengthText.draw(win)
    