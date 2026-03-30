reverse engineer du getflag:

adresse des instructions pour avoir accès à chaque flag (obtenu avec ghidra):

flag 06 : 0x08048ccb
flag 02 : 0x08048c3b
flag 00 : 0x08048bf3
flag 01 : 0x08048c17
flag 04 : 0x08048c83
flag 03 : 0x08048c5f
flag 05 : 0x08048ca7
flag 10 : 0x08048d5b
flag 08 : 0x08048d13
flag 07 : 0x08048cef
flag 09 : 0x08048d37
flag 12 : 0x08048da3
flag 11 : 0x08048d7f
flag 13 : 0x08048dc4
flag 14 : 0x08048de5

(connexion a un utilisateur flag)
gdb getflag
b main
r
set $eip = 0x08048de5
c
Continuing.
7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
 stack smashing detected : terminated

Program received signal SIGABRT, Aborted.
0xf7fc7579 in __kernel_vsyscall ()