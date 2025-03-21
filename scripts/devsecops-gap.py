import pandas as pd

# Define the data for the Excel file
practices = [
    "Secure Code Development",
    "Static Code Analysis",
    "Dynamic Application Security Testing (DAST)",
    "Software Composition Analysis (SCA)",
    "Continuous Monitoring",
    "Incident Response Planning",
    "Security Training for Teams",
    "Automated Security Testing",
    "Supply Chain Security",
    "Threat Modeling"
]

key_activities = [
    ["Implement Secure Coding Standards", "Conduct Code Reviews", "Integrate Security into Development Workflows"],
    ["Configure SAST Tools", "Analyze Code for Security Issues", "Integrate SAST into Development Pipelines"],
    ["Configure DAST Scans", "Run Regular DAST Scans", "Prioritize and Remediate DAST Findings"],
    ["Inventory Open-Source Components", "Scan for Vulnerabilities and Licensing Issues", "Update or Replace Vulnerable Components"],
    ["Implement Logging and Monitoring Tools", "Configure Alerts for Anomalies", "Regularly Review Monitoring Data"],
    ["Develop Incident Response Plan", "Conduct Regular Drills and Training", "Continuously Update the Plan"],
    ["Develop Role-Specific Training Programs", "Conduct Regular Training Sessions", "Promote a Culture of Security Awareness"],
    ["Integrate Security Tools into CI/CD Pipelines", "Run Automated Tests Regularly", "Review and Address Test Results"],
    ["Assess Third-Party Risks", "Implement Secure Procurement Practices", "Monitor Third-Party Components for Vulnerabilities"],
    ["Identify Threats and Assets", "Analyze and Prioritize Threats", "Mitigate Threats"]
]

# Create a new DataFrame for the reformatted data
formatted_data = []
for practice, activities in zip(practices, key_activities):
    formatted_data.append(practice)
    for activity in activities:
        formatted_data.append(f"- {activity}")

# Create a DataFrame with a single column
formatted_df = pd.DataFrame(formatted_data, columns=["DevSecOps Practices"])

# Save the DataFrame to an Excel file
file_name = "DevSecOps_Key_Activities_With_Threat_Modeling.xlsx"
formatted_df.to_excel(file_name, index=False)

print(f"File generated: {file_name}")



# Define the content of the Markdown file
content = """# DevSecOps Practices

## 1. Threat Modeling
- **Description**: This practice involves identifying potential threats to the application and documenting sensitive data flows, vulnerabilities, and mitigation options. It helps close security gaps and improve security knowledge for the entire team.
- **Integration into the pipeline**: Integrate threat modeling early in the development cycle to identify potential vulnerabilities and mitigate them early.

## 2. Security Testing
- **Description**: Includes manual and automated testing to identify security weaknesses in code and software artifacts. This includes SAST (Static Application Security Testing), DAST (Dynamic Application Security Testing), vulnerability analysis, and penetration testing.
- **Integration into the pipeline**: Automate security testing in the CI/CD pipeline to detect vulnerabilities early in development.

## 3. Analysis and Prioritization
- **Description**: Involves analyzing identified security risks and prioritizing them based on their potential impact and likelihood of exploitation.
- **Integration into the pipeline**: Use analysis tools to evaluate risks and prioritize fixes based on severity.

## 4. Remediation
- **Description**: After identifying and prioritizing vulnerabilities, this step involves fixing them. Continuous testing and penetration testing advice help remediate security weaknesses.
- **Integration into the pipeline**: Integrate continuous remediation processes to address identified vulnerabilities.

## 5. Monitoring
- **Description**: Involves monitoring the overall security posture of the application to identify new vulnerabilities or misconfigurations that may occur in production.
- **Integration into the pipeline**: Use monitoring tools to detect anomalies and adapt the DevSecOps process accordingly.

# BSIMM Practices

## 1. Governance
- **Description**: Includes activities such as security strategy and metrics, compliance, and policies. This involves setting risk-based controls to enable development teams to detect and fix defects earlier in the development cycle.
- **Example**: Use metrics to measure the effectiveness of security initiatives.

## 2. Intelligence
- **Description**: This category includes activities related to collecting and analyzing security information to improve overall security posture. This can include using attack intelligence to anticipate potential threats.
- **Example**: Use intelligence tools to identify potential vulnerabilities before they are exploited.

## 3. SSDL Touchpoints
- **Description**: These practices focus on integrating security into the software development lifecycle. This includes activities like architecture analysis to identify potential vulnerabilities in system design.
- **Example**: Conduct security reviews of features to identify vulnerabilities in design.

## 4. Deployment
- **Description**: Includes activities related to implementing and maintaining security in the production environment. This can include penetration testing to demonstrate existing security weaknesses.
- **Example**: Use external penetration testing to identify vulnerabilities in the production environment.

# Conclusion
By integrating these DevSecOps and BSIMM practices into your process, you can strengthen the security of your applications while improving the efficiency of software development.
"""

# Write the content to a Markdown file
file_name = "DevSecOps_Gap_Analysis_BSIMM.md"
with open(file_name, "w") as file:
    file.write(content)

print(f"File generated: {file_name}")
