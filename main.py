# Generates a SELF funding application document
# Written by Gavin Grubert
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# This function gets the folder of the event
def pickEventFolder():
    baseDir = os.path.dirname(os.path.abspath(__file__))
    eventsDir = os.path.join(baseDir, "events")

    if not os.path.isdir(eventsDir):
        messagebox.showerror("Error", f"Events folder not found:\n{eventsDir}")
        return

    folderPath = filedialog.askdirectory(
        initialdir=eventsDir,
        title="Select Event Folder"
    )

    if folderPath:
        selectedPathVar.set(folderPath)

# Runs the script to generate the self document
def runProgram():
    folderPath = selectedPathVar.get()

    if folderPath == "No folder selected":
        messagebox.showwarning("Missing Folder", "Please select an event folder first.")
        return

    # Close the Tkinter window
    root.destroy()

    # Path to the script you want to run
    scriptPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "self.py")

    # Run the script with the folder path as an argument
    subprocess.run(["python", scriptPath, folderPath])

# UI Setup
root = tk.Tk()
root.title("Auto-GG")
root.geometry("400x250")
root.configure(bg="#F5F5F5")
root.resizable(False, False)

# Styles
style = ttk.Style()
style.theme_use('clam')

style.configure("TButton",
                font=("Segoe UI", 11, "bold"),
                foreground="white",
                background="#4CAF50",
                padding=4)
style.map("TButton",
          background=[("active", "#45A049")])

style.configure("TLabel",
                font=("Segoe UI", 10),
                background="#F5F5F5",
                foreground="#333333")

selectedPathVar = tk.StringVar(value="No folder selected")

# Layout
main_frame = tk.Frame(root, bg="#F5F5F5")
main_frame.pack(padx=20, pady=20)

titleLabel = ttk.Label(main_frame, text="Auto-GG", font=("Segoe UI", 16, "bold"))
titleLabel.pack(pady=(0, 10))
authorLabel = ttk.Label(main_frame, text="Created by Gavin Grubert")
authorLabel.pack(pady=(0, 15))

openButton = ttk.Button(main_frame, text="Select Event Folder", command=pickEventFolder)
openButton.pack(pady=(0, 10))

pathLabel = ttk.Label(main_frame, textvariable=selectedPathVar, wraplength=360, justify="left")
pathLabel.pack(pady=(0, 15))

goButton = ttk.Button(main_frame, text="Go", command=runProgram)
goButton.pack(pady=(0, 10))

root.mainloop()