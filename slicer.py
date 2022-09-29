if __name__ == '__main__':
    my_string = 'yooooouuuuupppppaaaaaaaassssssseeeeeedd'
    current_slice = my_string.replace('oooo', '')
    current_slice = current_slice.replace('uuuu', '')
    current_slice = current_slice.replace('pppp', '')
    current_slice = current_slice.replace('aaaaaaa', '')
    current_slice = current_slice.replace('sssss', '')
    current_slice = current_slice.replace('eeeee', '')
    current_slice2 = current_slice.title()
    print(current_slice2)