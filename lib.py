from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv




def login(email,password):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "cl-socialButtonsIconButton__google"))
    )
    # print()

    google_login = driver.find_element(By.CLASS_NAME, "cl-socialButtonsIconButton__google")
    google_login.click()
    time.sleep(5)
    # data - identifier
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "anshumanrishi27@gmail.com")]'))
        )
        div_element = driver.find_element(By.XPATH, '//*[contains(text(), "anshumanrishi27@gmail.com")]')

        # Perform an action on the div element (e.g., click)
        div_element.click()

        # conti_text = "Continue"
        # xpath_expression = f"//*[contains(text(), 'Continue')]"
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), 'Continue')]"))
            )

            # Find the element by its text and click it
            conti = driver.find_element(By.XPATH, f"//*[contains(text(), 'Continue')]")
            conti.click()
        except:
            print("no continue needed")
    except:
        print("alredy login")

def is_row_created(file_path, row_index):
    # Check if the row at 'row_index' is marked as created in the CSV file
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == row_index and len(row) > 1 and row[-1] == 'Yes':
                return True
    return False
def is_row_dow(file_path, row_index):
    # Check if the row at 'row_index' is marked as created in the CSV file
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == row_index and len(row) > 1 and row[-2] == 'Yes' and row[-1] == "no":
                return True
    return False
def mark_created(file_path, row_indices):
    # Update the CSV file to mark the rows at 'row_indices' as created
    rows = []

    # Check if the header is already present
    header_present = False
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            existing_header = next(reader)
            if existing_header == ['Lyrics', 'Music', 'Title', 'Downloaded', 'Created']:
                header_present = True
    except FileNotFoundError:
        pass  # File does not exist, we will add the header

    # If header is not present, add it
    if not header_present:
        rows.append(['Lyrics', 'Music', 'Title', 'Downloaded', 'Created'])
    # else:
    #     rows.append(existing_header)  # Add the existing header

    # Read the existing content
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        if not header_present:
            next(reader)  # Skip the header if it was added

        for i, row in enumerate(reader):
            if i in row_indices:
                # Update the 'Created' column to 'Yes' for the rows that are already created
                row[-1]='Yes'
                # if row[-1] == 'Yes':
                #     row[-1] = 'Yes'
                # else:
                #     # Add a new column 'Downloaded' with the value 'No' for the created rows
                #     # Add a new column 'Created' with the value 'Yes' for the created rows
                #     row.extend(['No', 'Yes'])
            # if not header_present:
            #     # Add a new column 'Downloaded' with the value 'No' for other rows
            #     # Add a new column 'Created' with the value 'No' for other rows
            #     row.extend(['No', 'No'])
            rows.append(row)

    # Write the updated content back to the file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def mark_dow(file_path, row_indices):
    # Update the CSV file to mark the rows at 'row_indices' as created
    rows = []

    # Check if the header is already present
    header_present = False
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            existing_header = next(reader)
            if existing_header == ['Lyrics', 'Music', 'Title', 'Downloaded', 'Created']:
                header_present = True
    except FileNotFoundError:
        pass  # File does not exist, we will add the header

    # If header is not present, add it
    if not header_present:
        rows.append(['Lyrics', 'Music', 'Title', 'Downloaded', 'Created'])
    # else:
    #     rows.append(existing_header)  # Add the existing header

    # Read the existing content
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        if not header_present:
            next(reader)  # Skip the header if it was added

        for i, row in enumerate(reader):
            if i in row_indices:
                # Update the 'Created' column to 'Yes' for the rows that are already created
                row[-2]='Yes'
                # if row[-1] == 'Yes':
                #     row[-1] = 'Yes'
                # else:
                #     # Add a new column 'Downloaded' with the value 'No' for the created rows
                #     # Add a new column 'Created' with the value 'Yes' for the created rows
                #     row.extend(['No', 'Yes'])
            # if not header_present:
            #     # Add a new column 'Downloaded' with the value 'No' for other rows
            #     # Add a new column 'Created' with the value 'No' for other rows
            #     row.extend(['No', 'No'])
            rows.append(row)

    # Write the updated content back to the file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
