#Write a Python program to determine if a person is eligible to obtain a driver's license based on the following criteria:

#First, check if the applicant's age is valid (between 16 and 100).
#If the age is valid, check the following conditions:
#If the applicant is 18 years old or older, print "Eligible for a driver's license."
#If the applicant is between 16 and 17 years old, check if they have completed a driver's education course:
#If they have completed the course, print "Eligible for a driver's license."
#If they have not completed the course, print "Not eligible for a driver's license. Must complete driver's education."
#If the age is not valid, print "Invalid age."


age = 17
completed_education = "yes"

if 16 <= 100:
    if age >= 18:
        print("Eligible for a driver's license")
    else:
        if age >= 16:
            if completed_education == "yes":
                print("Eligible for driver's lisence")
            else:
                print("not eligible")
else:
    print("invalid age")
