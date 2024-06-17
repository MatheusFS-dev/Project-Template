
# Useful Git and Python Virtual Environment Commands

## Git Configuration
Set up your Git user email and username.
```bash
git config user.email "your.email@example.com"
git config user.name "YourUsername"
```

## Create and Switch Branch
Create a new branch and switch to it.
```bash
git checkout -b branch
```

## Add and Commit Changes
Add all changes and commit with a message.
```bash
git add .
git commit -m "Released new patch"
```

## Tagging a Commit
Create a new tag for the current commit.
```bash
git tag v1.0
```

## Pushing to Remote Repository
Push the branch and tag to the remote repository.
```bash
git push https://your_token@github.com/YourUsername/YourRepo.git branch
git push origin v1.0
git push origin v1.0 --force
```

## Python Virtual Environment

### Create Virtual Environment
Create a new virtual environment.
```bash
python3 -m venv .venv
```

### Activate Virtual Environment
Activate the virtual environment.
```bash
source .venv/bin/activate
```

## Freeze Installed Packages
Save the current list of installed packages to a file.
```bash
pip freeze > requirements.txt
```
## Create a virtual environment with system site packages
This is good if using Tensorrt in a virtual environment or when having path problems.
```bash
virtualenv --system-site-packages .venv
source .venv/bin/activate
pip install --upgrade pip

pip install --upgrade nvidia-pyindex
pip install -r ./requirements.txt
```
