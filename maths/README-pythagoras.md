Task: print N(c) where c = 10000

Performance profiles using cProfile

V1 - using generator for pairs

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

V2 - using for loops instead of generator for pairs

```
         78522688 function calls in 48.299 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   48.299   48.299 <string>:1(<module>)
        1   42.757   42.757   48.299   48.299 pythagoras.py:5(num_triplets)
        1    0.000    0.000   48.299   48.299 {built-in method builtins.exec}
 39261342    3.084    0.000    3.084    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 39261342    2.458    0.000    2.458    0.000 {method 'is_integer' of 'float' objects}
```

V3 - break when the sum of squares for (x,b) is larger than c squard

```
         78522688 function calls in 41.187 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   41.187   41.187 <string>:1(<module>)
        1   35.730   35.730   41.187   41.187 pythagoras.py:5(num_triplets)
        1    0.000    0.000   41.187   41.187 {built-in method builtins.exec}
 39261342    2.990    0.000    2.990    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 39261342    2.467    0.000    2.467    0.000 {method 'is_integer' of 'float' objects}
```



