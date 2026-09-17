import tkinter as tk
from datetime import datetime
monitoring = False
def start_monitoring():
    global monitoring
    monitoring = True
    status_label.config(text="Status: Monitoring")
    input_box.focus_set()
def stop_monitoring():
    global monitoring
    monitoring = False
    status_label.config(text="Status: Stopped")
def monitor_key(event):
    if monitoring:
        key = event.keysym
        time = datetime.now().strftime("%H:%M:%S")
        output_box.config(state="normal")
        output_box.insert(tk.END, f"{time} Key Pressed: {key}\n")
        output_box.config(state="disabled")
root = tk.Tk()
root.title("Keyboard Event Monitoring")
root.geometry("600x450")
title = tk.Label(root, text="Keyboard Event Monitoring", font=("Arial", 18, "bold"))
title.pack(pady=15)
tk.Label(root, text="Type something here:").pack()
input_box = tk.Text(root, height=5, width=60)
input_box.pack(pady=10)
input_box.bind("<KeyPress>", monitor_key)
start_button = tk.Button(root, text="Start Monitoring", command=start_monitoring)
start_button.pack(pady=5)
stop_button = tk.Button(root, text="Stop Monitoring", command=stop_monitoring)
stop_button.pack(pady=5)
status_label = tk.Label(root, text="Status: Stopped")
status_label.pack(pady=10)
tk.Label(root, text="Keyboard Events").pack()
output_box = tk.Text(root, height=10, width=65, state="disabled")
output_box.pack(pady=10)
root.mainloop()
