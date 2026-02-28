"""  
The **PDF Distributer** is an automated file management script 
that acts as a "Sentry" for your workflow. 
It monitors a specific landing folder and automatically sorts incoming PDF invoices
into organized directories based on specific **keys** extracted from the filename.
"""

import os 
import shutil
import time 

source_dir = "C:.."
supplier_dir = r"C:.." 
infpc_dir = r"C:.."

# Name/data validation lists
fleet_codes = ['b7', 'q4', 'e2', 'b7q4', 'b7e2', 'q4b7', 'q4e2', 'e2b7', 'e2q4']
trng_codes = ['re', 'co', 'reco', 're.co', 'co.re', 'reco.co', 'reco.re', 'core.co', 'core.re', 'co.reco', 'co.core', 're.reco', 'co.core','re.core']

while True:
    # Creates a list of the file names from source dir
    lstpdf = os.listdir(source_dir)
    # Looping over each pdf in the list of the directory
    for filename in lstpdf:
        
        # REMINDER key 1: supplier, 2: invoice_nr_IRRELEVANT, 3: fleet, 4: training type1, 5: training type2 , 6: consuption period, 7: po nr_IRRELEVANT
        if filename.endswith(".pdf") or filename.endswith(".xlsx"):
            # Safety net
            try:
                time.sleep(1) # waits for 1 second for the file to fully land in any case.
                # Creates a list with each key
                filekeys = filename.split("_")
                
                # File keys validation:
                def keys(filekeys):
                    supplier = tt = att1 = att2 = btt1 = btt2 = period = afl = bfl = None
                    if len(filekeys[0]) > 7 and len(filekeys[0]) < 12:
                            supplier = filekeys[0]
                            if filekeys[2] in fleet_codes and filekeys[3] in trng_codes:
                                tt = filekeys[3]
                                period = filekeys[4]
                                if len(filekeys[2]) > 2:
                                    afl = filekeys[2][0:2]
                                    bfl= filekeys[2][2:4]
                                    if len(tt) < 3:
                                        att1 = tt
                                        btt1 = tt 
                                    elif len(tt) < 5:
                                        att1 = tt[0:2]
                                        att2 = tt[2:4]
                                        btt1 = tt[0:2]
                                        btt2 = tt[2:4]
                                    else:
                                        tt = filekeys[3].split(".")
                                        if len(tt[0]) > 2:
                                            att1 = tt[0][0:2]
                                            att2 = tt[0][2:4]
                                            btt1 = tt[1]
                                        else:
                                            att1 = tt[0]
                                            btt1 = tt[1][0:2]
                                            btt2 = tt[1][2:4]
                                else:
                                    afl = filekeys[2]
                                    if len(tt) > 2:
                                        att1 = tt[0:2]
                                        att2 = tt[2:4]
                                    else:
                                        att1 = tt
                            else:
                                period = filekeys[2]
                            return supplier, afl, bfl, att1, att2, btt1, btt2, period  
                    else:    
                        return (None,)*8
                
                result = keys(filekeys)
                
                
                if result[0] is not None: # Looks on the first value which corresponds to supplier and always must be one if there is none follows to an error message otherwise it follows with the process.
                    supplier, afl, bfl, att1, att2, btt1, btt2, period = result

                    source_path = os.path.join(source_dir,filename) # This is the path were the file will be placed to be allocated
                    
                    # Looks for existing file name that starts with the supplier id
                    final_supplier_path = None
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
                        final_supplier_path = os.path.join(target_supplierdir,filename)
                    else:
                        target_supplierdir = os.path.join(supplier_dir,supplier,period)
                        os.makedirs(target_supplierdir, exist_ok=True)
                        final_supplier_path = os.path.join(target_supplierdir,filename)
                    
                    final_afl1_path = None
                    final_afl2_path = None

                    if afl: # If afl exists proceeds with the creation of paths and directories for each training type that exists
                        if att1:
                            afl1_path = os.path.join(infpc_dir,afl,att1,period)
                            os.makedirs(afl1_path, exist_ok=True)
                            final_afl1_path = os.path.join(afl1_path,filename)

                        if att2:
                            afl2_path = os.path.join(infpc_dir,bfl,att2,period)
                            os.makedirs(afl2_path, exist_ok=True)
                            final_afl2_path = os.path.join(afl2_path,filename)
                    
                    final_bfl1_path = None
                    final_bfl2_path = None
                    
                    if bfl:
                        if btt1:
                            bfl1_path = os.path.join(infpc_dir,bfl,btt1,period)
                            os.makedirs(bfl1_path, exist_ok=True)
                            final_bfl1_path = os.path.join(bfl1_path,filename)
                        if btt2: 
                            bfl2_path = os.path.join(infpc_dir,bfl,btt2, period)
                            os.makedirs(bfl2_path, exist_ok=True)
                            final_bfl2_path = os.path.join(bfl2_path,filename)
                    
                    
                    
                    # if supplier exists then the program will proceed successfully.
                    if final_supplier_path is not None:
                        shutil.copy2(source_path,final_supplier_path)    
                        if final_afl1_path is not None:
                            shutil.copy2(source_path, final_afl1_path)
                        if final_afl2_path is not None:
                            shutil.copy2(source_path, final_afl2_path)
                        if final_afl2_path is not None:
                            shutil.copy2(source_path, final_bfl1_path)
                        if final_afl2_path is not None:
                            shutil.copy2(source_path, final_bfl2_path)
                        os.remove(source_path)
                else:
                    print("Naming file error",filename)
        # Safety net    
            except:
                print(f"Error processing{filename}")    
    time.sleep(10)
