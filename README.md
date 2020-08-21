# **Garbled Circuit**

Reading circuit from a file. Only support combinational circuit and it must be hierarchy.

## Circuit File Description Format

The first line contains all of the circuit input name tag, separate with space.  
The second line contains all of the circuit output name tag, separate with space.

The next ***n*** lines are the two-input logic gates description, each line contains the logic type, first input name, second input name, and output name.


## Sample Circuit Description
> circuit_file.txt
```
i1 i2 i3 i4
o1 o2 o3 o4 o5
XOR i1 i2 o1
AND i2 i3 o2
OR i3 i4 o3
NAND o1 i1 o4
NOR o2 o3 o5
```

## Input Format
The input only have one line string ***s*** with 0 or 1. 

## Output Format
Output ***lo*** lines, which indicates the number of circuit output wire and each line has a name tag and a number either 0 or 1.

## Technical Specification
The input string length ***l<sub>s</sub>*** must same as the number of circuit input wire.

## Execute
```
$ python garbled_circuit.py circuit_file.txt
```

## Sample Input:
```
1010
```

## Sample Output:
```
o1 1
o2 0
o3 1
o4 0
o5 0
```

# SHA256 with Garbled Circuit

## Prepare
Using `python circuit_gererator.py` to generate the sha256 circuit file.

## Example
```
$ python sha256_gc.py

RANDOM STRING: A5V6S8M8qoIgte16PPls1Qq7LAtinDSO
Generate garbled circuit:  1.0856802463531494
Drcrypt garbled circuit:  0.11695456504821777
0x2b0fea56f3f4bd0305c0e9c1f69f9b1815563e9699f43ad73c2deab62d213412
```
```
$ python sha256_gc.py uAAAAAAAAAAAA

INPUT STRING: uAAAAAAAAAAAA
Generate garbled circuit:  1.098142147064209
Drcrypt garbled circuit:  0.10696935653686523
03ef0cd7871e4278b1f1b0554678ceee09b13abaf224c666018f98a5c4cd3425
```
