
import unittest
import io
import sys

from todo import Task, TaskPool


class TestTaskPool(unittest.TestCase):

    def setUp(self):
        self.task_pool = TaskPool()

    def test_add_task(self):
        task = Task("New Task")
        self.task_pool.add_task(task)
        self.assertEqual(len(self.task_pool.tasks), 1)

    def test_get_open_tasks(self):
        self.task_pool.populate()
        open_tasks = self.task_pool.get_open_tasks()

        self.assertEqual(len(open_tasks), 3)

        for task in open_tasks:
            self.assertEqual(task.status, "ToDo")

    def test_get_done_tasks(self):
        self.task_pool.populate()
        done_tasks = self.task_pool.get_done_tasks()

        self.assertEqual(len(done_tasks), 3)

        for task in done_tasks:
            self.assertEqual(task.status, "Done")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskPool)

    stream = io.StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    result = runner.run(suite)

    output = stream.getvalue()

    for line in output.splitlines():
        if " ... ok" in line:
            print(line.strip())

    if not result.wasSuccessful():
        print(output)
        sys.exit(1)
