"""
A script that extracts the memorymap from an update	file. Pass section 4 and a address

The	script uses	very basic shellcode extraction	algorithm

Copyright (c) 2018 Hypoxic
ALL	RIGHTS RESERVED.

Revision history
=========================
v1.0 - initial version

"""

import re
import zlib
import struct
import sys, getopt

def main(argv):
	filename = ''
	offset = ''
	
	if(len(sys.argv) < 2):
		print("Usage: section4.bin <offset>\n")
		sys.exit(2)

	filename=sys.argv[1]
	offset=int(sys.argv[2],16)
	
	print ("%s %x" % (filename, offset))
	
	with open(filename, "rb") as f:
		f.seek(offset)
		# Read the data
		
		print("Align Type Count Size\n")
		segment = 0
		
		while f:
			align = int.from_bytes(f.read(4), byteorder='little')
			
			if(align == 0 ):
				break
			
			ty = int.from_bytes(f.read(4), byteorder='little')
			
			if(ty == 0 ):
				break
			
			cn = int.from_bytes(f.read(4), byteorder='little')
			
			if(cn == 0 ):
				break
				
			sz = int.from_bytes(f.read(4), byteorder='little')
					
			print("[%d] %08x %08x %04x %08x\n" % (segment, align,ty,  cn, sz))
			segment += 1
		
			for i in range(cn):
				v = int.from_bytes(f.read(4), byteorder='little')	
				#print("\t\t%08x" % (v))
			
			# disgard end byte
	
	print("done\n")
	
	return 1

if __name__ == "__main__":
	main(sys.argv[1:])