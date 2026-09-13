dict={
  "name":"Aman",
  "Age":23,
  "subjects":["hindi","English","maths"],
  "Marks": (98,99,100)
}

print(dict)
dict["name"]="Gaur"
print(dict)

dict["is_adult"]=True
print(dict)

#nested dict
nested_dict={
  "name":"Aman",
  "Age":23,
  "subjects":{
    "Hindi":98,
    "English":99,
    "Maths":100
  }
}
print(nested_dict["subjects"]["Maths"]) #output will be 100

print(dict.keys()) #will print all keys
print(list(dict.keys()))

print(dict.values()) #will print all values
print(list(dict.values()))

print(dict.items()) #will print all (key,val) pairs as tuples
print(list(dict.items()))

# print(dict["Age2"]) this will throw error as Age2 key does not exist
print(dict.get("Age2"))#get method- to get value of key, it return NONE as output

#update method-insert specified items to the dictionary
dict.update({"City":"Muzaffarnagar"})
print(dict)

new_dict={"name":"Shanti"}
dict.update(new_dict)
print(dict)
