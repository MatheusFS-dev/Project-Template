
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
```bash
virtualenv --system-site-packages .venv
source .venv/bin/activate
pip install --upgrade pip
pip install --upgrade nvidia-pyindex
pip install -r ./requirements.txt
```

# How to Use Git LFS

## Install Git LFS on ubuntu

1. **Install Git LFS**:
   ```sh
   sudo apt install git-lfs
   ```

## Step 1: Initialize the Git LFS after installation:

1. **Initialize Git LFS**:
   ```sh
   git lfs install
   ```

## Step 2: Configure Git LFS for Your Repository

1. **Navigate to your repository**:
   ```sh
   cd /path/to/your/repo
   ```

2. **Track specific file types**:
   For example, if you want to track all `.psd` files:
   ```sh
   git lfs track "*.psd"
   ```

   This command will create a `.gitattributes` file in your repository with the necessary configuration.

3. **Add and commit the `.gitattributes` file**:
   ```sh
   git add .gitattributes
   git commit -m "Track PSD files with Git LFS"
   ```

## Step 3: Using Git LFS

1. **Add individual large files if you want**:
   ```sh
   git add path/to/large/file.psd
   ```

2. **Commit the files**:
   ```sh
   git commit -m "Add large file"
   ```

3. **Push to the remote repository**:
   ```sh
   git push origin main
   ```

   Git LFS will handle the large files appropriately during the push.

## Step 4: Cloning a Repository with Git LFS

When cloning a repository that uses Git LFS, simply clone as usual:
```sh
git clone https://github.com/your/repo.git
```

Git LFS will automatically fetch the large files.

## Step 5: Pulling and Fetching LFS Objects

If you need to update the LFS files after pulling updates from the repository:
```sh
git lfs pull
```

You can also fetch specific LFS objects:
```sh
git lfs fetch
```

## Additional Tips

- To see which files are being tracked by Git LFS:
  ```sh
  git lfs ls-files
  ```

- To untrack a file (e.g., if you no longer want a file to be managed by Git LFS):
  ```sh
  git lfs untrack "*.psd"
  ```

  Then commit the changes to `.gitattributes`.
