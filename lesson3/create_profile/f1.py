
def create_profile(given_name, *surnames, **details):
    name = given_name;
    if(surnames):
        name = name + " " + " ".join(surnames)
    print(name)
    for k,v in details.items():
        print(k, str(v), sep = ':')
        



if __name__ == '__main__':
    create_profile("Sam")
    create_profile("Martin", "Luther", "King", "Jr.", born=1929, died=1968)
    create_profile("Sebastian", "Thrun", cofounded="Udacity", experience="Stanford Professor")