class DatabaseRecord:
    def __init__(self, player_name, variant, numbered, is_autograph, is_relic, grading_company, grade, number, set):
        self.player_name = player_name
        self.variant = variant
        self.numbered = numbered
        self.is_autograph = is_autograph
        self.is_relic = is_relic
        self.grading_company = grading_company
        self.grade = grade
        self.number = number
        self.set = set

# =CONCAT(TRIM(CONCATENATE(A132," ",CONCAT("#",J132), IF(D132 <> "Base", CONCAT(" ",D132),""), IF(E132 <> " ",
# CONCAT(" ",E132),""), IF(F132 = "Y", " Autograph", ""), IF(G132 = "Y", " Patch", ""), IF(H132 <> "",
# CONCATENATE(" ", H132, " ", I132),""))), CONCAT(" ", K132))

    def return_search_term(self):
        #Format variant value
        variant_value = ""
        if self.variant != "Base":
            variant_value = self.variant + " "
        #Format numbered value
        numbered_value = ""
        if self.numbered != "":
            numbered_value = self.numbered + " "
        #Format is_autograph value
        is_autograph_value = ""
        if self.is_autograph == "Y":
            is_autograph_value = "Autograph "
        #Format is_relic value
        is_relic_value = ""
        if self.is_relic == "Y":
            is_relic_value = "Patch "
        #Format grading_company_value and grade_value
        grade_value = ""
        if self.grading_company != "":
            grade_value = self.grading_company + " " + self.grade.__str__() + " "
        return self.player_name + " " + "#" + self.number.__str__() + " " + variant_value + numbered_value + is_autograph_value + is_relic_value \
               + grade_value + self.set