from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def create_folders():
    base_path = "/storage/emulated/0/MyFolders"

    os.makedirs(base_path, exist_ok=True)

    for i in range(1, 1000):
        os.makedirs(os.path.join(base_path, f"Project{i}"), exist_ok=True)

    return "Folders created successfully 👍"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
