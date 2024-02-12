import sys
from PyQt5 import QtWidgets
from counter import Counter


class MainWindow(QtWidgets.QMainWindow):
    """
    This class handles interaction and and drawing of the window.  
    """
    
    def __init__(self):
        
        super().__init__()
        
        
        self.horizontal = QtWidgets.QHBoxLayout() #Creating a horizontal layout to add widgets (view and button) next to each other
        
        self.setCentralWidget(QtWidgets.QWidget()) #QMainWindow must have a centralWidget to be able to add layouts
        self.centralWidget().setLayout(self.horizontal) #Setting the layout
        
        self.init_window()
        
        self.counter = Counter()
        self.scene.addItem(self.counter)
        
        self.init_button()
        
        
        
    def init_button(self):
        """
        Adds the button to the window and connects it to it's respective function
        See: QPushButton at https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QPushButton.html
        """
        
        self.counter_button = QtWidgets.QPushButton("Add +1")
        self.counter_button.clicked.connect(self.counter.add)
        self.horizontal.insertWidget(0,self.counter_button)
        
        
    def init_window(self):
        """
        Sets up the window.
        """
        
        self.setWindowTitle('Counter')
        self.setGeometry(500, 400, 500, 350) #Setting the size of the main window
        self.show()
        
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 100, 100) #Setting the size of the scene
        
        self.view = QtWidgets.QGraphicsView() #Creating a QGraphicsView-widget where the QGraphicsScene will be added

        """
        Missing line here.
        """
        

        self.view.show()
        
        self.horizontal.addWidget(self.view) #The QGraphicsView-widget is added to the horizontal layout
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) #Launch an instance of QApplication
    window = MainWindow()
    sys.exit(app.exec_()) #Start the Qt event loop