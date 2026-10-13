import shutil
import os

print("===== Azure VM Health Monitor =====")

# Display server hostname
print("Hostname:", os.uname().nodename)

# Display disk usage
disk = shutil.disk_usage("/")

print(f"Total Disk: {disk.total / (1024**3):.2f} GB")
print(f"Used Disk: {disk.used / (1024**3):.2f} GB")
print(f"Free Disk: {disk.free / (1024**3):.2f} GB")

print("===== Monitoring Complete =====")
