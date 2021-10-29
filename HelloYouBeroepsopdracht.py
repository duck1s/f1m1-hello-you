import os

def cls():
    os.system("clear")

def voorbeeldFunctie(input1, input2, answer):
    if answer == "A" or answer == "a":
        input1()
    if answer == "B" or answer == "b":
        input2()
    if answer == "restart" or answer == "Restart" or answer == "Reset" or answer == "reset":
        voorstellen()

# Voorstellen
def voorstellen():
    cls()
    print("Hallo, ik ben Achmed. Ik ben 17 jaar oud en ik woon nu in Amsterdam. \n"
          "Zoals jullie misschien al verwachten, woon ik niet heel mijn leven in Nederland. \n"
          "Ik ben namelijk een vluchteling. Toen ik 12 was ben ik samen met mijn gezin gevlucht\n"
          "vanuit Afghanistan naar Europa en uiteindelijk door naar Nederland. Ik ben een \n"
          "aardige en verlegen jongen met een gezellige en fijn gezin. Mijn gezin bestaat uit \n"
          "mijn vader, moeder, zusje en ik. Samen zijn wij met 4 mensen.")
    input()
    beginscene()

# Beginscene
def beginscene():
    cls()
    print("Het begon allemaal op 4 juni 2016. Ik was op school en er waren opeens \n"
          "minder kinderen in de klas. Het waren maar een paar mensen, dus aan het \n"
          "begin vond ik het nog niet apart. Een dag later waren er nog minder kinderen \n"
          "en de dag daarna nog minder. Nu begon ik het raar te vinden. Ik ging naar mijn \n"
          "vader om te vragen waar iedereen naartoe was. Mijn vader vertelde me dat het \n"
          "sommige mensen bang waren dat er een oorlog zou komen. Later die avond hoorde \n"
          "ik opeens heel hard geluid. Toen wist ik nog niet wat dat was, maar nu weet ik \n"
          "dat het schoten waren die ik die avond hoorde. Ik ... \n"
          "")
    print("    A. ren naar buiten om te kijken wat er is")
    print("    B. ren naar mijn vader omdat ik bang ben")

    answer = input()
    voorbeeldFunctie(stukje2, stukje3, answer)

def stukje2():
    cls()
    print("Ik zie allemaal mensen in legerauto's onze buurt in rijden. Ze komen naar \n"
          "me toe. Ik probeerde weg te rennen, maar ze waren te snel. Ze pakte me op \n"
          "en namen me mee naar een legerbasis. Ik zit in een gevangenis samen met \n"
          "allemaal andere gevangenen. Een dag later hoor ik iemand praten over ontsnappen. \n"
          "Ik ga naar ze toe en ik doe mee met de ontsnapping. Een van de gevangenen wordt \n"
          "mee naar buiten genomen. Dit is het perfecte moment om weg te rennen. Ik …\n"
          "\n"
          "    A. ren samen met iedereen naar buiten\n"
          "    B. blijf in de gevangenis want ik durf niet")

    answer = input()
    voorbeeldFunctie(stukje4, stukje5, answer)

def stukje3():
    cls()
    print("Mijn vader neemt ons mee naar onze oom. Mijn oom heeft een boot. We gaan met de \n"
          "boot naar Europa. De boot is best klein en we hebben maar weinig eten mee. \n"
          "Onderweg zien we andere zinkende boten. We laten meer mensen in onze boot en \n"
          "nemen ze ook mee. We komen aan in …\n"
          "\n"
          "    A. Nederland\n"
          "    B. Spanje")

    answer = input()
    voorbeeldFunctie(stukje6, stukje7, answer)

def stukje6():
    cls()
    print("In Nederland is iedereen heel aardig. Ze geven ons een treinkaartje en daarmee \n"
          "moeten we naar Groningen. In Groningen brengen ze ons naar een Asielzoekerscentrum. \n"
          "Daar krijgen we meer informatie over hoe lang het gaat duren totdat we officieel \n"
          "in Nederland kunnen wonen. Binnen 1 jaar kregen we een huis. We wonen nu in Utrecht \n"
          "en hebben een fijn leven.")
    input()
    stukje11()

def stukje7():
    cls()
    print("In Spanje is het wat ingewikkelder. We worden opgepakt door een boot van Spanje. \n"
          "Ze vertellen dat we niet welkom zijn in dit land. Ze zien dat we met niet al te \n"
          "veel mensen en er zijn ook kinderen. Ze laten ons voor deze ene keer toch het land binnen. \n"
          "We worden doorgestuurd naar een haven en daar worden we achtergelaten. We kennen hier \n"
          "niemand en iedereen kijkt ons raar aan. We gaan naar … \n"
          "\n"
          "    A. Het politiebureau\n"
          "    B. Een gemeentehuis")

    answer = input()
    voorbeeldFunctie(stukje8, stukje9, answer)

