# Injection test

- First, it lists access points in the area which respond to broadcast probes.
  - Not every AP will respond to this type of request.
- Second, for each, it does a 30 packet test that indicates the connection quality.
  - This connection quality quantifies the ability of your card to successfully send and then receive a response to the test packet. The percentage of responses received gives an excellent indication of the link quality.

```bash
sudo ip link set wlp0s20f0u1 down
sudo iw wlp0s20f0u1 set monitor none
sudo ip link set wlp0s20f0u1 up
sudo airmon-ng start wlp0s20f0u1
sudo aireplay-ng -9 wlp0s20f0u1
```

## Other

```bash
sudo iw wlan0 set type managed
```
```bash
aireplay-ng -9 -e teddy -a 00:de:ad:ca:fe:00 -i wlan1 wlan0
```
Where:
- -9 is --test
- [optional] -e teddy is the network name (SSID)
- [optional] -a ```00:de:ad:ca:fe:00``` ath0 is MAC address of the access point (BSSID)
- [optional] -i wlan1 this interfaces acts as an AP and receives packets
- [Mandatory] wlan0 is the interface name or ```airserv-ng``` IP Address plus port number. This interface is used to send packets. For example - 127.0.0.1:666

```bash
aireplay-ng -9 127.0.0.1:666
```
Where:
- 9 means injection test
- 127.0.0.1:666 is the IP address and port number of airserv-ng. It does not have to be the local loopback address as in this example. It can be any IP address.
