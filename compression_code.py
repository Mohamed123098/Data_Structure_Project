import heapq
import os
class compression:
    def __init__(self, File_path):
        self.codes = {}
        self.reverse_mapping = {}
        self.heap = []
        self.File_path = File_path
    class node_of_Heap:
        def __init__(self, character, f):
            self.left = None
            self.right = None
            self.f = f
            self.character = character
            # f = frequency
        # defination of  comparators less_than and equals
        def __lt__(self, other):
            return self.f < other.f

        def __eq__(self, other):
            if (other == None):
                return False
            if (not isinstance(other, node_of_Heap)):
                return False
            return self.f == other.f
        # Compression functions
    def merge_of_nodes(self):
        while (len(self.heap)> 1):
            node_1 = heapq.heappop(self.heap)
            node_2 = heapq.heappop(self.heap)
            merged = self.node_of_Heap(None, node_1.f + node_2.f)
            merged.left = node_1
            merged.right = node_2
            heapq.heappush(self.heap, merged)
    # This function is used to merge between nodes
    def priority_queue(self, frequency):
        for k in frequency: #k is key
            node = self.node_of_Heap(k, frequency[k])
            heapq.heappush(self.heap, node)
    # This function is used for making priority queue
    def calc_frequency(self, text_file):
        frequency = {}
        for character in text_file:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] = frequency[character]+1
        return frequency
    # This function using for calculation of frequency and return it
    def make_codes_for_characters(self):
        current_code = ""
        rootCode = heapq.heappop(self.heap)
        self.make_code_helper(rootCode, current_code)
    # This function is used for making codes for characters and save it
    def make_code_helper(self, root_code, current_code):
        if (root_code.character != None):
            self.codes[root_code.character] = current_code
            self.reverse_mapping[current_code] = root_code.character
            return
        if (root_code == None):
            return
        self.make_code_helper(root_code.right, current_code + "1")
        self.make_code_helper(root_code.left, current_code + "0")
    # This function is used for helping in making code
    def pad_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text =encoded_text + "0"
        padded_information = "{0:08b}".format(extra_padding)
        encoded_text = padded_information + encoded_text
        return encoded_text
    # This function is used for pading the text which returned from replace_chracter_with_code function
    def replace_chracter_with_code(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text
    # This function is used for replacing chracters with code and return it
    def convert_bits_into_bytes(self, padded_encoded_text_file):
        if (len(padded_encoded_text_file) % 8 != 0):
            print("The encoded text not padded correct")
            exit(0)
        b = bytearray()
        for i in range(0, len(padded_encoded_text_file), 8):
            byte = padded_encoded_text_file[i:i + 8]
            b.append(int(byte, 2))
        return b
    # This function using for converting bits into bytes and return array of bytes
    def compress_file(self):
        file_name, file_extension = os.path.splitext(self.File_path)
        output_path = file_name +"_compressed_file"+ ".txt"

        with open(self.File_path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.calc_frequency(text)
            self.priority_queue(frequency)
            self.merge_of_nodes()
            self.make_codes_for_characters()

            encoded_text = self.replace_chracter_with_code(text)
            padded_encoded_text = self.pad_text(encoded_text)

            b = self.convert_bits_into_bytes(padded_encoded_text)
            output.write(bytes(b))

        print("The file is compressed...")
        return output_path
    # This function is used for compressing the text file
def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if (current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text
    # This function is used for decoding the text file and return it
    def delecte_padding(self, padded_text):
        padded_information = padded_text[:8]
        extra_padding = int(padded_information, 2)

        padded_text = padded_text[8:]
        encoded_text = padded_text[:-1 * extra_padding]

        return encoded_text
    # This function is used for deleting padding from the text file
    def decompress_file(self, input_path):
        file_name, file_extension = os.path.splitext(self.File_path)
        output_path = file_name + "_decompressed_file" + ".txt"

        with open(input_path, 'rb') as file, open(output_path, 'w') as output_file:
            bit_string = ""

            byte = file.read(1)
            while (len(byte) > 0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            encoded_text = self.delecte_padding(bit_string)

            decompressed_text = self.decode_text(encoded_text)

            output_file.write(decompressed_text)

        print("The file is decompressed... ")
        return output_path
    # This function is used for decompressing the text file and return it
    # i decompress file to check the compression algorithm doesn't change in original file 
    
