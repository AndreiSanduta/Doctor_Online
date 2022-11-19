inport drug_prescription

drog_prescription_options = []
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

def patient_symptoms():
    """
    Get symtoms typed in by the patient.
    run a while loop to collect patient symtoms data.
    print a message when the input is valid 
    the loop stops when the imput thata is not valid.
    """

while True:
    print('chose on of the symptoms listed below')
    def jls_extract_def():
        
        return 


    #print.print_symptoms_list = jls_extract_def()
    #symptoms = input(f'\n{patient_name}, type in one of the symptoms listed above:\n')
        

def get_pain_level():
    """
    Get level of pain by patient input data.
    Run a while loop to collect valid data.
    Print a message when the input is valid.
    The loop stops when the data is valid.
    """

    while True:
    print('Type in your level of pain in a scale from 1 to 10')
    level_pain = input(f'{patient_name}, what is your level of pain:\n')
    if validate_pain(level_pain):
        print('your level of pain has been registrated!\n')
    else:
        continue
    break


def validate_level_pain(value):
    """
    Validade pain level Input by Patient
    If the level of pain is not a valid number between 1 and 10
    Print message when data is not valid.
    the loop stops when the data is valid
    """
    try:
        value = float(value)
        if value not in range(1, 10):
            raise ValueError
    
    except ValueError as e:
        print('Invalid input, yor level of pain should contain a number between 1 and 10!\n')
        return False

    return True


def get_former_illnes(Value):
    """
    get imput data from patient regarding former elements.
    run while loop to collect all the valid data input from user,
    print message when the input is valid. 
    The loopstops when the input data is valid.
    """

    while True:
    former_illnes = input('Do you have any former illnes?\n')
    if valid_former_illnes(former_illnes):
        print(f'{name.title()}, your answer has been submited')
        else: 
            continue
        break

def get_drogs_alergies(Value):
    """
    get imput data from patient regardig drog alergies.
    run while loop to collect all the valid data input from user,
    print message when the input is valid. 
    The loopstops when the input data is valid.
    """

    while True:
    drogs_alergies = input('Do you have any drog alergies?\n')
    if valid_former_illnes(former_illnes):
        print(f'{name.title()}, your answer has been submited')
        else: 
            continue
        break



def drog_prescription_options():

    



    def main():
        """
        Run all program functions.
        """
        get_patient_data()
        get_pain_level()
        get_former_illnes()
        get_level_pain()

    if __name__== '__main__':
        main()

        
