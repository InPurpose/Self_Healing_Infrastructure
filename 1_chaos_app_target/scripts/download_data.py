# import subprocess


# subprocess.run(["uv", "run","kaggle","datasets","download","-d","olistbr/brazilian-ecommerce","-p","./data"], capture_output=True, text=True)
# subprocess.run(["unzip","./data/brazilian-ecommerce.zip","-d","./data/olist"], capture_output=True, text=True)

import subprocess
import os
import zipfile

# 1️⃣ 确保目录存在
os.makedirs("./data", exist_ok=True)
os.makedirs("./data/olist", exist_ok=True)

# 2️⃣ 下载数据
print("Downloading dataset...")
subprocess.run(
    [
        "uv", "run", "kaggle", "datasets", "download",
        "-d", "olistbr/brazilian-ecommerce",
        "-p", "./data"
    ],
    check=True
)

# 3️⃣ 解压（用 Python，更跨平台）
zip_path = "./data/brazilian-ecommerce.zip"

print("Unzipping dataset...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall("./data/olist")

print("Done!")