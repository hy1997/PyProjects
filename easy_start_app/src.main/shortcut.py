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
            "idea64.exe": r"D:\work\IntelliJ IDEA 2021.2\bin\idea64.exe",
            "navicat.exe": r"D:\work\Navicat Premium 15\navicat.exe",
            "openvpn-gui.exe": r"C:\Program Files\OpenVPN\bin\openvpn-gui.exe",
            "sublime_text.exe": r"D:\work\Sublime Text\sublime_text.exe",
            "ApiPost7.exe": r"D:\software\apipost\ApiPost7.exe",
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
        self.kill_Thread("sublime_text.exe")
        # 如果微信可执行文件存在，则启动微信
        if os.path.exists(self.app_path["sublime_text.exe"]):
            os.startfile(self.app_path["sublime_text.exe"])
        else:
            print("Sublime未安装或安装路径不正确。")

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
