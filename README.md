# thue
[Thue](https://esolangs.org/wiki/Thue) interpreter in python, plus utilities for generating Thue programs
# Files
`thue.py` - Main thue interpreter, to be used as a library<br>
`text2thue.py` - Converts text file to markov(?) Thue program. No command line arguments, so edit the script. Results are mostly nonsense `example: Funond tais the I Smyotalkyest`<br>
`thue2tracery.py` - Converts thue to Tracery, No command line arguments, so edit the script.
# Examples
```py
import thue

c = "*::=Hello World!\n::=\n*"
t = thue.VM(c)
print(t.run())
```