def stukje8():
    cls()
    print("We lopen naar het politiebureau. Het is niet heel druk. We lopen naar de balie en \n"
          "vertellen de officier over onze situatie. Hij vind ons irritant. Hij wil niet dat \n"
          "we zijn land binnenkomen en stuurt ons weg. We moeten naar het gemeentehuis.")
    input()
    stukje9()

def stukje9():
    cls()
    print("Bij het gemeentehuis is het druk. Er zijn veel meer mensen zoals ons. \n"
          "We moeten in een lange wachtrij staan. Na veel wachten worden we \n"
          "doorgestuurd naar een een kamertje. In het kamertje worden we ondervraagd over \n"
          "onze achtergrond en welke banen we hadden voor de oorlog. Na een lang gesprek komen \n"
          "we in aanraking voor asiel. We krijgen we horen dat we 2 weken moeten wachten voordat \n"
          "we antwoord kunnen krijgen. Na een tijdje wachten krijgen we een eigen huis.")
    input()
    stukje10()

def stukje10():
    cls()
    print("We hebben een huis en iedereen is heel blij. Het volgende doel is het zorgen voor banen \n"
          "zodat we in het land kunnen blijven. Als we namelijk geen geld verdienen kunnen we geen \n"
          "eten kopen en dan zullen we uiteindelijk weer moeten verhuizen naar een andere plek. \n"
          "Ik ga solliciteren voor een baan als … \n"
          "\n"
          "    A. Loodgieter\n"
          "    B. Advocaat")

    answer = input()
    voorbeeldFunctie(stukje11, stukje12, answer)

def stukje11():
    cls()
    print("Ik heb mijn kinderen ingeschreven voor een plek om school. Na 4 keer solliciteren \n"
          "ben ik aangenomen bij een klein reparatie bedrijf waar ik kan werken als loodgieter. \n"
          "Het werk is moeilijk en zwaar maar het betaald goed. Ik heb nu genoeg geld om voor een \n"
          "huis en eten te betalen voor ons gezin. In de toekomst wil ik …\n"
          "\n"
          "    A. Een nieuw huis en een auto\n"
          "    B. Een eigen bedrijf oprichten")

    answer = input()
    if answer == "A" or answer == "a":
        print("Einde!")
    if answer == "B" or answer == "b":
        stukje9("Einde!")

def stukje12():
    cls()
    print("Ondertussen heb ik mijn kinderen opgegeven voor een plek bij een school. \n"
          "Na 2 week solliciteren kreeg ik door dat een baan als Advocaat moeilijk ging worden. \n"
          "Dat kwam doordat ze in Spanje andere regels hebben voor advocaten. Als je uit een ander \n"
          "land komt ken je andere regels waardoor je opnieuw een diploma moet halen. Ik besluit toch \n"
          "om loodgieter te worden.")
    input()
    stukje11()

def stukje4():
    cls()
    print("Buiten zien we allemaal soldaten. We moeten heel snel rennen. \n"
          "Ze zijn veel sneller en ze hebben guns. Ze schieten ons neer. \n"
          "Einde.")

def stukje5():
    cls()
    print("Ik hoor buiten gillende mensen. Ik zie dat ze proberen weg te rennen. Oh nee. \n"
          "Ik hoor gunshots. Waarschijnlijk zijn ze dood. Ik hoop dat ze mij niet ook vermoorden. \n"
          "Samen met de andere mensen in de gevangenis blijven we stil en we wachten tot er iemand \n"
          "langs komt. We horen nog meer schoten. Misschien is het het verzet. \n"
          "Ze komen de gevangenis binnen en helpen ons naar buiten. Ik ga met het verzet \n"
          "mee en ze brengen me naar een ander dorp. We …\n"
          "\n"
          "    A. Ontsnappen en vluchten naar het vliegveld\n"
          "    B. Blijven en wachten waar we naartoe gaan")

    answer = input()
    voorbeeldFunctie(stukje13, stukje14, answer)

def stukje14():
    cls()
    print("We blijven bij het verzet en gaan naar een ander dorp om mensen te bevrijden. \n"
          "We gaan naar het dorp Habibo en proberen de Taliban weg te jagen. Er zijn veel \n"
          "soldaten en na een tijdje is het gelukt. We hebben een dorp bevrijd. We besluiten \n"
          "om met een deel van het verzet in dit dorp te blijven en dit als verzet basis te maken. \n"
          "Na een paar weken besluiten de leiders dat ik de organisator mag worden van deze basis. Ik … \n"
          "\n"
          "    A. Vertrek naar andere dorpen om mensen daar te helpen.\n"
          "    B. Ga naar het vliegveld om daar mensen het verzet te laten joinen.")

    answer = input()
    voorbeeldFunctie(stukje19, stukje20, answer)

