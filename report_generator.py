import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


class ReportGenerator:

    def __init__(self):

        genai.configure(
            api_key=os.getenv("GOOGLE_API_KEY")
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate(
        self,
        document_context,
        findings,
        score,
        web_context
    ):

        findings_text = "\n".join(
            [
                f"- {f['framework']} | {f['control']} | {f['severity']}"
                for f in findings
            ]
        )

        prompt = f"""
You are an expert Legal Compliance Auditor.

DOCUMENT:
{document_context}

COMPLIANCE FINDINGS:
{findings_text}

COMPLIANCE SCORE:
{score}

LEGAL UPDATES:
{web_context}

Generate a professional compliance audit report.

Format:

# Executive Summary

# Compliance Score

# Missing Controls

# Risk Assessment

# Recommendations

# Conclusion
"""

        response = self.model.generate_content(prompt)

        return response.text