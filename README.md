# HasturBoss Blob and Web
![LICENSE](https://img.shields.io/github/license/HasturBoss/Hastur)

* date -s "yy-mm-dd hh:mm:ss"
* Debian terminal connect wifi
```Shell
// Dynamic ip address setting
wpa_passphrase <wifi_id> <wifi_pwd> >> /etc/wpa_supplicant/wpa_supplicant.conf
wpa_supplicant -i <drivers> -c /etc/wpa_supplicant/wpa_supplicant.conf -B
dhclient <drivers>
// Static ip address setting
nmtui
or: nano /etc/network/interfaces
auto <drivers>
iface <drivers> inet static
address <ip>
netmask 255.255.255.0
gateway 192.168.1.1
dns-nameservers 192.168.1.1
// IP, gateway, DNS...setting
ip addr
apt install rfkill
or: dpkg -i rfkill.deb
rfkill list
rfkill unblock all
// Unlock network...setting
vim /etc/rc.local
rfkill unblock all
wpa_supplicant -i <drivers> -c /etc/wpa_supplicant/wpa_supplicant.conf -B
dhclient <drivers>
// exit 0
```

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

git config --global http.proxy "http://127.0.0.1:7890"
git config --global https.proxy "https://127.0.0.1:7890"
git config --global --unset http.proxy
git config --global --unset https.proxy
```

* Use curl
```Shell
curl -O -x http://127.0.0.1:7890 https://raw.githubusercontent.com/HasturBoss/Hastur/main/releases/*.py
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

* Use rpi.gpio of python3, Connect the triode(PNP) and fan(GPIO.15)!
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
If using clash, please modify the port: 
nano /usr/lib/systemd/system/cockpit.socket
For example: 9090 > 9099
```

* Use shellinabox(Android input method is not supported!)
```Shell
apt install openssh-client openssh-server openssl shellinabox ufw
ufw allow 4200
Open browser, input https://<ip>:4200
```

* Use Clash: http://clash.razord.top/
```
wget -O <https://shuttle.gt-in.com/clientarea.php>
Copy config.yaml to /etc/calsh
```
