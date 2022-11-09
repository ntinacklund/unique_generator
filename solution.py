from random import randint
from collections import Counter


def generate_numbers():
    filepath = input("Name your file: ")
    amount = int(input("Amount: "))
    with open(filepath, "w", encoding="utf-8") as f:
        for _ in range(amount):
            random_number = randint(1, 100)
            f.write(str(random_number)+"\n")
    print("----FILE HAS BEEN GENERATED----\n\n")
    return filepath

def count_uniques(filepath):
    count_list = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f.readlines():
            this_line = line.strip("\n")
            count_list.append(int(this_line))
    unique_counter = Counter(count_list)
    print(f"Amount of unique numbers: {len(unique_counter)}")
    #print(unique_counter)
    ordered_counter = dict(sorted(unique_counter.items()))
    
    for x in ordered_counter:
        print(x,"\t", ordered_counter[x])
    
            
def main():
    filepath = generate_numbers()
    count_uniques(filepath)

if __name__ == "__main__":
    main()
