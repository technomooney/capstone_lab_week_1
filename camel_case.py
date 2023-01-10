"""Marty Mooney, for Capstone class of spring 2023"""
invalid_char = ["'", '"', "1", "2","3","4","5","6","7","8","9","0","#","+","=",";",":","!","."]

def main():
    print("start")
    data = get_input("Enter a sentence to convert to camel case: ")
    for item in invalid_char:
        if item in data:
            print(f"\n{'*'*62}\nWarning sentence entered will not make a valid variable name!\n{'*'*62}")
            break
    camelized_sentence = camelize(data)
    output(camelized_sentence)

# creating a general purpous input funtion that will allow for different validations 
def get_input(prompt="Please enter data: ",validate=False):
    if validate:
        valid_data = get_valid_alpha_input(prompt)
        return valid_data
    else:
        data = input(prompt)
        return data


# validate if there is any chars other then alpha (A-Z and a-z),
# def get_valid_alpha_input(prompt):
#     data = input(prompt)
#     # invalid_char = ["'", '"', "1", "2","3","4","5","6","7","8","9","0","#","+","=",";",":"]
#     isvalid=False
#     while not isvalid:
#         for item in invalid_char:
#             if item in data:
#                 print(f"the data entered contains invalid charecters, it cant include the following chars\n"+
#                 f"{', '.join(invalid_char)}")
#                 data = input("Try again: "+prompt)
#             else:
#                 isvalid=True
#                 break
#     return data # it keeps returning the first input even if i input the right one after. 


def camelize(sentence_to_be_camilized):
    word_list = sentence_to_be_camilized.split()
    camelized_sentence = word_list[0].lower()
    for i in range(1,len(word_list)):
        camelized_sentence+=word_list[i].title()
    return camelized_sentence

def output(camelized_sentence):
    print(f"This is your camilized sentence: \n{camelized_sentence}")

main()