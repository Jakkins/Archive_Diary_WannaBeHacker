## Frames

WiFi Frames (like Ethernet Frame, a datapacket)
- Header
- PayLoad
  - Any kind of protocol packet (IP, UDP, ...)
- CRC (integrity check)

Type of Frames:
- Management Frames
  - Beacons
    - The ones sent by access point or base station to communicate their presence
  - Probes
    - Requests
      - Sended by clients
    - Responses
      - Sended by access point
  - Association
    - Requests 
    - Resposes (allocate memory when acceptin a request)
    - DisAssociation (unallocate memory on request)
  - Authentication
    - Authentication
      - WPA and WPA2 is more complex then WEP
    - Deauthentication (terminate secure session)
- Control Frames
  - Request to send (RTS)
  - Clear to Send (CTS)
  - Acknowledge (ACK)
- Data Frames

## Beacon Frames aka Beacons

- SSID
- Timestamp
- Channel
- Data Rate
- Other

mdk3

### Check if you can inject

```bash
# set interface to monitor mode
sudo airmon-ng start wlp3s0
# test if your radio can perform injection
sudo aireplay-ng -9 wlp3s0mon
# -9 : tests injection and quality
```

