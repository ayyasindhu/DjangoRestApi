from django.test import TestCase
from ..models import BookInventory


class ExperimentTest(TestCase):
    """ Test module for Experiment model """

    def setUp(self):
        BookInventory.objects.create(
            title='Project', author='project@project.com', dateCreated="2022-04-01", published=True)
        BookInventory.objects.create(
            title='Project 2', author='project@project.com', dateCreated="2022-04-01", published=True)

    def test_experiment_email(self):
        experiment_project = BookInventory.objects.get(title='Project')
        experiment_project_2 = BookInventory.objects.get(title='Project 2')
        self.assertEqual(
            experiment_project.get_author(), "Project belongs to project@project.com author.")

