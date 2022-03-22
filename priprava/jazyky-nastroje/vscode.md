## Nastavení VS Code

Aby se nám ve VS Code dobře programovalo, uložíme si některá užitečná nastavení. Spusťte VS Code a z horního menu vyberte _View_ → _Command Palette..._. Do textového políčka zkopírujte tento text

```
Open Settings (JSON)
```

a stiskněte enter. Otevře se okno s editorem. Do jeho pravé časti vložte tento text

```json
{
  "editor.tabSize": 2,
  "editor.detectIndentation": false,
  "editor.renderWhitespace": "boundary",
  "editor.insertSpaces": true,
  "editor.wordWrap": "on",
  "files.eol": "\n",
  "editor.minimap.enabled": false,
  "editor.fontSize": 16
}
```

a uložte stiskem Ctrl+S nebo z menu vyberte _File_ → _Save_.

**Hotovo.** Hurá, máte hotovo a jste připravení na kurz.
