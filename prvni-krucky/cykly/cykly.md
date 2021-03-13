<%inherit file="/course-chapter.mako"/> <%self:lesson>

Počítače a programování byly vymyšleny především proto, aby ušetřili lidem
nudnou a repetitivní práci. Proto chceme umět počítači říct, že má nějakou
činnost opakovat mnohokrát po sobě. K tomu nám v programování slouží takzvané
cykly.

## Cyklus FOR

Jeden z nejpoužívanějších cyklů v téměř všech programovacích jazycích ja
takzvaný cyklus FOR. Tento cyklus umí projít jakýkoliv zadaný seznam prvek po
prvku a pro každý prvek vykonat určitý blok kódu. Představme si například, že
máme seznam známek z písemek nějakého studenta a chceme tyto známky vypsat na
obrazovku, každou na nový řádek. K tomu nám stačí takovýto kousek kódu.

    
    
    znamky = [1, 3, 2, 1, 1, 2]
    for z in znamky:
      print(z)

V tomto konkrétním případě tedy náš cyklus prochází seznam známek jednu po
druhé. Známka, která je právě zpracovávána, je uložena v proměnné z. Jméno
této proměnné jsme si zvolili tak, aby bylo čitelné, co je v proměnné uloženo,
tedy z jako známka.

Podobně jako v případě podmínek můžeme cyklu FOR předat celý blok příkazů
najednou. Mějme například seznam jmen, kdy za každé jméno chceme přidat konec
e-mailové adresy.

    
    
    jmena = ['petr', 'pavel', 'jitka', 'jana']
    for jmeno in jmena:
      mail = jmeno + '@gmail.com'	
      print(mail)

Takto vytiskneme na obrazovku maily jednotlivých lidí, každý na jeden řádek.
Následující animace ukazuje, jakým způsobem Python prochází tento progam.

![](/img/intro-to-progr/for-cycle.gif)

Jak už bylo napsáno výše, cyklus může obsahovat libovolný blok příkazů, takže
se můžeme opravdu rozparádit a vložit do bloku v cyklu FOR třeba podmínku.

    
    
    jmena = ['petr', 'pavel', 'jitka', 'jana']
    for jmeno in jmena:
      if len(jmeno) <= 4:
        mail = jmeno + '@gmail.com'
      else:
        mail = jmeno + '@seznam.cz'
      print(mail)

Tímto jsme vlastně vysvětlili to hlavní a zásadní co o cyklu FOR zatím
potřebujeme vědět. Možná se to na první pohled nezdá, ale přidáním cyklu do
našeho programátorského arzenálu jsme otevřeli pandořinu skříňku plnou
možností, co v našich programech můžeme dělat. Taky jsme ale otevřeli bránu do
samotného pekla, neboť už díky cyklům dokážeme řešit mnohem složitější a
komplikovanější problémy, na které ale bude často potřeba pořádně roztočit
mozkové závity.

Ukažme si například jak se pomocí cyklu spočítá součet všech čísel v seznamu.

    
    
    soucet = 0
    for cislo in cisla:
      soucet = soucet + cislo

Ne, že bychom zrovna tento cyklus nutně potřebovali. Python obsahuje funkci
`sum()`, která umí dělat přesně toto. Tento příklad ale spíše ukázat, že s
cykly můžeme dělat spoustu zajímavých věci.

<%self:exercises>

## Cvičení

<%self:exrc title="Seznam hodnocení">

Mějme seznam hodnocení divadelní hry _Plyšáci na útěku_ , který vypadá takto:_

    
    
    hodnoceni = [7, 9, 6, 7, 9, 8]

  1. Vytvořte program, který projde tento seznam a vypíše každé hodnocení na nový řádek.
  2. Upravte program tak, aby vypisoval výstup v tomto formátu
    
        7/10
    9/10
    6/10
    7/10
    9/10
    8/10

<%self:exrc title="Procházení seznamu">

  1. Založte si program hesla.py a na jeho začátek vložte následující kód obsahující seznam hesel pro přihlášení do nějakého systému
    
        hesla = [
      'xyz101',
      'punťa',
      'razor-blade',
      '1234',
      '12011986',
      'martin111',
      'trhnisi',
      'hokuspokus',
      'jeník15',
      'kristus-te-spasi',
      'beruška',
      'strčprstskrzkrk'
    ]

  2. Pomocí cyklu vypište všechny hesla na obrazovku, každé na jeden řádek.
  3. Upravte váš program tak, aby vypisoval jen bezpečná hesla, tedy taková, jež jsou delší než 8 znaků.
  4. Upravte váš program tak, aby vypisoval jen ta hesla, jež obsahují znak pomlčky '-'.

<%self:exrc title="Složitější seznam">

Založte si program cykly02.py a použijte v něm následující seznam měsíců v
roce, Všimněte si, že je to seznam seznamů.

    
    
    mesice = [
      ['leden', 31],
      ['únor', 28],
      ['březen', 31],
      ['duben', 30],
      ['květen', 31],
      ['červen', 30],
      ['červenec', 31],
      ['srpen', 31],
      ['září', 30],
      ['říjen', 31],
      ['listopad', 30],
      ['prosinec', 31]
    ]

  1. Pomocí cyklu projděte tento seznam a vypište na výstup názvy jednotlivých měsíců.
  2. Pomocí dalšího cyklu vypište na výstup počty dní v jednotlivých měsících. 

${self.alert_done()}

## Bonusy

<%self:exrc title="Hry">

Následující seznam obsahuje seznam všech divadelních her, které se hrají v
divadle Pěst na oko. Každá hra má svůj název a trvání v minutách.

    
    
    hry = [
      ['Ňadro na ňadru na nádru', 180],
      ['Útok plyšových krokodýlů', 95],
      ['Cesta do říše zelí', 128],
      ['Romance na zdymadle', 144],
      ['Zátiší s mimozemšťanem', 135],
      ['Čtyři facky a dortík', 100],
      ['Motorová okurka', 165],
      ['Johnny Noir', 140],
      ['Pražská kavárna vrací úder', 130],
      ['Pět sester ve vratech', 111],
      ['Stařec a krajta', 187],
      ['Růžová nemoc', 210],
      ['Smrt v přímém přenosu', 265]
    ]

  1. Pomocí cyklu projděte tento seznam a vypište na výstup názvy všech her.
  2. Vypište na výstup názvy všech her, které trvají více než 120 minut.
  3. Vypište na výstup názvy všech her spolu s jejich trváním v hodinách a minutách.

<%self:exrc title="Průměr">

Napište cyklus, který projde zadaný seznam desetinných čísel a spočítá jejich
průměr. Seznam čísel si vytvořte na začátku programu.

<%self:exrc title="Největší prvek">

Napište cyklus, který projde zadaný seznam celých čísel a najde v něm největší
hodnotu.

