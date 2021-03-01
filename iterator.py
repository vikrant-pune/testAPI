

def get_ans( d: int):
    try:
        d = d+1
        yield d
    finally:
        print(f"Final value {d}")

if __name__ == '__main__':
    for x in get_ans(7):
        print (x)
    print("foo")
