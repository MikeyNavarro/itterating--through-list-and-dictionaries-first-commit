x = [ [5,2,3], [10,8,9] ] 
from curses import keyname


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students)

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z[0]["y"]= 30
print(z)


# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

def itterateDictionary(list):
  for i in range(len(list)):
    for key, val in list[i].items():
      print(key ,"=" ,val)

(itterateDictionary(students))

def itterateDictionary2(list):
  for i in range(len(list)):
    for val in list[i].values():
      print(val)

(itterateDictionary2(students))


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dictionary):
 print(dictionary["locations"])
 print(len(dictionary["locations"]) , "locations")
 for i in dictionary["locations"]:
    print(i)

 print(dictionary["instructors"])
 print(len(dictionary["instructors"]) , "instructors")
 for i in dictionary["instructors"]:
    print(i)

printInfo(dojo)
