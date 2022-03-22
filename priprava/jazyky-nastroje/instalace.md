## Instalace nástrojů

Abychom mohli začít programovat, je potřeba na počítač nainstalovat dva programy - samotný jazyk Python a Visual Studio Code. Postup se liší podle toho, jaký máte operační systém. Instrukce pro každý systém zvlášť naleznete níže.

### Windows

Pokud máte počítač s Windows, následujte tyto kroky:

1. Ujistěte se, že máte aktualizovaný systém. To zajistíte nejjednodušeji tak, že svůj počítač restartujete. Pokud jste již dlouho neaktualizovali, při restartu se může spustit aktualizace, která může trvat relativně dlouho, v extrémním případě třeba i hodinu. Nenechte se vyděsit, obrňte se trpělivostí a vyčkejte, dokud Windows opět nenaběhnou.
1. Stáhněte si instalaci jazyka Python z [oficiálních stránek](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe). Stažený soubor spusťte. Rozeběhne se průvodce instalací.
1. Na úvodní obrazovce je **velmi důležité** zaškrtnout volbu **Add Python 3.9 to PATH** (viz obrázek)

::fig[Instalace Pythonu]{src=assets/python-setup.png}
    
1. Klikněte na **Install Now**, odsouhlaste případné otázky ohledně změn na vašem počítači a vyčkejte dokončení instalace. Jakmile instalace skončí, zavřete okno tlačítkem **Close**.
1. Z [tohoto odkazu](https://aka.ms/win32-x64-user-stable) si stáhněte Visual Studio Code.
1. Stažený soubor spusťte. Rozeběhne se průvodce instalací, ve kterém stačí klikat na **Next** tak dlouho, dokud se nespustí instalace. Ve druhém kroku je pouze potřeba souhlasit s licencí.
1. Jakmile instalace doběhne, zavřete okno tlačítkem **Finish**. Visual Studio Code by se mělo samo spustit ihned po instalaci.
1. Pro jistotu restartujte počítač, aby se všechny provedené změny správně usadily.
  
### Mac OS
Pokud máte počítač se systémem Mac OS, následujte tyto kroky.
  
1. Stáhněte si instalaci jazyka Python z [tohoto odkazu](https://www.python.org/ftp/python/3.7.1/python-3.7.1-macosx10.9.pkg)
1. Stažený soubor spusťte a pokračujte dle pokynů instalace až do jejího konce.
1. Z [tohoto odkazu](https://go.microsoft.com/fwlink/?LinkID=620882) si stáhněte Visual Studio Code. Spusťte instalaci a opět ji následujte až do zdařilého konce.

### Linux
Pokud používáte některou z populárních distribucí Linuxu jako Ubuntu, Linux Mint apod., je velká naděje, že už máte Python nainstalovaný. Napište do příkazové řádky příkaz

```
python3
```

A sledujte, zda se objeví zpráva podobná této:

```
Python 3.6.6 (default, Sep 12 2018, 18:26:19)
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

Pokud je verze Pythonu na prvním řádku alespoň 3.5, jste připravení.
