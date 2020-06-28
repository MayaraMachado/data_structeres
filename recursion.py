# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!


def show_excitement(n):
    # Your code goes here!
    
    string = "I am super excited for this course!"
    
    if n == 1:
        return string
    else:
        return string + " " + show_excitement(n-1)
    

print show_excitement(5)
