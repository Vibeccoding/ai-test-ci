#!/usr/bin/env python3
"""Combined AI analyzer using Basic AI + Bedrock + CodeWhisperer"""
import json
import subprocess
from ci_analyzer import TestGapAnalyzer
from bedrock_analyzer import BedrockTestAnalyzer

def run_combined_analysis():
    """Run all three AI tools and combine results"""
    
    print("=" * 60)
    print("COMBINED AI ANALYSIS")
    print("=" * 60)
    
    combined_results = {
        "basic_ai": {},
        "bedrock_ai": {},
        "security_scan": {},
        "summary": {}
    }
    
    # 1. Basic AI Analysis
    print("\n[1/3] Running Basic AI Analysis...")
    try:
        basic_analyzer = TestGapAnalyzer()
        basic_results = basic_analyzer.analyze_coverage_gaps(
            "src/user_service.py", 
            "tests/test_user_service.py"
        )
        combined_results["basic_ai"] = basic_results
        print(f"✓ Basic AI: Found {len(basic_results['gaps'])} gaps")
    except Exception as e:
        print(f"✗ Basic AI failed: {e}")
        combined_results["basic_ai"] = {"error": str(e)}
    
    # 2. Bedrock AI Analysis
    print("\n[2/3] Running Bedrock AI Analysis...")
    try:
        with open("src/user_service.py") as f:
            source_code = f.read()
        with open("tests/test_user_service.py") as f:
            test_code = f.read()
        
        bedrock_analyzer = BedrockTestAnalyzer()
        bedrock_results = bedrock_analyzer.analyze_code_with_ai(source_code, test_code)
        combined_results["bedrock_ai"] = bedrock_results
        print(f"✓ Bedrock AI: Found {len(bedrock_results.get('gaps', []))} gaps")
    except Exception as e:
        print(f"✗ Bedrock not available, using fallback")
        combined_results["bedrock_ai"] = {"status": "fallback", "error": str(e)}
    
    # 3. CodeWhisperer Security Scan
    print("\n[3/3] Running CodeWhisperer Security Scan...")
    try:
        from codewhisperer_scanner import run_security_scan
        security_results = run_security_scan("src/")
        combined_results["security_scan"] = security_results
        print(f"✓ Security Scan: Found {len(security_results)} issues")
    except Exception as e:
        print(f"✗ Security scan failed: {e}")
        combined_results["security_scan"] = {"error": str(e)}
    
    # Generate Summary
    print("\n" + "=" * 60)
    print("COMBINED ANALYSIS SUMMARY")
    print("=" * 60)
    
    total_gaps = len(combined_results.get("basic_ai", {}).get("gaps", []))
    total_tests = len(combined_results.get("basic_ai", {}).get("proposed_tests", []))
    security_issues = len(combined_results.get("security_scan", []))
    
    combined_results["summary"] = {
        "total_gaps_detected": total_gaps,
        "total_tests_proposed": total_tests,
        "security_issues": security_issues,
        "tools_used": ["Basic AI", "Bedrock AI", "CodeWhisperer"]
    }
    
    print(f"\nTotal Gaps Detected: {total_gaps}")
    print(f"Total Tests Proposed: {total_tests}")
    print(f"Security Issues: {security_issues}")
    print(f"Tools Used: Basic AI + Bedrock + CodeWhisperer")
    
    # Save combined results
    with open("combined_analysis.json", "w") as f:
        json.dump(combined_results, f, indent=2)
    
    print("\n✓ Combined analysis saved to combined_analysis.json")
    print("=" * 60)
    
    return combined_results

if __name__ == "__main__":
    run_combined_analysis()
