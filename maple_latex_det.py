while True:
    orig_text = raw_input("Plak hier de LaTeX code: ")

    new_text = orig_text.replace('{array}', '{vmatrix}')
    new_text = new_text.replace('{ccc}','')
    new_text = new_text.replace('\left[','')
    new_text = new_text.replace('right]','')
    new_text = new_text.replace(' \ ','')

    print new_text
    print
