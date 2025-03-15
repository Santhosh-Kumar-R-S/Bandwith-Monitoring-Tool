import speedtest

def check_speed():
    """Fetch and display internet speed"""
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000

    return f"Download: {download_speed:.2f} Mbps | Upload: {upload_speed:.2f} Mbps"

if __name__ == "__main__":
    print(check_speed())
