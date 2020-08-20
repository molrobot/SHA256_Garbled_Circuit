# SHA256 with Garbled Circuit
# python 3.7.4
# encoding=utf-8

import os
import sys
import string
import random
from garbled_circuit import garbled_circuit

class sha256:
    # initial
    def __init__(self, plaintext):
        self._h = list() # data block of variables h[0] .. h[7]
        self._k = list() # data block of constants k[0] .. k[63]
        self._pathtext = ["ch", "ma", "s00", "s01", "s10", "s11"]
        self._circuit = dict()
        self._input_wire = dict()
        self._output_wire = dict()
        self.message = list()
        self.genTime = 0
        self.decTime = 0

        self.text_to_bits(plaintext)
        
        # load constant data block
        if os.path.isfile("sha256_h") and os.path.isfile("sha256_k"):
            self.read_h()
            self.read_k()
            self.read_circuit()
            self.pre_process()
            self.process()
        else:
            print("sha256_h & sha256_k not found")
            exit(0)
        print("Generate garbled circuit: ", self.genTime)
        print("Drcrypt garbled circuit: ", self.decTime)

    # pre-processing
    def pre_process(self):
        length = len(self.message)
        self.message += "1"
        while len(self.message) % 512 != 448:
            self.message += "0"
        self.message += "{0:064b}".format(length)
        # print(len(self.message))

    # process the message in successive 512-bit chunks
    def process(self):
        chunks = [self.message[i:i + 512] for i in range(0, len(self.message), 512)]
        for chunk in chunks:
            w = self.extend(chunk)
            al = self._h.copy()
            self.main_loop(w, al)
            for i in range(0, 8):
                self._h[i] = format(int(self._h[i], 2) + int(al[i], 2), "032b")
                while len(self._h[i]) > 32:
                    self._h[i] = self._h[i][1:]

    # extend the sixteen 32-bit words into sixty-four 32-bit words
    def extend(self, chunk):
        w = []
        for i in range(0, len(chunk), 32):
            w_ = chunk[i:i + 32]
            w.append(w_)
        for i in range(16, 64):
            s0 = self._sigma("s10", w[i - 15])
            s1 = self._sigma("s11", w[i - 2])
            w_ = format(int(w[i - 16], 2) + int(s0, 2) + \
                        int(w[i - 7], 2) + int(s1, 2), "032b")
            while len(w_) > 32:
                w_ = w_[1:]
            w.append(w_)
        return w

    # process main loop
    def main_loop(self, w, al):
        for i in range(0, 64):
            s0 = self._sigma("s00", al[0])
            ma = self._mach("ma", al[0], al[1], al[2])
            t2 = format(int(s0, 2) + int(ma, 2), "032b")
            while len(t2) > 32:
                t2 = t2[1:]
            s1 = self._sigma("s01", al[4])
            ch = self._mach("ch", al[4], al[5], al[6])
            t1 = format(int(al[7], 2) + int(s1, 2) + int(ch, 2) + \
                        int(self._k[i], 2) + int(w[i], 2), "032b")
            while len(t1) > 32:
                t1 = t1[1:]

            al.pop()
            al.insert(0, format(int(t1, 2) + int(t2, 2), "032b"))
            al[4] = format(int(al[4], 2) + int(t1, 2), "032b")

            while len(al[4]) > 32:
                al[4] = al[4][1:]
            while len(al[0]) > 32:
                al[0] = al[0][1:]

    # Sigma
    def _sigma(self, tag, x):
        gc = garbled_circuit(x, self._input_wire[tag], self._output_wire[tag], self._circuit[tag])
        gc.update()
        ans = gc.ans
        self.genTime += gc.genTime
        self.decTime += gc.decTime
        s = ""
        for i in range(0, 32):
            s += str(ans["o_" + str(i)])
        return s

    # Ma、Ch
    def _mach(self, tag, a, b, c):
        gc = garbled_circuit(a + b + c, self._input_wire[tag], self._output_wire[tag], self._circuit[tag])
        gc.update()
        ans = gc.ans
        self.genTime += gc.genTime
        self.decTime += gc.decTime
        s = ""
        for i in range(0, 32):
            s += str(ans["o_" + str(i)])
        return s

    # produce the final hash value
    # transform binary to heximal
    def hexdigest(self):
        bits = "".join(l for l in self._h)
        return "{0:0{1}x}".format(int(bits, 2), 64)

    # load variables from file
    def read_h(self):
        f = open("sha256_h", "r")
        if f.mode == "r":
            lines = f.readlines()
            for line in lines:
                self._h.append(format(int(line, 16), "032b"))
        # print(self._h)
        f.close()

    # load constants from file
    def read_k(self):
        f = open("sha256_k", "r")
        if f.mode == "r":
            lines = f.readlines()
            for line in lines:
                line_ = line.split()
                for l in line_:
                    self._k.append(format(int(l, 16), "032b"))
        # print(self._k)
        f.close()

    # load circuit
    def read_circuit(self):
        for pathname in self._pathtext:
            circuit = []
            if os.path.isfile("circuit/" + pathname):
                f = open("circuit/" + pathname, "r")
                if f.mode == "r":
                    lines = f.readlines()
                    self._input_wire[pathname] = lines.pop(0).split()
                    self._output_wire[pathname] = lines.pop(0).split()
                    for line in lines:
                        circuit.append(line)
                    self._circuit[pathname] = circuit
                f.close()

    # transform text to binary
    def text_to_bits(self, text, encoding="utf-8", errors="surrogatepass"):
        bits = bin(int.from_bytes(text.encode(encoding, errors), "big"))[2:]
        self.message = bits.zfill(8 * ((len(bits) + 7) // 8))

def main():
    if len(sys.argv) == 1:
        plaintext = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=32))
        print("RANDOM STRING: " + plaintext)
    else:
        plaintext = sys.argv[1]
        print("INPUT STRING: " + plaintext)
    sha256_gc = sha256(plaintext)
    print(sha256_gc.hexdigest())

if __name__ == "__main__":
    main()
