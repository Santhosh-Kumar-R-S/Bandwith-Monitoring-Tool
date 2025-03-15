import psutil
import tkinter as tk

def update_speed():
    """Fetch and update real-time bandwidth usage"""
    global prev_recv, prev_sent
    current_recv = psutil.net_io_counters().bytes_recv
    current_sent = psutil.net_io_counters().bytes_sent

    download_speed = (current_recv - prev_recv) / 1024  # KB/s
    upload_speed = (current_sent - prev_sent) / 1024

    speed_label.config(text=f"Download: {download_speed:.2f} KB/s\nUpload: {upload_speed:.2f} KB/s")

    prev_recv, prev_sent = current_recv, current_sent
    root.after(1000, update_speed)  # Refresh every second

# Initialize previous network data
prev_recv = psutil.net_io_counters().bytes_recv
prev_sent = psutil.net_io_counters().bytes_sent

# Tkinter UI Setup
root = tk.Tk()
root.title("Bandwidth Monitor")
root.geometry("300x150")

speed_label = tk.Label(root, text="Loading...", font=("Arial", 14), fg="blue")
speed_label.pack(pady=20)

update_speed()
root.mainloop()
