alumniList = []

def main():
    print("Welcome to the student grading system!")

    mainMenu()

def mainMenu():
    x = input("Select the action you want to do: \nA: Add a new student \nC: Check all alumni \nM: Modify any grade \nX: Exit Program \n")

    while x.upper() != 'A' and x.upper() != 'C' and x.upper() != 'M' and x.upper() != 'X':
        x = input("\nResponse not allowed. Please select a valid character: ")
        if x.upper() == 'A' or x.upper() == 'C' or x.upper() == 'M' or x.upper() == 'X':
            break

    if x.upper() == 'A':
        studentInfo = student()
        alumniList.append(studentInfo)
        print("\n")
        mainMenu()

    elif x.upper() == 'C':
        print("Alumni List:")
        for studentInfo in alumniList:
            print("Name: ", studentInfo[0], "/ Grade: ", studentInfo[1])
        print("\n")
        mainMenu()

    elif x.upper() == 'M':
        print("Not available on beta! Wait until the alpha drops.\n")
        mainMenu()

    elif x.upper() == 'X':
        print("Until next time!")


def student():
    studentName = str(input("Please, insert the student\'s name: "))
    studentGrade = calculator()
    print("The grade of ", studentName, " is: ", studentGrade)

    studentStruct = [studentName, studentGrade]
    return studentStruct

def calculator():
    quiz = float(input("Please, insert the quiz\'s grade: "))
    midterm = float(input("Please, insert the mid-term\'s grade: "))
    final = float(input("Please, insert the final\'s grade: "))

    return grader(quiz, midterm, final)

def grader(float1, float2, float3):
    if ((float1 + float2 + float3) / 3) >= 90:
        return 'A'

    elif ((float1 + float2 + float3) / 3) >= 70:
        return 'B'

    elif ((float1 + float2 + float3) / 3) >= 50:
        return 'C'

    else:
        return 'F'


if __name__ == "__main__":
    main()