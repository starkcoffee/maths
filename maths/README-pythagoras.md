Task: print N(c) where c = 10000

Performance profiles using cProfile

[V1 - using generator for pairs](https://github.com/starkcoffee/maths/commit/b41704ecb8b75f1c7b5b1ebaa35b2ccd2a86da22)

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

[V2 - using for loops instead of generator for pairs](https://github.com/starkcoffee/maths/commit/c113cebbbcb749379d70087cd4fcff9df949e81a)

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

[V3 - break when the sum of squares for (x,b) is larger than c squared](https://github.com/starkcoffee/maths/commit/62e053750e3fcd9a256bc57a1f5f843f93e381e9)

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

[V4 - use set comparison rather than sqrt](https://github.com/starkcoffee/maths/commit/8a9d24e55c12f8422e4ef58b8da90b78ff70a772)

```
         10004 function calls in 29.056 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   29.056   29.056 <string>:1(<module>)
        1   29.053   29.053   29.056   29.056 pythagoras.py:5(num_triplets)
    10000    0.003    0.000    0.003    0.000 pythagoras.py:8(<genexpr>)
        1    0.000    0.000   29.056   29.056 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

V5 - stop squaring n in the inner loop 😅 

```
         10004 function calls in 20.995 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   20.995   20.995 <string>:1(<module>)
        1   20.991   20.991   20.995   20.995 pythagoras.py:5(num_triplets)
    10000    0.004    0.000    0.004    0.000 pythagoras.py:8(<genexpr>)
        1    0.000    0.000   20.995   20.995 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

V6 - memoize b squared

```
         10004 function calls in 11.765 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   11.765   11.765 <string>:1(<module>)
        1   11.761   11.761   11.765   11.765 pythagoras.py:5(num_triplets)
    10000    0.004    0.000    0.004    0.000 pythagoras.py:8(<genexpr>)
        1    0.000    0.000   11.765   11.765 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

V7 - retrieve all squares from list rather than squaring

```
         5 function calls in 5.285 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    5.285    5.285 <string>:1(<module>)
        1    5.282    5.282    5.284    5.284 pythagoras.py:5(num_triplets)
        1    0.002    0.002    0.002    0.002 pythagoras.py:8(<listcomp>)
        1    0.000    0.000    5.285    5.285 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
```
