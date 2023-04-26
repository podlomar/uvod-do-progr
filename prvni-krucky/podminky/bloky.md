Do této chvíle všechny naše programy vypadaly jako sekvence příkazů vykonávané
jeden za druhým a měly pouze jeden možný průběh. Pro komplikovanější programy
ale budeme potřebovat umožnit, aby se některé části programu vykonaly jen za
určitých *podmínek* , tedy aby se naše programy dokázaly rozhodovat a měnit
svoje chování na základě zadaného vstupu od uživatele.

::fig[15plus]{src=assets/15plus_500.png size=60}

Naše divadlo hraje i divadelní hry, které nejsou vhodné pro děti. Na
takové představení chceme pustit pouze uživatele starší 15ti let. Náš program
tedy musí být schopný se podle zadaného věku rozhodnout, zda uživateli umožní
koupit si lístek nebo nikoliv. Takový program by pak mohl vypadat například
takto:

```python
if vek >= 15:
    print('Vítej na představení')
else:
    print('Dnes to není pro tebe')
```

## Bloky

Všimněte si, že některé řádky v naší podmínce jsou odsazené kousek doprava.
Tímto poprvé narážíme na takzvané bloky kódu. Blok je způsob jak seskupit
několik příkazů do jednoho celku. Takový celek pak může být součástí podmínky
nebo, jak později uvidíme, například cyklu. Blok vždy začíná **dvojtečkou** na
konci předchozího řádku. Tím říkáme k jaké konstrukci (v našem případě `if`)
náš blok příkazů patří.

Odsazování bloků se nejčastěji provádí pomocí několika mezer. Mnoho
programátorů preferuje čtyři mezery, někteří preferují dvě mezery.
V tomto kurzu se budeme držet oficiálního doporučení autorů Pythonu a používat
čtyři mezery na odsazení.
