import mercury
reader = mercury.Reader("tmr:///dev/ttyUSB0")

reader.set_region("NA2")
reader.set_read_plan([1],"GEN2")
print("Reader Model Is: ",reader.get_model())
print("The Regions supported by the Reader are: ",reader.get_supported_regions())
print("The availiable antennas are: ",reader.get_antennas())
print("The read powers availiable are: ",reader.get_read_powers())
reader.start_reading(lambda tag: print(tag.epc), 2000)

