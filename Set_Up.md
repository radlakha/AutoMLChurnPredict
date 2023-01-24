# Set-Up Instructions

1. Clone the repo

2. On conda prompt, run the command 
```
conda env create -f environment_droplet.yml
```
This creates an environment whose name is specified in the first line of the environment_droplet.yml file (feel free to change the name to your requirements). 

3. Change the absolute paths inside the streamlit app to corresponding absolute paths on your computer.

4. Run the app from conda prompt using streamlit run Home.py 
(Make sure you change your directory's path to point to the app's location using cmd before running this command)
