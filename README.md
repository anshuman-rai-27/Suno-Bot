
# Suno Bot

It lets you create and download songs from suno.ai




## Deployment

To deploy this project 

To create and download songs simultaneously

```bash
  ./main.py 
```
To create and download songs seperately

```bash
  ./lib.py 
```
Just to only download the songs 
```bash
  ./lib.py 
```




## Run Locally

* Install the requirments file 

* Provide the path to the chrome profile from which you want to create the song like:  

profile = "C:\\\Users\\\ASUS\\\AppData\\\Local\\\Google\\\Chrome\\\User Data"

change the path of the from the both program files main.py and lib.py

* change the email in login function  in both the files (i.e main.py and lib.py )

example: 

 WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "anshumanrishi27@gmail.com")]'))
        )
        div_element = driver.find_element(By.XPATH, '//*[contains(text(), "anshumanrishi27@gmail.com")]')

replace anshumanrishi27@gmail.com with your gmail

* Change the csv file with same header as in sample csv with same file name.

* The chrome profile path you provide make sure that your gmail is logined on that chrome before initializing the script



## Warnings

* Check the chromedrive and chrome's version  to be same 

* Do not open any other tab on chrome while running the script

* check if the chromedrive.exe is in same folder is not