def count_rows_with_yes_created_value(input_csv):
    # Read the input CSV file and store its data
    with open(input_csv, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Count the number of rows where the "Created" column is "no"
    count_no_created = sum(row['Created'] == 'Yes' for row in data)

    return count_no_created


def download():
    global row_count
    global error_create
    rows_to_dow = count_rows_with_yes_created_value(csv_file_path)
    to_download = 2*(row_count-error_create)
    to_download=2*(rows_to_dow)
    to_download = 2 * (row_count)
    index_d = row_count

    try:
        spinner = WebDriverWait(driver, 200).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'chakra-spinner'))
        )
        print("Spinner has disappeared. Continue with the program.")
    except:
        print("no spinner")


    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), 'Library')]"))
    )

    # Find the element by its text and click it
    lib = driver.find_element(By.XPATH, f"//*[contains(text(), 'Library')]")
    lib.click()
    time.sleep(5)


    if(to_download<20):
        print("hi")


        more_action = WebDriverWait(driver, 100).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="More Actions"]'))
        )
        # print("Number of elements with aria-label='More Actions':", len(more_action))

        for i in range(to_download):
            print(to_download)
            print(i)
            # Your actions on each element go here
            if is_row_dow(csv_file_path, index_d)&(i%2!=0):
                print(f"Skipping download for row {index_d} as it is already marked as download.")
                index_d -= 1

                continue
            elif (is_row_dow(csv_file_path, index_d)):
                print(f"Skipping download for row {index_d} as it is already marked as download elif.")
                # index_d -= 1
                continue


            time.sleep(1)
            element = more_action[i]
            # driver.execute_script("arguments[0].scrollIntoView();", element)
            # driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});",
            #                      element)
            time.sleep(1)
            element.click()
            print("element")
            time.sleep(2)

            actions = ActionChains(driver)
            for _ in range(5):
                actions.send_keys(Keys.DOWN)
                time.sleep(1)  # Add a small delay between key presses
            # download_button = WebDriverWait(driver, 100).until(
            #     EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Download Audio")]'))
            #     # EC.presence_of_element_located((By.CSS_SELECTOR, '[data-index="5"]'))
            # # EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-index="5"]'))
            # )

            # Simulate pressing the "Enter" key
            actions.send_keys(Keys.ENTER)
            actions.perform()
            if(i%2!=0):
                mark_dow(csv_file_path, [index_d])
                index_d -= 1

            print("Enter key pressed")
            time.sleep(10)
    else:
        upp = to_download
        inside = to_download
        for j in range(int(upp/20)+1):
            more_action = WebDriverWait(driver, 100).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="More Actions"]'))
                # EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="More Actions"]'))
            )
            # print("Number of elements with aria-label='More Actions':", len(more_action))
            for i in range(inside):
                if is_row_dow(csv_file_path, index_d) & (i % 2 != 0):
                    print(f"Skipping download for row {index_d} as it is already marked as download.")
                    index_d -= 1

                    continue
                elif (is_row_dow(csv_file_path, index_d)):
                    print(f"Skipping download for row {index_d} as it is already marked as download elif.")
                    # index_d -= 1
                    continue
                # Your actions on each element go here
                time.sleep(1)
                element = more_action[i]
                WebDriverWait(driver, 10).until(EC.presence_of_element_located(element))
                # expected_element.click()
                time.sleep(1)
                element.click()
                print("element")
                time.sleep(5)

                actions = ActionChains(driver)
                for _ in range(5):
                    actions.send_keys(Keys.DOWN)
                    time.sleep(1)  # Add a small delay between key presses
                # download_button = WebDriverWait(driver, 100).until(
                #     # EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Download Audio")]'))
                #     # EC.presence_of_element_located((By.CSS_SELECTOR, '[data-index="5"]'))
                #     EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-index="5"]'))
                # )

                # Simulate pressing the "Enter" key
                actions.send_keys(Keys.ENTER)
                actions.perform()
                # mark_dow(csv_file_path, [index_d])
                if (i % 2 != 0):
                    mark_dow(csv_file_path, [index_d])
                    index_d -= 1
                print("Enter key pressed")
                time.sleep(5)
                if(i==19):
                    break
            print(inside)
            inside = inside-19
            print(inside)
            next_page_button = WebDriverWait(driver, 100).until(
                # EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Next Page"]'))
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Next Page"]'))
            )

            # Click the element
            next_page_button.click()
            print("next page")
            time.sleep(5)

        print("hi")
    print("download complete")

