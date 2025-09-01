already_said = []


def modern_print(text):
    if text not in already_said:
        already_said.append(text)
        print(text)

modern_print("test!")
modern_print("test!")
modern_print("test2")
modern_print("test2")
modern_print("test1")
modern_print("test3")
modern_print("test3")
modern_print("test2")
