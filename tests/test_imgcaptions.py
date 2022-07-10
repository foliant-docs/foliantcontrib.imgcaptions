import io
import os
import sys

from foliant_test.preprocessor import PreprocessorTestFramework
from foliant_test.preprocessor import unpack_file_dict
from unittest import TestCase, skip


def count_output_warnings(source) -> int:
    return source.getvalue().lower().count('warning')


def rel_name(path: str):
    return os.path.join(os.path.dirname(__file__), path)


class TestShowCommits(TestCase):
    def setUp(self):
        self.ptf = PreprocessorTestFramework('imgcaptions')
        self.ptf.quiet = False
        self.ptf.capturedOutput = io.StringIO()
        sys.stdout = self.ptf.capturedOutput

    def test_default(self):
        file_dict = {
            'default.md': rel_name('test_data/default.md')
        }

        expected_file_dict = {
            'default.md': rel_name('expected_data/default.md')
        }

        self.ptf.test_preprocessor(
            input_mapping=unpack_file_dict(file_dict),
            expected_mapping=unpack_file_dict(expected_file_dict)
        )

        self.assertEqual(0, count_output_warnings(self.ptf.capturedOutput))

    def test_front_matter(self):
        file_dict = {
            'front_matter.md': rel_name('test_data/front_matter.md')
        }

        expected_file_dict = {
            'front_matter.md': rel_name('expected_data/front_matter.md')
        }

        self.ptf.test_preprocessor(
            input_mapping=unpack_file_dict(file_dict),
            expected_mapping=unpack_file_dict(expected_file_dict)
        )

        self.assertEqual(0, count_output_warnings(self.ptf.capturedOutput))

    def test_template(self):
        file_dict = {
            'template.md': rel_name('test_data/template.md')
        }

        expected_file_dict = {
            'template.md': rel_name('expected_data/template.md')
        }
        self.ptf.options = {
            'template': '<p class="image_caption">Fig - {caption}</p>'
        }
        self.ptf.test_preprocessor(
            input_mapping=unpack_file_dict(file_dict),
            expected_mapping=unpack_file_dict(expected_file_dict)
        )

        self.assertEqual(0, count_output_warnings(self.ptf.capturedOutput))

    @skip("does not work from shell script")
    def test_stylesheet_path(self):
        file_dict = {
            'stylesheet_path.md': rel_name('test_data/stylesheet_path.md')
        }

        expected_file_dict = {
            'stylesheet_path.md': rel_name('expected_data/stylesheet_path.md')
        }
        self.ptf.options = {
            'stylesheet_path': 'test_data/left_imgcaptions.css'
        }
        self.ptf.test_preprocessor(
            input_mapping=unpack_file_dict(file_dict),
            expected_mapping=unpack_file_dict(expected_file_dict)
        )

        self.assertEqual(0, count_output_warnings(self.ptf.capturedOutput))
