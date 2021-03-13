<%inherit file="/course-chapter.mako"/> <%self:lesson>

Při komplikovanějších výpočtech se nám často stane, že si potřebujeme nějaký
mezivýpočet uložit pro pozdější použití. K tomu nám slouží takzvané
_proměnné_.

Proměnná je jakási pojmenovaná krabička nebo šuplík, do kterého si můžeme
uložit nějakou hodnotu, abychom ji neztratili a mohli ji používat v dalších
výpočtech.

Můžeme například v rámci dietního programu spočítat kolik vanilkových věnečků
denně jsme spořádali za posledních 5 dní.

    
    
    >>> celkem = 1 + 2 + 4 + 1 + 6
    >>> prumer = celkem / 5

## Jména proměnných

Už do úplných začátků s programováním je dobré učit se dobrým návykům, které
budou později usnadňovat programátorský život nejen vám ale hlavně lidem kolem
vás. Jedním z takových návyků je správné pojmenovávání proměnných.

  * Název proměnné by neměl začínat velkým písmenem, např. Pocet. Takové názvy jsou rezervované pro speciální typy proměnných, ke kterým se v tomto kurzu nedostaneme. 
  * Název proměnné by neměl obsahovat diakritiku, např. počet. Programovací jazyky vznikaly v Anglickém prostředí, kde se diakritika napoužívá, takže si ní většina jazyků neporadí. 
  * Víceslovné proměnné nesmí obsahovat mezeru, např. pocet hodin. To by si Python myslel, že to jsou dvě proměnné za sebou a nevěděl by co s tím. Pokud chcete proměnnou s více slovy, použíjte takzvanou velbloudí notaci pocetHodin nebo hadí notaci pocet_hodin.
  * Vždy proměnnou pojmenujte tak, aby její název jasně napovídal, co se uvnitř ní nachází. Například proměnná pocet_hodin jasně říká, že v ní bude asi nějaký počet hodin. Můžeme podlehnout touze název proměnné zkrátit například na pcthd aby se nám lépe psala. Až ovšem někdo další bude takový program číst, bude mlátit hlavout do stolu cože proboha znamená zkratka `pcthdn`.
  * Naposledy je dobré si uvědomit, že programy i programátoři se téměř vždy pohybují v mezinárodním prostředí. Takže je vždycky lepší pojmenovávat proměnné anglicky. V tomto kurzu ještě tohle pravidlo trošku rozvolníme, ale i tak si můžete začít zvykat na proměnné s názvem numberOfHours.

## Nástrahy

Dejte pozor na to, že do proměnné se jako do šuplíku ukládá pouze hodnota a
nikoliv celý výpočet. Pokud tedy napíšeme například

    
    
    >>> sazba = 350
    >>> vyplata = 8 * sazba

bude v proměnné vyplata uložena hodnota 2800. Jestliže potom změníme hodnotu v
proměnné sazba na něco jiného, například

    
    
    >>> sazba = 420

v proměnné vyplata bude nadále uložena hodnota 2800. Pokud chceme výsledek
výpočtu aktualizovat, musíme jej spustit znova.

    
    
    >>> vyplata = 8 * sazba

<%self:exercises>

## Cvičení

<%self:exrc title="Hrátky s proměnnými">

Dbejte na to, aby proměnné měly vhodný název dobře naznačující, co je v které
z nich uloženo.

  1. Uložte do proměnné herci celočíselnou hodnotu udávající počet herců, kteří hrají v divadle. Do proměnné platy spočítejte celkové náklady divadla na platy herců, víme-li, že průměrný plat herce je 22 392 kč. 
  2. Do jiné proměnné s vhodným názvem uložte nějaké desetinné číslo, například velikost slevy na studentské vstupné. Do další proměnné uložte nějaký řetězec, například název nějakého představení.
  3. Zatímco jste dělali předchozí cvičení, do divadla přibyli dva noví herci. Aktualizujte tedy obsah proměnné herci a zařiďte, aby v proměnné platy byla správná hodnota nákladů. Zamyslete se nad tím co se stalo s hodnotou, která byla v proměnné herci uložena před tím.

<%self:exrc title="Celočíselné dělení a dělení se zbytkem">

Zaexperimentuje s operátory celočíselného dělení a dělení se zbytkem.

  1. Kolikrát se vejde číslo 72 do 1024? Kolik je zbytek po dělení čísla 1024 číslem 72? 
  2. Divadlo má délky představení vždy uloženo v minutách. Například extrémně nudné a zničující představení "Smrt v přímém přenosu" trvá 265 minut. Uložte tuto hodnotu do proměnné delka.
  3. Použijte proměnnou delka a spočítejte trvání představení vyjádřeno v hodinách a minutách. Do proměnné hodin uložte počet celých hodin a do proměné minut uložte zbylé minuty. 

${self.alert_done()}

## Bonusy

<%self:exrc title="Sedačky v sále">

Hlavní sál divadla má k dispozici 350 sedaček. Lze je poskládat do řad po 32
sedadlech tak, aby všechny řady byly úplné? Pokud ne, kolik sedaček musíme
přikoupit, aby to šlo? Kolik nám takto vznikne celkem řad?

