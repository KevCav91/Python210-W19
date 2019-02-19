#!/usr/bin/env python3

# ----------------------------------------------------------------------- #
# Title: Mailroom_Part_3
# Author: Kevin Cavanaugh
# Change Log: (Who,What,When)
# kcavanau, created document & completed assignment, 02/10/2019
# kcavanau, playing with compression and error handling, 02/10/2019
# ----------------------------------------------------------------------- #

import sys, io, os


# -------------------- DATA -------------------- #

donors = {}
donors['Kevin Cavanaugh'] = (500.55, 899.34, 78.94)
donors['Victor Murphy'] = (99.89, 87.02)
donors['Randy Brown'] = (10.11, 1000.01, 99.99)
donors['Piper Long'] = (190.99, 100.02)
donors['Kim Pinkie'] = (2344.44, 8999.66, 345.55)

prompt = "\n".join(("What would you like to do?",
                    "1. Send a Thank You to single donor",
                    "2. Create a Report",
                    "3. Send letters to all donors",
                    "4. Quit"))


def send_thank_you(name, donation):
    '''

    :param name:
    :param donation:
    :return:
    '''
    letter = '\n Dear {}, \n\n Thank you for the generous donation of ${:.2f}. \n We are very grateful for your' \
             ' donation. \n\n Sincerely, \n The Team'.format(name, donation)
    return letter + '\n'


def add_donation(record, person, donation):
    if person in record:
        record[person] += donation,
    else:
        record[person] = donation,
    return record


def donor_stats(donor):
    total = sum(donors[donor])
    num_donations = int(len(donors[donor]))
    avg_donation = int(total / num_donations)
    return '{:<20} ${:<15.2f} {:<10} ${:<15.2f} '.format(donor, total, num_donations, avg_donation)


def create_report(database):
    report = ('{:<20} |{:<15} |{:<10} |{:<15}\n '.format('Donor', 'Total', 'Num Gifts', 'Average Gift'))
    report += '-' * 60 + '\n'
    for donor in database:
        report += donor_stats(donor) + '\n'
    return report


def display_report():
    print(create_report(donors))

def write_letters():
    cwd = os.getcwd()
    try:
        os.mkdir('thank_you_letters')
        os.chdir('thank_you_letters')
    except FileExistsError:
        print('Files already exists.  Create new directory.')
        new_dir = input('New Directory Name: ')
        os.mkdir(new_dir)
        os.chdir(new_dir)

    for donor in donors.keys():
        file_name = ('thank_you_{:s}.txt'.format(donor))
        open(file_name, 'a').close()
        file = io.open(file_name, 'w')
        file.write(send_thank_you(donor, donors[donor][len(donors[donor]) - 1]))
        file.close()

    os.chdir(cwd)


def thank_single_donor():
    name = input('Enter name of donor: ').lower()
    while True:
        if name == 'list':
            print(create_donor_list())
            break
        else:
            try:
                donation = float(input('How much did {:s} donate?'.format(name)))
                add_donation(donors, name, donation)
                print(send_thank_you(name, donors[name][len(donors[name]) - 1]))
                break
            except ValueError:
                print('You must enter a number.')


def create_donor_list():
    donor_list = 'Donors: \n'
    for donor in donors:
        donor_list += donor + '\n'
    return donor_list


def quit_mailroom():
    input('Press enter to exit! :) Have nice day')
    return sys.exit()


def user_input(choice):
    options = {'1': thank_single_donor,
               '2': display_report,
               '3': write_letters,
               '4': quit_mailroom}
    return options.get(choice)()


def main():
    while True:
        try:
            response = input(prompt)
            user_input(response)
        except TypeError:
            print('\n Select a valid option! \n')
            input('Press enter to continue...')


if __name__ == "__main__":
    main()
