
### Bewertete Abgabe
#### Abgabe: 6. Februar 2023 (Anfang dritte Prüfungswoche)

Schreibt mit Hilfe von PyQt6 eine GUI, um die Mandelbrot-Menge darzustellen!
Features (nach Schwierigkeit geordnet)

    - Die Applikation hat ein Fenster mit der Darstellung der Mandelbrotmenge, ein paar Steuerelementen daneben und ein Hauptmenü.
    - Bei Klick auf einen Punkt der Mandelbrotmenge wird mit fixem Faktor gezoomt und das Bild neu aufgebaut (die GUI ist zu der Zeit nicht ansprechbar)
    - Unter den Steuerelementen hat es einen Button "Reset", mit dem der Zoom rückgängig gemacht wird und wieder die Standardansicht angezeigt wird.
    - Unter den Steuerelementen hat es eine Möglichkeit, den Zoomfaktor beim Klicken einzustellen zwischen 1.2 und 4.0 in Schritten von 0.1
    - Jedes Steuerelement hat einen "Tooltip"
    - Das Hauptmenü hat einen Eintrag "File" dem Unterpunkt "Save" mit dem das aktuelle Mandelbrot-Bild als PNG abgespeichert werden kann und einen Unterpunkt "Quit" zum Verlassen des Programms.
    - Wird das Programm geschlossen (Kreuz oben rechts, File->Quit) und das aktuelle Bild wurde nicht gespeichert: Anzeige eines Dialogs ("Wollen Sie wirklich das Programm verlassen?") mit den 3 Optionen Programm verlassen ohne speichern, Zurück ins Programm und Speichern.
    - Das Fenster des Programms kann variabel vergrössert/verkleinert werden. Dabei bleibt der Bereich der Steuerelement in der Grösse fix, der Bereich, der das Fraktal darstellt vergrössert und verkleinert sich; das Fraktal wird nicht jedes Mal neu berechnet, nur das Bild skaliert
    - Die Berechnung wird in einem separaten Thread gemacht, so dass die GUI nicht einfriert.
    - Während der Berechnung wird irgendwo eine Balkenanzeige angezeigt, die den Fortschritt der Berechnung anzeigt.

#### Zusammenfassend:
- Mandelbrot Menge = Bild
- Wenn auf einen Punkt im Mandelbrot Bild geklickt wird, wird in diesen Punkt hineingezoomt (mit dem jeweiligen Zoom-Faktor)
- Reset Knopf, um auf die Anfangs-Mandelbrot-Darstellung zu kommen
- Zoomfaktor einstellbar [1.2, 4.0], in 0.1er Schritten 
- Jedes Element bekommt ein `Tooltip` --> Help bez. kleine Erklärung
- Einträge (In der Menü Leiste oben):
  - File
    - Sava as PNG
    - Quit
- Wenn das Programm verlassen wird (entweder Quit oder Rechts oben):
  - Falls das Aktuelle Bild nicht gespeichert wurde:
    - 'Programm beenden ohne zu speichern?'
      - 'Ja'
      - 'Nein'
    - 'Das Programm nicht verlassen'
- Berechnung in separatem Thread
  - Inkl einem Fortschritt-Balken



#### Tipps/Bewertung

    - Verzichtet auf Parallelprogrammierung über multiprocessing, das führt möglicherweise zu Problemen!
    - Bildet eine Gruppe 2-3 Personen, frei Wahl
    - Bewertet wird die oben angegebene Funktionalität und ein gut strukturierter verständlicher Code
    - Diese Abgabe zählt 50% zur Note, die erste Abgabe zum Unittesting ebenfalls 50%
    

