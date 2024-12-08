import sys
from pybloom_live import BloomFilter


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
    count=1
    for line in f:
        if count==2:
            pure_line = line.strip()
            base_list += list(pure_line)
        if count==4:
            count=1
        else:
            count +=1
    f.close()

    kmers = [] #list containing all 31mers
    for i in range(len(base_list)-31):
        thirty_one = base_list[i:i+31]
        s=""
        kmers.append(s.join(thirty_one))
    return kmers

#def 
    #add to bloom filter using bf.add(thingtoadd)



def main():
    """
    """
    fastq_file = sys.argv[1]
    kmer_list = split_kmers(fastq_file)
    hash_dict = {} #initialize dictionary that is used as a hash table T
    m = 8*(len(kmer_list))
    #*********may want to change bloom filter error rate from  0.01
    bf = BloomFilter(m, 0.01)#initialize empty bloomfilter of size m=8xn where n=the number of kmers
    print(f"Number of hash functions: {bf.num_slices}")




if __name__ == "__main__":
    main()