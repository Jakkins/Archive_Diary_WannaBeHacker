
```diff
- Error setting channel: command failed: Device or resource busy (-16)
- Error -16 likely means your card was set back to station mode by something.
- Removing non-monitor mon0 interface...

+ you have to close internet on that interface and abilitate promiscuos mode
```

1. Shutdown internet
	```bash
	sudo ip link set wlp3s0 down
	netctl stop-all
	sudo airmon-ng check kill
	```
2. Create virtual monitors
	```bash
	sudo iw wlp3s0 interface add mon0 type monitor
	# you can add other virtual monitors
	```
3. Set virtual monitor
	```bash
	sudo airmon-ng start mon0
	```
4. Internet won't work on this interface