def check_wordin_line():
    word="I/O"
    data=True
    Line_no=1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if not data:
                break
            if word in data:
                print(Line_no)
                return Line_no
            Line_no += 1
    return -1
check_wordin_line()
