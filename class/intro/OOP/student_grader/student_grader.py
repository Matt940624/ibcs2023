import json
import curses
import os


class student:
    def get_assignments_from_subject(subject_name: str) -> list:
        # from subject.json get list of assignments from input subject_name
        location = "subject.json"
        with open(location, "r") as jsonfile:
            json_load = json.load(jsonfile)
        data = json_load['subject']['assignments']
        print(data)

    def show_grades(student_name: str) -> dict:
        pass


class subject:
    def get_assignments_for_student(student_name: str) -> dict:
        pass

    def get_student_grade(student_id) -> float:
        pass

    def get_student_grades() -> dict:
        pass


class assignment:
    def get_mean() -> float:
        pass

    def get_student_grade(student_id) -> float:
        pass

    def get_below(percent) -> list:
        pass

    def get_above(percent) -> list:
        pass


class student_grader:
    pass
# class student_input:
#     def __init__(self, r):
#         pass

#     def save():
#         pass

#     def data_pass():
#         pass


# def append(new_data, location="result.json"):

#     with open(location, "r+") as file:
#         old_data = json.load(file)
#         old_data["students"].append(new_data)
#         file.seek(0)
#         json.dump(old_data, file, indent=4)


# y = {
#     "id": "my_id",
#     "family name": "my_family_name",
#     "given name": "my_given_name",
#     "enrolled subjects": "my_enrolled_subjects"
# }
# append(y)

# r = open('student.json')
# data = json.load(r)
# r.close()
# jsonobject = json.dumps(data, indent=4)
# with open('data.json', "w") as outfile:
#     outfile.write(jsonobject)
