from graphics import *
def main():
		win = GraphWin('Link', 400, 400)
		win.yUp()
		
		aline = Line(Point(100, 100), Point(200, 100)) # bottom of left triangle
	
		aline.setWidth(3)
		aline.draw(win)
		
		bline = Line(Point(100, 100), Point(150, 200)) # left face of bottom left
		bline.setWidth(3)
		bline.draw(win)
		
		cline = Line(Point(150, 200), Point(200, 100)) # top corner of bottom left triangle
		cline.setWidth(3)
		cline.draw(win)
		
		dline = Line(Point(150, 200), Point(200, 300)) # set endpoints
		dline.setWidth(3)
		dline.draw(win)
		
		eline = Line(Point(150, 200), Point(250, 200)) # set endpoints
		eline.setWidth(3)
		eline.draw(win)
		
		fline = Line(Point(200, 300), Point(250, 200)) # set endpoints
		fline.setWidth(3)
		fline.draw(win)
		
		gline = Line(Point(250, 200), Point(300, 100)) # set endpoints
		gline.setWidth(3)
		gline.draw(win)
		
		hline = Line(Point(300, 100), Point(200, 100)) # set endpoints
		hline.setWidth(3)
		hline.draw(win)
		
		fline = Line(Point(200, 100), Point(250, 200)) # set endpoints
		fline.setWidth(3)
		fline.draw(win)
		
		message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
		message.draw(win)
		win.getMouse()
		win.close()	
main()
