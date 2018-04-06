#!/usr/bin/bash

/usr/bin/openpyn --kill
sleep 5
/usr/bin/openpyn -x            # reset firewall / kill flush
