# Circuit generator for SHA256
# python 3.7.4
# encoding=utf-8

import os
import string

def ma_gen():
    f = open("circuit\\ma", "w")
    if f.mode == "w":
        # generate input and output wire name tag
        for i in range(0, 32):
            s = "x_" + str(i) + ' '
            f.write(s)
        for i in range(0, 32):
            s = "y_" + str(i) + ' '
            f.write(s)
        for i in range(0, 32):
            s = "z_" + str(i) + ' '
            f.write(s)
        f.write("\n")
        for i in range(0, 32):
            s = "o_" + str(i) + ' '
            f.write(s)
        f.write("\n")

        # x ∧ y = t1
        for i in range(0, 32):
            s = "AND x_" + str(i) + " y_" + str(i) + " t1_" + str(i) + " \n"
            f.write(s)
        # x ∧ z = t2
        for i in range(0, 32):
            s = "AND x_" + str(i) + " z_" + str(i) + " t2_" + str(i) + " \n"
            f.write(s)
        # y ∧ z = t3
        for i in range(0, 32):
            s = "AND y_" + str(i) + " z_" + str(i) + " t3_" + str(i) + " \n"
            f.write(s)
        # t1 ∧ t2 = t4
        for i in range(0, 32):
            s = "XOR t1_" + str(i) + " t2_" + str(i) + " t4_" + str(i) + " \n"
            f.write(s)
        # t3 ∧ t4 = o
        for i in range(0, 32):
            s = "XOR t3_" + str(i) + " t4_" + str(i) + " o_" + str(i) + " \n"
            f.write(s)
    f.close()

def ch_gen():
    f = open("circuit\\ch", "w")
    if f.mode == "w":
        # generate input and output wire name tag
        for i in range(0, 32):
            s = "x_" + str(i) + ' '
            f.write(s)
        for i in range(0, 32):
            s = "y_" + str(i) + ' '
            f.write(s)
        for i in range(0, 32):
            s = "z_" + str(i) + ' '
            f.write(s)
        f.write("\n")
        for i in range(0, 32):
            s = "o_" + str(i) + ' '
            f.write(s)
        f.write("\n")

        # x ∧ y = t1
        for i in range(0, 32):
            s = "AND x_" + str(i) + " y_" + str(i) + " t1_" + str(i) + " \n"
            f.write(s)

        # ~x = t2
        for i in range(0, 32):
            s = "NAND x_" + str(i) + " x_" + str(i) + " t2_" + str(i) + " \n"
            f.write(s)

        # t2 ∧ z = t3
        for i in range(0, 32):
            s = "AND t2_" + str(i) + " z_" + str(i) + " t3_" + str(i) + " \n"
            f.write(s)

        # t3 ∧ t4 = o
        for i in range(0, 32):
            s = "XOR t1_" + str(i) + " t3_" + str(i) + " o_" + str(i) + " \n"
            f.write(s)
    f.close()

def s00_gen():
    f = open("circuit\\s00", "w")
    if f.mode == "w":
        # generate input and output wire name tag
        for i in range(0, 32):
            s = "x_" + str(i) + ' '
            f.write(s)
        f.write("\n")
        for i in range(0, 32):
            s = "o_" + str(i) + ' '
            f.write(s)
        f.write("\n")

        # (x rotate right 2) XOR (x rotate right 13)
        for i in range(0, 32):
            s = "XOR x_" + str((i + 30) % 32) + " x_" + str((i + 19) % 32) + " t1_" + str(i) + " \n"
            f.write(s)
        # t1 XOR (x rotate right 22)
        for i in range(0, 32):
            s = "XOR t1_" + str(i) + " x_" + str((i + 10) % 32) + " o_" + str(i) + " \n"
            f.write(s)
    f.close()

def s01_gen():
    f = open("circuit\\s01", "w")
    if f.mode == "w":
        # generate input and output wire name tag
        for i in range(0, 32):
            s = "x_" + str(i) + ' '
            f.write(s)
        f.write("\n")
        for i in range(0, 32):
            s = "o_" + str(i) + ' '
            f.write(s)
        f.write("\n")

        # (x rotate right 6) XOR (x rotate right 11)
        for i in range(0, 32):
            s = "XOR x_" + str((i + 26) % 32) + " x_" + str((i + 21) % 32) + " t1_" + str(i) + " \n"
            f.write(s)
        # t1 XOR (x rotate right 25)
        for i in range(0, 32):
            s = "XOR t1_" + str(i) + " x_" + str((i + 7) % 32) + " o_" + str(i) + " \n"
            f.write(s)
    f.close()

def s10_gen():
    f = open("circuit\\s10", "w")
    if f.mode == "w":
        # generate input and output wire name tag
        for i in range(0, 32):
            s = "x_" + str(i) + ' '
            f.write(s)
        f.write("\n")
        for i in range(0, 32):
            s = "o_" + str(i) + ' '
            f.write(s)
        f.write("\n")

        # (x rotate right 7) XOR (x rotate right 18)
        for i in range(0, 32):
            s = "XOR x_" + str((i + 25) % 32) + " x_" + str((i + 14) % 32) + " t1_" + str(i) + " \n"
            f.write(s)
        # t1 XOR (x shift right 3)
        # not sure add 0(AND) or 1(NAND)
        for i in range(0, 3):
            s = "AND t1_" + str(i) + " t1_" + str(i) + " o_" + str(i) + " \n"
            f.write(s)
        for i in range(3, 32):
            s = "XOR t1_" + str(i) + " x_" + str((i + 29) % 32) + " o_" + str(i) + " \n"
            f.write(s)
    f.close()

def s11_gen():
    f = open("circuit\\s11", "w")
    if f.mode == "w":
        # generate input and output wire name tag
        for i in range(0, 32):
            s = "x_" + str(i) + ' '
            f.write(s)
        f.write("\n")
        for i in range(0, 32):
            s = "o_" + str(i) + ' '
            f.write(s)
        f.write("\n")

        # (x rotate right 17) XOR (x rotate right 19)
        for i in range(0, 32):
            s = "XOR x_" + str((i + 15) % 32) + " x_" + str((i + 13) % 32) + " t1_" + str(i) + " \n"
            f.write(s)
        # t1 XOR (x shift right 10)
        # not sure add 0(AND) or 1(NAND)
        for i in range(0, 10):
            s = "AND t1_" + str(i) + " t1_" + str(i) + " o_" + str(i) + " \n"
            f.write(s)
        for i in range(10, 32):
            s = "XOR t1_" + str(i) + " x_" + str((i + 22) % 32) + " o_" + str(i) + " \n"
            f.write(s)
    f.close()

def main():
    # print(os.path.abspath('.'))
    if not os.path.exists("circuit"):
        os.mkdir("circuit")
    ch_gen()
    ma_gen()
    s00_gen()
    s01_gen()
    s10_gen()
    s11_gen()

# main function execution
if __name__ == "__main__":
    main()