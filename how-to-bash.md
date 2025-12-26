# How to use Git Bash  
## Initialize 
 1. git clone https://github.com/somang0813-ui/baekjoon_project
 2. cd baekjoon_project
## Create files & prepare commit  
 3. mkdir -p problems/BOJ_1000/yoon
 4. touch problems/BOJ_1000/yoon/solution.py
 5. git status (new file should appear in red: not staged yet)
 6. git add problems/BOJ_1000/yoon/solution.py (or git add . if you want to add all changes)
 7. git commit -m "boj 1000: initial solution."
 8. git push (Upload)

## USEFUL COMMAND

1. Check status:  
   git status

2. Check differences:  
   git diff

3. Stage files:  
   git add filename  
   git add .

4. Commit changes:  
   git commit -m "message"

5. Push to GitHub:  
   git push

6. Get latest changes from GitHub:  
   git pull

7. View commit history:  
   git log --oneline

8. Check branches:  
   git branch  
