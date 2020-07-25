from pwn import *

p = remote('pwn.ctf.unswsecurity.com',7002)

p.recvuntil('What\'s ')
number = p.recvuntil(' in hexadecimal', drop=True)
p.sendline(hex(int(number)))

p.recvuntil('What\'s ')
number = p.recvuntil(' in octal', drop=True)
p.sendline(oct(int(number)))

p.recvuntil('What\'s ')
a = p.recvuntil(' + ', drop=True)
b = p.recvuntil('?', drop=True)
p.sendline(str(int(a) + int(b)))

p.recvuntil('What\'s ')
number = p.recvuntil(' in decimal', drop=True)
p.sendline(str(int(number,2)))

p.recvuntil('What\'s ')
number = p.recvuntil(' in octal', drop=True)
p.sendline(oct(int(number,2)))

p.recvuntil('What\'s ')
number = p.recvuntil(' in hexadecimal', drop=True)
p.sendline(hex(int(number,2)))

p.recvuntil('What\'s ')
number = p.recvuntil(' in binary', drop=True)
p.sendline(bin(int(number,16)))

p.recvuntil('What\'s ')
number = p.recvuntil(' in octal', drop=True)
p.sendline(oct(int(number,16)))

p.recvuntil('What\'s ')
a = p.recvuntil(' + ', drop=True)
b = p.recvuntil(' in decimal', drop=True)
p.sendline(str(int(a,16) + int(b,2)))

p.recvuntil('What\'s ')
a = p.recvuntil(' + ', drop=True)
b = p.recvuntil(' in octal', drop=True)
p.sendline(oct(int(a,16) + int(b,2)))

p.interactive()
