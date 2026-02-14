"""
Custom tools for cybersecurity intelligence gathering using EXA API
"""
import os
from typing import List, Dict
from exa_py import Exa
from crewai_tools import BaseTool
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ThreatIntelligenceTool(BaseTool):
    name: str = "Threat Intelligence Search"
    description: str = "Search for latest cybersecurity threats, malware campaigns, ransomware attacks, and phishing trends using real-time intelligence sources."
    
    def _run(self, query: str) -> str:
        """Execute threat intelligence search"""
        try:
            exa = Exa(api_key=os.getenv("EXA_API_KEY"))
            
            # Search for threat intelligence
            results = exa.search_and_contents(
                query=f"cybersecurity {query} latest threats malware ransomware",
                type="neural",
                num_results=5,
                text=True,
                highlights=True
            )
            
            # Format results
            formatted_results = []
            for result in results.results:
                formatted_results.append({
                    "title": result.title,
                    "url": result.url,
                    "summary": result.text[:500] if result.text else "No summary available",
                    "highlights": result.highlights[:3] if hasattr(result, 'highlights') and result.highlights else []
                })
            
            output = f"Found {len(formatted_results)} threat intelligence sources:\n\n"
            for idx, item in enumerate(formatted_results, 1):
                output += f"{idx}. {item['title']}\n"
                output += f"   URL: {item['url']}\n"
                output += f"   Summary: {item['summary']}\n"
                if item['highlights']:
                    output += f"   Key Points: {'; '.join(item['highlights'])}\n"
                output += "\n"
            
            return output
            
        except Exception as e:
            logger.error(f"Error in ThreatIntelligenceTool: {str(e)}")
            return f"Error fetching threat intelligence: {str(e)}"


class CVEResearchTool(BaseTool):
    name: str = "CVE Vulnerability Research"
    description: str = "Search for latest CVE vulnerabilities, security advisories, and exploit information from authoritative sources."
    
    def _run(self, query: str = "latest CVE vulnerabilities") -> str:
        """Execute CVE research"""
        try:
            exa = Exa(api_key=os.getenv("EXA_API_KEY"))
            
            # Search for CVE information
            results = exa.search_and_contents(
                query=f"CVE vulnerability {query} security advisory CVSS score",
                type="neural",
                num_results=5,
                text=True,
                highlights=True
            )
            
            # Format results
            formatted_results = []
            for result in results.results:
                formatted_results.append({
                    "title": result.title,
                    "url": result.url,
                    "content": result.text[:600] if result.text else "No content available",
                    "highlights": result.highlights[:3] if hasattr(result, 'highlights') and result.highlights else []
                })
            
            output = f"Found {len(formatted_results)} CVE vulnerability sources:\n\n"
            for idx, item in enumerate(formatted_results, 1):
                output += f"{idx}. {item['title']}\n"
                output += f"   URL: {item['url']}\n"
                output += f"   Details: {item['content']}\n"
                if item['highlights']:
                    output += f"   Key Findings: {'; '.join(item['highlights'])}\n"
                output += "\n"
            
            return output
            
        except Exception as e:
            logger.error(f"Error in CVEResearchTool: {str(e)}")
            return f"Error fetching CVE data: {str(e)}"


class IncidentResponseTool(BaseTool):
    name: str = "Incident Response Research"
    description: str = "Search for incident response best practices, mitigation strategies, and security controls for specific threats."
    
    def _run(self, threat_context: str) -> str:
        """Execute incident response research"""
        try:
            exa = Exa(api_key=os.getenv("EXA_API_KEY"))
            
            # Search for incident response guidance
            results = exa.search_and_contents(
                query=f"incident response mitigation {threat_context} security controls remediation best practices",
                type="neural",
                num_results=4,
                text=True,
                highlights=True
            )
            
            # Format results
            formatted_results = []
            for result in results.results:
                formatted_results.append({
                    "title": result.title,
                    "url": result.url,
                    "guidance": result.text[:500] if result.text else "No guidance available",
                    "highlights": result.highlights[:3] if hasattr(result, 'highlights') and result.highlights else []
                })
            
            output = f"Found {len(formatted_results)} incident response resources:\n\n"
            for idx, item in enumerate(formatted_results, 1):
                output += f"{idx}. {item['title']}\n"
                output += f"   URL: {item['url']}\n"
                output += f"   Guidance: {item['guidance']}\n"
                if item['highlights']:
                    output += f"   Key Actions: {'; '.join(item['highlights'])}\n"
                output += "\n"
            
            return output
            
        except Exception as e:
            logger.error(f"Error in IncidentResponseTool: {str(e)}")
            return f"Error fetching incident response data: {str(e)}"
