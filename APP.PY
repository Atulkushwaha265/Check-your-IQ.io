import os

# ===== BASE PATH (change for phone / PC) =====
base_path = "/storage/emulated/0/MyFolders"
# PC ke liye use karo:
# base_path = "C:/Users/Public/Documents/MyFolders"

# ===== NUMBER OF FOLDERS =====
total_folders = 100

# ===== CREATE BASE FOLDER =====
os.makedirs(base_path, exist_ok=True)

# ===== CREATE MULTIPLE FOLDERS =====
for i in range(1, total_folders + 1):
    folder_name = f"Project{i}"
    folder_path = os.path.join(base_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created: {folder_path}")

print("All folders created successfully 👍")
