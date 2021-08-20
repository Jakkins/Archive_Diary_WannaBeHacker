
## Players

- SSH server 
    - is a software which uses the secure shell protocol to accept connections from remote computers
    - example
        - OpenSSH server
            - for example is already installed in raspberry pi
- SSH client
    - is a software program which uses the secure shell protocol to connect to a remote computer
    - example
        - PuTTY

```
Keywords:
    remote access without port forwarding
    bypass firewall
    NAT traversal
        - Socket Secure (SOCKS) is a technology created in the early 1990s that uses proxy servers to relay traffic between networks or systems.
        - Traversal Using Relays around NAT (TURN) is a relay protocol designed specifically for NAT traversal.
        - NAT hole punching is a general technique that exploits how NATs handle some protocols (for example, UDP, TCP, or ICMP) to allow previously blocked packets through the NAT.
        - UDP hole punching
        - TCP hole punching
        - ICMP hole punching
        - Session Traversal Utilities for NAT (STUN) is a standardized set of methods and a network protocol for NAT hole punching. It was designed for UDP but was also extended to TCP.
        - Interactive Connectivity Establishment (ICE) is a complete protocol for using STUN and/or TURN to do NAT traversal while picking the best network route available. It fills in some of the missing pieces and deficiencies that were not mentioned by STUN specification.
        - UPnP Internet Gateway Device Protocol (IGDP) is supported by many small NAT gateways in home or small office settings. It allows a device on a network to ask the router to open a port.
        - NAT-PMP is a protocol introduced by Apple as an alternative to IGDP.
        - PCP is a successor of NAT-PMP.
        - Application-level gateway (ALG) is a component of a firewall or NAT that allows for configuring NAT traversal filters.[2] It is claimed by numerous people that this technique creates more problems than it solves.[3]
```

## Tunnelling

### with external service (use their servers as the middle man)

reverse ssh
ngrok
Hamachi
gotoypc

### with local service

tor
openVPN
IPv6

### PLAN

`SSH client through OpenVPN client <-- to --> OpenVPN server to connect to SSH server`

https://raspberrypi.stackexchange.com/questions/103496/do-you-have-to-port-forward-when-using-openvpn
No, you do not have to use port forwarding when using OpenVPN, but a port number is still intrinsic to the process.
This does not require port forwarding because they can be distinguished by MAC address.

Which gets to your question, "Isn't the point of a VPN to not have the need to port forward?". Sort of. Once on the VPN you can connect to other nodes without port forwarding because every node on the VPN, like on a LAN, has a unique local address. That doesn't mean port numbers aren't still used -- they are -- but traffic does not have to be forwarded by a router as described in the next paragraph.

#### Server - setup OpenVPN server

1. create server.crt, server.key, ca.crt, dh2048.pem ta.key
2. launch openvpn server
        ```
        sudo openvpn --script-security 2 --config /etc/openvpn/server/server.cfg
        ```

#### Client - setup OpenVPN client 

1. install

```bash
# openvpn client
sudo apt install openvpn
```

2. test

On Windows, file are named "server.ovpn" and " client.ovpn ".
On Unix, "server.conf" and "client.conf". 

```bash
# ./usr/share/doc/openvpn/examples/sample-config-files/client.conf
cat ./usr/share/doc/openvpn/examples/sample-config-files/client.conf
# sudo openvpn --config /path/to/config.ovpn
sudo openvpn /etc/openvpn/client.conf
tail -f /var/log/messages
```