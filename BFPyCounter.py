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


    