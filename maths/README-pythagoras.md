Task: print N(c) where c = 10000

First version profile results:

```
         178526833 function calls in 69.853 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   69.853   69.853 <string>:1(<module>)
        1   51.548   51.548   69.853   69.853 pythagoras.py:5(num_triplets)
 49995002    4.940    0.000    4.940    0.000 pythagoras.py:6(<genexpr>)
        1    0.000    0.000   69.853   69.853 {built-in method builtins.exec}
 49995001    7.454    0.000   12.393    0.000 {built-in method builtins.next}
 39268413    3.277    0.000    3.277    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 39268413    2.635    0.000    2.635    0.000 {method 'is_integer' of 'float' objects}
```
