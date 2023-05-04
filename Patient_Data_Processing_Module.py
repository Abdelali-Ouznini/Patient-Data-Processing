
def import_lines(file_name):
    """
    file_name: a string that represents the name
    of a data file.
    """

    data_file = open(file_name, 'r')
    lines = data_file.readlines()
    data_file.close()

    return lines


def create_patient(line):

    patient = {}
    l = line.split(" ")

    patient['name'] = l[0]
    patient['weight'] = float(l[1])
    patient['height'] = float(l[2])

    return patient


def list_patients_from_file_name(file_name):
    """
    list_patients_from_file_name(file_name) takes a file name
    as argument and returns a list of dictionaries
    If the file does not exist then the function returns -1.
    """
    patients = []
    lines = import_lines(file_name)
    if lines == -1:
        raise FileExistsError("The file is not read properly.")

    for line in lines:
        patients.append(create_patient(line))

    return patients


def bmi(patient):
    """
    """
    bmi = patient['weight'] / patient['height']**2
    return round(bmi, 2)


def average_bmi(patients):
    """
    patients represent a list of all patients
    list of dictionaries.
    """
    total = 0
    for patient in patients:
        total = total+bmi(patient)
    return round(total/len(patients), 2)


def list_names_of_normal_weight_patients(patients):
    """
    patients represent a list of all patients
    list of dictionaries.
    """

    list_names = []
    for patient in patients:
        if 18.5 <= bmi(patient) <= 25:
            list_names.append(patient['name'])

    return list_names

    # return [patient['name'] for patient in patients if 18.5 <= bmi(patient) <= 25]


def produce_string(patient):
    return f"{patient['name']} {bmi(patient)}\n"


def write_bmi(patients, file_name):

    data_file = open(file_name, 'w')
    for patient in patients:
        data_file.write(produce_string(patient))

    data_file.write(f"\n Average BMI: {average_bmi(patients)}\n")

    data_file.write("\nNames of normal weight patients:\n")
    for name in list_names_of_normal_weight_patients(patients):
        data_file.write(f"{name}\n")
    data_file.close()


def complete_data_processing(data_file, result_file):
    patients = list_patients_from_file_name(data_file)
    write_bmi(patients, result_file)


if __name__ == "__main__":

    cabinet1_patients = list_patients_from_file_name("data.txt")
    # print(cabinet1_patients)
    # print(average_bmi(cabinet1_patients))
    # print(list_names_of_normal_weight_patients(cabinet1_patients))
    write_bmi(cabinet1_patients, "results.txt")

    """
    cabinet1_patients = list_patients_from_file_name("data.txt")
    write_bmi(cabinet1_patients,"results-cabinet1.txt")
    print(list_names_of_normal_weight_patients(cabinet1_patients))
    print(average_bmi(cabinet1_patients))
     """
