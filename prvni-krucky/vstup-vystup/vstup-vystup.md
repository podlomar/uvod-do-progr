<%inherit file="/course-chapter.mako"/> <%self:lesson>

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

    
    
    kurz = 25
    cena = 12 * 25
    print(cena)
    

Toto je jednoduchý program, který nám spočítá cenu lístku v korunách podle
kurzy 25 korun za euro. Takovýto program pak spustíme příkazem

    
    
    $ python program.py

<%self:alert_warning>

Pozor na znak dolaru na začátku tohoto příkazu. Tento znak nepíšeme! Znak
dolaru pouze naznačuje, že tento příkaz musíme zadat do terminálu operačního
systému, nikoliv do Python konzole. Pokud tedy váš příkazový řádek stále
začíná třemi zobáčky jste ještě pořád uvnitř Python konzole a musíte z ní
vyskočit pomocí funkce `exit()`.

<%self:exercises>

## Cvičení

<%self:exrc title="Jednoduchý výstup">

Náš vůbec první program nebude dělat nic víc, než vypisovat text na obrazovku.

  1. Založte si program `vstup-vystup.py`. V tomto programu pomocí funkce `print()` vypište na obrazovku
    
        Divadlo Pěst na oko

Program spusťte na konzoli a vyzkoušejte, že dělá co má.

  2. Upravte tento program tak, že do proměnné nazev uložíte název nějakého divadelního představení a do proměnné cas uložte čas konání tohoto představení. Nyní pomocí funkce `print()` nechte program vypsat na obrazovku na jeden řádek název představení a čas konání, např.
    
        Zkrocení zlé ženy - 19:30

  3. Upravte dále program tak, že do proměnné hodina uložíte hodinu konání představení (jako celé číslo) a do proměnné minuta minutu konání, také jako celé číslo. Zařiďte, aby výstup programu vypadal takto:
    
        Zkrocení zlé ženy - 19:30

Pozor na to, že hodina a minuta je hodnota typu číslo, takže ji budete při
výpisu muset převést na řetězec pomocí funkce str().

<%self:exrc title="Jednoduchý vstup">

Teď už budeme chtít, aby náš program dokázal získat vstup od uživatele.

  1. Napište program `jmeno.py`, který získá jméno a příjmení od uživatele voláním funkce `input()`. Vypište je na obrazovku podobně jako v předchozím cvičení.
  2. Nechte uživatele zadat také věk. Pozor na to, že funkce `input()` vždy vrací řetězec, ale my chceme v proměnné vek mít číslo. Použijte tedy funkci `int()`, abyste převedli uživatelem zadaný řetězec na číslo. Opět vypište na obrazovku jméno příjmení a věk tak jako v předchozí verzi.

<%self:exrc title="Zakázka pro divadlo">

Divadlo požaduje systém pro online rezervaci vstupenek na pořádaná
představení. Váš první úkol na této zakázce je vytvořit registraci pro nové
uživatele tohoto systému.

  1. Založte si program `vstupenky01.py`. Bude to první verze našeho programu pro nákup vstupenek.
  2. Napište program tak, aby nejprve vypsal na obrazovku "Divadlo Pěst na oko" na první řádek, na druhý řádek chceme vypsat "Vítejte v online rezervaci vstupenek" a na třetí řádek "Pro vstup do systému je potřeba registrace".
  3. Na dalším řádku požádejte uživatele o jeho uživatelské jméno a poté o jeho věk. Ten si uložte to nějaké proměnné jako číslo.

${self.alert_done()}

## Bonusy

<%self:exrc title="Házení kostkami">

Napište program `kostky.py`, který bude simulovat hod dvěma klasickými
šestistěnnými kostkami. Jeho výstupu bude součet bodů na těchto dvou kostkách.

**Nápověda:**

  * Generování náhodných čísel dělá funkce `random.randint()`.
  * Pokud chcete ve vašem programu použít modul `random`, musíte na jeho úplném začátku napsat příkaz 
    
        import random

<%self:exrc title="Generátor čísel">

Napište program `generator.py`, který si od uživatele vyžádá dvě celá čísla -
dolní mez a horní mez - a vypíše na výstup náhodné číslo v zadaných mezích.

<%self:lesson>

## Výstup na stejný řádek

Jistě jste si všimli, že funkce `print()` při každém výstupu na obrazovku
odřádkuje, takže další volání této funkce už bude na nový řádek. Občas ale
chceme výstup bez odřádkování, abychom mohli pokračovat stále na tom stejném
řádku.

