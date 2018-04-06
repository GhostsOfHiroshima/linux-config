#!/usr/bin/bash

/usr/bin/openpyn --kill
sleep 2
/usr/bin/openpyn -x            # reset firewall / kill flush
sleep 2
/home/icebox/Documents/scripts/public_ip.py        # update IP / location

