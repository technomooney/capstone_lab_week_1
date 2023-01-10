"""Marty Mooney, for Capstone class of spring 2023"""

def main():
    class_list = get_class_list()
    class_list_output(class_list)


def get_class_list():
    class_list = []
    class_input = "Start"
    while class_input:
        class_input = input(f"What class(s) do you have? to be finished just press enter: ")
        class_list.append(class_input)
        # flag= input("To add more press Y and enter, otherwise just press enter: ").lower()
    class_list.pop()
    return class_list


def class_list_output(class_list):
    for item_num,item in enumerate(class_list):
        print(f"Item {item_num+1:>5}: {item:>20}")

main()