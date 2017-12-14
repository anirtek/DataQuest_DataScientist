## 1. Introduction ##


cd ~
git clone /dataquest/user/git/chatbot
cd chatbot
git checkout -b feature/king-bot
printf "\nprint('I am the king')" >> bot.py
git add .
git commit -m "Make more kinglike"
git checkout master
git checkout -b feature/queen-bot
printf "\nprint('I am the queen)" >> bot.py
git add .
git commit -m "Make more queenlike"
git checkout master
git merge feature/king-bot
git merge feature/queen-bot

## 2. Aborting a Merge ##


cd /home/dq/chatbot
git merge --abort

## 3. Resolving Conflicts ##


cd /home/dq/chatbot
git merge feature/queen-bot
echo "print('I am the queen')" > bot.py
git add .
git commit -m "Fixed conflicts"
git push origin master