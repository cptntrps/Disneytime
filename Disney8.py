import tkinter as tk
from PIL import Image, ImageTk
import requests
import time
import random
import threading
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def fetch_wait_times():
    url = "https://queue-times.com/parks/6/queue_times.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rides = []
        for land in data['lands']:
            land_name = land['name']
            for ride in land['rides']:
                ride_info = {
                    'name': ride['name'],
                    'wait_time': ride.get('wait_time'),
                    'is_open': ride['is_open'],
                    'land': land_name
                }
                rides.append(ride_info)
        return rides
    else:
        return []

def update_attraction_info(label, background_label, root, images):
    while True:
        rides = fetch_wait_times()
        random.shuffle(rides)
        for ride in rides:
            name = ride['name']
            land = ride['land']
            wait_time = ride['wait_time']
            status = "Closed" if not ride['is_open'] else f"{wait_time} min wait"
            text = f"{name}: {status}"
            label.config(text=text)

            # Update background image based on land
            if land in images:
                background_label.config(image=images[land])
            
            root.update_idletasks()
            time.sleep(10)

def create_gui():
    root = tk.Tk()
    root.title("MK Wait Times")

    window_width = 300
    window_height = 100

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_right = int(screen_width - window_width - 10)
    position_down = int(screen_height - window_height - 50)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

    root.attributes('-topmost', True)

    # Load background images for each land
    land_images = ["Adventureland.png", "Fantasyland.png", "Tomorrowland.png", "Frontierland.png", "Main Street U.S.A..png", "Liberty Square.png"]
    images = {land.split('.')[0]: ImageTk.PhotoImage(Image.open(resource_path(land)).resize((window_width, window_height), Image.Resampling.LANCZOS)) for land in land_images}

    background_label = tk.Label(root)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    text_label = tk.Label(root, font=("Helvetica", 10), fg="white", bg="black", wraplength=window_width-20)
    text_label.place(relx=0.5, rely=0.5, anchor='center')

    threading.Thread(target=update_attraction_info, args=(text_label, background_label, root, images), daemon=True).start()

    root.mainloop()

create_gui()
