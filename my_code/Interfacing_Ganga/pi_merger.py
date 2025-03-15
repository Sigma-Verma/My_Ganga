import os

total_pi = 0
subjob_count = 0

# Base path where Ganga stores job output
base_dir = "/home/uverma/gangadir/workspace/uverma/LocalXML"

# Change this to your actual job ID
job_id = 137  # Make sure this is correct!

# Path to the job's output directory
job_output_dir = os.path.join(base_dir, str(job_id))

# Iterate over all subjobs
for subjob_id in range(1000):  
    output_file = os.path.join(job_output_dir, str(subjob_id), "output", "stdout")
    
    if os.path.exists(output_file):
        with open(output_file, "r") as f:
            try:
                pi_value = float(f.read().strip())
                total_pi += pi_value
                subjob_count += 1
            except ValueError:
                print(f"Skipping subjob {subjob_id}: Invalid output")
    else:
        print(f"Skipping subjob {subjob_id}: stdout file not found at {output_file}")

# Compute final approximation
if subjob_count > 0:
    final_pi = total_pi / subjob_count
    print(f"Final π approximation: {final_pi}")
else:
    print("No valid results found!")
