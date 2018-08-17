#!/usr/bin/bash

# check if network is still "on", otherwise exit
result=$(ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null $
if [[ $result = *"not_connected"* ]]; then
    # we are not connected anymore, exit here
    echo "Network is down, stopping here"
    exit
fi

echo "Stopping VPN connection ..."

/usr/bin/openpyn --kill
sleep 2
/usr/bin/openpyn -x            # reset firewall / kill flush
sleep 2
/home/icebox/Documents/scripts/public_ip.py        # update IP / location

