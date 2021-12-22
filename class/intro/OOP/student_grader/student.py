import json
import curses
import os


# class student_input:
#     def __init__(self, r):
#         pass

#     def save():
#         pass

#     def data_pass():
#         pass

def append(new_data, location="data.json"):

    with open(location, "r+") as file:
        old_data = json.load(file)
        old_data["students"].append(new_data)
        file.seek(0)
        json.dump(old_data, file, indent=4)


y = {
    "id": "my_id",
    "family name": "my_family_name",
    "given name": "my_given_name",
    "enrolled subjects": "my_enrolled_subjects"
}
append(y)

# r = open('student.json')
# data = json.load(r)
# r.close()
# jsonobject = json.dumps(data, indent=4)
# with open('data.json', "w") as outfile:
#     outfile.write(jsonobject)
