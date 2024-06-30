import sys
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)

print("Initializing Game Assets. Please Wait...")

import GameScreens.StartMenu as StartMenu

# calls start menu 
window = StartMenu.StartMenu()
window.setWindowTitle("Gothic Swine")

sys.exit(app.exec())