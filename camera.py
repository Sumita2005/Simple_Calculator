import subprocess
import time
from plyer import notification

camera_ip = "192.168.0.104"

# Check initial status
result = subprocess.run(
    ["ping", "-n", "1", camera_ip],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

previous_status = (result.returncode == 0)

# Show initial status only once
if previous_status:
    print(f"Camera {camera_ip} ONLINE")
else:
    print(f" Camera {camera_ip} OFFLINE")

while True:

    result = subprocess.run(
        ["ping", "-n", "1", camera_ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    current_status = (result.returncode == 0)

    # Camera went OFFLINE
    if previous_status and not current_status:
        print(f" Camera {camera_ip} OFFLINE")

        notification.notify(
            title="Camera Offline",
            message=f"{camera_ip} is OFFLINE",
            timeout=5
        )

    # Camera came ONLINE
    elif not previous_status and current_status:
        print(f" Camera {camera_ip} ONLINE")

        notification.notify(
            title="Camera Online",
            message=f"{camera_ip} is ONLINE",
            timeout=5
        )

    previous_status = current_status

    time.sleep(2)