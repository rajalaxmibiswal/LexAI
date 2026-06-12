import streamlit as st

from document_parser import (
    extract_text,
    smart_chunk
)

from vector_store import VectorStore

from compliance_rules import load_rules

from risk_engine import evaluate_compliance

from report_generator import ReportGenerator

from web_research import search_legal_updates


st.set_page_config(
    page_title="AI Legal Compliance Auditor",
    layout="wide"
)

st.title("⚖️ AI Legal Compliance Auditor")


uploaded_file = st.file_uploader(
    "Upload Legal PDF",
    type=["pdf"]
)

framework = st.selectbox(
    "Select Compliance Framework",
    ["GDPR", "DPDP", "ISO27001"]
)


if uploaded_file:

    with st.spinner("Reading document..."):

        text = extract_text(uploaded_file)

        chunks = smart_chunk(text)

        vector_db = VectorStore()

        vector_db.add_documents(chunks)

        st.success("Document Processed")


    if st.button("Run Compliance Audit"):

        with st.spinner("Auditing..."):

            rules = load_rules()

            findings, score = evaluate_compliance(
                text,
                {framework: rules[framework]}
            )

            legal_updates = search_legal_updates(
                f"{framework} latest compliance regulations"
            )

            reporter = ReportGenerator()

            report = reporter.generate(
                text[:3000],
                findings,
                score,
                legal_updates
            )

        st.metric(
            "Compliance Score",
            f"{score}%"
        )

        st.subheader("Findings")

        for f in findings:

            st.error(
                f"{f['framework']} : "
                f"{f['control']}"
            )

        st.subheader("Audit Report")

        st.write(report)