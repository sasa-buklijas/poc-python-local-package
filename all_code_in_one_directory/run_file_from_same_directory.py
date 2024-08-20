from file_in_same_directory import double

def main():
    assert double(2) == 4
    assert not double(2) == 5

if __name__ == "__main__":
    main()
