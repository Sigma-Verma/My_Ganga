import unittest
import subprocess
import os , time

submit_script = os.path.join(os.path.dirname(__file__), "../my_code/submit_jobs.py")


class TestSubmitJobs(unittest.TestCase):

    def setUp(self):
        """Ensure a clean Ganga job list before running tests."""
        subprocess.run(["ganga", submit_script], input="y\n", text=True, capture_output=True)

    def test_submit_jobs(self):

        """Test if submit_jobs.py successfully creates and runs Ganga jobs."""
        
        # Run the job submission script
        result = subprocess.run(
            ["ganga", submit_script],
            capture_output=True, text=True
        )

        print("Ganga Output:", result.stdout)
        print("Ganga Error:", result.stderr)

        # Ensure the job was submitted
        self.assertIn("submitted", result.stdout.lower(), "Job was not submitted.")

        # Wait for jobs to complete
        time.sleep(30)

        # Check job list
        ganga_jobs = subprocess.run(
            ["ganga", "-e", "jobs"],
            capture_output=True, text=True
        )

        print("🔹 Jobs Output:", ganga_jobs.stdout)
        print("🔹 Jobs Error:", ganga_jobs.stderr)

        # Verify if expected output exists
        self.assertIn("total occurrences of 'it'", result.stdout.lower(), "Expected output not found.")

if __name__ == "__main__":
    unittest.main()
