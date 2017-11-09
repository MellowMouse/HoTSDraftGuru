# HoTSDraftGuru
A small program that takes a Heroes of the Storm draft so far as input and returns recommended heroes based on things like battlefield, allied and enemy picks thus far, etc...

All of the results here are calculated based on hero strengths and weaknesses defined by me in the first hero_list dictionary.

As we update this dictionary, the results should become more and more relevant.

Usage:

python python.py -e <comma-separated-list-of-enemy-heroes-chosen-so-far> -a <comma-separated-list-of-allied-heroes-chosen-so-far> -b <battlefield-name-enclosed-in-quotes>

This will generate a basic report on recommended heroes, non-recommended-heroes, controversial heroes, and neutral heroes.

Ex.

python ../HoTSDraftGuru/python.py -e genji,cassia,samuro,azmodan,sonya -a tracer,morales,anubarak,leoric,lucio -b "battlefield of eternity"

Will output:

ALLIED HEROES:
tracer
morales
anubarak
leoric
lucio

ENEMY HEROES:
genji
cassia
samuro
azmodan
sonya

BATTLEFIELD: battlefield of eternity

PICK THESE HEROES:
medivh:
Any hero with multiple heroes makes for good fast stacking of medivh's quest.
Protect strong against high burst damage skills like pryroblast.


anubarak:
Cocoon invaluable against heroes with extended ults, ex. genji dragonblade. completely nullifies it.


tassadar:
Good synergy with any up-front or dive heroes


DONT PICK THESE HEROES:
illidan:
Illidan is weak against opponents with blinds.
Illidan is weak against opponents with CC's.

CONTROVERSIAL HEROES:
PICK THESE HEROES IF YOU LIKE THEM:
auriel
alarak
ana
lucio
artanis
sgt
uther
gall
xul
stukov
dehaka
ragnaros
chen
chromie
cassia
sylvanas
li-li
nova
leoric
vikings
kerrigan
murky
guldan
thrall
butcher
cho
junkrat
jaina
sonya
arthas
lt-morales
gazlowe
stitches
genji
garrosh
azmodan
valeera
rehgar
tychus
zarya
zagara
kelthuzad
brightwing
falstad
greymane
zuljin
nazeebo
muradin
diablo
kharazim
rexxar
johanna
raynor
tyrande
malfurion
zeratul
dva
probius
valla
kaelthas
etc
varian
malthael
lunara
abathur
tyrael
samuro
tracer

