# SST39SF010 flash programmer
# by Phillip Pearson

# Copyright 2017 Google Inc
# Licensed under the GPL; see LICENSE.txt for details.


# Create (and open) a .wav file to transfer data to an Acorn Electron.

# You'll need a 3.5mm-to-DIN cable to connect the source computer to
# the Electron's cassette input.

import os, stat, sys

def cmd(s):
	print s
	return os.system(s)

fn, leaf, load_addr = sys.argv[1:]

cmd("mkdir -p out")
cmd("cp -v %s out/file" % fn)
size = os.stat("out/file")[stat.ST_SIZE]
load = start = int(load_addr, 16)
print>>open("out/file.inf", "w"), "$.%s\t%X\t%X\t%X" % (
    leaf, load, start, size)
cmd("rm -f out/file.uef")
cmd("python UEFtrans.py out/file.uef new Electron any")
cmd("python UEFtrans.py out/file.uef append out/file")
cmd("rm -f out/file.wav")
cmd("python uef2wave.py out/file.uef out/file.wav")
cmd("open out/file.wav")

print "On the Electron, run: *LOAD %s %x" % (leaf, load)
