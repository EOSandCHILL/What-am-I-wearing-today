#I consider it to be cold outside if the weather is 64 degrees or lower. I consider it to be warm outside if the weather is 65 degrees or higher. The weather will determine what I will wear outside today!
print("What am I wearing today? Let me check the temperature.")

cold = 64
warm = 65
temperature = 60

if temperature >= 65:
  print("It is warm today! I am wearing a T shirt and shorts outside!")
else:
  print("It is cold today! I am wearing a hoodie and pants outside!")
  
#If it is raining outside I will wear my rain coat but if it is not I will not.

print("Is it raining outside today?")

rain = True

if rain == True:
  print("Yes! It is raining so I am wearing my rain coat today!")
else:
  print("No rain today! Im good!")
  
#If it is cold and raining outside I cant wear the same thing Id usually wear if it were warm and rainy outside. So what do I do?

print("But what do I wear if it is raining and warm outside? Or raining and cold outside? I am confused.")

if rain == True and temperature >= 65:
  print("It is raining but warm so I will just use an umbrella today!")
else:
  print("It is warm and not raining! Im good!")
if rain == True and temperature <= 64:
  print("It is cold and raining so I will need a rain coat today!")
else: 
  print("It is not raining so I don't need a rain coat!")