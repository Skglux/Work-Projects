"""  
The **PDF Distributer** is an automated file management script 
that acts as a "Sentry" for your workflow. 
It monitors a specific landing folder and automatically sorts incoming PDF invoices
into organized directories based on specific **keys** extracted from the filename.
"""

import os 
import shutil
import time 

source_dir = "C:/Users/fotis/Desktop/inputtest"
supplier_dir = r"C:\Users\fotis\Desktop\test\supplierstest2" 
infpc_dir = r"C:\Users\fotis\Desktop\test\infpcstest1"

while True:
    # Creates a list of the file names from source dir
    lstpdf = os.listdir(source_dir)
    # Looping over each pdf in the list of the directory
    for word in lstpdf:
        
        # REMINDER key 1: supplier, 2: invoice_nr, 3 IRRELEVANT : fleet, 4: training type, 5: consuption period, 6: po_nr IRRELEVANT
        if word.endswith(".pdf"):
            # safety net
            try:
                time.sleep(1) # waits for 1 second for the file to fully land in any case.
                # Creates a list with each key
                pdfkeys = word.split("_")
                
                supplier = pdfkeys[0]
                fleet = pdfkeys[2]
                trng_type = pdfkeys[3]
                period = pdfkeys[4]

                # Maps the current file path of the pdf
                current_file_path = os.path.join(source_dir,word)
                
                # Looks for existing file name that starts with the supplier id
                existing_supplier = None
                for folder_name in os.listdir(supplier_dir):
                    if folder_name.startswith(supplier):
                        existing_supplier = folder_name
                        break
                if existing_supplier:
                    # Maps the path where the file will be placed.
                    target_supplierdir = os.path.join(supplier_dir,existing_supplier,period)
                    # The below is the building function it goes and checks the target_supplier dir parameters: existing_supplier and period if the file with the same name exists then proceeds and checks for subfolder with the same name as the variable period if it does not exist then it creates one.
                    os.makedirs(target_supplierdir, exist_ok=True)
                else:
                    target_supplierdir = os.path.join(supplier_dir,supplier,period)
                    os.makedirs(target_supplierdir, exist_ok=True)

                existing_fleet = None
                for infpcsub_folder in os.listdir(infpc_dir):
                    if infpcsub_folder.startswith(fleet):
                        existing_fleet = infpcsub_folder
                        break
                if existing_fleet:
                    target_infpcdir = os.path.join(infpc_dir,existing_fleet,trng_type,period)
                    os.makedirs(target_infpcdir, exist_ok=True)
                else:
                    target_infpcdir = os.path.join(infpc_dir,fleet,trng_type,period)
                    os.makedirs(target_infpcdir, exist_ok=True)

                # Construct the full destination paths (directory + filename)
                # This ensures the file is placed correctly and allows for overwriting
                final_supplier_path = os.path.join(target_supplierdir, word)
                final_infpc_path = os.path.join(target_infpcdir, word)
                
                # Copy the PDF to the supplier directory (overwrites if a file with the same name exists)
                shutil.copy2(current_file_path, final_supplier_path)
                
                # Move the original PDF to the final INFPC destination (overwrites if file exists)
                shutil.move(current_file_path, final_infpc_path)

            # Safety net    
            except:
                print(f"Error processing{word}")    
    time.sleep(10)

        
   