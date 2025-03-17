from GangaCore.GPI import Job, ArgSplitter, Local, Executable
import os

# Number of subjobs and simulations per subjob
num_subjobs = 1000
sims_per_subjob = 1000

# Path to the simulation script
simulation_script = os.path.join(os.path.dirname(__file__), "../my_code/Interfacing_Ganga/pi_simulation.py")

# Create the job
j = Job(
    application=Executable(
        exe="/home/uverma/Documents/code/My_Ganga/p_env/bin/python"
    ),
    backend=Local(),
    splitter=ArgSplitter(
        args=[[simulation_script, str(sims_per_subjob)]] * num_subjobs  # Correctly format the args
    )
)

# Submit the job
j.submit()
