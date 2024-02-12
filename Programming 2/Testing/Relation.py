def relation(n, m):
    if n < m:
       return m/n
    else:
       return n/m

def main():


    assert relation(1, 4) == 4, 'False'




    assert relation(2, 3) == 1.5, 'False'

    assert relation(3, 2) == 1.5, 'False'


main()
