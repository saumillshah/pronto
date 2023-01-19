import os
import subprocess
import datetime

# This program uses the subprocess module to run Git commands and capture the output. 
# The os.chdir() function is used to change the current working directory to the specified git_dir so that the Git commands are run in the correct location. 
# The program uses the git rev-parse command to get the active branch, git status to check if there are any modified files and git log command to get the author name, time of commit. 
# The program then uses the datetime module to check whether the commit was made within the last week and to check whether the author is Rufus.

def git_info(git_dir):
    os.chdir(git_dir)
    active_branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True).stdout.strip()
    modified = "M" in subprocess.run(["git", "status", "--short"], capture_output=True, text=True).stdout
    author = subprocess.run(["git", "log", "-1", "--pretty=%an"], capture_output=True, text=True).stdout.strip()
    author_time = subprocess.run(["git", "log", "-1", "--pretty=%at"], capture_output=True, text=True).stdout.strip()
    date_authored = datetime.datetime.fromtimestamp(int(author_time))
    last_week = datetime.datetime.now() - datetime.timedelta(days=7)
    return {
        "active branch": active_branch,
        "local changes": modified,
        "recent commit": date_authored > last_week,
        "blame Rufus": author == "Rufus"
    }

print(git_info("C:/Users/Saumil/Desktop/m5/demo"))