import os
import subprocess
import time  # Import the time module

# Path to the repository
repo_path = 'D:/TestGithubCommits'

# Check for changes in the repository
def check_for_changes(path):
    os.chdir(path)
    status = subprocess.check_output('git status --porcelain', shell=True).decode().strip()
    return status

# Main script
for i in range(10000):
    with open('D:/TestGithubCommits/some_file.txt', 'w') as f:
        f.write('This is for educational purposes. I am testing the Python code to make a lot of commits to GitHub Server to check if the server is working well. DO NOT TRY THIS FOR EDUCATIONAL PURPOSE.')
        f.write(str(i))
        f.write('\n')

    time.sleep(2)
    print('sleep 5 sec')

    # Check for changes
    changes = check_for_changes(repo_path)
    if not changes:
        print('No changes detected for git add.')
        continue

    # Run git commands and handle errors
    commands = [
        ('cd D:/TestGithubCommits && git add .', 'err1'),
        ('cd D:/TestGithubCommits && git commit -m "another yet commit"', 'err2'),
        ('cd D:/TestGithubCommits && git push -u origin main', 'err3')
    ]
    for command, error_label in commands:
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            print(f'{error_label} Output:\n{result.decode()}')
        except subprocess.CalledProcessError as e:
            print(f'{error_label} Error:\n{e.output.decode()}')
        except Exception as e:
            print(f'{error_label} Unexpected Error:\n{str(e)}')
