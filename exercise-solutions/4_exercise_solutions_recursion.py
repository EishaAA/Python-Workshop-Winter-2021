"""
    File name: 4_exercise_solutions_recursion
    Author: Eisha Ahmed
    Last Modified: 2021/02/25
    Python Version: 3.6
"""

def reverseStr(myStr):
    if len(myStr) == 1:
        return myStr
    else:
        return reverseStr(myStr[1:]) + myStr[0]

if __name__ == "__main__":
    print(reverseStr("Hi there"))
