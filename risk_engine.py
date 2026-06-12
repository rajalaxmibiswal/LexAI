def evaluate_compliance(document_text, rules):

    findings = []

    score = 100

    for framework, controls in rules.items():

        for control in controls:

            if control.lower() not in document_text.lower():

                findings.append({
                    "framework": framework,
                    "control": control,
                    "severity": "High"
                })

                score -= 5

    score = max(score, 0)

    return findings, score