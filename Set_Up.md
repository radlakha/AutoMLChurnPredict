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

3. Your directory should look something like this 

![image](https://user-images.githubusercontent.com/80118039/217454740-83736989-c216-4281-acdf-520385a605ee.png)

* **Home.py** is the first page which is displayed when you run the Streamlit App.
* Inside the **pages** folder, the other pages of the app are stored. They're numbered numerically in the order of their display. Please follow this order while using the app as well. 
* The **data** folder contains the original dataset to be used (after it is loaded by the user). 
* The **data_mod** folder contains the modified data that is stored from the app. (This is the dataset produced after the user deletes some columns)
* **deployment_28042020.pkl** is the Pickle file which stores the best performing model. 

3. Change the absolute paths inside the streamlit app to corresponding absolute paths on your computer.

These include:

* In the file 2_Upload_Your_Data.py, line 62 which is 

``` save_path = os.path.join(parent_path, "data") ```

Change ```data``` to whatever the name of the folder where you want the original dataset to be stored is. 

Similary, for line 68 in the same file, which is

``` save_path2 = os.path.join(parent_path, "data_mod")```

Chnage ```data_mod``` to whatever the name of the folder where you want the modified dataset to be stored is. 

* In the file 3_Know_Your_Data.py, line 13 which is 

``` path = 'C:/Users/sbhadwal/sol1/streamapp/data_mod' ```

Change this path to the path of the folder where you're storing the modified data. 

* Same as above for file 4_Train_Your_Model.py (line 13) and file 5_Predict.py (line 16)

4. Run the app from conda prompt using streamlit run Home.py 
Use command activate to switch to env you created above if necessary
conda activate env5
(Make sure you change your directory's path to point to the app's location using cd before running this command)
