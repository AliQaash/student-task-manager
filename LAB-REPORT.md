# Lab Report: Assignment 4

**Student:** Ali Qaash  
**Registration No.:** FA23-BSE-026  
**Course:** CSC418 DevOps for Cloud Computing  
**Assignment:** Student Task Manager Development and Version Control Using Git and GitHub  
**Repository:** https://github.com/AliQaash/student-task-manager

## 1. Git vs GitHub; add, commit and push

**Git** is a version control tool that runs on my own computer. It records snapshots of
my project so I can see the history, go back to an older version and work on branches.
**GitHub** is a website that hosts Git repositories online. It adds collaboration features
on top of Git, like Issues, Pull Requests, code review, Actions and Releases.

- `git add` puts the changes I choose into the staging area, ready for the next commit.
- `git commit` saves the staged changes as a snapshot in my local history, with a message.
- `git push` uploads my local commits to the remote repository on GitHub.

## 2. Branches, Pull Requests and merge conflicts

A **branch** lets me work on one feature separately without breaking `main`. In this
project, add-task validation, completing tasks and deleting tasks were each built on their
own branch. **Pull Requests** let me (or a teammate) review the changed files, discuss them,
link them to an Issue and let the automated tests run before the code is merged into `main`.

A **merge conflict** happens when two branches change the same lines of the same file
differently, so Git cannot decide which version to keep. In Part D, `status/in-development`
and `status/testing` both changed the "Project status" line in README.md. After the first
branch was merged, merging the second one caused a conflict that I had to resolve by hand.

## 3. fetch vs pull; merge vs rebase

- `git fetch` downloads new commits from the remote but does not change my working files.
  `git pull` does a fetch and then merges those commits into my current branch.
- `git merge` joins two branches and keeps both histories, usually with a merge commit.
  `git rebase` moves my commits so they sit on top of the other branch, which gives a
  straight-line history but rewrites commit IDs, so it should not be used on shared branches.

## 4. How Issues and Actions help a team

**GitHub Issues** keep a list of the work to do: features, bugs and documentation. Each one
has a description, labels and an assignee, and it closes automatically when a linked Pull
Request is merged. Everyone on the team can see what is planned and what is finished.

**GitHub Actions** runs the tests automatically on every push and Pull Request to `main`.
A teammate can see straight away if a change breaks something, before it is merged. In
this project the first workflow run failed because of a wrong test assertion, and the
next run passed after I fixed it.

## 5. A difficulty I faced and how I solved it

My first problem was getting connected to GitHub from the terminal. The first time I ran
`gh auth login`, the login did not go through, so I could not create the repository or push
anything. I tried again, chose **GitHub.com → HTTPS → Login with a web browser**, copied the
one-time code into the browser page and approved it. After that, `gh auth status` showed my
account as active and `git push` worked without asking for a password.

The second difficulty was the merge conflict in Part D. After merging `status/in-development`,
merging `status/testing` stopped with `CONFLICT (content): Merge conflict in README.md`, and the
file had `<<<<<<<`, `=======` and `>>>>>>>` markers around the "Project status" line. I used
`git status` to find the conflicted file and `git diff` to see both versions. Then I replaced the
two lines with one combined line ("In development and testing"), deleted the markers, and checked
that the Roadmap section from the second branch was still there. Finally I ran `git add README.md`
and `git commit` to finish the merge. I learned that a conflict only happens when both branches
change the same lines, and that Git keeps all the other changes automatically.

## Evidence

Screenshots and command output for each part are in [lab-evidence/](lab-evidence/).
