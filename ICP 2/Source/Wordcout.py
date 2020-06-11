from collections import Counter
from pathlib import Path


def main():
    input_folder_path = Path("C:\\Users\\Aishwarya\\Desktop\\CSEE5590_python_Icp\\ICP 2\\Textfiles\\Text_file_Input.txt")
    ouput_folder_path = Path("C:\\Users\\Aishwarya\\Desktop\\CSEE5590_python_Icp\\ICP 2\\Textfiles\\Text_Output_file.txt")
    file = open(input_folder_path, "r", encoding="utf-8-sig")
    wordcount = Counter(file.read().split())
    f = open(ouput_folder_path, "w")
    for item in wordcount.items():
        f.write("{}\t{}\n".format(*item))


if __name__ == "__main__":
    main()
