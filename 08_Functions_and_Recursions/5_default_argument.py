def greet(name, ending="Thank you..."):
    print(f"Good Day, {name}")
    print(ending)

greet("Sankalp")

# Here we have used default argument for ending parameter. So, if we do not provide any value for ending while calling the function, it will take the default value "Thank you.."
