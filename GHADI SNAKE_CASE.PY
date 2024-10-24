def camel_case(name) :
    snake_case=""
    for char in name :
        if char. isupper() :
            snake_case+="_"+char()
        else :
            snake_case+=char
    return snake_case
name=input("enter any word")
print(f"the snake_case of name is:{camel_case(name)}")
