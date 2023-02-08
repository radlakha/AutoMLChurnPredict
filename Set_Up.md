# Set-Up Instructions

1. Clone the repo

2. On conda prompt, run the command 
```
conda env create -f environment_droplet.yml
```
This creates an environment whose name is specified in the first line of the environment_droplet.yml file (feel free to change the name according to your preferences). 

If you run into SSL Error when working from corporate network it is likely that you are behind a proxy like Zscaler. Follow steps below for windows platform:
    Run certlm.msc

    Find Zscaler Root CA in Trusted Root Certificate Authorities and export it to a folder choosing the base-64 encoded X.509 (.CER)

    Open Anaconda Prompt

    conda config --set ssl_verify path_of_the_file_that_you_just_saved

    Remember when you are not working from office edit the file and comment out ssl_verify by placing a # sign in front.

    code %USERPROFILE%\.condarc

There is a prefix label in YAML which also needs to be edited per your env.
The below statement 3 needs to be more specific

3. Change the absolute paths inside the streamlit app to corresponding absolute paths on your computer.

4. Run the app from conda prompt using streamlit run Home.py 
Use command activate to switch to env you created above if necessary
conda activate env5
(Make sure you change your directory's path to point to the app's location using cd before running this command)