index_c=1
# Lyrics, Music, Title
def fill(Lyrics, Music, Title,dow,create):

    global index_c
    global error_create
    if is_row_created(csv_file_path, index_c):
        print(f"Skipping creation for row {index_c + 1} as it is already marked as created.")
        index_c += 1
        return

    # try:
    #     download_element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, 'div.chakra-stack.css-1pv08kv'))
    #     )
    #
    #     # Find the elements with aria-label="More Actions" inside the div
    #     downloded_before_create = download_element.find_elements(
    #         By.CSS_SELECTOR, '[aria-label="More Actions"]'
    #     )
    #     index = len(downloded_before_create)
    #     index = int(index)
    #     print(index)
    # except:
    #     print("empty")
    input_lyrics = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[placeholder="Enter your lyrics"]'))
    )
    input_lyrics.clear()

    input_lyrics.send_keys(Lyrics)

    input_music = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[placeholder="Enter style of music"]'))
    )
    input_music.clear()

    input_music.send_keys(Music)

    input_title = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[placeholder="Enter a title"]'))
    )
    input_title.clear()

    input_title.send_keys(Title)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "css-b0ppuc"))
    )
    create = driver.find_element(By.CLASS_NAME, "css-b0ppuc")
    create.click()


    # Increment the index for the next iteration

    # wait = WebDriverWait(driver, 5)  # 10 seconds timeout

    alert_description_text = ""
    alert_description_element = None
    try:
        alert_description_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-status="error"]'))
        )
        print("wait complete")
        error_create+=1
        alert_description_text = alert_description_element.text
        print(f"Chakra Alert Description: {alert_description_text}")
        print(f"Error while creating song with this Lyric: {Lyrics},Music: {Music},Title: {Title}")
        time.sleep(10)
    except:
        print("no error")
        mark_created(csv_file_path, [index_c])
        time.sleep(5)
    index_c += 1


