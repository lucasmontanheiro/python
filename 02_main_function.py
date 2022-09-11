# Explain why python files often include the __main__ function

# The main function is implemented to make sure that this library uses 
# the prefix library_name.function in future uses

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()