import json
import curses
import os


class student:
    def __init__(self) -> None:
        with open('student.json') as studentfile:
            self.jsonObject1 = json.load(studentfile)
        with open('subject.json') as subjectfile:
            self.jsonObject2 = json.load(subjectfile)
        with open('assignments.json') as assignmentfile:
            self.jsonObject3 = json.load(assignmentfile)

    def get_assignments_from_subject(self, subject_names) -> list:
        # from subject.json get list of assignments from input subject_name
        for item in self.jsonObject2['subject']:
            if item['subject name'] == subject_names:
                return item['student assignments']
            else:
                pass

    def show_grades(self, student_name) -> dict:
        sb = subject()
        assignments = sb.get_assignments_for_student(student_name)
        res_dict = {}
        id = self.get_student_id(student_name)
        for task in assignments:
            dict = sb.get_student_grades(task)

            res_dict[task] = dict[f'{id}']
        return res_dict
        # from the assignments use student id to get the marks
        # show it in a dictionary

    def get_student_id(self, given_name):
        for item in self.jsonObject1['students']:
            if item['given name'] == given_name:
                return item['id']
            else:
                pass


class subject:
    def __init__(self) -> None:
        with open('student.json') as studentfile:
            self.jsonObject1 = json.load(studentfile)
        with open('subject.json') as subjectfile:
            self.jsonObject2 = json.load(subjectfile)
        with open('assignments.json') as assignmentfile:
            self.jsonObject3 = json.load(assignmentfile)

    def get_assignments_for_student(self, student_name) -> dict:
        # from the student name get the enrolled subject
        for item in self.jsonObject1['students']:
            if item['given name'] == student_name:
                enrolled = item['enrolled subjects']
            else:
                pass
        # from the enrolled subject get the assignments
        total = []
        for subject in enrolled:

            st = student()
            total.extend(st.get_assignments_from_subject(subject))
        return total

    # def get_student_grade(self, student_id) -> float:
    #     pass

    def get_student_grades(self, assignment) -> dict:
        for item in self.jsonObject3['assignments']:
            if item['assignment_name'] == assignment:
                return item['student marks']
            else:
                pass


class assignment:
    def __init__(self) -> None:
        with open('student.json') as studentfile:
            self.jsonObject1 = json.load(studentfile)
        with open('subject.json') as subjectfile:
            self.jsonObject2 = json.load(subjectfile)
        with open('assignments.json') as assignmentfile:
            self.jsonObject3 = json.load(assignmentfile)

    def get_mean(self, assignment) -> float:
        for item in self.jsonObject3['assignments']:
            if item['assignment_name'] == assignment:
                average = sum(item['student marks'].values()) / \
                    len(item['student marks'].values())
                return average
            else:
                pass

    # def get_student_grade(self, student_id) -> float:
    #     pass

    def get_below(self, percentage, assignment) -> list:
        # get max mark for assignment * by percentage
        result = {}
        for item in self.jsonObject3['assignments']:
            if item['assignment_name'] == assignment:
                max_grade = int(item['max marks']) * percentage/100

                for value in item['student marks']:

                    if int(item['student marks'][value]) < max_grade:
                        result[value] = int(item['student marks'][value])
                    else:
                        pass
                return result
            else:
                pass
        # compare that to all possible values in dict
        # return values lower than max grade

    def get_above(self, percentage, assignment) -> list:
        # get max mark for assignment * by percentage
        result = {}
        for item in self.jsonObject3['assignments']:
            if item['assignment_name'] == assignment:
                min_grade = int(item['max marks']) * percentage/100

                for value in item['student marks']:

                    if int(item['student marks'][value]) > min_grade:
                        result[value] = int(item['student marks'][value])
                    else:
                        pass
                return result
            else:
                pass
        # get max mark for assignment * percentage
        # compare that to all possible values in dict
        # return values higher than min grade


def main():
    a = student()
    b = subject()
    c = assignment()
    A = 'English'
    B = 'Aaron'
    C = 'English1'
    # print(a.get_assignments_from_subject(A))
    # print(b.get_assignments_for_student(B))
    # print(b.get_student_grades(C))
    # print(a.show_grades(B))
    # print(c.get_mean(C))
    print(c.get_below(95, C))
    print(c.get_above(90, C))


if __name__ == "__main__":
    main()
