# Vstup a výstup

Nyní přichází na řadu velký zlom. Zatím jsme s Pythonem komunikovali pouze na
konzoli a posílali jsme mu k vyhodnocení vždy pouze jeden příkaz. Když ale už
umíme pracovat s proměnnými a funkcemi, můžeme vytvořit náš první program.

Program je v podstatě textový soubor, který obsahuje více příkazů najednou a
Python tyto příkazy postupně vykonává. Nemusíme už tedy nic psát na konzoli,
všechny příkazy budeme psát dovnitř programu.

## Výstup do terminálu

Máme tu ale jeden problém. Když jsme zadávali příkazy na konzoli, Python nám
vždy rovnou vrátil výsledek. Když ale spustíme program, Python nám automaticky
žádné výsledky nevrací. Programy totiž často obsahují tisíce příkazů a my
nechceme vidět výsledek každého z nich, to bychom se v tom množství výsledků
nevyznali. Pokud tedy nějaký výsledek chceme vidět, musíme Pythonu přímo říct,
aby ho vypsal do terminálu, ve kterém program spouštíme. K tomu slouží funkce
`print()`. Vybavení touto funkcí už můžeme napsat náš první program.

## První program

Vytvořme si ve Visual Studiu program s názvem `program.py` a do něj vložme
následující řádky

```python
kurz = 25
cena = 12 * 25
print(cena)
```

Toto je jednoduchý program, který nám spočítá cenu lístku v korunách podle
kurzy 25 korun za euro. Takovýto program pak spustíme příkazem

```
$ python program.py
```


Pozor na znak dolaru na začátku tohoto příkazu. Tento znak nepíšeme! Znak
dolaru pouze naznačuje, že tento příkaz musíme zadat do terminálu operačního
systému, nikoliv do Python konzole. Pokud tedy váš příkazový řádek stále
začíná třemi zobáčky (`>>>`), jste ještě pořád uvnitř Python konzole a musíte z ní
vyskočit pomocí funkce `exit()`.


## Cvičení

- [jednoduchy-vystup](excs/Jednoduchy-vystup.md)
- [jednoduchy-vstup](excs/Jednoduchy-vstup.md)
- [zakazka-pro-divadlo](excs/Zakazka-pro-divadlo.md)

### Bonusy

- [hazeni-kostkami](excs/Hazeni-kostkami.md)
- [generator-cisel](excs/Generator-cisel.md)
