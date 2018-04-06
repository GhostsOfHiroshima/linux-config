#!/usr/bin/bash
# Start openpyn, called from openpyn.service

# connect, using dedicated, from DE, with firewall `killswitch`
/usr/bin/openpyn de -f -t 10 --dedicated &
sleep 15        # give it 15 seconds to connect

# get IP and location for conky
/home/icebox/Documents/scripts/public_ip.py

sleep infinity  # aaaah, time to sleep for a bit
