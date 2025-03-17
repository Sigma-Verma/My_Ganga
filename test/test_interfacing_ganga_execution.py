import unittest
import subprocess
import os

interfacing_ganga_path = os.path.join(os.path.dirname(__file__), "../my_code/Interfacing_Ganga/create_pi_job.py")


class TestInterfacingGangaExec(unittest.TestCase):

    def test_ganga_job_submission(self):
        
        """Test if the create_pi_job is attempted in Ganga."""

        # Run the create_pi_job script
        result = subprocess.run(["ganga", interfacing_ganga_path], capture_output=True, text=True)

        # Check Ganga job list
        ganga_check = subprocess.run(["ganga", "--batch", "jobs"], capture_output=True, text=True)
        ganga_output = ganga_check.stdout.lower()

        # Test will pass if command 'jobs' produces any output.
        self.assertTrue("job" in ganga_output or "submitted" in result.stdout.lower(), 
                        "Ganga job submission was not attempted.")

if __name__ == "__main__":
    unittest.main()
