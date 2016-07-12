# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Detective',color="#0D8DB0")
define a = Character( 'Art', color="#0D8DB0")
define b = Character('Burn', color="#0D8DB0")
define c = Character('Carl', color="#0D8DB0")
define w = Character('Gato', color="#0D8DB0")
image fondo = "menu3.jpg"
image carcel = "interno.jpg"
image testigos ="testigos.png"
image victima ="victima.png"
image negro = "#000000"
image sala = "saladesospechosos.png"
image detective = "detective.png"
image art = "art.png"
image burn = "burn.png"
image carl = "carl.png"
image gato = "gato.png"

# The game starts here.
label start:

scene fondo9

show detective
e "Bienvenidos, Soy un Detective tratando de resolver un caso de asesinato."
e "Tenemos tres sospechosos de este asesinato; Art, Burn y Carl."
hide detective
show testigos at left
e "Los testigos afirman haber los vistos con la victima (Caroline) 3 dias antes de su asesinato."
scene victima
e "... eh aqui la victima."
e "Caroline fue encontrada en las afueras de la ciudad."
scene sala
e "eh dado con los sospechosos."
e "Aqui sus declaraciones:"
scene carcel
show art at left
a "Lo unico que puedo decir es lo siguiente:"
a "Burn era amigo de la victima, pero la victima y Carl eran enemigos mortales"
show gato at left
w "Y este no era amigo de nadie!!, y ese burn no me cae bien, habla mucho"
return
