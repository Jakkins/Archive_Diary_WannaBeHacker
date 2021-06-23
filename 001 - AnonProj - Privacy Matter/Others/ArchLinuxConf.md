
<h1 align="center">Arch Linux Configuration</h1>

- [Network configuration](https://wiki.archlinux.org/index.php/Network_configuration)

```diff
- Arch Linux has deprecated net-tools in favor of iproute2

Deprecated command 	Replacement commands
netstat 	        ss

netstat -tanp | grep tor
```
- Rsync per il backup, anche in ssh

