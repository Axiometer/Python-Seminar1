# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("X", "\t", "Y", "\t", "Z", "\t", "¬(X ⋁ Y ⋁ Z)", "\t\t", "¬X ⋀ ¬Y ⋀ ¬Z", "\t\t", "¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")
print("*"*110)

Tozhdestvo = True

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            first_check = not(X or Y or Z)
            second_check = not X and not Y and not Z
            if first_check != second_check:
                Tozhdestvo = False
            print(X, "\t", Y, "\t", Z, "\t", first_check, "\t\t\t", second_check, "\t\t\t", first_check == second_check)
print("*"*110)
if Tozhdestvo:
    print("Тождество всегда истина")
else:
    print("Тождество не всегда истина")