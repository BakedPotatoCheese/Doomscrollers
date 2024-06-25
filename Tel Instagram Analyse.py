import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

text = """verkiezingen, stemmen, coaching




compliment, aardig, waardering, coaching








haar, stijlist, coaching



bloem, slechtnieuws, opvoedingtips













bananenbrood, koken, vegan, coaching






natuur, dieren, rust, coaching





coaching, doel






vrienden, samenkomen, coach




interview, coaching









verjaardag, vrienden, familie, coaching, feestdag






vrouwendag, coaching, feestdag



boeken, honden, coaching




samenwerking, coaching









samenwerking, coaching







verjaardag, kinderen, coaching, feestdag










kunst, bloemen



















boeken, coaching




nieuwsbrief, coaching






familie, kerstmis, lockdown, hulp, feestdag












vakantie, coaching



honden, coaching



korting, coaching










samenwerking, coaching







kerstmis, kado, feestdag












jaarwisseling,rust, coaching, feestdag









korting, coaching, feestdag, cadeau










korting, coaching, feestdag, cadeau













workshop, doomscrolling
















cadeau, coaching, doomscrolling, korting















doomscrolling, slapen, dankbaarheid





boeken, coaching







korting, coaching







halloween, feestdag, familie, coaching



boeken, koffie, katten, rust, coaching



vakantie, coaching, korting











coaching, dankbaar





kerstmis, feestdag, muziek, concert




natuur

socialemediastop, rust, coaching







coaching, koffie, review









boeken, coaching





vrienden, dankbaar, coaching



katten, coaching



concert, muziek, coaching



kinderen



boeken, lidmaatschap, coaching






eten, coaching








coaching, lidmaatschap









doomscrolling, freeschoolmeals, jamieoliver








coaching, dankbaar, blacklivesmatter







boeken, dankbaar, coaching





bloemen, compliment, coaching



eten, samenwerking, coaching







pridemonth, jezelf, coaching



kinderen, mijlpalen



kleding





reclame, coaching



honden, hondenadoptie, coaching





vooruitzicht, reclame,









coaching, uitjecomfortzone






coaching



vragen, reflectie



mijlpaal, rijbewijs, kinderen



doel, coaching



verjaardag, kinderen, feestdag, eten






kaartspel, rust




boek, coaching



honden, vrienden



dankbaar, coaching



eten, vegan



feestdag, katten



theater




coaching, feedback, rust





boeken, kinderen, coaching



review, coaching




progressie, doorzetten, coaching



school



vegan, coaching







kleuren, kleding, dieren






stemmen, verkiezingen



lezen, boeken, coaching

stress, doorzetten
























jaarwisseling, feestdag



kerstmis, feestdag



dankbaar

theater, komedie











coaching





eten, koken, coaching



boeken, coaching

telefoonhoesjes, reclame, kerstmis

















rust, coaching




feestdag



boeken

stress, stemmen



doomscrolling





boeken





gezondheid, gewoontes



energie



coaching



socialemedia, samenkomen, doomscrolling, gezondheid







anti-perfectionisme,  coaching



doomscrolling



gezondeheid








gezondheid



breintraining



mediteren



aanmoedigentotjoyscrollen

coaching











alligator, natuur


museum, kinderen, kunst









aanzettentotjoyscrollen















gewoontes



hoop









scrollen, reflectie

vrijheid, reflectie



gewoontes




natuur
















doomscrolling, kleuren, aanzettentotjoyscrollen













welzijn



welzijn



vakantie



energie



familie

zorgen



bewegen



aanzettentotjoyscrollen
natuur, dieren, vegan







bloemen





coaching






telefoonhoesjes











anti-perfection







aanzettentotjoyscrollen



halloween, feestdag








jongeren



doorzetten



dieren, feestdag, honden









doel







natuur, zee



natuur



natuur, zee



natuur



doomscrolling




natuur, zee



zee, natuur



natuur, zee







natuur, zee


reflectie



rust



feestdag










natuur




natuur



podcast




doomscrolling, bloemen







boeken





natuur



boeken





familie, kinderen












rust, slapen



koffie, natuur









natuur, koffie









natuur, gewoontes











zorgen



familie, natuur












reizen, familie











natuur



































































familie, reizen





















feestdag, verjaardag



natuur, familie, gewoontes











familie









liefde











welzijn, gezondheid





reizen, natuur


















reizen, natuur


















haar, kinderen




koken












energie

stemmen, verkiezingen



perfectionisme, coaching







cat, natuur, dieren

loslaten








vooruitkijken

boeken









telefoonhoesjes, reclame
















jaarwisseling, feestdag


















natuur, honden








vakantie, coaching














reflectie




kinderen, koken




kerstmis, feestdag




kunst, familie












































































reflectie



honden








reflectie








uitjecomfortzonegaan

liefde



reflectie, socialemedia





familie

koffie, natuur















aanzettentotjoyscrollen


















reflectie















liefde

liefde












samenkomen



coaching




natuur, slapen, dankbaar






feestdag





positiviteit








kinderen, familie, rust

natuur
















liefde
















natuur









succes, coaching


















boeken




doomscrolling

dankbaar




natuur, welzijn




















dankbaar, fotos




















dieet, eten, gezondheid, sport









natuur




verandering












familie, therapie





boeken, dieren




rust




coaching







reflectie, focus






boeken



socialemedia







natuur








gewoontes







honden, dieren



samenwerken




boeken






dankbaar













loslaten



doomscrolling













rust

reflectie











dankbaar















fotos, dankbaar
















waardering
















fotos, dankbaar

















fotos, dankbaar

















zorgen






fotos, dankbaar

















doomscrolling


dankbaar















dankbaar















dankbaar















dankbaar















fotos, dankbaar
















emoties, gezondheid










aandacht




fotos, dankbaar
















liefde, jezelf






verandering, jezelf





fotos, dankbaar

















katten, dieren









vooruitgang, hulp, samenkomen



dankbaar, coaching




eten, vegan, handgemaakt




dankbaar, regen








lezen










fotos, dankbaar















coach, gezondheid, dankbaar










reflectie



toezettentotjoyscrollen









coaching, dankbaar, mijlpaal














socialemedia, doomscrolling, nieuws, toezettentotjoyscrolling























succes, coaching





loslaten, welzijn, gezondheid




















gezondheid















doomscrolling, hulp, emoties, socialemedia





opvoeden, familie









beschamen, gezongheid





















doel, hulp






feestdag, reflectie




bang




socialemedia, zorgen









paradigmawisseling

















halloween, feestdag



scrollen, socialemedia, doomscrollen















liefde, familie






rust, coaching






doomscrolling, toezettentotjoyscrolling













jezelf, reflectie










dankbaar, gezondheid








coaching, handgemaakt























rust, vakantie




vakantie





vooruitkijken






hulp









dankbaar















pride, doomscrolling, liefde, rust




















familie, kinderen





mijlpaal, school





reflectie




rust, feest






samenkomen



























moederdag, feestdag, familie









rust, gezondheid, welzijn
























doorzetten





blacklivesmatter






familie















blog, vooruitkijken









emotie, dankbaar

















choosejoy




choosejoy, therapie



moederdag, feestdag, reclame










reflectie, jezelf, choosejoy






feestdag, film










dankbaar, reflectie















jezelf, eigenwaarde




rust




energie, coaching











choosejoy





choosejoy, socialemedia, gezondheid, doomscrolling, vegan











fotos, reflectie















reflectie





drinken, eten





vasten, ramadan, eten, geloof









reflectie, jezelf





handgemaakt, telefoonhoesjes





















weer, storm, dankbaar















natuur, telefoonhoesjes


















doomscrolling



































muziek, vrienden, trots
















dankbaar





boeken, verandering, socialemedia













vrouwen










natuur, vrienden, dankbaar















fotos, dankbaar



































natuur, vrienden, gezondheid, dankbaar



















verandering, quotes, coaching



vrouwen, qoutes















vrouwen, quotes














vrouwen, quotes










vrouwen, quotes









gewoontes, doel




natuur






vrouwen, quotes









vrouwen, quotes










vrouwen, quotes











vrouwen, quotes








reizen, natuur, avontuur






vrouwen, quotes









choosejoy, verandering, doomscrollen











vrouwen, quotes









vrouwen, quotes















verandering, doel






telefoonhoesjes, feestdag, dankbaar, reflectie



















telefoonhoesjes














verandering, hulp, visie, choosejoy










quotes, vrouwen



















vrouwen, quotes










vrouwen, quotes











vrouwen, quotes









vrouwen, quotes










vrouwen, quotes









vrouwen, quotes








kunst, schilderij, hokusai









doel, succes






quotes, vrouwen








quotes, vrouwen










quotes, vrouwen










quotes, vrouwen








hokusai, kunst, Kanagawa







quotes, vrouwen








natuur, noorderlicht, reizen






quotes, vrouwen








quotes, vrouwen








quotes, vrouwen, coaching


















natuur, honden






quotes, vrouwen







honden

quotes, coaching






reclame











kunst, doomscrolling


















reizen, natuur, tropen, winter







natuur, pompoenen












koffie, energie















freethenipple, vrouwen, feminisme







telefoonhoesjes








vakantie, liefde



verjaardag, feestdag, familie, doel




tropen, natuur, reizen







telefoonhoesjes






















verjaardag, feestdag




natuur






katten







rust, jezelf, energie






welzijn



doel






quote, coaching










katten

verandering, jezelf





choosejoy







scrollen











hulp, choosejoy



blog, verandering




kerstmis, feestdag





choosejoy
















honden, dieren




doomscrolling, gezondheid, natuur







natuur, avontuur, reizen, ijsland, ijsland, ijsland, ijsland, ijsland, ijsland, ijsland




















natuur, zee



valentijnsdag, liefde











massage, reclame











storm, natuur



scrollen, doomscrolling









coaching














quotes












flowers

valentijnsdag, liefde



coaching







ijsland, natuur













ijsland, natuur

































telefoonhoesjes















reflectie, choosejoy



ijsland, fotos, natuur






natuur






doorzetten



honden

doel, choosejoy





sneeuw, winter, natuur







natuur



telefoonhoesjes, tropen, Amazone



















blog













natuur





boeken








vrouwen






katten, honden, dieren










kerstmis, familie





boeken







ijsland, natuur









boeken







doomscrolling

ijsland, natuur






ijsland, natuur, socialemedia, doomscrolling
















honden, dieren, adoptie







valentijnsdag, telefoonhoesjes





















kerstmis, feestdag









ijsland, natuur, avontuur, reizen









georganiseerd, productiviteit, gewoontes, muziek





























doomscrolling, choosejoy, choosejoy

socialemedia











doomscrolling, choosejoy, dieren

bloemen

















natuur, winter, telefoonhoesjes

















kerstmis, feestdag












ijsland, natuur














doomscrolling, samenwerken, choosejoy, dankbaar





















korting, reclame


















natuur



joke



muziek















kerstmis, grammy, feestdag



























cadeau, kerstmis, feestdag





kerstmis























doomscrolling, honden, sneeuw, choosejoy














choosejoy





lockdown




















choosejoy







coaching








reflectie







gezondheid












jaarwisseling, doel, visie









eten, bagel






natuur, ijsland




jaarwisseling, eten, koken,feestdag, doel












dieren, natuur, ijsland

























covid, lockdown





kerstmis





















ijsland, natuur










doel, visie, vrouwen













ijsland, natuur


















toernooi, visie





kinderen





kerstmis, feestdagen




reflectie, vrienden, familie, lockdown























ijsland, kerstmis
























ijsland, natuur












influencer



kerstmis,




film















kerstmis





kerstmis

























































familie, rust, vakantie






visie, doel



meme



winter, quarantaine








dieren




dieren, telefoonhoesjes





















dieren, ratten, pizza



chocolade, toernooi, quarantaine
babies
















ijsland, natuur




kerstmis






comfortabel





natuur, ijsland






avontuur, avontuur





dieren




katten







haar





kerstmis

















haar





scrollen, doomscrolling



ijsland, muziek, natuur, eten























tempel, oud

slapen









vrouwen

enrgie, visie














doomscrolling, gezondheid, ijsland

















gezondheid, doomscrolling, welzijn

















kleuren





gezondheid, ijsland, reizen
























dieren
























muziek, quarantaine
















katten, dieren, babies


























visie, doel






katten, dieren




muziek












doomscrolling, nieuws






trots, kunst











choosejoy




winter


doomscrolling, choosejoy



aanzettentotjoyscrolling



vakantie
sneeuw







slapen








kerstmis







doomscrolling


ijsland


natuur



joyscroll.com






choosejoy









choosejoy
ijsland
















doomscrolling

ijsland






ijsland


choosejoy


socialemedia










biden


honden, dieren












vrienden, speelgoed







ijsland, reizen, kerstmis, doomscrolling, ijsland











jezelf




choosejoy






hulp, coaching

mediteren




biden




sneeuw






honden


weer, natuur





















biden





welzijn

doomscrolling




ijsland




doomscrolling


honden


weer
therapie
dieren
choosejoy


muziek




reflectie






reflectie






weer

vakantie
katten
dieren



fotos
reflectie










weer

koken, choosejoy, aanzettentotjoyscrolling











cadeau, koffie, weer



verandering







kerstmis









podcast






visie, doel, gewoontes

hulp



succes
dankbaar
















vaderdag, kinderen, liefde




fotos, dankbaar



















dankbaar















babies














rust
honden
dieren

ramadan



choosejoy

rust

jezelf



katten
dieren




telefoonhoesjes











reflectie, choosejoy



vrouwen, quotes

























vrouwen, quotes










doorsturen, dankbaar, vrienden























katten, dieren


vrouwen, quotes









vrouwen, quotes



















doomscrolling



choosejoy
welzijn


doomscrolling











katten
dieren







films


honden








choosejoy




vakanite




ijsland


















kleuren
telefoonhoesjes


vrouwen, quotes
kerstmis
doomscrolling
kerstmis
doel
visie
inspiratie
telefoonhoesjes
kerstmis
podcast
reflectie
reizen
avonturen
ontmoeten
samenkomen
choosejoy
doomscrolling
choosejoy
ijsland
natuur
muziek
quotes
choosejoy
verkiezingen
dankbaar
babies
boeken
kerstmis
otter
scrollen
doomscrolling
biden
trump
choosejoy
ijsland
doomscrolling
natuur
kunst
identiteit
reflectie
welzijn
gezond
gewoontes
"""

# Split the text into lines
lines = text.strip().split("\n")

# Initialize a Counter to count the words
word_counter = Counter()

# Count the occurrences of each word
for line in lines:
    words = line.split(", ")
    word_counter.update(words)

# Convert the Counter to a dictionary and sort it by frequency
word_counts = dict(word_counter)
# Sort the dictionary by frequency in descending order
sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

print(sorted_word_counts)
