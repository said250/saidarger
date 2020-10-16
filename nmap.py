#explicacion y recomendaciones
print ("")
print ("este script te ayudara a usar nmap de una manera mas automatica ")
print ("¿que es nmap?")
print ("")
print ("Nmap es un programa de código abierto que sirve para efectuar rastreo de puertos escrito originalmente por Gordon Lyon y cuyo desarrollo se encuentra hoy a cargo de una comunidad. Fue creado originalmente para Linux aunque actualmente es multiplataforma.")
print ("")
print ("")
print ("advertencia:este script es solo para uso en termux :)") 
#menu 1
print ("a continucion se mostrara un menu para que tu elijas lo que quieras")
print ("")
print ("opcion 1 = escaneo a la red que estes conectado")
print ("opcion 2 = escaneo a una ip en concreto")
print ("opcion 3 = saber tu ip")
print ("opcion 4 = saber tu ip publica")
print ("opcion 5 = instalar nmap en caso de no tenerlo")
print ("si quieres salir escribe exit ")

#if's

    
y =int(input(">>> "))

if y==1:
   print ("okey comencemos :) ")
   print ("en primera haremos un escaneo de tu red ")
   import os
   os.system ('bash esc.sh')
   
   
       
elif y==2:
   print (" ")
   print ("haremos un escaneo a una direccion ip conectada a tu red")
   import os
   os.system ('bash esc2.sh ')    
    

elif y==3:
    print ("encontrando ip...")
    print (" ")
    import os
    os.system ('ifconfig')
    print ("te dire tu ip primero encuentra donde dice wlan y donde dice inet es la ip de tu dispocitivo en la red privada ")
    print ("aqui esta tu ip ")
    print ("si quieres salir escribe exit si quieres volver al menu princpal escribe 99")
    c = int(input(">>>"))
    if c==99:
       print ("volviendo al menu principal")
       print (" ")
       import os
       os.system ('python3 nmap.py')
       
elif y==4:
     print ("instalando requerimientos")
     print ("")    
     import os
     os.system (' apt update &&  apt upgrade ')
     os.system (' sudo apt install curl')
     print ("tu ip publica es...")
     print ("")
     import os
     os.system ('curl ifconfig.me')
     print ("esa es tu ip publica")
     print ("si quieres salir escribe exit si quieres volver al menu princpal escribe 99")
     x = int(input(">>>"))
     if x==99:
       print ("volviendo al menu principal..")
       print (" ")
       import os
       os.system ('python3 nmap.py')

elif y==5:
    print ("instalando nmap")
    import os 
    os.system ('apt update && apt upgrade')
    os.system ('apt install nmap')
    print ("nmap instalado correctamente :) ")
    print ("si quieres volver al menu principal escribe 99 si quieres salir escribe exit")
    m = int(input(">>>"))
    if m==99:
       print ("volviendo al menu principal...")
       print ("")
       import os
       os.system ('python3 nmap.py')                    
