<%inherit file="/course-chapter.mako"/> <%self:lesson>

Do této chvíle všechny naše programy vypadaly jako sekvence příkazů vykonávané
jeden za druhým a měly pouze jeden možný průběh. Pro komplikovanější programy
ale budeme potřebovat umožnit, aby se některé části programu vykonaly jen za
určitých _podmínek_ , tedy aby se naše programy dokázaly rozhodovat a měnit
svoje chování na základě zadaného vstupu od uživatele.

![Adult only](/img/intro-to-progr/adult-only.png)

Naše divadlo obsahuje některé lechtivé kusy s obsahem pouze pro dospělé. Na
takové představení chceme pustit pouze uživatele starší 18ti let. Náš program
tedy musí být schopný se podle zadaného věku rozhodnout, zda uživateli umožní
koupit si lístek nebo nikoliv. Takový program by pak mohl vypadat například
takto:

    
    
    if vek >= 18:
      print('Vítej ve světě slasti')
    else:
      print('Odpal, holomku!')

## Bloky

Všimněte si, že některé řádky v naší podmínce jsou odsazené kousek doprava.
Tímto poprvé narážíme na takzvané bloky kódu. Blok je způsob jak seskupit
několik příkazů do jednoho celku. Takový celek pak může být součástí podmínky
nebo, jak později uvidíme, například cyklu. Blok vždy začíná dvojtečkou na
konci předchozího řádku. Tím říkáme k jaké konstrukci (v našem případě `if`)
náš blok příkazů patří.

Odsazování bloků se nejčastěji provádí pomocí několika mezer. Mnoho
programátorů preferuje čtyři mezery, někteří (jako já) preferují dvě mezery.
Jsou i tací, kteří odsazují bloky pomocí jednoho tabulátoru. Podobně jako v
případě jmen proměnných, opět zde přichází do hry různé programovací styly.
Opět je to na jakémsi vašem estetickém cítění. Já budu v tomto kurzu vždy
doporučovat dvě mezery.

Pokud si zvolíte konkrétní styl, je velice důležité jej dodržovat. Pokud v
rámci jednoho bloku budete míchat mezery a tabulátory, Python vašemu kódu
nebude rozumět a bude vyhazovat chyby. Pokud budete jeden blok odsazovat
pomocí tabulátorů a jeden pomocí mezer, tak vám to Python odpustí, ale je to
strašlivá prasárna, takže to opravdu nedělejte.

## Podmínky s více větvemi

Podobně jako u filmů tak i u divadelních představení bychom mohli chtít
jemnější rozdělení přístupnosti nějakého představení. Můžeme například mít
představení nevhodné vyloženě pro malé děti, zatímco teenageri jsou v pohodě.
Budeme tady potřebovat podmínku s více větvemi:

    
    
    if vek < 6:
      print('Předškolák')
    elif vek < 15:
      print('Školák')
    elif vek < 18:
      print('Mladistvý')
    else:
      print('Dospělý')

## Porovnávací operátory

V podmínkách jsme zatím používali operátory menší než `<` a větší nebo rovno
`>=`. Zde je přehled všech ostatních porovnávacích operátorů

  * rovno: **==**
  * nerovno: **!=**
  * větší: **>**
  * větší nebo rovno: **> =**
  * menší: **<**
  * menší nebo rovno: **< =**

Všimněte si, že rovnost se testuje pomocí dvou rovná se. Je to proto, že jedno
rovná se už používáme k něčemu jinému - k přiřazení hodnoty do proměnné.

<%self:exercises>

## Cvičení

<%self:exrc title="Jednoduché podmínky">

  1. Založte si program `prihlaseni.py`. V tomto nechte uživatele zadat svoje uživatelské jméno a poté heslo. Pokud se heslo shoduje s heslem _simsalabim_ vypište na výstup
    
        Smíš vstoupit

Program spusťte na konzoli a vyzkoušejte, že dělá co má.

  2. Upravte tento program tak, aby vypsal 
    
        Vstup nepovolen

pokud uživatel zadá špatné heslo.

  3. Upravte dále program tak, že pokud uživatel zadá správné heslo, program se ho ještě zeptá na věk a pustí jej dál pouze pokud je starší 18ti let. Pokud uživatel zadá heslo špatně, už se ho na věk neptejte a ukončete program voláním funkce `exit()`.

<%self:exrc title="Cena vstupenky">

A nyní opět pokračujeme v našem rezervačním systému.

  1. Program `vstupenky01.py`, který jste napsali v předchozí fázi, si uložte jako `vstupenky02.py`, abychom ho mohli dále rozšířit o výpočet ceny vstupenky.
  2. Jakmile máte v programu načtený věk uživatele, vytvořte si proměnnou plnaCena, do které uložte hodnotu 12.
  3. Vytvořte podmínku, která do proměnné cena uloží cenu spočítanou podle věku uživatele dle následujících pravidel

    * 0 euro pro návštěvníky mladší 6 let,
    * 65% ze základní ceny pro návštěvníky 6 až 26 let (žák, student),
    * 100% ze základní ceny pro návštěvníky 27 až 64 let (dospělý),
    * 50% ze základní ceny pro ostatní (senior).

Nezapomeňte na zaokrouhlování, ať nám cena vyjde v celých centech.

  4. Nakonec spočtenou cenu vypište s nějakou hezkou zprávou na výstup.

${self.alert_done()}

## Bonusy

<%self:exrc title="Registrace">

Založte si program `registrace.py`. Program nechá uživatele, aby si zvolil
uživatelské jméno a heslo. Heslo jej nechejte zadat dvakrát a ověřte, že jej
uživatel zadal dvakrát stejně. V opačném případě vypište varování, že hesla
nejsou stejná. Při prvním zadávání ověřte, že heslo je bezpečné, což v tomto
případě znamená, že je delší než 8 znaků.

<%self:exrc title="Ruleta">

Na obrázku vidíte rozložení čísel na klasické Francouzské ruletě. Ruleta
obsahuje čísla 0 - 36. Každé číslo s výjimkou nuly je buď sudé nebo liché a
zároveň červené nebo černé. Pro čísla 1 až 10 a 19 až 28 platí, že lichá čísla
jsou červená a sudá jsou černá. Pro zbytek platí obrácené pravidlo, tedy lichá
jsou černá a sudá červená. Nula není ani lichá ani sudá, ani černá ani
červená.

![](/img/intro-to-progr/roulette.png)

Napište program, kterému uživatel zadá číslo a program odpoví jestli jde o
číslo sudé nebo liché, černé nebo červené, nebo je to nula.

<%self:exrc title="Přestupný rok">

Napište program, který po zadání kalendářního roku vypíše, zda jde o rok
přestupný, či nikoliv. Letopočet je přestupný, pokud je dělitelný čtyřmi.
Roky, které jsou dělitelné 100 jsou ovšem přestupné pouze tehdy, jsou-li
zároveň dělitelné 400.

