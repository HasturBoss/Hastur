# HasturBoss.github.io
Blob and Web

* Use git
```Git
git init
git add .
git commit -m "Initial commit"
git branch -M main
git branch -a
git remote add origin git@github.com:HasturBoss/<Res>.git
git pull --rebase origin main
git push -u origin main
```

* Use curl
```Shell
curl -O -x socks5://127.0.0.1:10808 https://raw.githubusercontent.com/HasturBoss/HasturBoss.github.io/main/*.py
```

* Use FTP
```Shell
apt install vsftpd
vim /etc/vsftpd.conf
```

* Use SSD1306 of python3
```Shell
apt install i2c-tools
raspi-config
pip3 install Adafruit_SSD1306
python3 oled.py

Your command should be added before: exit 0!
vim /etc/rc.local
python3 ~/*.py &

OR
vim /etc/crontab
* * * * * root python3 ~/*.py &
```

* Use rpi.gpio of python3, Connect the triode（PNP）and fan(GPIO.15)!
```Shell
apt install i2c-tools
raspi-config
pip3 install RPi.GPIO
python3 temp.py

Your command should be added before: exit 0!
vim /etc/rc.local
python3 ~/*.py &

OR
vim /etc/crontab
* * * * * root python3 ~/*.py &
```

* Use cockpit
```Shell
apt install cockpit ufw
ufw allow 9090
Open browser, input https://<ip>:9090
```

* Use shellinabox(Android input method is not supported!)
```Shell
apt install openssh-client openssh-server openssl shellinabox ufw
ufw allow 4200
Open browser, input https://<ip>:4200
```

* Use Lynx
```Shell
apt install lynx
Chinese course:
移动命令：
下方向键：页面上的下一个链接(用高亮度显示)。
上方向键：页面上的前一个链接(用高亮度显示)。
回车和右方向键：
跳转到链接指向的地址。
左方向键：回到上一个页面。
滚动命令：
+,Page-Down,Space,Ctrl+f：
向下翻页。
-,Page-Up,b,Ctrl+b：
向上翻页。
Ctrl+a： 移动到当前页的最前面。
Ctrl+e： 移动到当前页的最后面。
Ctrl+n： 向下翻两行。
Ctrl+p： 往回翻两行。
)： 向下翻半页。
(： 往回翻半页。
#： 回到当前页的 Toolbar 或 Banner。
文件操作命令：
c： 建立一个新文件。
d： 下载选中的文件。
E： 编辑选中的文件。
f： 为当前文件显示一个选项菜单。
m： 修改选中文件的名字或位置。
r： 删除选中的文件。
t： Tag highlighted file。
u： 上载一个文件到当前目录。
其他命令：
?,h： 帮助。
a： 把当前链接加入到一个书签文件里。
c： 向页面的拥有者发送意见或建议。
d： 下载当前链接。
e： 编辑当前文件。
g： 跳转到一个用户指定的URL或文件。
G： 编辑当前页的URL，并跳转到这个URL。
i： 显示文档索引。
j： 执行预先定义的“短”命令。
k： 显示键盘命令列表。
l： 列出当前页上所有链接的地址。
m： 回到首页。
o： 设置选项。
p： 把当前页输出到文件，e-mail，打印机或其他地方。
q： 退出。
/： 在当前页内查找字符串。
s： 在外部搜索输入的字符串。
n： 搜索下一个。
v： 查看一个书签文件。
V： 跳转到访问过的地址。
x： 不使用缓存。
z： 停止当前传输。
[backspace]：
跳转到历史页(同 V 命令)。
=： 显示当前页的信息。
： 查看当前页的源代码。
!： 回到shell提示符下。
_： 清除当前任务的所有授权信息。
*： 图形链接模式的切换开关。
@： 8位传输模式或CJK模式的切换开关。
[： pseudo_inlines 模式的切换开关。
]： 为当前页或当前链接发送一个“HEAD”请求。
Ctrl+r： 重新装如当前页并且刷新屏幕。
Ctrl+w： 刷新屏幕。
Ctrl+u： 删除输入的行。
Ctrl+g： 取消输入或者传送。
Ctrl+t： 跟踪模式的切换开关。
;： 看 Lynx 对当前任务的跟踪记录。
Ctrl+k： 调用 Cookie Jar 页。
数字键： 到后面的第 n 个链接。
```
