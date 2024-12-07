class DumpBF:

    #Figure out what the purpose of this file is.... 

    '''
    'Counts k-mer occurrences in fastq or fasta files and saves results'
    Usage: "BFPyCounter count [options] fasta or fastq files

    -k, --kmer-size=INT         Size of k-mers, at most (int) (Kmer::MAX_K-1)
    -n, --num-kmers=LONG        Estimated number of k-mers (upper bound)
    -t, --threads=INT
    -c, --chunk-size=INT
    -s, --seed=INT
    -o, --output=STRING
    -b, --bloom-bits=INT
        --quake
        --quality-scale=INT
        --verbose
    '''

    def __init__(self):
        self.k = k
        self.n_kmers = n_kmers
        self.str_output = str_output
        self.verbose = verbose
        self.quake = quake
        self.bloom_filter = bloom_filter
        self.qs = qs
        self.threads = threads
        self.seed = seed
        self.read_chunksize = read_chunksize
        self.files_list = files.list


    # def ...set()

    # def ... get()

    def ParseOptions():
        next

    def GuessQualityScore():
        next

    def CheckOptions():
        next

    
    def PrintSummary():
        next

    def Quake():
        #Creates the hash table and the bloom filter
        next

    

