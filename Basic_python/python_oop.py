
def lbs_to_kg(weight_kg):
    return weight_kg * 0.45


def kg_to_lbs(weight_lbs):

    return weight_lbs / 0.45

while True:

    try:

        weight = int(input('Weigth : '))
        enter_input = input('(k)g or (L)bs : ')

        if enter_input.upper() == 'L':
            print(lbs_to_kg(weight))

        elif enter_input.upper() == 'K':
            print(kg_to_lbs(weight))
        else:
            print('please input k or l ')
            enter_input = input('(k)g or (L)bs : ')
            if enter_input.upper() == 'L':
                print(lbs_to_kg(weight))

            elif enter_input.upper() == 'K':
                print(kg_to_lbs(weight))

    except:
        print('Invalid value')
