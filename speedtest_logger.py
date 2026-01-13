import speedtest
import time

#st = speedtest.Speedtest()

# print(f"Testing download speed...")

def download():
    st = speedtest.Speedtest()
    time.sleep(1)
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    #print(f"Download speed: {download_speed:.2f} Mbps")
    return f"Download speed: {download_speed:.2f} Mbps"


def upload():
    st = speedtest.Speedtest()
    time.sleep(1)
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    #print(f"Upload speed: {upload_speed:.2f} Mbps")
    return f"Upload speed: {upload_speed:.2f} Mbps"