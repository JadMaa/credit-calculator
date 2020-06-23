import sys
import math


def calculate_annuity():
    p = float(parameters_dict['principal'])
    n = int(parameters_dict['periods'])
    interest = float(parameters_dict['interest'])
    i = (interest / 100) / (12 * 1)
    annuity = math.ceil(p * ((i * math.pow((1 + i), n)) / ((math.pow((1 + i), n)) - 1)))
    print("Your annuity payment = {}!".format(annuity))
    print("Overpayment = {}".format((annuity * n) - p))


def calculate_principal():
    annuity = float(parameters_dict['payment'])
    n = int(parameters_dict['periods'])
    interest = float(parameters_dict['interest'])
    i = (interest / 100) / (12 * 1)
    p = math.floor(annuity / ((i * math.pow((1 + i), n)) / ((math.pow((1 + i), n)) - 1)))
    print("Your credit principal = {}!".format(p))
    print("Overpayment = {}".format(int((annuity * n) - p)))


def calculate_months():
    p = float(parameters_dict['principal'])
    annuity = float(parameters_dict['payment'])
    interest = float(parameters_dict['interest'])
    i = (interest / 100) / (12 * 1)
    total_months = math.ceil(math.log((annuity / (annuity - i * p)), 1 + i))
    n_years = math.floor(total_months / 12)
    n_months = math.ceil(total_months - 12 * n_years)
    if n_years == 0:
        print("You need {} months to repay this credit!".format(n_months))
    elif n_months == 0:
        print("You need {} years to repay this credit!".format(n_years))
    else:
        print("You need {} years and {} months to repay this credit!".format(n_years, n_months))
    print("Overpayment = {}".format(int((annuity * total_months) - p)))


def calculate_diff():
    p = float(parameters_dict['principal'])
    n = int(parameters_dict['periods'])
    interest = float(parameters_dict['interest'])
    i = (interest / 100) / (12 * 1)
    total_diff = 0
    for j in range(1, n + 1):
        diff_pay = math.ceil((p / n) + i * (p - ((p * (j - 1)) / n)))
        print("Month {}: paid out {}".format(j, diff_pay))
        total_diff += diff_pay
    print()
    print("Overpayment = {}".format(int(total_diff - p)))


parameters_dict = {}
annuity_params_list = ['principal', 'periods', 'interest', 'payment']
args = sys.argv[1:]
if len(args) < 4 or "--type" not in args[0]:
    print("Incorrect parameters")
else:
    payment_type = args[0].split("=")[1]
    for arg in args[1:]:
        name = arg.split("=")[0].replace("--", "")
        value = arg.split("=")[1]
        if '-' in value:
            print("Incorrect parameters")
            exit()
        parameters_dict[name] = value

    if payment_type == 'annuity':
        for annuity_param in annuity_params_list:
            if annuity_param not in parameters_dict:
                annuity_to_compute = annuity_param
        if annuity_to_compute == 'payment':
            calculate_annuity()
        elif annuity_to_compute == 'principal':
            calculate_principal()
        elif annuity_to_compute == 'periods':
            calculate_months()
        elif annuity_to_compute == 'interest':
            print("Incorrect parameters")

    elif payment_type == 'diff':
        if 'payment' in parameters_dict:
            print("Incorrect parameters")
        else:
            calculate_diff()
