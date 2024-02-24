Git:

Clone a repository:

```bash
git clone <url>
```

Add a file to staging area:

```bash
git add <file>
git add .  # Add all files
```

Commit changes:

```bash
git commit -m "Message"
```

Combine add and commit:

```bash
git commit -am "Message"
```

Push changes to remote repository:

```bash
git push
```

Pull changes from remote repository:

```bash
git pull
```

Reset changes:

```bash
git reset --hard <commit hash>
git reset --head origin/master # Reset to remote repository
```

Create a new branch:

```bash
git branch <branch_name>
```

Switch to a branch:

```bash
git checkout <branch_name>
```

Create a new branch and switch to it:

```bash
git checkout -b <branch_name>
```

Merge a branch:

```bash
git merge <branch_name>
```

Delete a branch:

```bash
git branch -d <branch_name>
```

Show the status of the repository:

```bash
git status
```

Show the history of the repository:

```bash
git log
```

Show the differences between two commits:

```bash
git diff <commit1> <commit2>
```
