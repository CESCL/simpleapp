1. Create a new directory - local.
2. Develop the main.py, text.txt, annotations may become the readme.md in the future. 
(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> ls 


    Directory: C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         11/4/2023   8:53 PM           2153 Annotations.md
-a----         11/4/2023   7:23 PM            451 main.py
-a----         11/4/2023   7:28 PM           1162 text.txt

3. Test the code locally 

(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> python .\main.py 
The number of lines in the file is: 8

4. Use the terminal to validate the git version. 

(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> git --version
git version 2.42.0.windows.1

5. Configure credentials for the github.
git config --global user.name "Carlos Escalona"
git config --global user.email "carlos.armando.escalona@gmail.com"

6. Include the public key in the deploy key.
#Generate a public key.
ssh-keygen -t rsa -b 4096 -C "carlos.armando.escalona@gmail.com"
type id_rsa.pub
#Add the public key in the deploy key on github.
#Validate SSH authentication. 
(myenv) PS C:\Users\Carlos Escalona\.ssh> ssh -T git@github.com              
Hi CESCL/simpleapp! You've successfully authenticated, but GitHub does not provide shell access.

7. Initialize Git, add GitHub repository as a remote, commit and push the code. 

(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> git init
Initialized empty Git repository in C:/Users/Carlos Escalona/code/1_UoT/dot503/Assessment2/.git/

git remote add origin git@github.com:CESCL/aubenops.git
(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> git remote add origin git@github.com:CESCL/simpleapp.git
(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> git add .
(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> git commit -m "Initial commit"
[master (root-commit) 393d244] Initial commit
 3 files changed, 50 insertions(+)
 create mode 100644 Annotations.md
 create mode 100644 main.py
 create mode 100644 text.txt

8. Create 3 different branches. 

(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> git branch feature-x
(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> git branch feature-y
(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> git branch feature-z

9. Checkout feature-x and modify the source file. In feature-x a word count feature is addedd to the main.py file. 

(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> git checkout -b feature-x
(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> python .\main.py
The number of lines in the file is: 8
The number of words in the file is: 182

10. Checkout feature-y and modify the source file. In feature-y a byte count feature is addedd to the main.py file. 
mor
(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> git checkout -b feature-y
(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> python .\main.py
The number of lines in the file is: 8
The number of bytes in the file is: 1155

11. Checkout feature-y and modify the source file. In feature-z includes the same word and line count but shows a different message.

(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> git checkout -b feature-z
(myenv) PS C:\Users\Carlos Escalona\code\1_UoT\dot503\Assessment2> python .\main.py      
[Feature Z] The file 'text.txt' has 8 lines and 182 words.

