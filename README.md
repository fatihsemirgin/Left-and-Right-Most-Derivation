# Left-and-Right-Most-Derivation

### A Python program for <b>left and right most derivation</b>. For this purpose, your program should take three inputs. First is “ll.txt” which contains LL(1) parsing table for left most derivation. Second is “lr.txt” which contains LR(1) parsing table for right most derivation. Third is “input.txt” which contains input strings (could be more than 2) you should process with their corresponding tables.

<hr>

<h3>FILE_LL = “ll.txt”<br>
FILE_LR = “lr.txt”<br>
FILE_INPUT = “input.txt”</h3>

### These variables contains names of the files you must read. Their default value should be the values given here, not different or personalized. In addition, you should NOT use global addressing for these files (e.g. C:\user\student\Desktop\input.txt). You should only use their names so that they are searched on local folder only.

### Example files for ll.txt, lr.txt and input.txt are also given. You can examine them and change them to test your software. Your program will be graded by using different parsing tables and inputs, so make sure that your program works for all parsing tables and inputs, not just one.

### Assuming your program takes the given example files as input, you are expected to generate an output on console (not in a file) like given on the page below (the text given inside parenthesis is for information only, you are not required to print it out but you can if you wish):

![image](https://github.com/fatihsemirgin/Left-and-Right-Most-Derivation/assets/109742155/9e631eb1-7dce-413c-9554-a466f0ccec00)
![image](https://github.com/fatihsemirgin/Left-and-Right-Most-Derivation/assets/109742155/3a519640-f112-46b0-a0ed-ae454993349a)

### As you may have seen, there is a special character at your input files called Epsilon (ϵ). Make sure your program detects this character correctly. Uppercase and lowercase version of this character is shown in the links below. 
https://www.compart.com/en/unicode/U+03B5
https://www.compart.com/en/unicode/U+03F5
### Your input files uses spaces to make it more readable and table like, however this is not a requirement. You should eliminate empty spaces when you read these files because input strings “E->TA” and “E -> T A” are functionally equivalent in this context and you should consider them as the same too.


