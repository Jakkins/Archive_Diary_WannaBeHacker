
## Reset

1. Shut Everything
	```bash
	sudo ip link set wlp3s0 down
	netctl stop-all
	sudo airmon-ng check kill
   	```
2. Delete all monitor if any
	```bash
	sudo airmon-ng stop wlp3s0mon
	```
3. Reset MAC Spoofing ?
