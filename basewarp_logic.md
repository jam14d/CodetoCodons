### Logic for Basewarp game

<br>Take one base at a time from self.template_strand.</br>
<br>Example: If self.template_strand = "ATGCTC", the loop goes through "A", "T", "G", etc.</br>

Look up the complementary base using the self.base_pairing dictionary:

```python
self.base_pairing = {"A": "T", "T": "A", "C": "G", "G": "C"}
```

If base = "A", the dictionary gives "T".
If base = "T", the dictionary gives "A".
If base = "G", the dictionary gives "C".
If base = "C", the dictionary gives "G".

Collect the complementary bases into a new list (self.correct_strand).

If self.template_strand = "ATGCTC", it builds:

```python
self.correct_strand = ["T", "A", "C", "G", "A", "G"]
```

### Visualization
If self.template_strand = "ATGCTC", the process looks like this:

| Template Base | Complementary Base (Looked up in Dictionary) |
|--------------|----------------------------------|
| "A"        | "T"                           |
| "T"        | "A"                           |
| "G"        | "C"                           |
| "C"        | "G"                           |
| "T"        | "A"                           |
| "C"        | "G"                           |

So the final self.correct_strand is:

```python
["T", "A", "C", "G", "A", "G"]
```

