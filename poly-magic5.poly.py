%%kernel_defs
python1 = kernel(language="python", executable="/usr/bin/env python")
R1 = kernel(language="R", executable="/usr/bin/env /R")
shell1 = kernel(language="bash", executable="/bin/bash")
/%%

%%meta
maybe other meta stuff here?
styles? directives?
/%%

%%shell1
a=10
%%

%%markdown:
---
stylesheet: sleek
imports:
    a: shell1.a
---
This section can be markdown.
`this is normal displayed code`.

This is executed code: ${a}.
The syntax for executed code is simply javascript literals.

```python
This is a normal block (not executed)
displayed code (here python syntax highlighted)
```

Or even latex $\frac{1}{\sqrt{\sigma}}$.

Or variables can be accessed by namespace.
In `shell1`, `a` has the value ${shell.a}.

The current directory is $bash{pwd}.
/%%

%%html:
---
stylesheet: style.css
---
This section contains html and even
  <javascript>
    embedded scripts
  </javascript>
as well as displayed code <code>cat("hello")</code>

or executed inline code <inline bash>a="hello"; echo "$a"</inline> that does not
affect other kernels.

or displayed variables such as in shell1, a=<inline shell1>echo "$a"</inline>
/%%

Anything outside of a defined block is ignored. Essentially,
this is where comments go.

Quick code blocks can be made by.

%%python
print("this is a frame not associated with a particular kernel")
/%%

You can import variables by doing:

%%R1:
---
imports:
    myvar: shell1.var1
    the_title: shell1.a
    data: python1.data
stdout: hide
stderr: show
graphics: inline
---
plot(data);
title(the_title);
/%%

Import equivalencies can be defined:

data.table <==> DataFrame (Python), Object (JS), TSV (bash)
string <==> string
int <==> int
Array <==> List, Array, etc.
Dict <==> JS object (JS), nested named lists (R), YAML, XML
etc.

Need definition scheme.
int, float, string, array, dict, table







