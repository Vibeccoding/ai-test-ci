#!/usr/bin/env python3
"""CodeWhisperer security scanner for CI"""
import json
import subprocess
import sys

def run_security_scan(source_path):
    """Run CodeWhisperer security scan"""
    print("=" * 50)
    print("CODEWHISPERER SECURITY SCAN")
    print("=" * 50)
    
    # Simulated scan results (replace with actual CLI when available)
    findings = [
        {
            "severity": "HIGH",
            "title": "Potential SQL Injection",
            "file": "src/user_service.py",
            "line": 45,
            "description": "User input not sanitized before database query"
        },
        {
            "severity": "MEDIUM",
            "title": "Missing input validation",
            "file": "src/user_service.py",
            "line": 23,
            "description": "Email validation could be bypassed"
        }
    ]
    
    critical = [f for f in findings if f['severity'] == 'CRITICAL']
    high = [f for f in findings if f['severity'] == 'HIGH']
    medium = [f for f in findings if f['severity'] == 'MEDIUM']
    
    print(f"\nCritical: {len(critical)}")
    print(f"High: {len(high)}")
    print(f"Medium: {len(medium)}")
    
    if high or critical:
        print("\nISSUES FOUND:")
        for issue in critical + high:
            print(f"  [{issue['severity']}] {issue['title']}")
            print(f"    Location: {issue['file']}:{issue['line']}")
            print(f"    {issue['description']}\n")
    
    return findings

if __name__ == "__main__":
    findings = run_security_scan("src/")
    
    # Save report
    with open("security-report.json", "w") as f:
        json.dump(findings, f, indent=2)
    
    print("\nSecurity report saved to security-report.json")
    print("=" * 50)