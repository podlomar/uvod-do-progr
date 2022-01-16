Do této chvíle jsme uměli do nějaké proměnné uložit pouze jednu hodnotu,
například číslo nebo řetězec. Počítače ale často potřebují pracovat v mnohem
větším objemem dat, než je několik čísel nebo řetězců.

## Řetězce

Sekvence nám umožňují do jedné proměnné uložit více hodnot. Hodnoty uvnitř
sekvencí sídlí na takzvaných _indexech_ , které se vždy počítají od nuly. To
je takový zvláštní programátorský úzus, že se většinou začíná počítat od nuly
a ne od jedničky. Má to svoje důvody, které tady ovšem nebudeme rozvádět.
Raději si rovnou ukážeme jedna z nejjednodušší sekvencí, a to je řetězec. Díky
tomu, že řetězec je sekvence, je možné přistupovat k jednotlivým jeho prvkům,
v tomto případě písmenům.

```pycon
>>> jmeno = 'hubert'
>>> jmeno[0]
'h'
>>> jmeno[4]
'r'
```

## Seznamy

Ty vůbec nejpoužívanější sekvence jsou ovšem seznamy. Do nich lze uložit
jakékoliv množství hodnot jakéhokoliv typu. Dokonce můžeme mít seznamy
seznamů.

```pycon
>>> znamky = [2, 3, 4, 1, 1]
>>> teploty = [13.4, 13.5, 12.8, 11.9]
>>> uzivatele = ['mark', 'carl', 'eve', 'ellen']
>>> platby = ['Jan Novák', 12000, True]
>>> body = [[140, 120], [60, 92], [34, 68]]
```

Přístupy k indexům sekvencí se dají skládat za sebe. Můžeme tak získat
například čtvrté písmenko druhého jména v seznamu `uzivatele`

```pycon
>>> uzivatele[1][3]
'l'
```

nebo první číslo třetího seznamu v proměnné `body`

```pycon
>>> body[2][0]
'34'
```

[[[ excs Cvičení
- retezce-jako-sekvence
- seznamy
]]]

[[[ excs Bonusy
- overovani-hesla
]]]
