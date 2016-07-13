image cdp ="fondo2.png"
image oficina="fondo3.png"
image testigos ="testigos.png"
image victima ="victima.png"
#image negro ="#000000"
image reportera="reportera2.png"
image detective ="detective.png"
image peter ="peter.png"
image lois ="lois.png"
image stewie ="stewie2.png"
image tm = "tm.png"
image th = "th.png"

define d = Character('Detective',color="#0D8DB0")
define pt = Character( 'Peter', color="#0D8DB0")
define ls = Character('Lois', color="#0D8DB0")
define st = Character('Stewie', color="#0D8DB0")
define r = Character('reportera', color="#0D8DB0")
define tm= Character('Testigo', color="#0D8DB0")
define th= Character('Testigo', color="#0D8DB0")

label start:
    scene cdp
    show reportera
    r "buen día televidentes, en horas de la mañana se encontró el cadáver de la famosa estrella canina Brian o conner." 
    r "en las afueras de la ciudad de Panamá, se desconoce las causas de su muerte."
    r "Esta noticia nos tiene a todos consternados ya que la estrella era muy querida por el pueblo panameño." 
    r "Está con nosotros el detective Peñate quien es el encargado en este caso."
    hide reportera

    show detective at left
    d "lo único que puedo decir es que estamos  investigando los hechos para dar con el presunto asesino."

    #########  

    scene oficina
    show testigos at right 
    d "quienes son ustedes?" 
    #(chris Griffin y Meg G.)
    d "buenas tardes detective venimos a dar nuestra declaración sobre el asesinato de la estrella Brian O conner"
    d "ok... tomare sus decalciones de manera individual"
    d "pase el primer testigo"
    hide testigos

    ########

    scene oficina
    show th at right
    th "soy residente del pueblo donde se encontró el cadáver de la víctima"
    th "en horas de la madrugada vi una sombra pequeña alejarse del lugar"
    th "me acerque y al darme cuenta de los hechos di partes a las autoridades de que era un presunto cadáver"
    d  "es todo lo que tiene para declarar?"
    th "si"
    d  "ok...puedes retirarte....que pase el siguiente"
    hide th
    
    show tm at right
    tm "bueno yo trabajaba en  casa de la víctima"
    tm "ayer vino su familia a visitarlo; Él salió con ellos pero no volvió mientras estuve ahí"
    tm "Es lo único que puedo aportar a la investigación,ojala den con el culpable"

    d  "ok! Me puede facilitar el nombre de los familiares que salieron con la victima?"
    tm "si claro… la familia Griffin"
    tm "la señito se llama Lois, el señor Peter y el niño Stewie"
    tm "tenía entendido que el niño es adoptado y tiene problemas mentales"
    d "gracias por la valiosa información"
    
    hide tm 
    
#########

    show detective at right
    d "buenas! Soy el detective Peñate, y necesito sus declaraciones ya que son sospechosos del asesinato de Brian"
    hide detective
    
  #########

   
    show detective at right
    d "eh dado con los sospechosos? eh aquí sus declaraciones "
    d "comenzaremos con usted Sr. Peter"
    hide detective

    show  peter at right
    pt "Sí, salimos con él, pero lo dejamos en la puerta de su casa antes que anocheciera"
    pt " El niño pidió permiso para quedarse a hacerle compañía a su hermano por esa noche"
    d  "Estaba con ustedes la señora Lois?"
    pt "sí, pero ella se quedó en el mall haciendo compras"
    hide  peter 

    show lois at right
    ls "Yo no hice nada yo no  estuve con ellos, la pase todo el día en el mall"
    ls "Lo único que puedo decir es que mis hijos no se llevaban bien"
    d  "su hijo Stewie es adoptado como lo era Brian??"
    ls "sí, fue nuestro primer hijo adoptivo, luego llego Brian"
    hide lois 
 
    show stewie at right 
    st "Yo soy inocente y no se quien lo hizo, pero yo solo puedo decir que amaba a mi hermano"
    d  "tiene algo mas que agregar a su decaracion"
    st "NO, eso es todo"
    hide stewie
    
   
    scene oficina
    show detective at right
    d"Quien crees que es el ASESINO?"
    
    menu:
               "Lois":

                         python:
     
     
                                       from pyswip import Prolog
                                       prolog=Prolog()
                                       prolog.consult("/home/liizy/Escritorio/detective.pl")
                                       asesino=list(prolog.query("murderer(X)"))
                                       d("Felicidades encontraste al asesino %s"%asesino[0]["X"]) 

               "Peter":
                   d"LO SENTIMOS...NECESITAS INVESTIGAR MAS A FONDO PARA DAR CON EL ASESINO"
                   d"VULVE A JUGAR"

               "Stiwie":
                   d"LO SENTIMOS...NECESITAS INVESTIGAR MAS A FONDO PARA DAR CON EL ASESINO"
                   d"VULVE A JUGAR"


return
