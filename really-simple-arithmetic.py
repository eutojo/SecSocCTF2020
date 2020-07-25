from pwn import *

p = remote('pwn.ctf.unswsecurity.com', 7003)

p.recvuntil('Navigation = ')
nav = p.recvuntil(' ')
p.recvuntil('Power = ')
power = p.recvuntil(' ')

q = long(nav)/long(power)

p.sendline(str(q))

p.interactive()