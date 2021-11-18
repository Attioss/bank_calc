import random
def bank_calc():
    #kamat = 1.0075
    kamat = (1+(random.randint(3,6))/12/100)
    kerdes = input('Hitelt szeretne felvenni? (igen/nem)')
    if kerdes == 'igen':
        print('A bank ', round((kamat-1)*12*100), '% kamatot ad onnek! ', sep='')
        osszeg = int(input('Mekkora osszeget szeretne felvenni?' ))
        idotartam = (int(input('Hany ev alatt szeretne visszafizetni?' )))*12
        havi_torleszto = osszeg*kamat**idotartam*(kamat-1)/(kamat**idotartam-1)
        teljes = havi_torleszto*idotartam
        print('A havi torlesztoreszlet:', round(havi_torleszto), 'Ft')
        print('A teljes visszafizetendo osszeg:' , round(teljes), 'Ft')
    else:
        print('Akkor a lekotott beteteinket ajanlanam! ')
        print('A bank ', round((kamat - 1) * 12 * 100), '% kamatot ad onnek! ', sep='')
        befiz = int(input('Mekkora osszeget kivan befizetni havonta?' ))
        idotartam = (int(input('Hany evre tervezi megtakaritasat?'))) * 12
        vegosszeg = befiz*kamat*(kamat**idotartam-1)/(kamat-1)
        print('A lejarat utani teljes osszeg:', round(vegosszeg), 'Ft')


def bank_calc_v2():
    osszeg = int(input('Mekkora osszeget szeretne felvenni?' ))
    idotartam = int(input())  # itt majd másféleképpen folytatom

def main():
    bank_calc()


if __name__ == "__main__":
    main()