def stukje19():
    cls()
    print("Ik ga met een groep van 10 mensen op zoek naar andere dorpen. Na een maand hebben \n"
          "we 3 andere dorpen geholpen en nieuwe mensen overgehaald. Ik besluit dat ik beter \n"
          "mensen kan helpen door naar het vliegveld te gaan, want daar zijn meer mensen.")
    input()
    stukje20()

def stukje20():
    cls()
    print("Bij het vliegveld is veel chaos. Er zijn hier 10 duizenden mensen. We lopen naar \n"
          "rustige plekken om chaos te vermijden. We nemen 20 mensen mee in onze auto’s en \n"
          "rijden terug naar ons kamp. De komende 2 weken hebben wij elke dag mensen opgehaald \n"
          "van het vliegveld. Er zijn steeds minder mensen bij het vliegveld en we zijn blij \n"
          "dat we zo veel mensen hebben kunnen helpen.")
    input()
    stukje21()

def stukje21():
    cls()
    print("In de toekomst wil het verzet veel meer mensen bevrijden. Uiteindelijk willen \n"
          "we zo veel mensen hebben verzameld bij het verzet dat we een kans hebben om de \n"
          "Taliban te verslaan. We zijn daar helaas nog lang niet en we blijven mensen bevrijden \n"
          "om uiteindelijk op dat punt te komen.\n"
          "\n"
          "Einde!")

def stukje13():
    cls()
    print("We rennen naar het vliegveld. Er zijn hier niet normaal veel mensen. Het vliegveld \n"
          "is nog niet overgenomen door de Taliban. Er gaan mega grote vliegtuigen vol mensen \n"
          "vliegen naar andere landen. Om in zo een vliegtuig te komen moet je over een hek \n"
          "klimmen of wachten tot de mensen van het leger je binnenlaten. We lopen naar de \n"
          "andere kant van het vliegveld en klimmen over het hek waar niemand kijkt. We …\n"
          "\n"
          "    A. Vragen aan iemand die er niet gevaarlijk uitziet wat we moeten doen.\n"
          "    B. Rennen naar een vliegtuig en stappen in")

    answer = input()
    voorbeeldFunctie(stukje15, stukje16, answer)

def stukje15():
    cls()
    print("De lopen naar een man toe die geen wapens heeft. We vragen hem waar we naartoe \n"
          "moeten om in een veilig land te komen. Hij vertelt ons dat duitsland een goed \n"
          "idee is en hij wijst naar het vliegtuig.")
    input()
    stukje16()

def stukje16():
    cls()
    print("We sneaken naar het vliegtuig toe en klimmen in de laadruimte. Het vliegtuig is heel groot. \n"
          "We komen er wel achter dat de laadruimte niet goed geïsoleerd is en dat het waarschijnlijk \n"
          "heel koud gaat worden. We …\n"
          "\n"
          "    A. Blijven in de laadruimte\n"
          "    B. Breken in bij de cabine voor mensen")

    answer = input()
    voorbeeldFunctie(stukje17, stukje18, answer)

def stukje17():
    cls()
    print("We blijven in de laadruimte. Het is heel koud en we kunnen geen dekens vinden. \n"
          "Na een paar uur vliegen besluiten we toch om naar de cabine te gaan zodat we veilig \n"
          "naar Duitsland kunnen komen.")
    input()
    stukje18()

def stukje18():
    cls()
    print("We lopen de trap op en gaan naar de deur. De deur zit op slot. We kloppen aan. \n"
          "Er komt iemand naar ons toe. Hij schrikt. Hij verteld ons dat we meteen weg moeten \n"
          "want als andere mensen ons zien worden we van het vliegtuig gegooid. We verstoppen \n"
          "in een kastje totdat we aankomen in Duitsland. We komen aan in Duitsland. De mensen \n"
          "hier zijn heel aardig. Na een tijdje wachten krijgen we een huis en na nog een tijdje \n"
          "hebben we allemaal een baan en zitten onze kinderen op school. In de toekomst wil ik \n"
          "een bedrijf starten die geld verzameld voor vluchteling zodat er meer vliegtuigen en \n"
          "andere diensten kunnen komen voor mensen die moeten vluchten vanwege oorlog of andere \n"
          "gevaarlijke dingen.\n"
          "\n"
          "Einde!")

voorstellen()
