#!bin/bash
echo "escribe tu ip  a escanear"
echo "ejemplo: 192.168.1.65 " 
echo ""
echo "¿cual es tu ip?"
echo "recuerda que este es un escaneo de tu red por lo que entre mas dispocitivos esten conectados mas tardara y puede que se puede poner mas lento el internet al aser el escaneo y volvera a la normalidad cando termine el escaneo suerte :) "

read ip 
echo "tu ip es:" $ip

nmap -sV -A -p- $ip -T 5

echo "escaneo terminado"
echo ""
echo "si ya no quieres continuar preciona ctrl + c"
echo "si quieres volver al menu principal  preciona enter"
echo ""
read o

echo "volviendo al menu principal... "
echo ""
python3 nmap.py



