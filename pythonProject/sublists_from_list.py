def chunked(my_list):
    result = [[]]
    for n in range(1, len(my_list)):
        for i in range(0, len(my_list) -n + 1):
            result.append(my_list[i:i + n])
    result.append(my_list)
    return result


def main():
    my_list = input().split()
    print(chunked(my_list))


if __name__ == "__main__":
    main()
