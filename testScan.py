import mercury
reader = mercury.Reader("tmr:///dev/ttyUSB0")
reader.set_region("NA2")
reader.set_read_plan([1],"GEN2")
reader.set_read_powers([1],[500])

print("Starting RFID Single Read Script...")
readTag = reader.read();
apc_code=str(readTag[0]);
apc = apc_code[2:26]
print("The tag being read is:",apc_code)
print("Formatted Code is: ",apc)
