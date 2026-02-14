"""
CrewAI Agents for Cybersecurity Intelligence System
"""
from crewai import Agent
from langchain_groq import ChatGroq
from tools import ThreatIntelligenceTool, CVEResearchTool, IncidentResponseTool
import os


def create_llm():
    """Create Groq LLM instance"""
    return ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama3-70b-8192",
        temperature=0.3,
        max_tokens=4096
    )


def create_threat_analyst_agent(llm):
    """Create Threat Analyst Agent"""
    return Agent(
        role="Threat Intelligence Analyst",
        goal="Identify and analyze the latest cybersecurity threats including malware, ransomware, phishing campaigns, and APT activities",
        backstory="""You are a senior threat intelligence analyst with 10+ years of experience 
        tracking global cyber threats. You specialize in identifying emerging attack patterns, 
        malware families, and threat actor TTPs. You provide clear, actionable threat assessments 
        with impact ratings.""",
        tools=[ThreatIntelligenceTool()],
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=3
    )


def create_vulnerability_researcher_agent(llm):
    """Create Vulnerability Researcher Agent"""
    return Agent(
        role="Vulnerability Research Specialist",
        goal="Research and analyze the latest CVE vulnerabilities, assess their severity, identify affected systems, and determine exploit availability",
        backstory="""You are an expert vulnerability researcher with deep knowledge of CVE databases, 
        CVSS scoring, and exploit development. You excel at analyzing security advisories, 
        understanding technical vulnerability details, and assessing real-world exploitability. 
        You provide comprehensive vulnerability assessments with clear severity ratings.""",
        tools=[CVEResearchTool()],
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=3
    )


def create_incident_response_advisor_agent(llm):
    """Create Incident Response Advisor Agent"""
    return Agent(
        role="Incident Response Advisor",
        goal="Provide actionable incident response recommendations, mitigation strategies, patching priorities, and security controls for identified threats",
        backstory="""You are a seasoned incident response consultant with extensive experience 
        in handling major security incidents. You specialize in developing mitigation strategies, 
        prioritizing remediation efforts, and implementing security controls. You provide 
        clear, prioritized action plans that balance security needs with operational requirements.""",
        tools=[IncidentResponseTool()],
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=3
    )


def create_report_writer_agent(llm):
    """Create Cybersecurity Report Writer Agent"""
    return Agent(
        role="Cybersecurity Report Writer",
        goal="Synthesize threat intelligence, vulnerability data, and incident response recommendations into comprehensive, executive-ready cybersecurity reports",
        backstory="""You are a professional cybersecurity report writer with expertise in 
        translating technical security findings into clear, actionable reports for both 
        technical and executive audiences. You excel at creating structured reports with 
        executive summaries, risk assessments, and prioritized recommendations. Your reports 
        are known for clarity, accuracy, and actionable insights.""",
        tools=[],
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=2
    )
