<%inherit file="/course-chapter.mako"/> <%self:lesson>

Do této chvíle jsme uměli do nějaké proměnné uložit pouze jednu hodnotu,
například číslo nebo řetězec. Počítače ale často potřebují pracovat v mnohem
větším objemem dat, než je několik čísel nebo řetězců.

Sekvence nám umožňují do jedné proměnné uložit více hodnot. Hodnoty uvnitř
sekvencí sídlí na takzvaných _indexech_ , které se vždy počítají od nuly. To
je takový zvláštní programátorský úzus, že se většinou začíná počítat od nuly
a ne od jedničky. Má to svoje důvody, které tady ovšem nebudeme rozvádět.
Raději si rovnou ukážeme jedna z nejjednodušší sekvencí, a to je řetězec. Díky
tomu, že řetězec je sekvence, je možné přistupovat k jednotlivým jeho prvkům,
v tomto případě písmenům.

    
    
    >>> jmeno = 'hubert'
    >>> jmeno[0]
    'h'
    >>> jmeno[4]
    'r'

Ty vůbec nejpoužívanější sekvence jsou ovšem seznamy. Do nich lze uložit
jakékoliv množství hodnot jakéhokoliv typu. Dokonce můžeme mít seznamy
seznamů.

    
    
    >>> znamky = [2, 3, 4, 1, 1]
    >>> teploty = [13.4, 13.5, 12.8, 11.9]
    >>> uzivatele = ['mark', 'carl', 'eve', 'ellen']
    >>> platby = ['Jan Novák', 12000, true]
    >>> body = [[140, 120], [60, 92], [34, 68]]

Přístupy k indexům sekvencí se dají skládat za sebe. Můžeme tak získat
například čtvrté písmenko druhého jména v seznamu `uzivatele`

    
    
    >>> uzivatele[1][3]
    'l'

nebo první číslo třetího seznamu v proměnné `body`

    
    
    >>> points[2][0]
    'l'

<%self:exercises>

## Cvičení

<%self:exrc title="Řetězce jako sekvence">

  1. Uložte si v Python konzoli do proměnné jmeno svoje celé jméno a nechte vypsat jeho třetí, pátý a sedmý znak. Vyzkoušejte, co se stane, když budete chtít znak na pozici, která překračuje délku řetězce. 
  2. Upravte program `registrace.py` tak, že bude kromě uživatelského jména chtít také e-mailovou adresu. Ověřte, že adresa je v platném formátu, tedy že obsahuje zavináč, tečku a má alespoň pět znaků.

<%self:exrc title="Seznamy">

Celé toto cvičení dělejte v příkazové řádce Pythonu.

  1. Vytvořte nějaký seznam celých čísel, například počty diváků na několika po sobě jdoucích představeních. Použije metodu `append` a přidejte do seznamu počet diváků na jednom dalším představení.
  2. Vytvořte nějaký seznam desetinných čísel, například zaplněnost divadla v několika po sobě jdoucích představeních.
  3. Vytvořte nějaký seznam řetězců, například seznam názvů několika divadelních představení, která divadlo hraje. Uložte tento seznam do proměnné hry. Uložte do nějaké proměnné druhou položku tohoto seznamu.
  4. Do proměnné hodnoceni uložte seznam hodnocení, které obdržela divadelní hra _Plyšáci na útěku_ v různých recenzních časopisech. Hodnocení je vždy dvouprvkový seznam obsahující název recenzního časopisu jako řetězec a samotné hodnocení jako číslo mezi 1 až 10. Přidejte na konec tohoto seznamu nové hodnocení z časopisu Divadelní oběžník. 

${self.alert_done()}

## Bonusy

<%self:exrc title="Ověřování hesla">

Ověřování hesla se někdy dělá tak, že se vás systém ptá pouze na některé jeho
znaky. Napište program, který má uloženo heslo, které musí uživatel zadat. Pak
se jej postupně zeptejte například na druhý, pátý a sedmý znak hesla.
Propusťte uživatele pouze tehdy, zadá-li všechny tyto znaky správně.

