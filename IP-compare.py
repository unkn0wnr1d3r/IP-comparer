path_file1=input("Enter the path of source file:")
path_file2=input("Enter file path for comparing:")
unique_count=0
duplicate_count=0
with open(path_file1, "r") as f1:
    data1 = set()
    for line in f1.readlines():
        data1.add(line.strip('\n'))

with open(path_file2, "r") as f2:
    data2 = set()
    for line in f2.readlines():
        data2.add(line.strip('\n'))

unique_list = data1.difference(data2)
duplicate_list = data1.intersection(data2)

with open("duplicate_ip.txt", "w") as duplicate:
    for ip in duplicate_list:
        duplicate.write(ip+ "\n")
        duplicate_count+=1


with open("unique_ip.txt", "w") as unique:
    for ip in unique_list:
        unique.write(ip+ "\n")
        unique_count+=1
print("--------------------------------------------------")
print("\nProcess completed ...\n")
print("\nUnique IP's are stored in unique_ip.txt\n")
print("\nDuplicate IP's are stored in duplicate_ip.txt\n")
print("\n Total unique IP:"+str(unique_count))
print("\n Total duplicate IP:"+str(duplicate_count))
print("--------------------------------------------------")