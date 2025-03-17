import os
import time
from GangaCore.GPI import Job, ArgSplitter, Local, Executable

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
python_exe = os.path.join(BASE_DIR, "p_env", "bin", "python")
split_pdf_script = os.path.join(BASE_DIR, "my_code", "split_pdf.py")
lhc_pdf_path = os.path.join(BASE_DIR, "LHC.pdf")
count_it_script = os.path.join(BASE_DIR, "my_code", "count_it.py")
output_folder = os.path.join(BASE_DIR, "my_code", "output_pages")

j1 = Job(
    application=Executable(exe=python_exe, args=[split_pdf_script, lhc_pdf_path]),
    backend=Local(),
)
j1.submit()

# Wait for Job 1 to complete
while j1.status not in ["completed", "failed"]:
    time.sleep(2)

# --- Job 2: Count "it" in PDFs ---
pdf_files = [os.path.join(output_folder, f) for f in os.listdir(output_folder)]

j2 = Job(
    application=Executable(exe=python_exe),
    backend=Local(),
    splitter=ArgSplitter(args=[[count_it_script, pdf_file] for pdf_file in pdf_files]),
)
j2.submit()

# Wait for Job 2 completion
while any(subjob.status not in ["completed", "failed"] for subjob in j2.subjobs):
    time.sleep(2)

# --- Collect Results ---
total_count = sum(
    int(open(os.path.join(subjob.outputdir, "stdout"), "r").read().strip())
    for subjob in j2.subjobs
)

# Print the total count
print(f"Total occurrences of 'it': {total_count}")
