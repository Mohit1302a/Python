def check_for_word():
    word="learning"
    with open("practice.txt","r") as f:
        data=f.read()
        if(data.find(word)!=-1):
            print("found")
        else:
            print("notfound")

check_for_word()