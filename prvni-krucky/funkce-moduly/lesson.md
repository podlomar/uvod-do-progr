S čísly a řetězci jsme zatím byli schopní pracovat pouze pomocí aritmetických
operátorů. To nám ale brzy nebude stačit a budeme potřebovat složitější
operace, kterým říkáme *funkce*.

## Funkce

Funkce je nějaký komplikovanější výpočet nebo malý program zabalený do jakési
krabičky. Této krabičce dáme nějaké jméno, abychom jej mohli používat na
různých místech v našem programu. Funkci si můžeme představit jako topinkovač.
Topinkovač pro nás dělá nějakou užitečnou činnost (opéká topinky), která by
byla otravná a zdlouhavá, kdybychom ji chtěli dělat sami, například smažit
topinky na oleji na pánvičce. Každá funkce má svoje jméno a obvykle má nějaký
vstup (čerstvý chleba) a výstup (opečená topinka). Funkci spustíme tak, že ji
takzvaně **zavoláme**.

Dobrým příkladem v jazyce Python je funkce `round()`, která pro nás dělá
zaokrouhlování. Můžeme tedy psát

```pycon
>>> round(3.141592)
3
```

Tomuto zápisu se říká *volání funkce*. Funkce se vždy volá tak, že napíšeme
její jméno a do kulatých závorek za něj její vstupy (odborně se vstupům říká
*argumenty*). V našem případě funkci předáváme jeden argument (vstup), číslo
3.141592. Když funkci zavoláme s nějakým argumentem, funkce takzvaně *vrátí*
výsledek.

Pozor na to, že zaokrouhlování v jazyce Python se chová trošku jinak než jak
jsem zvyklí ze školy. Zkuste například následující příkazy:

```pycon
>>> round(3.5)
4
>>> round(2.5)
2
```

Funkce `round()` totiž zaokrouhluje vždy k nejbližšímu sudému číslu pokud se
vstup funkce nachází přesně uprostřed mezi dvěma hodnotami. Například 3.5 je
přesně mezi 3 a 4. Díky tomuto pravidlu tak Python namísto zaokrouhlování vždy
nahoru zaokrouhluje v polovině případů nahoru a v polovině dolů. Je to jakýsi
pokus být víc fér, ale zatím jsem nepotkal žádný jiný programovací jazyk,
který by se o něco takového snažil.

Kromě funkce `round()` Python obsahuje mnoho dalších užitečných funkcí a mnoho
z nich uvidíme v pozdějších částech tohoto kurzu. Nyní můžeme kromě funkce
`round()` zmínit například funkci `len()`, která vrací počet znaků uvnitř
nějakého řetězce. Například:

```pycon
>>> jmeno = 'Theodor Holohlávek'
>>> len(jmeno)
18
```

## Moduly

Python sice obsahuje mnoho užitečných funkcí, ale vzhledem k množství
problémů, které chceme pomocí Pythonu řešit, je to pořád málo a různých funkcí
potřebujeme opravdu hodně. Abychom se v tom všem vyznali, třídíme funkce do
takzvaných modulů.

Jeden z užitečných modulů nese název `math`, a obsahuje mnoho standardních
matematických funkcí. Mimo jiné obsahuje funkce pro zaokrouhlování nahoru a
dolů. Pokud chceme modul `math` použít, musíme jej nejdříve importovat
příkazem

```pycon
>>> import math
```

Poté, co tento příkaz zadáme do Python konzole, můžeme volat všechny funkce z
tohoto modulu tak, že vždy před název funkce pomocí tečky připojíme název
modulu, ze kterého funkce pochází. Například

```pycon
>>> math.ceil(3.14)
4
```

Dalším užitečným modulem je modul `random`, který obsahuje funkce pro
generování náhodných čísel. Jedna z takových funkcí se jmenuje `randint()`.
Umí generovat náhodná celá čísla v zadaném rozmezí. Můžeme tak například
simulovat házení kostkou.

```pycon
>>> import random
>>> random.randint(1, 6)
5
>>> random.randint(1, 6)
1
>>> random.randint(1, 6)
4
>>> random.randint(1, 6)
4
>>> random.randint(1, 6)
1
>>> random.randint(1, 6)
2
>>> random.randint(1, 6)
4
```

[[[ excs Cvičení
- delka-nazvu
- zaokrouhlovani
- zaokrouhlovani-nahoru
- nahodna-cisla
]]]

[[[ excs Bonusy
- klasicke-zaokrouhlovani
]]]
