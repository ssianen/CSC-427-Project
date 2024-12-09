import sys
from pybloom_live import BloomFilter
import pypocketmap as pkm

def split_kmers(fastq_f):
    """
    - takes a fastq file
    - concatonates all lines containing a read into a list of bases
    - finds all 31mers in the file
    - returns the list of 31mers
    """
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
    #new_T = pkm.create(str, int)
    for key in T:
        if T[key] == 1:
            del T[key]
    return T

def reverse_complement(kmerToRC):
    """
    - function finds the reverse complement of a 31mer
    - parameter kmerToRC is a kmer with k=31
    - return value is a 31mer that is a reverse complement of the input kmer
    """
    RCstr = ""
    rev = kmerToRC[::-1]
    for x in rev: #read the kmer in reverse
        if (x.upper() == "A"):
            RCstr += "T"
        elif (x.upper() == "C"):
            RCstr += "G"
        elif (x.upper() == "G"):
            RCstr += "C"
        elif (x.upper() == "T"):
            RCstr += "A"
    return(RCstr)

def dump(T):
    """
    - function outputs all the kmers and their counts for all kmers that appear more than once to a new file called dump.txt
    - parameter T is the dictionary that acts as a hash table
    """
    f = open("dump.txt", "w")
    wa = "kmer"
    wb = "count"
    f.write(f"{wa}\t{wb}\n")
    for kmer in T:
        rev_comp = reverse_complement(kmer)
        x_rep = min(str(kmer), rev_comp) #*******this should be the minimum lexographically of the kmer or its reverse complement
        count =T[kmer]
        f.write(f"{x_rep}\t{count}\n")
    f.close()

def main():
    """
    """
    fastq_file = sys.argv[1]
    kmer_list = split_kmers(fastq_file)
    hash_dict = pkm.create(str, int) #initialize dictionary that is used as a hash table, key is kmer, value (64bit) is count of appearences of kmer. all kmers in dict should appear at least once in reads
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