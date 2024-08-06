import time
import subprocess
import traceback

# Define commands with corrected path separators
com1 = 'cd D:/TestGithubCommits && git add .'
com2 = 'cd D:/TestGithubCommits && git commit -m "another yet commit"'
com3 = 'cd D:/TestGithubCommits && git push -u origin main'

for i in range(10000):
    # Update file with new content
    with open('D:/TestGithubCommits/some_file.txt', 'w') as f:
        f.write('This is for educational purposes. I am testing the Python code to make a lot of commits to GitHub Server to check if the server is working well. DO NOT TRY THIS FOR EDUCATIONAL PURPOSE.')
        f.write(str(i))
        f.write('\n')

    # Pause before running commands
    time.sleep(2)
    print('sleep 5 sec')

    # Run git commands and handle errors
    for command, error_label in [(com1, 'err1'), (com2, 'err2'), (com3, 'err3')]:
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            print(f'{error_label} Output:\n{result.decode()}')
        except subprocess.CalledProcessError as e:
            print(f'{error_label} Error:\n{e.output.decode()}')
            print(traceback.format_exc())
        except Exception as e:
            print(f'{error_label} Unexpected Error:\n{str(e)}')
            print(traceback.format_exc())
