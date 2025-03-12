import os, time
from GangaCore.GPI import Job, ArgSplitter, Local, Executable

# this script takes takes the LHC.pdf file and splits it into single pdfs

j1 = Job(
    application=Executable(exe="/home/uverma/Documents/code/My_Ganga/p_env/bin/python",
                           args=["/home/uverma/Documents/code/My_Ganga/my_code/split_pdf.py", "/home/uverma/Documents/code/My_Ganga/LHC.pdf"]),
                           backend=Local())
j1.submit()
time.sleep(3)


# this ganga code takes in all the pdfs and runs the count_it.py on each of them n gives the total output at the end


folder_path = "/home/uverma/Documents/code/My_Ganga/my_code/output_pages"


pdf_files = []      # gets path of all the pdfs
for f in os.listdir(folder_path):
    pdf_files.append(os.path.join(folder_path, f))

j2 = Job(
    application=Executable(
        exe="/home/uverma/Documents/code/My_Ganga/p_env/bin/python"
    ),
    backend=Local(),
    splitter=ArgSplitter(
        args=[["/home/uverma/Documents/code/My_Ganga/my_code/count_it.py", pdf_file] for pdf_file in pdf_files]
    )
)

j2.submit()

print(f"Job {j2.id} submitted. Waiting for subjobs to complete...")
time.sleep(5)   # ensure j2 gets completed

# add the result of all the sub_job
total_count = 0
for subjob in j2.subjobs:
    subjob_output_path = os.path.join(subjob.outputdir, "stdout")
    with open(subjob_output_path, "r") as f:
        count = int(f.read().strip())  # Read the num from stdout file
        total_count += count  # Add it to the total

# Print the total count

print(f"Total occurrences of 'it': {total_count}")