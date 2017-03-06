# formulas.py
Generate note formulas as described in the book [An Improviser's OS by Wayne Krantz](http://www.abstractlogix.com/xcart/product.php?productid=24532&cat=0&page=1) (All Rights Reserved)

formulas.py is a simple Python script that will generate a list of all possible note combinations for a given (optional) root note.

Usage: **python formulas.py** [note]<br />
where [note] is a note name e.g. C, C#, Db, etc. If [note] is omitted, formulas are generated with C as root.

Requirements:
* Python 3
* [mingus](https://github.com/urbster1/python-mingus) *(if you use pip to install, replace Lib/site-packages/mingus/core/notes.py with the notes.py from this repo, otherwise if you install using my fork it should work)*

2048 formulas of 1 through 12 notes will be generated. These comprise all possible combinations of notes in the chromatic scale which include the given root note.

For more information, please [read the book](http://www.abstractlogix.com/xcart/product.php?productid=24532&cat=0&page=1) - no, really - it will tell you everything you need to know.
