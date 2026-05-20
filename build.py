import os
import shutil
import configparser
name = "Autovisor"

cmd = (
    f"pyinstaller "
    f"--log-level=INFO "
    f"--noconfirm "
    f"-c "
    f"-i ./res/zhs.ico "
    f"--onedir "
    f"--contents-directory=internal "
    f"--name={name} "
    f"./Autovisor.py "
    f"--exclude-module cv2 "
    f"--exclude-module numpy "
)
os.system(cmd)

os.makedirs(f"./dist/{name}/res", exist_ok=True)
open(f"./dist/{name}/为防止启动失败, 建议使用Chrome浏览器", "w").close()
shutil.copyfile("./res/QRcode.jpg", f"./dist/{name}/res/QRcode.jpg")
shutil.copyfile("./res/stealth.min.js", f"./dist/{name}/res/stealth.min.js")
# 复制 configs.ini 并清空账号密码
config = configparser.ConfigParser()
config.read("./configs.ini", encoding="utf-8")
config["user-account"]["username"] = ""
config["user-account"]["password"] = ""
with open(f"./dist/{name}/configs.ini", "w", encoding="utf-8") as f:
    config.write(f)
shutil.rmtree("./build", ignore_errors=True)
try:
    os.remove("./Autovisor.spec")
except FileNotFoundError:
    pass
