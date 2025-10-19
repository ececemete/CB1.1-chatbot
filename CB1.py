print("Hi!")
print("What is your name?")
YourName = input()
print("Hello " + YourName + ", so nice to meet you!")
print("How old are you?")
YourAge = input()
print("You will be " + str(int(YourAge) + 1) + " next year!")
print("What is your favorite color?")
YourColor = input()
if YourColor == "blue":
    print("Same! I love blue too!")
elif YourColor == "green":
    print("A calming one! Great choice.")
elif YourColor == "white":
    print("Classy! Love it.")
else:
    print(YourColor + " such a nice pick! You have great taste!")
print("plesure to meet you " + YourName + "!")
print("My name is CB1, and I am a little chatbot created by a student who's learning to code. I may not look aesthetically pleasing, but it took her a while to make me, so please be loving!")
print("what are you hobbies? I wanna know more about you!")
YourHobby = input()

words = YourHobby.split()
word_count = len(words)

if word_count == 1:
    print(f"Wow! {YourHobby} is so cool! I wish I could do that!")
elif word_count == 2:
    print(f"Amazing hobbies! {YourHobby}, these sound like so much fun!")
else:
    print(f"Oh wow, so many hobbies! {YourHobby}, you must be a very interesting person!")


print("What would be a word to dexcribe your experience with me so far?")
yourword = input()
print("Thank you soo much! I really appreciate your feedback and will work hard to be better!")