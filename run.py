def get_patient_data():
    """
    Allow the data collect from the patient such as, name, 
    id number age and gender.
    Run a while loops to collect all the valid data from the patient. 
    The loop will continuously ask the data input until is valid.
    """

    global patient_name
    global document_id 
    global patient_age
    global patient_gender

    while True:
        patinet_name = input('Enter your first and last name: (The name should be between 2 and 20 characters)\n')
        if validate_name(patient_name):
            print(f"Hi {patient_name.title()}, your name has been submited")
        else:
            continue
        break

    while True:
        print("The id document shold be a number composed by 9 digits.")
        document_id = input('Please type in your ID compesed by 9 digits')
        if validate_document_id(document_id):
            print(f'Your id is {document_id}, it has been submitted.\n')
        else:
            continue
        break

    while True:
        print('your age should be written in numbers only:')
        patient_age = input('Please type in your age:')
        if validate_patient_age(patient_age):
            print(f'You have {patient_age} years old')
        else:
            continue
        break

    while True:
        print("What is your gender?")
        patient_gender = input('Type in your gender ("male" or "female"):')
        if validate_patient_gender(patient_gender):
            print('your answer has been submitted.\n')
        else:
            continue
        break


def validate_name(value):
    """
    Validade the name input provided by user.
    Print a message if the input is not valid and repeat the loop.
    """

    if len(value) not in range(2, 20):
        print('n\Your name should be composed by min 2 and max 20 letters')
        return False

    return True

def validate_document_id(value):
    """
    Validate the ID inputed by the patient.
    If the ID is not composed by exactly 9 digits print a message and repeat the loop.
    """
    try:
        value = float(value)
        if document_id.isnumeric() and len(value) == 9:
            raise ValueError
        
    except ValueError as e:
        print('Invalid ID, your ID should contain exactly 9 digits!')

        return True

def validate_patient_age(value):
    """
    Validade age Input by Patient
    If the age is not a number between 1 and 99 print message and repet the loop
    """
    try:
        value = float(value)
        if value not in range(1, 99):
            raise ValueError
    
    except ValueError as e:
        print('Invalid input, your age should be a number between 1 and 99!\n')
        return False

    return True




        



