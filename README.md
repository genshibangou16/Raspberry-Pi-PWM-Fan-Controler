# Raspberry-Pi-PWM-Fan-Controler
Pigpio's PWM signal controls fan perfectly.<br>
Connect fan with GPIO 18 and Ground.<br>
# Features
- Quiet at night.
- Change RPM according to CPU temperatue.
- Few noise.
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
4. Reload daemon
```
sudo systemctl daemon-reload
```
5. Enable & Start service
```
sudo systemctl enable fancoltrol && sudo systemctl start fancontrol
```
