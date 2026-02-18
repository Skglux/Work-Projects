"""  
The **PDF Distributer** is an automated file management script 
that acts as a "Sentry" for your workflow. 
It monitors a specific landing folder and automatically sorts incoming PDF invoices
into organized directories based on specific **keys** extracted from the filename.
"""

import os 
import shutil
import time 

source_dir = r"C:\.."
supplier_dir = r"C:\.."
infpc_dir = r"C:\.."

while True:
    # Creates a list of the file names from source dir
    lstpdf = os.listdir(source_dir)
    # Looping over each pdf in the list of the directory
    for filename in lstpdf:
        

=======
        # REMINDER key 1: supplier, 2: invoice_nr, 3 IRRELEVANT : fleet, 4: training type1, 5: training type2 , 6: consuption period, 7: po_nr IRRELEVANT
        if filename.endswith(".pdf") or filename.endswith(".xlsx"):

            # Safety net

            try:
                time.sleep(1) # waits for 1 second for the file to fully land in any case.
                # Creates a list with each key
                pdfkeys = filename.split("_")
                
                supplier = pdfkeys[0]
                fleet = pdfkeys[2]

                # Condition in case of an invoice split repositing of the keys to adjust the allocation result.
                trng_type = pdfkeys[3]
                trng_type2 = pdfkeys[4]
                period = None
                
                if trng_type2 not in ("re","co"):
                    trng_type2 = None
                    period = pdfkeys[4]
                    if trng_type not in ("re","co"):
                        trng_type = None
                        period = pdfkeys[3]
                else:
                    period = pdfkeys[5]
                    
                # Maps the current file path of the pdf
                current_file_path = os.path.join(source_dir,filename)
                
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

<<<<<<< HEAD
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

=======
                    # Construct the full destination paths (directory + filename)
                    # This ensures the file is placed correctly and allows for overwriting
                    final_infpc_path = os.path.join(target_infpcdir, filename)
>>>>>>> 42c825a (Update pdf_distributer.py)

                # Below it checks for a second training type if it does not exist does not proceed to create path.   
                final_infpc2_path = None
                if trng_type2 is not None:
                    existing_fleet2 = None
                    for infpcsub_folder2 in os.listdir(infpc_dir):
                        if infpcsub_folder2.startswith(fleet):
                            existing_fleet2 = infpcsub_folder2
                            break
                    if existing_fleet2:
                        target_infpcdir2 = os.path.join(infpc_dir,existing_fleet2,trng_type2,period)
                        os.makedirs(target_infpcdir2, exist_ok=True)
                    else:
                        target_infpcdir2 = os.path.join(infpc_dir,fleet,trng_type2,period)
                        os.makedirs(target_infpcdir2, exist_ok=True)
                    
                    # Construct the full destination paths (directory + filename)
                    # This ensures the file is placed correctly and allows for overwriting   
                    final_infpc2_path = os.path.join(target_infpcdir2,filename)
                    
                # Construct the full destination path (directory + filename) for the supplier dir

                # This ensures the file is placed correctly and allows for overwriting
<<<<<<< HEAD
                final_supplier_path = os.path.join(target_supplierdir, word)
                final_infpc_path = os.path.join(target_infpcdir, word)
=======
                final_supplier_path = os.path.join(target_supplierdir, filename)
>>>>>>> 42c825a (Update pdf_distributer.py)
                
                # Copy the PDF to the supplier directory (overwrites if a file with the same name exists)
                shutil.copy2(current_file_path, final_supplier_path)
                
                # Move the original PDF to the final INFPC destination (overwrites if file exists)
                shutil.move(current_file_path, final_infpc_path)

        # Safety net    
            except:
                print(f"Error processing{filename}")    
    time.sleep(10)

        

   

   



