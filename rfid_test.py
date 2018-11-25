import mercury
reader = mercury.Reader("tmr:///dev/ttyUSB0")
BoxA =["b'E20000196302010027100886'"];
BoxB =["b'E2000019630201032710088F'"];
BoxC =["b'E20000196302010627100895'"];

print("Starting RFID Single Read Script...");
reader.set_region("NA2")
reader.set_read_plan([1],"GEN2")
reader.set_read_powers([1],[500])
#print("Reader Model Is: ",reader.get_model())
#print("The Regions supported by the Reader are: ",reader.get_supported_regions())
#print("The availiable antennas are: ",reader.get_antennas())
#print("The read powers availiable are: ",reader.get_read_powers())
#reader.start_reading(lambda tag: print(tag.epc))
readTag = reader.read();
print("The tag being read is:", readTag)
#print("Read Tag is", type(readTag));
#print("BoxA is type",type(BoxC));
if (str(readTag[0]) == str(BoxA[0])):
	print("Box A was read. Box A contains Apples.");
elif (str(readTag[0])  == str(BoxB[0])):
	print("Box B was scanned. Box B has Bananas.");
elif (str(readTag[0]) == str(BoxC[0])):
	print("Box C was scanned. Box C has Oranges.");
#print(str(BoxC[0]) == str(readTag[0]));
#print(type(readTag[0]));
#print(type(BoxC[0]));
