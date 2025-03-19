import subprocess
from ganga.GangaCore.testlib.GangaUnitTest import GangaUnitTest

class TestInterfacingGangaExec(GangaUnitTest):
    def test_ganga_job_submission(self):

        from GangaCore.GPI import jobs

        # Run the create_pi_job.py script and capture output
        result = subprocess.run(
            ["python3", "my_code/Interfacing_Ganga/create_pi_job.py"],
            capture_output=True,
            text=True
        )

        # Debugging: Print script output
        print("SCRIPT OUTPUT:", result.stdout)
        print("ERROR OUTPUT:", result.stderr)

        # Ensure script ran successfully
        self.assertEqual(result.returncode, 0, "❌ ERROR: create_pi_job.py execution failed.")

        # Find the most recent job
        self.assertGreater(len(jobs), 0, "❌ ERROR: No jobs found after script execution.")
        j = jobs[-1]  # Get the latest submitted job

        self.assertIsInstance(j, Job, "❌ ERROR: The created job is not an instance of Job.")

        # Ensure job is submitted
        self.assertTrue(j.status in ["submitted", "running", "completed"], "❌ ERROR: Job was not submitted properly.")

        # Wait for job completion
        self.assertTrue(sleep_until_completed(j, 60), "❌ ERROR: Timeout waiting for job to complete.")

        # Check final status
        self.assertEqual(j.status, "completed", "❌ ERROR: Job did not complete successfully.")
