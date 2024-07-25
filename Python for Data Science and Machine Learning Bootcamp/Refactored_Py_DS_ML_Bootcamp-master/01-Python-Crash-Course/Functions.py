def domainGet(email):
    return email.split('@')[1]


def findDog(text):
    return 'dog' in text.lower()


print(findDog("is there a dog here?"))


def countDog(text):
    return text.count('dog')


print(countDog('This dog runs faster than the other dog dude!'))

seq = ['soup', 'dog', 'salad', 'cat', 'great']
newlist = list(filter(lambda item: item.startswith('s'), seq))
print(newlist)


def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        print("No ticket")
    elif 61 <= speed <= 80:
        print("Small Ticket")
    elif speed >= 81:
        print("Big Ticket")


caught_speeding(81, True)
