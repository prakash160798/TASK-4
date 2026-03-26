name = input("Enter your name: ")
product = input("Enter a product: ")
sentence = f"Hello {name}, thank you for purchasing {product}!"
print("Formatted Sentence:")
print(sentence)
width = 50

print("Padded Output:")
print("Left Align :")
print(sentence.ljust(width, '-'))#here l for left
print("Right Align :")
print(sentence.rjust(width, '-'))# here r for right
print("Center Align :")
print(sentence.center(width, '-'))# here centre
