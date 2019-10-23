"""
# Build A Python GUI App Tutorial - Chaverri Davi`s / 20 hours ago
# Not that good example; - http://bit.ly/2PcNpL1
"""
# In todays episode we are going to take a look on how we can build out
# a python gui app. In todays era of improving our workflow, we are going to
# build an app that lets us auto open up a bunch of other apps that we would
# normally use. You can imagine it as being a workspace opener.
# If you want to learn more about python or you are a python beginner this is
# a great tutorial for you to build out some practical apps.
#
# All the code will be available on patreon.

import os
import tkinter as tk

from tkinter import filedialog, Text
from assets.config import dir_results

print(__doc__)

apps = []
root = tk.Tk()

filename_save = dir_results + "run_app_gui.txt"

# 화일이 존재하면 읽어온다.
if os.path.isfile(filename_save):
    with open(filename_save, 'r') as f:
        temp_apps = f.read()
        temp_apps = temp_apps.split(",")
        apps = [app for app in temp_apps if app is not ' ']


canvas = tk.Canvas(master=root, height=400, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(master=root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


def main():
    button_openfile = tk.Button(master=root,
            text="Open File", padx=10,
            pady=5, fg="white", bg="#263D42",
            command=add_apps,
        )
    button_openfile.pack()

    button_runapps = tk.Button(master=root,
            text="Run Apps",
            padx=10, pady=5, fg="white", bg="#263D42",
            command=run_apps,
        )
    button_runapps.pack()
    root.mainloop()

    # 종료(끝나면)되면 실행목록을 기록한다
    with open(filename_save, 'w') as f:
        for app in apps:
            f.write(app + ', ')

def add_apps():
    for widget in frame.winfo_children():
        widget.destroy()

    file_name = filedialog.askopenfilename(
        # initaldir="/",            # cause Error
        # titile="Select File",     # cause Error
        filetypes=(
            ("python", "*.py"),
            ("executables", "*.exe"),
            ("all files", "*.*"),

            )
        )
    apps.append(file_name)

    print(file_name)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def run_apps():
    for app in apps:
        os.startfile(app)


if __name__ == '__main__':
    main()
