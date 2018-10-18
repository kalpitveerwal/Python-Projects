#!bin/bash/

ans=$(head /dev/urandom | tr -dc A-Z0-9 | head -c 3)

temp="AAA"
sed "s/[A-Z][A-Z][0-9]/$ans/g" $1




