### `printff.h`

A single header library which provides the `printff` macro, which is similiar to `printf`, but doesn't require type specifiers in the format string.

In order to combine variadic function and macro arguments with dispatching on types, I had to use some ugly techniques, which I automated with a code generating python file. The end result:

``` C
printff("Hello %, % + % = %", "World", 3.0, 1, 3.0 + 1);
```

```
Hello World, 3.000000 + 1 = 4.000000 
```
