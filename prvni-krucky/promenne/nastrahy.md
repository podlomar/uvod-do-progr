## Nástrahy

Dejte pozor na to, že do proměnné se jako do šuplíku ukládá pouze hodnota a
nikoliv celý výpočet. Pokud tedy napíšeme například

```pycon
>>> sazba = 350
>>> vyplata = 8 * sazba
```

bude v proměnné `vyplata` uložena hodnota 2800. Jestliže potom změníme hodnotu v
proměnné `sazba` na něco jiného, například

```pycon
>>> sazba = 420
```

v proměnné `vyplata` bude nadále uložena hodnota 2800. Pokud chceme výsledek
výpočtu aktualizovat, musíme jej spustit znova:

```pycon
>>> vyplata = 8 * sazba
```
