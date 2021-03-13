<%inherit file="/course-chapter.mako"/> <%self:lesson>

V této kapitole si představíme úplné základy programování v Pythonu. Zatím
ještě nebudeme psát celé programy, nýbrž budeme Pythonu posílat jednotlivé
příkazy a uvidíme, co nám odpoví. Jak už jsme si řekli dříve, počítač je v
podstatě jen trochu chytřejší a pekelně rychlá kalkulačka. Nejsnadněji se tedy
s programováním seznámíme, když si pomocí Pythonu necháme něco spočítat.

## Python konzole

Abychom si mohli s Pythonem povídat, musíme spustit takzvanou _Python
konzoli_. To je prostředí, ve kterém můžeme s Pythonem komunikovat a posílat
mu příkazy.

Pokud pracujete pod Windows, Python konzoli spustíte tak, že do termínálu
napíšete příkaz.

    
    
    $ python

Pozor, že znak dolaru není součástí příkazu. Používáme ho pouze k tomu,
abychom naznačili, že je třeba tento příkaz napsat do terminálu vašeho
operačního systému. Pokud pracujete na Macu nebo Linuxu, správný příkaz je

    
    
    $ python3

<%self:alert_warning> Pokud v Linuxu nebo na Macu spustíte příkaz jako ve
Windows, pravděpodobně se vám spustí jiná verze Pythonu, se kterou vám
následující lekce nebudou fungovat.

## Hodnoty

_Hodnoty_ představují všechny možné druhy dat, se kterými můžou naše programy
pracovat. Hodnoty se dle způsobu použití dělí do různých kategoríí zvaných
_datové typy_. Datových typů existuje velké množství. V tuto chvíli si
představíme ty nejzákladnější - celá čísla a desetinná čísla.

### Celá čísla

Nejjednodušší datový typ jsou _celá čísla_. Pod tento typ patří hodnoty jako
12, 1321500, -5, 0 a podobně. Pokud do Python konzole napíšete hodnotu, Python
vám ji vypíše zpátky, což znamená, že vám rozumí :-)

    
    
    >>> 127
    127

### Desetinná čísla

S celými čísly bychom si dlouho nevystačili. Dalším datovým typem tedy budou
_desetinná čísla_ , např. 13.4, 6.0, -0.0001, 0.0 apod. Pozor, že programátoři
vždycky píší desetinná čísla s tečkou, nikoliv s čárkou.

    
    
    >>> 3.141592
    3.141592

## Aritmetické operátory

Nyní už máme prostředky k tomu, abychom mohli pomocí Pythonu něco spočítat. V
Python máme k dispozici běžné aritmetické operátory:

  * sčítání: **+**
  * odčítání: **-**
  * násobení: *****
  * dělení: **/**

Díky těmto operátorům můžeme Python použít jako kalkulačku a psát _aritmetické
výrazy_ jako

    
    
    >>> 12 * 13 + 10
    
    
    >>> (13.4 - 1.4) / 4

Python ovšem nabízí ještě další užitečné operátory:

  * mocnění: **\*\***
  * celočíselné dělení: **//**
  * zbytek po dělení: **%**

Pomocí mocnění můžeme umocňovat čísla, například

    
    
    >>> 2 ** 8
    256

Pomocí celočíselného dělení můžeme dělit celá čísla

    
    
    >>> 14 // 4
    3

Pokud by nás zajímal zbytek po celočíselném dělení, můžeme použít operátor pro
zbytek po dělení

    
    
    >>> 14 % 4
    2

## Řetězce

Pokud chceme v Pythonu zadat nějaký kousek textu, použijeme takzvaný
_řetězec_. Řetězce se v Pythonu uzavírají do jednoduchých nebo dvojitých
uvozovek. Například:

    
    
    >>> 'martin'
    
    
    >>> '12. března 2018'
    
    
    >>> "prací prášek"
    
    
    >>> "Don't panic"

Řetězce se v něčem chovají podobně jako čísla, můžeme je například sčítat a
násobit

    
    
    >>> 'martin' + ' ' + 'podloucký'
    martin podloucký
    >>> 'bla ' * 10
    'bla bla bla bla bla bla bla bla bla bla '

<%self:exercises>

## Cvičení

<%self:exrc title="Jednoduchá aritmetika">

Použijte Python konzoli jako kalkulačku:

  1. Jeden lístek do divadla _Pěst na oko_ stojí 12 euro. Spočítejte měsíční příjem divadla ze vstupného přichází-li průměrně 174 návštěvníků na jedno představení a divadlo hraje 15 představení měsíčně.
  2. Divadlo se rozhodlo prodávat studentské vstupné ve výši 65% plného vstupného. Jak se změní měsíční příjem divadla pokud víme, že polovina návštěvníků jsou studenti?

<%def name="solution()"> <%self:exrc title="Hrátky s řetězci">

  1. Vytvořte řetězec obsahující jméno divadla.
  2. Vytvořte řetězec obsahující jméno divadla tak, že sečtete dohromady jednotlivá slova toho jména.
  3. Zkuste vynásobit řetězec celým číslem. Jaký jste dostali výsledek?
  4. Vytvořte řetězec který vypadá takto: '111111000000', ale místo šesti jedniček a šesti nul obsahuje 256 jedniček a 256 nul.

<%def name="solution()"> ${self.alert_done()}

## Bonusy

<%self:exrc title="Úroky">

Fíha banka a.s. nabízí na svých stránkách spořící účet s úrokem 2,4%. Když si
na takový účet uložíte 1 000 000 kč, kolik peněz nastřádáte za 10 let?

<%def name="solution()"> <%self:exrc title="Nový koberec">

Do malého sálu v divadle, který má tvar čtverce o rozloze 30m2 potřebujeme
koupit nový koberec. Jakou délku má mít strana koberce? Vejde se nám srolovaný
do dodávky s nákladovým prostorem dlouhým 5m?

<%def name="solution()"> <%self:exrc title="Shannonovo číslo">

  1. Takzvané _Shannonovo číslo_ má hodnotu 10120 a udává kolik nejméně lze odehrát různých šachových partií. Vytvořte řetězec, který obsahuje toto číslo zapsané běžným způsobem pomocí cifer. Například 103 je 1000, 106 je 1000000 atd.
  2. Čísla s mnoha nulami je v Česku zvykem zapisovat tak, že každé tři nuly následuje mezera. Jeden milión se tedy zapíše jako 1 000 000\. Vytvořte řetězec, který obsahuje Shannonovo číslo z předchozího cvičení zapsané v tomto formátu.

<%def name="solution()">

