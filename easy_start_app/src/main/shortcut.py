import os
import psutil
import sys
from PyQt5.QtWidgets import QApplication, QDialog
import window


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.ui = window.Ui_Dialog()
        self.ui.setupUi(self)

        # 初始化应用程序的路径字典
        self.app_path = {
            "WeChat.exe": r"D:\software\WeChat\WeChat.exe",
            "idea64.exe": r"D:\IntelliJ IDEA 2021.2\bin\idea64.exe",
            "navicat.exe": r"D:\work\Navicat Premium 16\navicat.exe",
            "openvpn-gui.exe": r"C:\Program Files\OpenVPN\bin\openvpn-gui.exe",
            "Notepad++.exe": r"D:\work\Notepad++\Notepad++.exe",
            "Apifox.exe": r"D:\work\Apifox\Apifox.exe",
            "mysql.exe": r"D:\MySQL\MySQL Server 5.7\bin\mysql.exe",
            "redis-server.exe": r"D:\work\Redis-x64-5.0.14.1\redis-server.exe",
        }

    def startWeChat(self):
        # 遍历当前系统中所有进程，并检查微信是否在运行
        self.kill_Thread("WeChat.exe")
        # 如果微信可执行文件存在，则启动微信
        if os.path.exists(self.app_path["WeChat.exe"]):
            os.startfile(self.app_path["WeChat.exe"])
        else:
            print("微信未安装或安装路径不正确。")

    def startIdea(self):
        # 遍历当前系统中所有进程，并检查微信是否在运行
        self.kill_Thread("idea64.exe")
        # 如果微信可执行文件存在，则启动微信
        if os.path.exists(self.app_path["idea64.exe"]):
            os.startfile(self.app_path["idea64.exe"])
        else:
            print("Idea未安装或安装路径不正确。")

    def startNavicat(self):
        # 遍历当前系统中所有进程，并检查微信是否在运行
        self.kill_Thread("navicat.exe")
        # 如果微信可执行文件存在，则启动微信
        if os.path.exists(self.app_path["navicat.exe"]):
            os.startfile(self.app_path["navicat.exe"])
        else:
            print("Navicat未安装或安装路径不正确。")

    def startOpenVpn(self):
        # 遍历当前系统中所有进程，并检查微信是否在运行
        self.kill_Thread("openvpn-gui.exe")
        # 如果微信可执行文件存在，则启动微信
        if os.path.exists(self.app_path["openvpn-gui.exe"]):
            os.startfile(self.app_path["openvpn-gui.exe"])
        else:
            print("OpenVpn未安装或安装路径不正确。")

    def startSublime(self):
        # 遍历当前系统中所有进程，并检查微信是否在运行
        self.kill_Thread("Notepad++.exe")
        # 如果微信可执行文件存在，则启动微信
        if os.path.exists(self.app_path["Notepad++.exe"]):
            os.startfile(self.app_path["Notepad++.exe"])
        else:
            print("Sublime未安装或安装路径不正确。")

    def startMysql(self):
        # 遍历当前系统中所有进程，并检查微信是否在运行
        self.kill_Thread("mysql.exe")
        # 如果微信可执行文件存在，则启动微信
        if os.path.exists(self.app_path["mysql.exe"]):
            # 使用 MySQL 可执行文件的完整路径来启动 MySQL 服务
            mysql_exe_path = self.app_path["mysql.exe"]
            os.system(f'"{mysql_exe_path}" -u root -p root')
        else:
            print("mysql未安装或安装路径不正确。")

    def startRedis(self):
        # 遍历当前系统中所有进程，并检查微信是否在运行
        self.kill_Thread("redis-server.exe")
        # 如果微信可执行文件存在，则启动微信
        if os.path.exists(self.app_path["redis-server.exe"]):
            os.startfile(self.app_path["redis-server.exe"])
        else:
            print("Redis未安装或安装路径不正确。")

    def apiBost(self):
        # 遍历当前系统中所有进程，并检查微信是否在运行
        self.kill_Thread("Apifox.exe")
        # 如果微信可执行文件存在，则启动微信
        if os.path.exists(self.app_path["Apifox.exe"]):
            os.startfile(self.app_path["Apifox.exe"])
        else:
            print("Apifox未安装或安装路径不正确。")

    def startAll(self):
        for key in self.app_path:
            print(key)
            # 遍历当前系统中所有进程，并检查微信是否在运行
            self.kill_Thread(key)
            # 如果微信可执行文件存在，则启动微信
            if os.path.exists(self.app_path[key]):
                os.startfile(self.app_path[key])
            else:
                print("启动失败")

    def kill_Thread(self, process_name):
        for proc in psutil.process_iter():
            try:
                # 获取进程名称
                pname = proc.name()
                # 如果微信正在运行，先关闭微信进程
                if process_name in pname:
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())
