from ganga.GangaCore.testlib.GangaUnitTest import GangaUnitTest


class TestInterfacingGangaExec(GangaUnitTest):
    def test_ganga_job_submission(self):
        from GangaCore.GPI import Job
        from my_code.Interfacing_Ganga.create_pi_job import create_pi_job

        j = create_pi_job()
        
        self.assertIsInstance(j, Job, "❌ ERROR: create_pi_job did not return a Job instance.")

        j.submit()

        self.assertTrue(j.status in ["submitted", "running", "completed"], "❌ ERROR: Job was not submitted properly.")

        from ganga.GangaTest.Framework.utils import sleep_until_completed
        self.assertTrue(sleep_until_completed(j, 60), "❌ ERROR: Timeout waiting for job to complete.")

        self.assertEqual(j.status, "completed", "❌ ERROR: Job did not complete successfully.")
