from codecs import namereplace_errors
import time

print("(=================================)")
print("(     THE TOMB OF CLEOPATRA       )")
print("(=================================)")
print("")

name = input("hallo, hoe mag ik je noemen? ")
print (f"hallo {name}")
print ("je bent een makelaar met een groote intressen in het oude egypte, je besteet al je vrije tijd aan het ontcijferen van hyroglyven en de oude goden.")
ready = input(f"ben je er klaar voor {name}? y/n ")
if ready == "n":
    print(f"oke, {name} jij mag niet meer. ga maar huilen bij mama.")
    raise NameError("jankbal")
else: 
    print ("je bent op je zoveelste klus als makelaar bij een oud vrouwtje om de zolder op te knappen. op de zolder heeft zij een oude doos gevonden.")
    doos_hebben = input("ze vraagt, wil jij deze oude doos mee nemen? jij andwoord y/n ")
    if doos_hebben == "n":
        print("je maakt rustig de klus af en gaat door naar de volgende dit is het einde van jou verhaal")
        raise NameError("watje")
    else:
        print("je neemt de doos mee naar huis en zet hem om de eettafel.")
        open_doos = input ("je vraagt jezelf af of je de doos wel moet openmaken omdat hij zooo oud is. y/n ")
        if open_doos == "n":
            print("je gaat avondeten maken je buik rammeld je maakt je favorite maaltijd klaar en kan niet wachten om het op te eten je bent zelfs zo enthousiast dat \nje de doos omstoot!")
            time.sleep(3)
        print("je kijkt naar de doos en je schuift wat stof aan de kant het lijkt wel op een kaart! je ziet de symbolen op de kaart en ziet dat het een kaart\nis naar de tombe van cleopatra!")
        naar_egypte = input(f"je vraagt je af of je de kaart moet volgen of niet. wat denk je {name}? y/n ")
        if naar_egypte == "n":
            print(f"je gaat de volgende dag weer naar het werk voor de laatste finishing touches. \nje maakt het af en de klant vraag hey, {name} wat heb je eigelijk met de doos gedaan?")
            time.sleep(3)
            print("je zecht dat er een kaart in zat die naar de tombe van cleopatra zou lijden. ze vraagt of je hem achter na gaat want ze weet \nhoeveel je van egypte houd.")
            time.sleep(3)
            print("je zecht dat je het nog niet zeker weet maar ze zecht dat ze wil dat je je dromen achterna gaat met de wijsheid die alleen een oud persoon heeft \nzorgt ze er toch voor dat je naar egypte gaat")
        print("je boekt een mooi hotel en vlugt en stapt op het vliegtuig")
        time.sleep(2)
        voertuig = input("op het hotel kun je de volgende voertuigen kiezen.\n1) een jeep met een touw schep en navigatie\n2) een snelle quat met een schep\n3) een trage kameel met een tent\n1/2/3? ")
        if voertuig == "1":
            print (f"de jeep een goede keuze {name}!")
            print ("je springt in de jeep en begind te rijden")
            print ("je volgt de kaart zogoed als je kunt maar je ziet halverwege dat je hem de hele tijd al op zijn kop houd!")
            print ("gelukkig heb je voor de jeep gekozen je voerd de locatie in en begind weer te rijden")
        elif voertuig == "2":
            print (f"aha {name}, je gaat dus voor de quat\nje krijgt de uitleg van de quat en begind je tocht\nje quat is snel dus je bent er zo")
        elif voertuig == "3":
            print(f"zozo {name}, je gaat voor de style points!\nje begind je tocht maar je kameel is traag dus het word snel nacht\nje zet je tent op en gaat slapen\nje word wakker... maar je bent berooft!\nje probeerd je weg terug te vinden naar het hotel maar tervergeefs\nhier eindigt jou verhaal")
            raise NameError("dood")
        graaf_boven = input(f"poepoe {name}, je bent eindelijk aangekomen en je ziet 2 mogelijke ingangen\nje kunt via boven of de voorkant uitgraven\n1)boven 2)graven")
        if graaf_boven == "1":
            print("je klimt naar boven en gaat kijken het is een diepe put")
            if voertuig == "1":
                print("gelukkig heeft de man van de jeep je uitgelegt dat deze jeep is uitgerust met een speciaal lier systeem")
                print("je pakt de lier en laat jezelf naar benede zakken")
            else:
                print ("je zal toch moeten gaan graven!")
                print("je pakt je schep en je begind te graven")
                print("je weet gelukkig van aanpakken en bent zo klaar")
        else:
            print("je pakt je schep en je begind te graven")
            print("je weet gelukkig van aanpakken en bent zo klaar")
        print("je komt binnen en ondsteekt de bouwlamp die je mee hebt genomen van je werk")
        print("je weet dat egyptische tombes vaak veel vallen hebben en dit al wel geen uitzondering zijn dus wees op je hoede")
        print("je loopt verder de tombe in en stapt op een tegel die wegzakt\nje hebt dit natuurlijk in elke film ooit wel gezien\ner zouden nu speeren uit de muur moeten komen... maar er gebeurd niks\nje wacht nog even en bedenkt dat het systeem vast kapot is na 2052 jaar")
        print("je waarschuwd jezelf nog maals dat je op je hoede moet zijn en loopt verder")
        print("1) queen of the nile")
        print(" _  ,~~~~~~~~~~,")
        print("9>)(_______     |")
        print(" (()_____   /    )_")
        print("  /     ///  / /)(()")
        print("  |--    //___ \)())")
        print(" )c>-    ___    )())")
        print(" /      s)_     )  (()")
        print(" `      | _     )   ())")
        print("  >     /  _   )    (()")
        print("  L____/    -_)     ())")
        print("     \      |      (()")
        print("      \      \    (()")
        print("       \      \   ())")
        print("       _\    _<7\ (()")
        print("")
        print("2) symbol of the underworld")
        print("         , - ~ ~ ~ - ,	")
        print("     , '               ' ,")
        print("   ,           8           ,")
        print("  ,        8   8   8        ,")
        print(" ,          9  8  9          ,")
        print(" ,	     9 8 9           ,")
        print(" ,           88888           ,")
        print(" ,           98 89           ,")
        print("  ,         98   89          ,")
        print("   ,       9       9	    ,")
        print("     ,                   , '")
        print("       ' - , _ _ _ , - '")
        print("")
        gang = input("je ziet 2 gangen met vreemde symboolen welke gang kies je? ")
        if gang == "2":
            print(f"je loopt de gang in... \nje kijkt om je heen en let niet goed op\ndan val je ineens het is een put met hele glade muuren.. je kijkt om je heen en ziet nergens een uitweg... alles wat je ziet zijn de overblijfselen van je voorgangers\nhelaas hier eindigt you verhaal {name}")
            raise NameError("dood")
        else: 
            print("je hebt de goede gang gekozen dit was de koningin van de neil de levensbron van egypte! ")
            print("je loopt verder maar de gang loopt dood?\nzou er ergens een verborgen doorgang zijn?")
            print("je kijkt nog eens goed naar de muur en ziet wat beestjes uit de spleed tussen 2 tegels komen\nje gooit je volledig tegen de steen aan en hij beweegd!\nje kruipt door de doorgang die is ondstaan en daar zie je het! alle schatten en de sacrofaag van cleopatra!")
            print("je pakt zoveel als je kan en gaat naar buiten je gooit alles in zakken maar je weet niet wat je er mee moet doen\nje eerste instinkt was om de spullen te verkopen op de zwarte markt maar je kunt de spullen ook doneeren aan musea")
            laatse_keuze = input("doneren/verkopen? ")
            if laatse_keuze == "doneren":
                print(f"je hebt een goede keuze gemaakt je belt de ambasade en je word beschoud als een nationale held er word zelfs een {name}museum geopend!")
                print("ook krijg je een mooi geldbedrag als beloning waar je een deel van aan de oude vrouw geeft\nlater begin je aan een boek van je avondtuur en het word een bestseller")
                print("")
                print("(=================================)")
                print("(          THE END OF             )")
                print("(     THE TOMB OF CLEOPATRA       )")
                print("(=================================)")        
            elif laatse_keuze == "verkopen":
                print("je verkoopt de schatten voor een bedrag van $67.000.000 je besluit een eiland te kopen en leeft daar de rest van je levensdagen uit")
                print("")
                print("(=================================)")
                print("(          THE END OF             )")
                print("(     THE TOMB OF CLEOPATRA       )")
                print("(=================================)")      