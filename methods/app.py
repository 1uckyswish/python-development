def greet(first_name, last_name):
    print(f"Hi There, {first_name}")
    print(f"Welcome cowboy, {last_name}")


greet("Noel", "Guillen")

def get_greet(name):
    return f"hi {name}"

message = get_greet("Noel")

print(message)
file = open("content.txt", "w")
file.write(message)
