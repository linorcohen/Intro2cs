#################################################################
# FILE : lab6_test.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse lab6 2021
# DESCRIPTION: tester for lab6
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################
import os
import subprocess


def terminal_run(file_to_input, file_to_output):
    input_file = open(file_to_input)
    output_file = open(file_to_output, 'w')
    subprocess.Popen(["python.exe", "lab6.py"], stdin=input_file,
                     stdout=output_file, stderr=subprocess.STDOUT)
    input_file.close()
    output_file.close()


def check_list_of_inputs():
    inputs_lst = [file for file in os.listdir('Lab6/') if file.endswith(".txt")]
    for file in inputs_lst:
        terminal_run('Lab6/'+file, file[:2]+'output.txt')


if __name__ == '__main__':
    check_list_of_inputs()
