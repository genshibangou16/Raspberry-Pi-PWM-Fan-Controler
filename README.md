# Raspberry-Pi-PWM-Fan-Controler
Pigpio's PWM signal controls fan perfectly.
# Instalation
1. Copy this files into `/opt/`.
2. Make service file as follows.
```
sudo nano /etc/systemd/system/fancontrol.service
```
3. Copy follows into `fancontrol.service`.
```
[Unit]
Description=FanControl

[Service]
ExecStart=/opt/fan_start.py
ExecStop=/opt/fan_stop.py
Restart=always
Type=forking
PIDFile=/run/fan.pid

[Install]
WantedBy=multi-user.target
```
