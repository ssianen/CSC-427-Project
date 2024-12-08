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

def fill_bloom_hash(B,T,k):
    """
    -function adds kmers to bloom filter B and dictionary T
    - parameter B is a bloom filter
    - parameter T is a dictionary acting as a hash table
    - parameter k is a list of all kmers in the first fasta file (not reverse complement)
    
    """
    for kmer in k:
        if kmer in B: 
            if kmer not in T:
                T[kmer] = 0
        else:
            B.add(kmer)

def increment(T,k):
    """
    - function increments the count of kmers in hash dictionary for every time they appear in the read
    - parameter T is the dictionary that acts as a hash table
    - parameter k is a list of kmers
    """
    for kmer in k:
        if kmer in T:
            T[kmer] = T[kmer] + 1

def remove_unique(T):
    """
    - function removes all false positives from the dictionary
    - parameter T is the dictionary that acts as a hash table
    - returns new dictionary only containing kmers that have appeared in reads more than once
    """
    new_T = {}
    for key in T:
        if T[key] != 1:
            new_T[key] = T[key]
    return new_T


def reverse_complement(kmerToRC):
    """
    """

    RCstr = ""

    for baseIndex in range(1, len(kmerToRC)+1): #read the kmer in reverse
        base = kmerToRC[-baseIndex]
        if (base.upper() == "A"):
            RCstr += "T"
        elif (base.upper() == "C"):
            RCstr += "G"
        elif (base.upper() == "G"):
            RCstr += "C"
        elif (base.upper() == "T"):
            RCStr += "A"

    print(RCstr)


def dump(T):
    """
    - function outputs all the kmers and their counts for all kmers that appear more than once
    - parameter T is the dictionary that acts as a hash table
    """
    for kmer in T:
        x_rep = kmer #*******this should be the minimum lexographically of the kmer or its reverse complement
        print("the kmer is ",x_rep," with count ",T[x_rep]) #*********probably need a different print format




def main():
    """
    """
    fastq_file = sys.argv[1]
    kmer_list = split_kmers(fastq_file)
    hash_dict = {} #initialize dictionary that is used as a hash table, key is kmer, value is count of appearences of kmer. all kmers in dict should appear at least once in reads
    m = 8*(len(kmer_list))
    #*********may want to change bloom filter error rate from  0.01
    bf = BloomFilter(m, 0.01)#initialize empty bloomfilter of size m=8xn where n=the number of kmers
    bf.num_slices = 3 #set the number of hash functions used for the bloom filter to 3
    fill_bloom_hash(bf,hash_dict,kmer_list)
    increment(hash_dict,kmer_list)
    final_dict = remove_unique(hash_dict)
    dump(final_dict)

if __name__ == "__main__":
    main()