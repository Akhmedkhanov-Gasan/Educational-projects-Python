FIRSTFILE = input()
SECONDFILE = input()
OUTPUTFILE = input()

with open(FIRSTFILE, 'r', encoding="UTF-8") as file_in:
    first_dir = {tok for tok in file_in.read().split()}

with open(SECONDFILE, 'r', encoding="UTF-8") as file_in:
    second_dir = {tok for tok in file_in.read().split()}

out = sorted(list(first_dir ^ second_dir))

with open(OUTPUTFILE, 'w', encoding="UTF-8") as file_out:
    file_out.writelines(tok + "\n" for tok in out)
