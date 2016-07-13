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




return

