import sys
import psutil
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar, QTimer

class BandwidthMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        # Network Data
        self.prev_recv = psutil.net_io_counters().bytes_recv
        self.prev_sent = psutil.net_io_counters().bytes_sent

        # Timer to update speeds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_speed)
        self.timer.start(1000)  # Refresh every second

    def initUI(self):
        self.setWindowTitle("Bandwidth Monitor")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Loading...", self)
        self.label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(self.label)

        self.progress_download = QProgressBar(self)
        self.progress_upload = QProgressBar(self)
        layout.addWidget(self.progress_download)
        layout.addWidget(self.progress_upload)

        self.setLayout(layout)

    def update_speed(self):
        current_recv = psutil.net_io_counters().bytes_recv
        current_sent = psutil.net_io_counters().bytes_sent

        download_speed = (current_recv - self.prev_recv) / 1024  # KB/s
        upload_speed = (current_sent - self.prev_sent) / 1024

        self.label.setText(f"Download: {download_speed:.2f} KB/s | Upload: {upload_speed:.2f} KB/s")
        
        # Set progress bars (max 1000 KB/s for visualization)
        self.progress_download.setValue(min(int(download_speed), 1000))
        self.progress_upload.setValue(min(int(upload_speed), 1000))

        self.prev_recv = current_recv
        self.prev_sent = current_sent

# Run Application
app = QApplication(sys.argv)
window = BandwidthMonitor()
window.show()
sys.exit(app.exec())
