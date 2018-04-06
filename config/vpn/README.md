## VPN

For anonymity I'm using NordVPN, which does a decent job in what it's supposed to do.

### openpyn

To control the connection easier, I'm using [openpyn](https://github.com/jotyGill/openpyn-nordvpn). It's a tool built in python3 which helps a lot into handling the communication with nordvpn, such as autostart, picking servers by fastest response time, select server based on location, etc

#### Installation
For installation, unfortunetly currently it can't be installed on arch through pacman or yaourt, but following the github README file of openpyn steps, will do the job

#### Usage

After installation, first thing to do is to initialize it which is done running `sudo openpyn --init`

The following command will ask you for few things such as credentials.

Once done, a service file should be found in `/etc/systemd/system/openpyn.service`

The service file I'm using can be found in the repo.

**IMPORTANT** For the service file, use the one openpyn generate, and replace only this two lines:
```
ExecStart=/home/icebox/Documents/scripts/start_openpyn.sh
ExecStop=/home/icebox/Documents/scripts/stop_openpyn.sh
```

#### IP and Location

I've written a python script that gathers the IP address and location of your current connection.

The service (well, script that the service is starting) is using the `public_ip.py` script when it starts, to gather the IP and location right after it connects.

The script can be also set in `~/.config/openbox/autostart` with the forever argument like this
`./public_ip.py forever` which will make the script run forever, so that if the VPN goes down, or you disconnect and reconnect to a different server, the IP and location will be also updated.

To actually make use of the IP and location, I'm showing them in conky. Conky file can be found inside conky folder in this repo