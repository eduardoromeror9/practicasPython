def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {
        'firstname': 'Eduardo',
        'lastname': 'Romero'
    }
    
    super_list = [
        {'firstname': 'Eduardo','lastname': 'Romero'},
        {'firstname': 'Hector','lastname': 'Romer'},
        {'firstname': 'Miguel','lastname': 'Romeros'},
        {'firstname': 'Caro','lastname': 'Rodriguez'},
        {'firstname': 'Nucita','lastname': 'Canina'},
        {'firstname': 'Facundo','lastname': 'Garcia'},        
    ]
    
    super_dict = {
        'narural_nums': [1,2,3,4,5],
        'integer_nums': [-1,-2,0,1,2],
        'floating_nums': [1.1, 4.5, 6.43]
    }
    
    for key, value in super_dict.items():
        print(key, '-', value)



if __name__ == '__main__':
    run()