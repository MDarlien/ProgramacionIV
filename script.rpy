image cdp ="fondo2.png"
image oficina="fondo3.png"
image testigos ="testigos.png"
image victima ="victima.png"
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

return

