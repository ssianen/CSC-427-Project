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