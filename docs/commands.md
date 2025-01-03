
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

## Conda Virtual Environment with CUDA

### Create a Conda Environment

```bash
conda create --prefix ./env tensorflow-gpu
```

Activate the environment:

```bash
conda activate ./env
```

### Install ipykernel

```bash
pip install ipykernel notebook
```

### Add venv to kernels

```bash
python -m ipykernel install --user --name=tf-gpu --display-name "Python (tf-gpu)"
```

Verify by running:
```bash
jupyter kernelspec list
```

### Add Cuda to any conda enviroment
```bash
conda install -c conda-forge cudatoolkit cudnn
```

```bash
pip install tensorflow[and-cuda]
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
```bash
virtualenv --system-site-packages .venv
source .venv/bin/activate
pip install --upgrade pip
pip install --upgrade nvidia-pyindex
pip install -r ./requirements.txt
```
