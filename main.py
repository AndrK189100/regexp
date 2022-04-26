import csv
import re
from patterns import pattern_tel, sub_tel


def get_corrected_list():
    with open("phonebook_raw.csv") as csv_f:
        rows = csv.reader(csv_f, delimiter=",")
        contact_list = list(rows)

    for contact in contact_list[1:]:
        fls = (contact[0] + ' ' + contact[1] + ' ' + contact[2]).rstrip().split(' ')
        if len(contact) > 7:
            del contact[7:]
        for i, item in enumerate(fls):
            contact[i] = item
        contact[5] = re.sub(pattern_tel, sub_tel, contact[5])

    for contact in contact_list:
        if not contact[2]:
            for contact_ in contact_list[1:]:
                if contact[0] == contact_[0] and contact[1] == contact_[1] and contact_[2]:
                    contact[2] = contact_[2]
                    break

    return contact_list


def del_double(contact_list: list):
    list_len = len(contact_list)
    i = 1
    while i < list_len - 1:

        j = i + 1
        while j < list_len:

            if contact_list[i][0] == contact_list[j][0] and contact_list[i][1] == contact_list[j][1] and \
                    contact_list[i][2] == contact_list[j][2]:
                if contact_list[j][3] != '':
                    contact_list[i][3] = contact_list[j][3]
                if contact_list[j][4] != '':
                    contact_list[i][4] = contact_list[j][4]
                if contact_list[j][5] != '':
                    contact_list[i][5] = contact_list[j][5]
                if contact_list[j][6] != '':
                    contact_list[i][6] = contact_list[j][6]
                contact_list.pop(j)
                list_len = list_len - 1
                continue
            j += 1

        i += 1
    return contact_list


if __name__ == '__main__':
    contacts_list = get_corrected_list()
    contacts_list = del_double(contacts_list)

    with open("phonebook_raw_corrected.csv", mode='w') as f:
        writer = csv.writer(f)
        writer.writerows(contacts_list)
