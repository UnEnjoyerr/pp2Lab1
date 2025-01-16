a = "Hello, World!"
print(a[1]) #strings are arrays

for x in "banana":
  print(x) # can loop through strings 

a = "Hello, World!"
print(len(a))  #length of strings

txt = "The best things in life are free!"
print("free" in txt)       #checking string

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")    #can be used for if statements

txt = "The best things in life are free!"
print("expensive" not in txt)    #check if not

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.") #print only if "expensive" is NOT present
