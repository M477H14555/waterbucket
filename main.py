import sys

water_in_bucket = {8: 5, 5: 0, 3: 0}


def get_empty_bucket():
    bucket = []
    for index in range(8):
        if water_in_bucket[8] < index+1:
            bucket.append("      ")
        else:
            bucket.append('WWWWW')

    for index in range(5):
        if water_in_bucket[5] < index+1:
            bucket.append("      ")
        else:
            bucket.append('WWWWW')

    for index in range(3):
        if water_in_bucket[3] < index+1:
            bucket.append("      ")
        else:
            bucket.append('WWWWW')

    return bucket

def display_buckets(bucket):
    print(f"""
    8|{bucket[7]}|
    7|{bucket[6]}|
    6|{bucket[5]}|
    5|{bucket[4]}|  5|{bucket[12]}|
    4|{bucket[3]}|  4|{bucket[11]}| 
    3|{bucket[2]}|  3|{bucket[10]}|  3|{bucket[15]}|
    2|{bucket[1]}|  2|{bucket[9]}|  2|{bucket[14]}|
    1|{bucket[0]}|  1|{bucket[8]}|  1|{bucket[13]}|
    +--8L---+  +--5L---+  +--3L---+
""")


def main():
    while True:
        print('Try to get 4L of water into one of these buckets:')
        bucket = get_empty_bucket()
        display_buckets(bucket)

        while True:
            print('You can:')
            print('\t(F)ill the bucket')
            print('\t(E)mpty the bucket')
            print('\t(P)our one bucket into another')
            print('\t(Q)uit')
            bottom = input("> ").upper()
            if bottom =="Q" or bottom == "QUIT":
                print("Thanks for playing!")
                sys.exit()

            if bottom in ("F", "E", "P"):
                break
            print("Please enter in F, E, P or Q")

        print("Select a bucket: 8, 5, 3 or you can (Quit)")
        while True:
            src_bucket = input("> ").upper()
            if src_bucket == "Q" or src_bucket == "QUIT":
                print("Thanks for playing!")
                sys.exit()

            if src_bucket in ("8", "5", "3"):
                src_bucket = int(src_bucket)
                break

            print("Select a bucket: 8, 5, 3 or you can (Quit)")

        if 4 in water_in_bucket.values():
            print("Well done!")
            sys.exit()

        if bottom == "F":
            water_in_bucket[src_bucket] = src_bucket
        elif bottom == "E":
            water_in_bucket[src_bucket] = 0
        else:
            while True:
                print("Select a bucket 8, 5, 3 or (Q)UIT: ")
                dst_bucket = input("> ").upper()
                if dst_bucket == "Q" or dst_bucket == "QUIT":
                    print("Thanks for playing!")
                    sys.exit()

                if dst_bucket in ("8", "5", "3"):
                    dst_bucket = int(dst_bucket)
                    break

                print("Select a bucket 8, 5, 3 or (Q)UIT: ")

            water_src_bucket = water_in_bucket[src_bucket]
            water_dst_bucket = water_in_bucket[src_bucket]
            empty_in_dst_bucket = dst_bucket - water_in_bucket[dst_bucket]
            amount_to_pour = min(empty_in_dst_bucket, water_src_bucket)

            water_in_bucket[src_bucket] = water_in_bucket[src_bucket] - amount_to_pour
            water_in_bucket[dst_bucket] = water_in_bucket[dst_bucket] + amount_to_pour


if __name__ == '__main__':
    main()