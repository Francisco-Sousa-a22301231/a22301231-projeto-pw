import subprocess

print("\nTo push | push('message')\n\nTo pull | pull()\n")
username = 'Francisco-Sousa-a22301231'
token = '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'
url = f"https://{username}:{token}@github.com/{username}/a22301231-projeto-pw.git"

def push(commit_message):

    try:
        # Add all changes to the staging area
        subprocess.run(["git", "add", "."], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Commit changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Push changes
        # Note: Replace <username> and <token> with your actual username and token
        subprocess.run(["git", "push", url], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        print("\nGit commit and push successful.\n")
    except subprocess.CalledProcessError as e:
        print(f"\nError: {e.stderr.decode('utf-8')}\n")

def pull():

    try:
        # Pull changes
        subprocess.run(["git", "pull", url], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        print("\nGit pull successful.\n")
    except subprocess.CalledProcessError as e:
        print(f"\nError: {e.stderr.decode('utf-8')}\n")
