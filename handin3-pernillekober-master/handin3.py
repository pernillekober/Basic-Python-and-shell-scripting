def unscramble_attempt1(list_of_strings):
    ''' Inputs a list of strings and returns a list of sorted strings. It does not give the 
    expected output as the strings are sorted on the first character in the line number'''
    sorted_list = sorted(list_of_strings)
    return sorted_list


scrambled_file = open("m_scrambled.txt")
unscrambled_lines = unscramble_attempt1(scrambled_file.readlines())
print("".join(unscrambled_lines))
scrambled_file.close()


def unscramble_attempt2(list_of_strings):
    ''' uses sorted() on a list of strings where string split is used to seperate line number 
    (as int) and content string, treating them like a tuple, andputputting a sorted based on 
    line number'''


    sorted_list = sorted(list_of_strings, key=lambda line: int(line.split(" ")[0]))

#   list_of_tuples = []
#   for element in list_of_strings:
#      line, content = (int(element[:3]), element[3:])
#      list_of_tuples.append((line, content))

#    sorted_list = []
#    for tuple_element in sorted(list_of_tuples):
#        joined_back = str(tuple_element[0]) + tuple_element[1]
#        sorted_list.append(joined_back)
        
    return sorted_list

scrambled_file = open("m_scrambled.txt") 
unscrambled_lines = unscramble_attempt2(scrambled_file.readlines())
print("".join(unscrambled_lines))
scrambled_file.close()
