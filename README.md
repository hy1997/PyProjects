# PyProjects
easy_start_app  通过python快速启动应用APP



# 打包 exe文件命令
pyinstaller -F -w shortcut.py 

# 打包 exe文件命令 停缴图标
pyinstaller -F -w -i C:\Users\10078\IdeaProjects\PyProjects\easy_start_app\src\image\favicon.ico shortcut.py 


常用参数 含义
-i 或 -icon 生成icon
-F 创建一个绑定的可执行文件
-w 使用窗口，无控制台
-C 使用控制台，无窗口
-D 创建一个包含可执行文件的单文件夹包(默认情况下)
-n 文件名
