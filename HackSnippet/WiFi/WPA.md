
## Brute Force (in a video on youtube in 2011)

```Take the output from JTR and pipe it into aircrack that will try it against the capture handshake```

- BSSID is the address of the access point
- log.cap should contain the handshake
```
john --increment -sdout | aircrack-ng -b BSSID -w - log.cap
```