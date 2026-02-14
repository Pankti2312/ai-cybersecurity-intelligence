"""
CrewAI Tasks for Cybersecurity Intelligence System
"""
from crewai import Task


def create_threat_analysis_task(agent, threat_focus=""):
    """Create threat analysis task"""
    description = f"""Conduct comprehensive threat intelligence analysis focusing on:
    {threat_focus if threat_focus else "latest cybersecurity threats, malware campaigns, ransomware attacks, and phishing trends"}
    
    Your analysis must include:
    1. Identify top 5-7 current threats
    2. Describe attack methods and TTPs
    3. Assess impact level (Critical/High/Medium/Low)
    4. Identify targeted industries/sectors
    5. Note any attribution to threat actors
    
    Use the Threat Intelligence Search tool to gather real-time data.
    Provide structured, actionable intelligence."""
    
    expected_output = """A structured threat intelligence report containing:
    - List of current threats with names and descriptions
    - Attack methods and techniques used
    - Impact assessment for each threat (Critical/High/Medium/Low)
    - Targeted sectors and potential victims
    - Threat actor attribution (if available)
    - Timeline of recent attacks"""
    
    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent
    )


def create_vulnerability_research_task(agent, cve_focus=""):
    """Create vulnerability research task"""
    description = f"""Research and analyze the latest CVE vulnerabilities:
    {cve_focus if cve_focus else "focusing on critical and high-severity vulnerabilities from the past 30 days"}
    
    Your research must include:
    1. Identify 5-7 critical/high severity CVEs
    2. Extract CVE IDs, CVSS scores, and severity ratings
    3. Identify affected products, vendors, and versions
    4. Determine exploit availability (PoC/active exploitation)
    5. Assess real-world risk and exploitability
    
    Use the CVE Vulnerability Research tool to gather authoritative data.
    Provide detailed vulnerability assessments."""
    
    expected_output = """A comprehensive vulnerability analysis report containing:
    - List of critical CVEs with CVE IDs
    - CVSS scores and severity ratings
    - Affected systems, products, and versions
    - Exploit status (PoC available, actively exploited, etc.)
    - Technical vulnerability details
    - Real-world exploitability assessment"""
    
    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent
    )


def create_incident_response_task(agent, context_tasks):
    """Create incident response advisory task"""
    description = """Based on the identified threats and vulnerabilities, develop comprehensive 
    incident response recommendations:
    
    Your recommendations must include:
    1. Immediate mitigation actions (quick wins)
    2. Patching priorities with timelines
    3. Security controls to implement
    4. Detection and monitoring strategies
    5. Long-term security improvements
    6. Risk-based prioritization
    
    Use the Incident Response Research tool to gather best practices.
    Provide clear, prioritized, actionable recommendations."""
    
    expected_output = """An actionable incident response plan containing:
    - Immediate actions (0-24 hours)
    - Short-term actions (1-7 days)
    - Medium-term actions (1-4 weeks)
    - Patching priorities with CVE IDs
    - Security controls to implement
    - Detection rules and monitoring guidance
    - Risk mitigation strategies
    - Resource requirements"""
    
    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context_tasks
    )


def create_report_writing_task(agent, context_tasks):
    """Create comprehensive report writing task"""
    description = """Synthesize all intelligence into a professional Cybersecurity Threat Intelligence Report.
    
    The report MUST follow this exact structure:
    
    # EXECUTIVE SUMMARY
    - High-level overview of the threat landscape
    - Key findings and critical risks
    - Top recommendations (3-5 bullet points)
    
    # TOP THREATS
    - Detailed analysis of identified threats
    - Impact assessment and risk ratings
    - Attack methods and indicators
    
    # LATEST VULNERABILITIES (CVEs)
    - Critical and high-severity CVEs
    - Affected systems and exploit status
    - CVSS scores and technical details
    
    # RISK ASSESSMENT
    - Overall risk posture evaluation
    - Prioritized risk areas
    - Business impact analysis
    
    # RECOMMENDED ACTIONS
    - Immediate actions (Critical priority)
    - Short-term actions (High priority)
    - Medium-term actions (Medium priority)
    - Patching schedule
    
    # CONCLUSION
    - Summary of key takeaways
    - Strategic recommendations
    - Next steps
    
    Write in clear, professional language suitable for both technical teams and executives.
    Use bullet points, tables, and structured formatting for readability."""
    
    expected_output = """A complete, professionally formatted Cybersecurity Threat Intelligence Report 
    with all sections: Executive Summary, Top Threats, Latest CVEs, Risk Assessment, 
    Recommended Actions, and Conclusion. The report should be comprehensive yet concise, 
    actionable, and suitable for presentation to stakeholders."""
    
    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context_tasks
    )
