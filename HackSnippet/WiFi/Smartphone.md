
Looking at the types of frame:
- Management Frames
  - Beacons
  - **Probes**
    - Requests
    - Responses
  - Association
  - Authentication
- Control Frames
- Data Frames

We know that to connecto to an access point a smartphone can send **Probe Request** or listen to **Beacons frames** (passive scan).

## Listen to Beacons

```bash
#
# Open a fake access point that send beacons
#
# channel 11
sudo airmon-ng start wlp3s0 11
sudo airbase-ng -c 11 -e this_is_an_SSID wlp3s0mon
```
```bash
#
# This is the client
#
# bring up a second wireless card in monitor mode
sudo airmon-ng start XXXXX 11
```

Open wireshark on access point
```bash
wireshark &
# remove our beacons != 0x08
# search for probe request == 0x04
wlan.addr == 00:0f:04:b2:48:68 && wlan.fc.type_subtype != 0x08 && wlan.fc.type_subtype == 0x04
# 0x05 are the probe responses (from access point)
```

### Make client perform a passive scan

```bash
iw dev XXXXX scan passive
```
**this will listen to the beacons in the air without send any request**

### Make client perform an active scan

```bash
iw dev XXXXX scan 
```

