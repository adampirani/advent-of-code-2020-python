import unittest

from day4 import passport


class TestPasswords(unittest.TestCase):

    def test_is_field_valid(self):
        self.assertEqual(passport.is_field_valid('byr', '2002'), True)
        self.assertEqual(passport.is_field_valid('byr', '2003'), False)
        self.assertEqual(passport.is_field_valid('hgt', '60in'), True)
        self.assertEqual(passport.is_field_valid('hgt', '190cm'), True)
        self.assertEqual(passport.is_field_valid('hgt', '190in'), False)
        self.assertEqual(passport.is_field_valid('hgt', '190'), False)
        self.assertEqual(passport.is_field_valid('hcl', '#123abc'), True)
        self.assertEqual(passport.is_field_valid('hcl', '#123abz'), False)
        self.assertEqual(passport.is_field_valid('hcl', '#123abcc'), False)
        self.assertEqual(passport.is_field_valid('hcl', '123abc'), False)
        self.assertEqual(passport.is_field_valid('ecl', 'brn'), True)
        self.assertEqual(passport.is_field_valid('ecl', 'wat'), False)
        self.assertEqual(passport.is_field_valid('pid', '000000001'), True)
        self.assertEqual(passport.is_field_valid('pid', '0123456789'), False)

    def test_process_line(self):

        passport_set = {}

        passport_set = passport.process_line(
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
            passport_set
        )
        self.assertEqual(passport_set['ecl'], 'gry')
        self.assertEqual(passport_set['pid'], '860033327')
        self.assertEqual(passport_set['eyr'], '2020')
        self.assertEqual(passport_set['hcl'], '#fffffd')
        self.assertEqual(len(passport_set), 4)

        passport_set = passport.process_line(
            "byr:1937 iyr:2017 cid:147 hgt:183cm",
            passport_set
        )

        self.assertEqual(passport_set['byr'], '1937')
        self.assertEqual(passport_set['iyr'], '2017')
        # self.assertEqual(passport_set['cid'], None)
        self.assertEqual(passport_set['hgt'], '183cm')
        self.assertEqual(len(passport_set), 7)

    # def test_is_valid(self):

    #     set1 = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}

    #     self.assertTrue(
    #         passport.is_valid(set1)
    #     )

    #     set2 = {'iyr', 'ecl', 'eyr', 'pid', 'hcl', 'byr'}

    #     self.assertFalse(
    #         passport.is_valid(set2)
    #     )

    #     set1 = {'hcl', 'iyr', 'eyr', 'ecl', 'pid', 'byr', 'hgt'}

    #     self.assertTrue(
    #         passport.is_valid(set1)
    #     )

    def test_num_valid(self):
        sample = [
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
            "byr:1937 iyr:2017 cid:147 hgt:183cm",
            "",
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
            "hcl:#cfa07d byr:1929",
            "",
            "hcl:#ae17e1 iyr:2013",
            "eyr:2024",
            "ecl:brn pid:760753108 byr:1931",
            "hgt:179cm",
            "",
            "hcl:#cfa07d eyr:2025 pid:166559648",
            "iyr:2011 ecl:brn hgt:59in"
        ]
        self.assertEqual(passport.num_valid(sample), 2)


if __name__ == '__main__':
    unittest.main()
