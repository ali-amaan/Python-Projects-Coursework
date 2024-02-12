import sys
from PyQt5 import QtWidgets
from game import Game


class MainWindow(QtWidgets.QMainWindow):
    """
    This class handles interaction and and drawing of the game.  
    """

    def __init__(self):
        super().__init__()
        
        
        self.vertical = QtWidgets.QVBoxLayout() #Buttons will be added to a vertical layout
        self.horizontal = QtWidgets.QHBoxLayout() #Button column and the view will be added next to each other in a horizontal layout
        self.horizontal.insertLayout(0, self.vertical) #Vertical layout is added inside the horizontal layout so the buttons can be added on top of each other
        
        self.setCentralWidget(QtWidgets.QWidget()) #QMainWindown must have a centralWidget to be able to add layouts
        self.centralWidget().setLayout(self.horizontal) #Setting the layout
        
        self.init_window()
        
        self.game = Game(self.scene)
        
        self.init_buttons()

        
        
    def init_buttons(self):
        """
        Adds buttons to the window and connects them to their respective functions
        See: QPushButton at https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QPushButton.html
        """
        
        self.fish_button = QtWidgets.QPushButton("Fish")
        self.fish_button.clicked.connect(lambda: self.game.switch_item_type(0))
        self.vertical.addWidget(self.fish_button)
        
        self.bucket_button = QtWidgets.QPushButton("Bucket")
        self.bucket_button.clicked.connect(lambda: self.game.switch_item_type(1))
        self.vertical.addWidget(self.bucket_button)
        
        self.boot_button = QtWidgets.QPushButton("Boot")
        self.boot_button.clicked.connect(lambda: self.game.switch_item_type(2))
        self.vertical.addWidget(self.boot_button)
        
        self.clear_button = QtWidgets.QPushButton("Clear")
        self.clear_button.clicked.connect(self.game.clear_items)
        self.vertical.addWidget(self.clear_button)
        
        
    def init_window(self):
        """
        Sets up the window.
        """
        
        self.setWindowTitle('Ponds')
        self.setGeometry(500, 400, 450, 350) #Setting the size of the main window
        self.show()
        
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300) #Setting the size of the scene
        
        self.view = QtWidgets.QGraphicsView() #Creating a QGraphicsView-widget where the QGraphicsScene will be added
        self.view.setScene(self.scene) #Adding the scene to the QGraphicsView
        self.view.show()
        
        self.horizontal.addWidget(self.view) #The QGraphicsView-widget is added to the horizontal layout
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) #Launch an instance of QApplication
    window = MainWindow()
    sys.exit(app.exec_()) #Start the Qt event loop
