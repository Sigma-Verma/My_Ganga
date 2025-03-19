from GangaCore.GPI import Job, ArgSplitter, Local, Executable
import os


# Number of subjobs and simulations per subjob
num_subjobs = 1000
sims_per_subjob = 1000

# Path to the simulation script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
simulation_script = os.path.join(BASE_DIR, "pi_simulation.py")

# Create the job
j = Job(
    application=Executable(
        exe="sys.executable"
    ),
    backend=Local(),
    splitter=ArgSplitter(
        args=[[simulation_script, str(sims_per_subjob)]] * num_subjobs  # Correctly format the args
    )
)

# Submit the job
j.submit()
