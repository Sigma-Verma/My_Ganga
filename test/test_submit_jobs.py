import unittest
import subprocess
import os

submit_script = "/home/uverma/Documents/code/My_Ganga/my_code/submit_jobs.py"


class TestSubmitJobs(unittest.TestCase):

    def test_submit_jobs(self):

        """Test if submit_jobs.py successfully creates and runs Ganga jobs."""
        

        # Run the job submission script
        result = subprocess.run(["ganga", submit_script], capture_output=True, text=True)

        # Print output or error of jobs
        print("Ganga Output:", result.stdout)
        print("Ganga Error:", result.stderr)

        # Test will pass if "total occurrences of 'it'" occurs in the output
        self.assertIn("total occurrences of 'it'", result.stdout.lower(), "Expected output not found.")

if __name__ == "__main__":
    unittest.main()
