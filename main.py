"""
AI Cybersecurity Intelligence System - Main Application
"""
import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import (
    create_llm, create_threat_analyst_agent, create_vulnerability_researcher_agent,
    create_incident_response_advisor_agent, create_report_writer_agent
)
from tasks import (
    create_threat_analysis_task, create_vulnerability_research_task,
    create_incident_response_task, create_report_writing_task
)

# Load environment variables
load_dotenv()

def main():
    """Main function to run the cybersecurity intelligence crew"""
    
    # Verify API keys
    if not os.getenv("GROQ_API_KEY"):
        print("❌ GROQ_API_KEY not found in environment variables")
        return
    
    if not os.getenv("EXA_API_KEY"):
        print("❌ EXA_API_KEY not found in environment variables")
        return
    
    print("🚀 Starting AI Cybersecurity Intelligence System...")
    
    # Create LLM
    llm = create_llm()
    
    # Create agents
    threat_analyst = create_threat_analyst_agent(llm)
    vulnerability_researcher = create_vulnerability_researcher_agent(llm)
    incident_advisor = create_incident_response_advisor_agent(llm)
    report_writer = create_report_writer_agent(llm)
    
    # Create tasks
    threat_task = create_threat_analysis_task(threat_analyst)
    vuln_task = create_vulnerability_research_task(vulnerability_researcher)
    incident_task = create_incident_response_task(incident_advisor, [threat_task, vuln_task])
    report_task = create_report_writing_task(report_writer, [threat_task, vuln_task, incident_task])
    
    # Create crew
    crew = Crew(
        agents=[threat_analyst, vulnerability_researcher, incident_advisor, report_writer],
        tasks=[threat_task, vuln_task, incident_task, report_task],
        process=Process.sequential,
        verbose=True
    )
    
    # Execute the crew
    print("🔍 Executing cybersecurity intelligence analysis...")
    result = crew.kickoff()
    
    # Save report
    with open("cybersecurity_report.md", "w", encoding="utf-8") as f:
        f.write(result)
    
    print("✅ Analysis complete! Report saved as 'cybersecurity_report.md'")
    print(f"📄 Report preview:\n{result[:500]}...")

if __name__ == "__main__":
    main()