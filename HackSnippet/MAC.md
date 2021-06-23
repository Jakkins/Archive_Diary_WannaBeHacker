# Media Access Control Adrresses

## Schemes

- MAC 48
- EUI 48 (Extended Unique Identifier)
- EUI 64

## OUIs

| Group | starting OUI | Date |
| --- | --- | --- |
| Linksys | 00:04:5A:##:##:## and other | 2011 |
| NetGear | 00:09:5B:##:##:## and other | 2011 |
| Xerox | 00:00:00:##:##:## and other | 2011 |
| Realtek | 00:E0:4C:##:##:## and other | 2020 |

## Change it, MAC Spoofing

```bash
ip link show
ip link set dev wlp3s0 down
```
```Unless you control the network(s) you are connecting to, use MAC prefix of any real vendor (basically, the first three bytes), and use random values for next three bytes. For more information please read Wikipedia:Organizationally unique identifier.```

To change the MAC, we need to run the command:
```bash
ip link set dev wlp3s0 address XX:XX:XX:XX:XX:XX
```
Then
```bash
ip link set dev wlp3s0 up
# or something
```