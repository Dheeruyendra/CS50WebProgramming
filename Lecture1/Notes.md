Git:
`<br>`
Clone a repository: 
```bash 
git clone <url>
```
`<br>`

Add a file to staging area:
```bash
git add <file>
git add .  # Add all files
``` 
`<br>`

Commit changes:
```bash
git commit -m "Message"
```
`<br>`

Combine add and commit:
```bash 
git commit -am "Message"
```
`<br>`

Push changes to remote repository:
```bash
git push
```
`<br>`

Pull changes from remote repository:
```bash
git pull
```
`<br>`

Reset changes:
```bash
git reset --hard <commit hash>
git reset --head origin/master # Reset to remote repository
```
`<br>`

Create a new branch:
```bash
git branch <branch_name>
```
`<br>`

Switch to a branch:
```bash
git checkout <branch_name>
```
`<br>`

Merge a branch:
```bash
git merge <branch_name>
```
`<br>`

Delete a branch:
```bash
git branch -d <branch_name>
```
`<br>`

Show the status of the repository:
```bash
git status
```
`<br>`

Show the history of the repository:
```bash
git log
```
`<br>`

Show the differences between two commits:
```bash
git diff <commit1> <commit2>
```
`<br>`

