from compression_code import compression
import sys
with open('sample.xml') as file:
    lines = file.read()
text_file = open("Output.txt", "w")
text_file.write(lines)
text_file.close()
path_of_File = "Output.txt"

h = compression(path_of_File)

output_path = h.compress_file()
print("Compressed file path: " + output_path)

decom_path = h.decompress_file(output_path)
print("Decompressed file path: " + decom_path)


