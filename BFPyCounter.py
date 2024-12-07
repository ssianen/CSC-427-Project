import sys
import logging

'''
BFPyCounter: Reimplementing BFCounter to count k-mers in Python and Compiling with Codon

Based the BFCounter software, from the paper by Melsted and Pritchard: Efficient counting of k-mers in DNA sequences using a bloom filter. 
BMC Bioinformatics 2011 12:333. Available at http://www.biomedcentral.com/1471-2105/12/333

How to Compile and Run the Program:
codon run BFPyCounter.py BFPyCounter count      -------     'Counts k-mer occurences in sequence files'
codon run BFPyCounter.py BFPyCounter dump       -------     'Writes k-mer occurences into a tab-separated text file'
'''

def main():
    int argc = len(sys.argv)
    str command = sys.argv[1]

    if (argc < 2):
        print("Oops! Not enough arguments. Please provide 2")
    else:
        if (command == "count"):
            CountBF(argc-1, argv[1])
        elif (command == "dump"):
            DumpBF(argc-1, argv[1])


if __name__ == "__main__":
    main()



from pybloom_live import BloomFilter

# Create a Bloom filter
bloom = BloomFilter(capacity=1000, error_rate=0.01)

# Add an item
bloom.add("example")

# Check internal structure
print("empty bit array ")
print(bloom.bitarray)  # Shows the internal bit array (compact representation of bits)

bloom.add("example")
print("something in array")
print(bloom.bitarray)  # Shows the internal bit array (compact representation of bits)
print(" ")
print(bloom.num_bits)  # Total number of bits in the bit array
print(" ")

'''
python3 p1.py chr22.fa test.sam
#To change file permissions
chmod +x p1.py  
'''


from pybloom_live import BloomFilter

class BloomFilter:

    def CreateBF():
        bf = BloomFilter(capacity=1000, error_rate=0.01)

    def WriteToBF(BloomFilter bf, item):
        bf.add(item)

    
    def ReadBF(BloomFilter bf):
        print(bf.bitarray)
        print(bf.num_bits)
        print(bf.num_hashes)

    # def ClearBF():
    #     #how ?

