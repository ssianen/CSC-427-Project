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

