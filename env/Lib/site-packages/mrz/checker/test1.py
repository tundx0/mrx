from checker._report import _Report, Kind


class Test:
    def __init__(self):
        self.report = _Report()

    def prueba(self):
        self.report.add("document type format", True)
        self.report.add("loquesea", False, level=Kind.ERROR)
        self.report.add("una cosa", False, level=Kind.WARNING)
        self.report.add("otra cosa", level=Kind.WARNING)
        self.report.add("blabla", True)

        print(self.report.fields)
        print(self.report.errors)
        print(self.report.falses)
        print(self.report.warnings)

    def prueba2(self):
        self._check_expiry = True
        check1 = check2 = check3 = check4 = True
        check3 = False
        print("Debug:", ("check1:", check1), ("check3:", check3), ("check4:", check4))
        rep = lambda s, c, k=Kind.ERROR: not c and self.report.add(s, level=k)
        rep("expiry date before than birth date", check1)
        # rep("birth date after than today", check2)  # check2 canceled
        self._check_expiry and rep("document expired", check3, Kind.WARNING)
        self._check_expiry and rep("expiry date greater than 10 years", check4, Kind.WARNING)



        print("FIELDS", self.report.fields)
        print("ERROR", self.report.errors)
        print("FALSES", self.report.falses)
        print("WARNINGS", self.report.warnings)

Test().prueba2()