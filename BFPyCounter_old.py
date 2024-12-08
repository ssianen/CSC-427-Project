import sys


def split_kmers(fastq_f):
    """
    - takes a fastq file
    - concatonates all lines containing a read into a list of bases
    - finds all 31mers in the file
    - returns the list of 31mers
    """
    #step1 go through fastq file and make list of every sequence
    base_list = []
    f = open(fastq_f, 'r') #open file to read
    for line in f:
        if line.startswith(("A","C","T","G","N","a","c","t","g","n")):
            pure_line = line.strip()
            base_list += list(pure_line)
    f.close()



def main():
    """
    """
    fastq_file = sys.argv[1]
    kmer_list = split_kmers(fastq_file)
    print(kmer_list)
    print("project is running!")




if __name__ == "__main__":
    main()