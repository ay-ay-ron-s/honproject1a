from random import randint

alpha = (randint(1,100))/100
beta = (randint(1,100))/100
p = randint(1,100)/100

Zf = p*alpha + (1-p)*beta
Zm = (1-p)*alpha + p*beta

Pa12 = p*Zf + (1-p)*Zm
Pa13 = p*Zf + (1-p)*Zm

def get_gender()->str:
    '''
    generates a random number x from (1-100)/100 (inclusive), and if x is within the range of 0.01-p (inclusive),
    we return the gender of female, and otherwise return the gender of male
    '''
    x = randint(1,100)/100
    if x <= p:
        return "female"
    else:
        return "male"

def make_friend_group(group_size:int)->list:
    '''
    takes an input of the size of a friend group you want. returns the list of
    the genders of all friends in the group
    '''
    new_group = []
    for i in range(group_size):
        new_group.append(get_gender())
    return new_group

def make_friend_collection(collection_size:int, group_size:int)->list:
    '''
    takes the input of the amount of friend groups you want and the desired
    size of each of them and returns a list of a list of strings (the genders)
    '''
    friend_collection = []
    for i in range(collection_size):
        friend_group = make_friend_group(group_size)
        friend_collection.append(friend_group)
    return friend_collection

def is_friends(person1: str, person2: str):
    '''
    generates a random number and, depending on the gender of the 2 inputted people,
    will determine if they are friends
    
    returns 0 if not friends, 1 if friends
    '''
    number_sample = randint(1,100)/100
    if person1 == 'female':
        if person2 == 'female':
            if number_sample <= alpha:
                return 1
            else:
                return 0
        elif person2 == 'male':
            if number_sample <= beta:
                return 1
            else:
                return 0
    elif person1 == 'male':
        if person2 == 'male':
            if number_sample <= alpha:
                return 1
            else:
                return 0
        elif person2 == 'female':
            if number_sample <= beta:
                return 1
            else:
                return 0

def getfriend12results(friend_collection:list[list[str]]):
    group_total = len(friend_collection)
    friend_result_amount = 0
    for group_number in range(group_total):
        first = friend_collection[group_number][0]
        second = friend_collection[group_number][1]
        result = is_friends(first, second)
        friend_result_amount += result
    return friend_result_amount/group_total

def getfriend13results(friend_collection:list[list[str]]):
    group_total = len(friend_collection)
    friend_result_amount = 0
    for group_number in range(group_total):
        first = friend_collection[group_number][0]
        second = friend_collection[group_number][2]
        result = is_friends(first, second)
        friend_result_amount += result
    return friend_result_amount/group_total

def get12intersect13(friend_collection:list[list[str]]):
    group_total=len(friend_collection)
    friend_intersection_amount = 0
    for group_number in range(group_total):
        first = friend_collection[group_number][0]
        second = friend_collection[group_number][1]
        third = friend_collection[group_number][2]
        both_check = 0
        both_check += is_friends(first, second)
        both_check += is_friends(first, third)
        if both_check == 2:
            friend_intersection_amount += 1
    return friend_intersection_amount/group_total

def filter_p1_gender(desired_gender:str, friend_collection:list[list[str]]):
    filtered_friend_collection = []
    group_total = len(friend_collection)
    for group_number in range(group_total):
        if friend_collection[group_number][0] == desired_gender:
            filtered_friend_collection.append(friend_collection[group_number])
    return filtered_friend_collection

sample_friend_collection = make_friend_collection(250000,3)
sample_female_led_collection = filter_p1_gender('female', sample_friend_collection)
sample_male_led_collection = filter_p1_gender('male', sample_friend_collection)

actual_Pa12 = getfriend12results(sample_friend_collection)

Pa12intPa13 = (p*Zf*Zf)+((1-p)*Zm*Zm)
actual_Pa12intPa13 = get12intersect13(sample_friend_collection)

Pa12Pa13 = ((p*Zf)+(1-p)*Zm)**2
actual_Pa12Pa13 = (actual_Pa12)*(getfriend13results(sample_friend_collection))

Pa12f = (p*alpha) + (1-p)*beta
actual_Pa12f = getfriend12results(sample_female_led_collection)

Pa12m = (1-p)*alpha + p*beta
actual_Pa12m = getfriend12results(sample_male_led_collection)

Pa12a13f = (Pa12f)**2
actual_Pa12a13f = (actual_Pa12f)**2

Pa12a13m = (Pa12m)**2
actual_Pa12a13m = (actual_Pa12m)**2

Pa12inta13f = ((p*alpha) + (1-p)*beta)**2
actual_Pa12inta13f = get12intersect13(sample_female_led_collection)

Pa12inta13m = ((1-p)*alpha + p*beta)**2
actual_Pa12inta13m = get12intersect13(sample_male_led_collection)

Pa12inta13v2 = p*((p*alpha)+(1-p)*beta)**2 + (1-p)*((1-p)*alpha + p*beta)**2
actual_Pa12inta13v2 = (get12intersect13(sample_female_led_collection))*p + (get12intersect13(sample_male_led_collection))*(1-p)

print(f"Alpha: {alpha:.2f} | Beta: {beta:.2f} | p: {p:.2f}")
print("-------")
print("Part A:")
print(f"Expected value P(A12): {Pa12:.4f} | Actual value P(A12): {actual_Pa12:.4f}")
print("-------")
print("Part B:")
print(f"Expected value P(A12∩A13): {Pa12intPa13:.4f} | Actual value P(A12∩A13): {actual_Pa12intPa13:.4f}")
print(f"Expected value P(A12)P(A13): {Pa12Pa13:.4f} | Actual value P(A12)P(A13): {actual_Pa12Pa13:.4f}")
print("-------")
print("Part C:")
print(f"Expected value P(A12∩A13|P1=F): {Pa12inta13f:.4f} | Actual value P(A12∩A13|P1=F): {actual_Pa12inta13f:.4f}")
print(f"Expected value P(A12|P1=F)P(A13|P1=F): {Pa12a13f:.4f} | Actual value P(A12|P1=F)P(A13|P1=F): {actual_Pa12a13f:.4f}")
print(f"Expected value P(A12∩A13|P1=M): {Pa12inta13m:.4f} | Actual value P(A12∩A13|P1=M): {actual_Pa12inta13m:.4f}")
print(f"Expected value P(A12|P1=M)P(A13|P1=M): {Pa12a13m:.4f} | Actual value P(A12|P1=M)P(A13|P1=M): {actual_Pa12a13m:.4f}")
print("-------")
print("Part D:")
print(f"Expected value P(A12∩A13): {Pa12inta13v2:.4f} | Actual value P(A12∩A13): {actual_Pa12inta13v2:.4f}")
