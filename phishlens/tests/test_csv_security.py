import csv
import io
import unittest
from email.message import EmailMessage
from phishlens.analyzer import analyze_message
from phishlens.reporting import render_batch_csv, spreadsheet_literal


class CsvSecurityTests(unittest.TestCase):
    def test_formula_prefixes_and_controls_are_literal(self):
        for prefix in ("=", "+", "-", "@", " \t=", "\ufeff=", "\x00="):
            with self.subTest(prefix=prefix):
                self.assertTrue(spreadsheet_literal(prefix + "1").startswith("'"))
        self.assertEqual(spreadsheet_literal('ordinary, "İstanbul"'), 'ordinary, "İstanbul"')

    def test_export_protects_header_and_filename_without_mutating_result(self):
        message = EmailMessage()
        message["Subject"] = "=1+1"
        message["From"] = "@example"
        message.set_content("ordinary body")
        result = analyze_message(message, source="+source")
        row = next(csv.DictReader(io.StringIO(render_batch_csv([result]))))
        self.assertEqual(row["subject"], "'=1+1")
        self.assertEqual(row["source"], "'+source")
        self.assertEqual(result.headers["subject"], "=1+1")
        self.assertEqual(int(row["score"]), result.score)