# *row
def download_song():
    global index
    # time.sleep(5)
    try:
        spinner = WebDriverWait(driver, 200).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'chakra-spinner'))
        )
        print("Spinner has disappeared. Continue with the program.")
    except:
        print("no spinner")


    div_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.chakra-stack.css-1pv08kv'))
    )

    # Find the elements with aria-label="More Actions" inside the div
    elements_with_aria_label = div_element.find_elements(
        By.CSS_SELECTOR, '[aria-label="More Actions"]'
    )
    print("Number of elements with aria-label='More Actions':", len(elements_with_aria_label))

    # start_index = index  # Change this to the desired starting index

    # Get the sublist starting from the specified index
    # elements_to_interact = elements_with_aria_label[index:]
    print(index)

    # Perform actions on the elements (if needed)
    # for element in elements_to_interact:
    #     # Your actions on each element go here
    #
    #     element.click()
    #     print("element")
    #     time.sleep(5)
    #     # download_button = WebDriverWait(driver, 10).until(
    #     #     # EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Download Audio")]'))
    #     #     EC.presence_of_element_located((By.CSS_SELECTOR, '[data-index="5"]'))
    #     # )
    #     # print("download_button_select")
    #     #
    #     # # Click the button
    #     # download_button.click()
    #     # Simulate pressing the "Down" key five times using ActionChains
    #     actions = ActionChains(driver)
    #     for _ in range(5):
    #         actions.send_keys(Keys.DOWN)
    #         time.sleep(1)  # Add a small delay between key presses
    #
    #     # Simulate pressing the "Enter" key
    #     actions.send_keys(Keys.ENTER)
    #     actions.perform()
    #     print("Enter key pressed")
    #     time.sleep(10)
    for i in range(2):
        # Your actions on each element go here
        element=elements_with_aria_label[-1-i]
        element.click()
        print("element")
        time.sleep(5)
        # download_button = WebDriverWait(driver, 10).until(
        #     # EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Download Audio")]'))
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '[data-index="5"]'))
        # )
        # print("download_button_select")
        #
        # # Click the button
        # download_button.click()
        # Simulate pressing the "Down" key five times using ActionChains
        actions = ActionChains(driver)
        for _ in range(5):
            actions.send_keys(Keys.DOWN)
            time.sleep(1)  # Add a small delay between key presses
        download_button = WebDriverWait(driver, 100).until(
                # EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Download Audio")]'))
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-index="5"]'))
            )
        # Simulate pressing the "Enter" key
        actions.send_keys(Keys.ENTER)
        actions.perform()
        print("Enter key pressed")
        time.sleep(2)
def row_csv(file_path):
    global row_count
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header row if present
        print("row_i")
        row_count = sum(1 for rows in reader)
        print(f"row done:{row_count}")


def process_csv(file_path):
    # global row_count
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            fill(*row)
def song():
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "css-ghot30"))
    )
    switch_element = driver.find_element(By.CLASS_NAME, "css-ghot30")


    # Check if the "data-checked" attribute is present
    if switch_element.get_attribute("data-checked"):
        print("The 'data-checked' attribute is present.")
        process_csv(csv_file_path)
        # for _ in range(row_count):
        #     process_csv(csv_file_path)
        download()
        # download_song(result_index)
    else:

        print("The 'data-checked' attribute is not present.")
        switch_element.click()
        process_csv(csv_file_path)
        # for _ in range(row_count):
        #     process_csv(csv_file_path)
        download()
        # download_song(result_index)
def add_columns_to_csv_if_needed(input_csv):
    # Read the input CSV file and store its data
    with open(input_csv, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Check if the headers already exist
    headers_exist = all(header in data[0] for header in ['Downloaded', 'Created'])

    if not headers_exist:
        # Add "downloaded" and "created" columns with initial value "no"
        data[0].extend(['Downloaded', 'Created'])
        for row in data[1:]:
            row.extend(['no', 'no'])

        # Save the updated data back to the same CSV file
        with open(input_csv, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("Columns added successfully.")
    else:
        print("Columns already exist. No modifications needed.")

# Specify the path to the ChromeDriver executable
chrome_driver_path = "chromedriver.exe"

# Use Options to set the debuggerAddress
# opt = Options()
# opt.add_experimental_option("debuggerAddress", "localhost:9222")

options = webdriver.ChromeOptions()
# options.headless = False
# profile = "C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\User Data"
# options.add_argument(f"user-data-dir={profile}")
options.add_argument("--start-maximized")
options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=options)

print("connect")

try:
    # service = Service(executable_path=chrome_driver_path)
    # # Initialize the Chrome WebDriver with both Service and Options
    # driver = webdriver.Chrome(service=service)

    # Navigate to a website
    driver.get("https://app.suno.ai/create/")
    time.sleep(5)
    try:
        login("anshumanrishi27@gmail.com", "1234")
    except:
        print("alredy logedin")


    csv_file_path = "data.csv"
    row_count=0
    index=0
    error_create=0
    row_csv(csv_file_path)
    add_columns_to_csv_if_needed(csv_file_path)


    song()
    # login()
    # download()

    time.sleep(5)

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Quit the browser
    if 'driver' in locals():
        driver.quit()

