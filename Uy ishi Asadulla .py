# class fan:
#     def __init__(self, ismi, familiya, yoshi):
#         self.ismi = ismi
#         self.familiya = familiya
#         self.yoshi = yoshi
#
#     def info(self):
#         return self.ismi, self.familiya, self.yoshi
#
#
# class Student(fan):
#     def __init__(self, ismi, familiya, yoshi, kurs, ID):
#         super().__init__(ismi, familiya, yoshi)
#         self.kurs = kurs
#         self.ID = ID
#
#     def st_info(self):
#         print("\n" + "="*50)
#         print(f"{'Ismi':<15}{'Familiya':<15}{'Yoshi':<8}{'Kurs':<8}{'ID':<10}")
#         print("-"*50)
#         print(f"{self.ismi:<15}{self.familiya:<15}{self.yoshi:<8}{self.kurs:<8}{self.ID:<10}")
#         print("="*50)
#
# st1 = Student("Vasto", "Lord", 99, 5, 934372)
# st1.st_info()
# class Odam:
#     def __init__(self, ism, familiya, yosh):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh
#
#     def info(self):
#         return f"{self.ism} {self.familiya}, {self.yosh} yoshda"
#
#
# class Dasturchi(Odam):
#     def __init__(self, ism, familiya, yosh, til, tajriba):
#         super().__init__(ism, familiya, yosh)
#         self.til = til
#         self.tajriba = tajriba
#
#     def kod_yozish(self):
#         return f"{self.ism} {self.til} tilida kod yozmoqda"
#
#     def info(self):
#         return f"{super().info()}, {self.tajriba} yil tajribali {self.til} dasturchisi"
#
#
# class Muhandis(Odam):
#     def __init__(self, ism, familiya, yosh, soha, loyihalar_soni):
#         super().__init__(ism, familiya, yosh)
#         self.soha = soha
#         self.loyihalar_soni = loyihalar_soni
#
#     def loyiha_yaratish(self):
#         return f"{self.ism} yangi {self.soha} loyihasini boshladi"
#
#     def info(self):
#         return f"{super().info()}, {self.soha} muhandisi, {self.loyihalar_soni} ta loyiha"
#
#
# dasturchi1 = Dasturchi("Anvar", "Toshev", 25, "Python", 3)
# muhandis1 = Muhandis("Jamshid", "Aliyev", 30, "Qurilish", 12)
#
# print(dasturchi1.info())
# print(dasturchi1.kod_yozish())
# print()
# print(muhandis1.info())
# print(muhandis1.loyiha_yaratish())







