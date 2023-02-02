from models import *

def generate_txt():
    question = complain.objects.all()
    with open('complain.txt','wb') as file:
        for i in question:
            file.write(i.title)
            # file.write("\n")
    # file.close()

generate_txt()