# How to use DevBox to setup Python development environment

## Setup Devbox

To setup devbox, follow the instructions at https://www.jetpack.io/devbox/docs/installing_devbox/

## Setup your project for the first time

You need to git clone this project using any project name you like. 

For example to create new project with name `myNewProject` at Desktop, run the following:

```bash
cd ~/Desktop/
git clone https://github.com/devrealm/python_devbox_template.git myNewProject
```

The above instructions will create a new project with Python and PIP ready by using DevBox.

## Use your new project with Visual Studio Code

To use your new project with visual studio code **for the FIRST TIME**, you need to run command `devbox install`, for example:

```bash
cd ~/Desktop/myNewProject
devbox install
code .
```

**For any other time you want to open your project**, you simple open it at Visual Studio Code, for example:

```bash
cd ~/Desktop/myNewProject
code .
```


## Use PIP

To use PIP in order to install Python packages you need the following:

1. Open a new terminal: `CMD + SHIT + P`
2. Type: `Terminal: Create New Terminal`
3. In the new terminal, type `pip install pandas` _or any python package you need_
