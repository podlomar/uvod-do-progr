V této kapitole si představíme úplné základy programování v Pythonu. Zatím
ještě nebudeme psát celé programy, nýbrž budeme Pythonu posílat jednotlivé
příkazy a uvidíme, co nám odpoví. Jak už jsme si řekli dříve, počítač je v
podstatě jen trochu chytřejší a pekelně rychlá kalkulačka. Nejsnadněji se tedy
s programováním seznámíme, když si pomocí Pythonu necháme něco spočítat.

## Python konzole

Abychom si mohli s Pythonem povídat, musíme spustit takzvanou *Python
konzoli*. To je prostředí, ve kterém můžeme s Pythonem komunikovat a posílat
mu příkazy.

Pokud pracujete pod Windows, Python konzoli spustíte tak, že do termínálu
napíšete příkaz.

```shell
$ python
```

Pozor, že **znak dolaru není součástí příkazu**. Používáme ho pouze k tomu,
abychom naznačili, že je třeba tento příkaz napsat do terminálu vašeho
operačního systému.

Pokud pracujete na Macu nebo Linuxu, správný příkaz je

```shell
$ python3
```

Pokud v Linuxu nebo na Macu spustíte příkaz jako ve Windows, pravděpodobně se
vám spustí jiná verze Pythonu, se kterou vám následující lekce nebudou
fungovat.

## Hodnoty

*Hodnoty* představují všechny možné druhy dat, se kterými můžou naše programy
pracovat. Hodnoty se dle způsobu použití dělí do různých kategoríí zvaných
*datové typy*. Datových typů existuje velké množství. V tuto chvíli si
představíme ty nejzákladnější - celá čísla a desetinná čísla.

### Celá čísla

Nejjednodušší datový typ jsou *celá čísla*. Pod tento typ patří hodnoty jako
12, 1321500, -5, 0 a podobně. Pokud do Python konzole napíšete hodnotu, Python
vám ji vypíše zpátky, což znamená, že vám rozumí :-)

```pycon
>>> 127
127
```

### Desetinná čísla

S celými čísly bychom si dlouho nevystačili. Dalším datovým typem tedy budou
*desetinná čísla*, např. 13.4, 6.0, -0.0001, 0.0 apod. Pozor, že programátoři
vždycky píší desetinná čísla s **tečkou**, nikoliv s čárkou.

```pycon
>>> 3.141592
3.141592
```

## Aritmetické operátory

Nyní už máme prostředky k tomu, abychom mohli pomocí Pythonu něco spočítat. V
Python máme k dispozici běžné aritmetické operátory:

* sčítání: `+`
* odčítání: `-`
* násobení: `*`
* dělení: `/`

Díky těmto operátorům můžeme Python použít jako kalkulačku a psát *aritmetické
výrazy* jako

```pycon
>>> 12 * 13 + 10
>>> (13.4 - 1.4) / 4
```

Python ovšem nabízí ještě další užitečné operátory:

* mocnění: `**`
* celočíselné dělení: `//`
* zbytek po dělení: `%`

Pomocí mocnění můžeme umocňovat čísla, například

```pycon
>>> 2 ** 8
256
```

Pomocí celočíselného dělení můžeme dělit celá čísla

```pycon
>>> 14 // 4
3
```

Pokud by nás zajímal zbytek po celočíselném dělení, můžeme použít operátor pro
zbytek po dělení

```pycon
>>> 14 % 4
2
```

## Řetězce

Pokud chceme v Pythonu zadat nějaký kousek textu, použijeme takzvaný
*řetězec*. Řetězce se v Pythonu uzavírají do jednoduchých nebo dvojitých
uvozovek. Například:

```pycon
>>> 'martin'
>>> '12. března 2018'
>>> "prací prášek"
>>> "Don't panic"
```

Řetězce se v něčem chovají podobně jako čísla, můžeme je například sčítat a
násobit

```pycon
>>> 'martin' + ' ' + 'podloucký'
'martin podloucký'
>>> 'bla ' * 10
'bla bla bla bla bla bla bla bla bla bla '
```

[[[ excs Cvičení
- jednoducha-aritmetika
- hratky-s-retezci
]]]

[[[ excs Bonusy
- uroky
- novy-koberec
- shannonovo-cislo
]]]
