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
    try:
        result1 = subprocess.check_output(com1, shell=True, stderr=subprocess.STDOUT)
        print(result1.decode())
    except subprocess.CalledProcessError as e:
        print('err1:', e.output.decode())
        print(traceback.format_exc())

    try:
        result2 = subprocess.check_output(com2, shell=True, stderr=subprocess.STDOUT)
        print(result2.decode())
    except subprocess.CalledProcessError as e:
        print('err2:', e.output.decode())
        print(traceback.format_exc())

    try:
        result3 = subprocess.check_output(com3, shell=True, stderr=subprocess.STDOUT)
        print(result3.decode())
    except subprocess.CalledProcessError as e:
        print('err3:', e.output.decode())
        print(traceback.format_exc())
