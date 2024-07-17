import time
import sys
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import tkinter as tk
from tkinter import messagebox

def start_process():
    from_date = entry_from_date.get()
    to_date = entry_to_date.get()
    status_value = entry_status_value.get()
    page_number = int(entry_page_number.get())
    start_row = int(entry_start_row.get())
    end_row = int(entry_end_row.get())

    options = webdriver.EdgeOptions()
    options.add_argument("--disable-notifications")
    driver = webdriver.Edge(options=options)
    driver.maximize_window()

    url = ""
    driver.implicitly_wait(10)
    driver.get(url)

    from_date_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[@width='35%']//input[@id='fromDate']"))
    )
    from_date_field.clear()
    from_date_field.send_keys(from_date)
    time.sleep(2)

    to_date_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[@width='45%']//input[@id='toDate']"))
    )
    to_date_field.clear()
    to_date_field.send_keys(to_date)
    time.sleep(2)
    to_date_field.send_keys(Keys.ENTER)
    time.sleep(2)

    select_status = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "select#status"))
    )
    select_status.click()
    time.sleep(1)

    option_belum_kirim = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//option[@value='{status_value}']"))
    )
    option_belum_kirim.click()
    time.sleep(2)
    
    select_filter = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button#filter.btn-send"))
    )
    select_filter.click()
    time.sleep(5)

    input_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class='ui-pg-input ui-corner-all']"))
    )
    input_box.clear()
    input_box.send_keys(page_number)
    time.sleep(2)

    input_box.send_keys(Keys.ENTER)
    time.sleep(7)
    
    sorting_nik = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "th#jqGrid_NIK.ui-th-column.ui-th-ltr.ui-state-default.ui-sortable-handle"))
    )
    sorting_nik.click()
    time.sleep(5)

    time.sleep(10)

    for row_id in range(start_row, end_row + 1):
        try:
            button_1 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[@class='btn-satusehat' and @id='openBundleButton ' and @data-rowid='{row_id}']"))
            )
            button_1.click()
            time.sleep(5)

            try:
                combined_dialog = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[@id='ui-id-1' and (contains(text(), 'Not_found') or contains(text(), 'Not_valid') or contains(text(), 'Error'))]"))
                )
                ok_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='ui-button ui-corner-all ui-widget']"))
                )
                ok_button.click()
                time.sleep(2)
                continue
            except:
                pass

            nadi_value = random.randint(60, 65)
            pernafasan_value = random.randint(22, 26)
            suhu_tubuh_value = round(random.uniform(35.8, 36.2), 1)
            kesadaran_value = "compos mentis"

            field_nadi = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input#field-nadi.form-control"))
            )
            field_nadi.clear()
            field_nadi.send_keys(nadi_value)

            field_pernafasan = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input#field-pernafasan.form-control"))
            )
            field_pernafasan.clear()
            field_pernafasan.send_keys(pernafasan_value)

            field_suhutubuh = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input#field-suhutubuh.form-control"))
            )
            field_suhutubuh.clear()
            field_suhutubuh.send_keys(suhu_tubuh_value)

            field_kesadaran = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input#field-kesadaran.form-control.form-control-sm"))
            )
            field_kesadaran.clear()
            field_kesadaran.send_keys(kesadaran_value)

            button_2 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='btn-send' and @id='send-bundle' and @name='send-bundle']"))
            )
            button_2.click()
            time.sleep(2)

            button_3 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='ui-button ui-corner-all ui-widget']"))
            )
            button_3.click()
            time.sleep(2)

        except Exception as e:
            print(f"Error processing row_id {row_id}: {e}")

    print("Skrip selesai dijalankan.")
    messagebox.showinfo("Info", "Skrip selesai dijalankan.")

root = tk.Tk()
root.title("Web Automation Satu Sehat")

tk.Label(root, text="From date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
entry_from_date = tk.Entry(root)
entry_from_date.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="To date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
entry_to_date = tk.Entry(root)
entry_to_date.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Status(All/Belum kirim):").grid(row=2, column=0, padx=10, pady=5)
entry_status_value = tk.Entry(root)
entry_status_value.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Page yang akan diproses:").grid(row=3, column=0, padx=10, pady=5)
entry_page_number = tk.Entry(root)
entry_page_number.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Rentang tabel (start row):").grid(row=4, column=0, padx=10, pady=5)
entry_start_row = tk.Entry(root)
entry_start_row.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Rentang tabel (end row):").grid(row=5, column=0, padx=10, pady=5)
entry_end_row = tk.Entry(root)
entry_end_row.grid(row=5, column=1, padx=10, pady=5)

start_button = tk.Button(root, text="Start", command=start_process)
start_button.grid(row=8, columnspan=5, pady=20)

tk.Label(root, text="Copyright IT RSU UMM .v1").grid(row=6, columnspan=5, pady=10)

root.mainloop()
