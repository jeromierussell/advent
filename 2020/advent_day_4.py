import re

raw_bad="""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

raw_good="""pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

def yo():
    with open('./input/advent_day_4_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()

    entries = []

    entry = {}
    for line in raw_lines:
        if line == '':
            entries.append(entry)
            entry = {}
        else:
            record = line.split(":")
            # first record in line starts w/ key
            #print(record)

            key = None
            value = None
            for i in range(len(record)):
                if i == 0 and key is None:
                    key = record[0]
                else:
                    the_next = record[i].split(' ')
                    value = the_next[0]
                    entry[key] = value
                    value = None

                    if len(the_next) > 1:
                        key = the_next[1]
                    else:
                        key = None

    # need to get the lst entry too
    entries.append(entry)

    print(entries)

    """
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
    """

    passes = 0
    for e in entries:
        if e.get('byr') and e.get('iyr') and e.get('eyr') and e.get('hcl') and e.get('ecl') and e.get('pid') and e.get('hgt'):
            print("PASSES: " + str(e))
            passes += 1
        else:
            print("FAILS: " + str(e))

    print(passes)

def yo2():
    with open('./input/advent_day_4_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()

    entries = []

    entry = {}
    for line in raw_lines:
        if line == '':
            entries.append(entry)
            entry = {}
        else:
            record = line.split(":")
            # first record in line starts w/ key
            #print(record)

            key = None
            value = None
            for i in range(len(record)):
                if i == 0 and key is None:
                    key = record[0]
                else:
                    the_next = record[i].split(' ')
                    value = the_next[0]
                    entry[key] = value
                    value = None

                    if len(the_next) > 1:
                        key = the_next[1]
                    else:
                        key = None

    # need to get the lst entry too
    entries.append(entry)

    print(entries)

    """
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
    """

    hcl_re = re.compile(r'#[a-f0-9]{6}')
    pid_re = re.compile(r'[0-9]{9}')

    counter = 0

    passes = 0
    for e in entries:
        if e.get('byr') and e.get('iyr') and e.get('eyr') and e.get('hcl') and e.get('ecl') and e.get('pid') and e.get('hgt'):
            # print("PASSES PRESENCE: " + str(e))

            this_pass = True

            try:
                byr = e.get('byr')
                if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
                    # print("byr failed")
                    this_pass = False

                iyr = e.get('iyr')
                if this_pass and (len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020):
                    # print("iyr failed")
                    this_pass = False

                eyr = e.get('eyr')
                if this_pass and (len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030):
                    # print("eyr failed")
                    this_pass = False

                hcl = e.get('hcl')
                if this_pass:
                    if len(hcl) != 7 or not hcl_re.match(hcl):
                        # print("hcl failed")
                        this_pass = False

                ecl = e.get('ecl')
                if this_pass and (ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                    # print("ecl failed")
                    this_pass = False

                pid = e.get('pid')
                if this_pass and (len(pid) != 9 or not pid_re.match(pid)):
                    # print("pid failed")
                    this_pass = False

                hgt = e.get('hgt')
                if this_pass:
                    split_cm = hgt.split('cm')
                    split_in = hgt.split('in')

                    if len(split_cm) == 2:
                        if int(split_cm[0]) < 150 or int(split_cm[0]) > 193:
                            this_pass = False
                            # print("hgt failed - cm")
                    elif len(split_in) == 2:
                        if int(split_in[0]) < 59 or int(split_in[0]) > 76:
                            this_pass = False
                            # print("hgt failed - in")
                    else:
                        this_pass = False
                        # print("hgt failed - general")
            except:
                # print("EXCEPTION!!!")
                this_pass = False

            if this_pass:
                passes += 1
                print(str(counter) + " - PASS!")
        else:
            pass
            # print("FAILS PRESENCE: " + str(e))

        counter += 1

    print(passes)


if __name__ == "__main__":
    yo()
