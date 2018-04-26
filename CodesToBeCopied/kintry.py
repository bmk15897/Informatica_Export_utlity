import Tkinter as tk
import tkMessageBox
def show_alert(a):
	root = tk.Tk()
	root.withdraw()
	tkMessageBox.showwarning('Export of '+ a, 'Export file has been created. Please edit the excel.')