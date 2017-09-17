#tatesen2でエラー

Traceback (most recent call last):
  File "tatesen2.py", line 16, in <module>
    w.create_line(x, 0, x, 400, fill=c)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/tkinter/__init__.py", line 2486, in create_line
    return self._create('line', args, kw)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/tkinter/__init__.py", line 2474, in _create
    *(args + self._options(cnf, kw))))
_tkinter.TclError: unknown color name "ff0000"
