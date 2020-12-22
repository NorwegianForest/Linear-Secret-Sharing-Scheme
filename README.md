# Linear Secret Sharing Scheme (LSSS)
### Test Results

```
Access formula: (A or B)
ρ(i) Matrix
A    [1]
B    [1]

Access formula: (A and B)
ρ(i) Matrix
A    [0, -1]
B    [1, 1]

Access formula: (B or C)
ρ(i) Matrix
B    [1]
C    [1]

Access formula: (B and C)
ρ(i) Matrix
B    [0, -1]
C    [1, 1]

Access formula: ((A or B) or C)
ρ(i) Matrix
A    [1]
B    [1]
C    [1]

Access formula: ((A and B) and C)
ρ(i) Matrix
A    [0, 0, -1]
B    [0, -1, 1]
C    [1, 1, 0]

Access formula: (A or (B or C))
ρ(i) Matrix
A    [1]
B    [1]
C    [1]

Access formula: (A and (B and C))
ρ(i) Matrix
A    [0, -1, 0]
B    [0, 0, -1]
C    [1, 1, 1]

Access formula: ((A or B) and C)
ρ(i) Matrix
A    [0, -1]
B    [0, -1]
C    [1, 1]

Access formula: (A or (B and C))
ρ(i) Matrix
A    [1, 0]
B    [0, -1]
C    [1, 1]

Access formula: (C or D)
ρ(i) Matrix
C    [1]
D    [1]

Access formula: (C and D)
ρ(i) Matrix
C    [0, -1]
D    [1, 1]

Access formula: ((A and B) or (C and D))
ρ(i) Matrix
A    [0, -1, 0]
B    [1, 1, 0]
C    [0, 0, -1]
D    [1, 0, 1]

Access formula: ((A or B) and (C or D))
ρ(i) Matrix
A    [0, -1]
B    [0, -1]
C    [1, 1]
D    [1, 1]

Access formula: (((A and B) or (C and D)) or ((A or B) and (C or D)))
ρ(i) Matrix
A    [0, -1, 0, 0]
B    [1, 1, 0, 0]
C    [0, 0, -1, 0]
D    [1, 0, 1, 0]
A    [0, 0, 0, -1]
B    [0, 0, 0, -1]
C    [1, 0, 0, 1]
D    [1, 0, 0, 1]

Access formula: (E and (((A and B) or (C and D)) or ((A or B) and (C or D))))
ρ(i) Matrix
E    [0, -1, 0, 0, 0]
A    [0, 0, -1, 0, 0]
B    [1, 1, 1, 0, 0]
C    [0, 0, 0, -1, 0]
D    [1, 1, 0, 1, 0]
A    [0, 0, 0, 0, -1]
B    [0, 0, 0, 0, -1]
C    [1, 1, 0, 0, 1]
D    [1, 1, 0, 0, 1]

```