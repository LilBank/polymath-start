## Git Branching Exercise

This repository contains 2 branches:

* master - the home html page
* mobile-phone - a process for applying film to a phone screen

Files:
```
home.md      - Home page, written in Markdown
processes/
    change-screen-protector.md - procedure written in Markdown
```

1. Clone this repo to your computer.
2. Look at the branches you have:
   ```
   git branch
   ```
   and **all** branches including remote ones:
   ```
   git branch -a
   ```
2. Create a local `mobile-phone` branch that **tracks** the remote `mobile-phone` branch (the `-t` or `--track` option), and switch to that branch:
   ```
   git branch -t origin/mobile-phone
   git checkout mobile-phone
   ```
   You can also do both in one command:
   ```
   git checkout -t origin/mobile-phone
   ```
3. Fix some markdown and spelling errors.
4. Commit the work (on branch mobile-phone).
5. Push the branch to Github.
6. Change to master branch.
7. Merge the mobile-phone branch into master
   * Fix conflicts
   * Preview the fix -- verify formatting is correct
   * Commit the work
8. Push master to Github
9. Create a new branch for another process.
10. Switch to that branch.
11. Write your process in Markdown.
    * Preview it to verify the formatting is correct
12. Commit work
13. Add github as remote for this branch and push it to Github.
14. Switch back to master.
15. Merge your branch into master.
16. Push master to Github.

Result:
* Github has 3 branches containing up-to-date code
  - master
  - mobile-phone
  - your branch
* You can view the markdown on Github

## Git Commands

When you want to create a local branch that "tracks" a branch
on a remote repository, there are 2 ways:

1. Create the tracking branch, but don't switch to it:
   ```
   git branch -t remotes/origin/branch_name
   ```
2. Check a tracking branch and switch to it immediately:
   ```
   git checkout -b branch_name origin/branch_name
   ```
   the syntax is `git checkout -b local_branch remote/remote_branch_name`.
3. A shortcut for (2) when the local and remote tracking branch have the same name is:
   ```
   git checkout -t origin/branch_name
   ```


When you have a local branch that you want to add to a remote repository (Github),
do this:
```
git branch                    # check you are on the correct branch
git checkout my_branch        # switch to local branch you want to push
git push -u origin my_branch  # "my_branch" is name for new branch on Github
```
Only do this for a branch not already on Github.  Once the branch is on github and your local branch is "tracking" it, just "push" as usual.
