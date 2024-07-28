def main():
    list_a = [input("Input an element for the first list: ") for _ in range (3)]
    list_b = [input("Input an element for the second list: ") for _ in range (3)]

    print(difference(list_a, list_b))

def difference(l1, l2):
    list_difference = [i for i in l1 + l2 if i not in l1 or i not in l2]

    return list_difference

if __name__ == "__main__":
    main()