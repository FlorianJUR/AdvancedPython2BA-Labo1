# Laboratory 1 ECAM 2026
+ The first exercice is to write functions in utils.py and then test it with test_utils using pytest
+ The second exercice is to find the problems in main.py and galaxy.py without using print() or brain
## Basic git
1. Open a folder on your computer
2. Open VScode with this folder and put <code>git clone \<github repository link></code><br>
   2.1. <code>git branch \<branch name></code> (create a git branch, <code>git branch</code> to see all branches)<br>
            usage: create a branch for adding a feature and then delete it<br>
   2.2. <code>git add \<file name></code> or the + on VScode (<code>git status</code> to see all selected files) <br>
        <code>git commit -m \<message></code> or commit button on VScode<br>
   2.3. <code>git push origin \<branch name></code> push on github (origin) the branch <br>
   2.4. go on github > in your repository > pull requests > new pull request > selecte the branch you want to merge on main and a description<br>
   2.5. on main <code>git pull origin main</code><br>
   2.6. <code>git branch -d \<branch name></code> to delete the branch<br>
      Update branch: use <code>git rebase \<branch name></code><br>
      <img src="https://github.com/FlorianJUR/AdvancedPython2BA-Labo1/blob/2435d8e3a56aaa71194332bc6403e8f8b0246954/Capture%20d'%C3%A9cran%202026-04-26%20182132.png" width="300" height="300" /><br>
      delete commits on the branch one by one, update main branch, reconstruct you branch commits one by one (you can modify a commit during the process if necessary)
   4.1. <code>git checkout main</code> (we go on main)<br>
   
   4.2. <code>git merge --no-ff\<branch name></code> (update main with branche info, you should never commit and push directly on main --no-ff : no fast forward)

