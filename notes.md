# COLLABORATING WITH A PEER

## steps
* create a PAT for the repository and save somewhere safe.
* clone the shell repository with the PAT (not your general PAT but one generated for the particular project)
* The collaborator also clones the repository with the PAT they generate for the same shell repository
* run `git config --list` to show details of repository or directory you have cloned.
* use git fetch then git pull to update the files you have on your local machine.
* if you intend to create a new function or make changes, you create a branch and work on the branch. [git checkout -b `branch name`; after the edit or creation, git add .;git commit -m `"[Feature]: added `function/file name`"`;git push origin `branch name`].
* you go to github and create a pull request and tell the other party what you have done in the branch.
* the one that receives the request goes through the code, click `review changes`, add comment, approve or request changes. merge if everything works well.
* `GIT STASH` can be a way to track the changes and resolve before commiting.

## when there's an issue because both parties made changes on the same branch/file and one hasn't updated yet and is pushing
* git config pull.rebase false # merge (the default strategy) - applies all remote commits first then apply the local commit next. it fixes the commit issue and you can see the changes that has been made to the file.
* after the changes have been made by deleting the conflict markers; git status to see the possible solutions; follow the instructions (git add `file name`;git commit -m `"commit message"`;git push/git merge).
* git add `filename`; git commit (without a commit message will open a text editor; commit message on the first line and the message on the subsequent lines will go into the commit message in the pull request);git pull.

