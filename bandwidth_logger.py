import psutil
import time
import csv

def log_bandwidth():
    """Logs bandwidth usage in a CSV file"""
    with open("bandwidth_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Download Speed (KB/s)", "Upload Speed (KB/s)"])

        while True:
            current_recv = psutil.net_io_counters().bytes_recv
            current_sent = psutil.net_io_counters().bytes_sent

            time.sleep(1)  # Update every second

            download_speed = (psutil.net_io_counters().bytes_recv - current_recv) / 1024
            upload_speed = (psutil.net_io_counters().bytes_sent - current_sent) / 1024

            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([timestamp, f"{download_speed:.2f}", f"{upload_speed:.2f}"])
            print(f"{timestamp} - Download: {download_speed:.2f} KB/s | Upload: {upload_speed:.2f} KB/s")

log_bandwidth()
