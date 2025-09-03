#!/usr/bin/env python3
"""
Enhanced Meta-Orchestrator Test Suite
Tests the integrated Intelligence Engine capabilities
"""

import asyncio
import json
from meta_orchestrator import MetaOrchestrator, ConsultationRequest

async def test_intelligence_enhanced_orchestration():
    """Test Meta-Orchestrator with Intelligence Engine integration"""
    print("🚀 TESTING ENHANCED META-ORCHESTRATOR")
    print("=" * 60)
    
    orchestrator = MetaOrchestrator()
    
    # Test 1: Complex scenario with potential overlaps
    print("\n🔍 TEST 1: OVERLAP DETECTION & OPTIMIZATION")
    request1 = ConsultationRequest(
        objective="Develop comprehensive pricing and sales strategy for premium design consultancy",
        context={
            "consultation_type": "pricing_and_sales_strategy_development",
            "business_context": {
                "service_type": "premium_design_consultancy",
                "client_segment": "enterprise_technology_companies",
                "current_challenge": "pricing_strategy_and_sales_process_optimization",
                "market_position": "established_boutique_agency"
            },
            "strategic_complexity": "high_overlap_potential"
        },
        constraints={
            "methodology_requirements": "must_integrate_multiple_expert_frameworks",
            "delivery_timeline": "comprehensive_strategic_plan_needed"
        },
        success_criteria="Integrated strategy combining Chris Do sales methodology with Becca Luna pricing framework"
    )
    
    result1 = await orchestrator.execute_consultation(request1)
    
    print(f"Status: {result1['status']}")
    print(f"Pattern: {result1['orchestration_pattern']}")
    
    # Display Intelligence Engine insights
    if 'intelligence_assessment' in result1:
        intel = result1['intelligence_assessment']
        print(f"Overlaps Detected: {intel['overlaps_detected']}")
        print(f"Conflicts Analyzed: {intel['conflicts_analyzed']}")
        print(f"Overall Quality: {intel['quality_metrics']['overall_quality']}")
        print(f"Optimization Suggestions: {intel['optimization_suggestions'][0] if intel['optimization_suggestions'] else 'None'}")
    
    # Test 2: Conflict-prone scenario
    print("\n⚡ TEST 2: CONFLICT DETECTION & RESOLUTION")
    request2 = ConsultationRequest(
        objective="Brand identity approach with potential methodology conflicts",
        context={
            "consultation_type": "brand_identity_development",
            "design_approach": "systematic_vs_creative_tension",
            "business_context": {
                "brand_challenge": "balancing_systematic_design_with_creative_expression",
                "target_outcome": "cohesive_brand_identity_system"
            }
        },
        constraints={
            "methodology_considerations": "massimo_vignelli_vs_paula_scher_approaches"
        },
        success_criteria="Resolved brand identity approach with clear methodology justification"
    )
    
    result2 = await orchestrator.execute_consultation(request2)
    
    print(f"Status: {result2['status']}")
    print(f"Pattern: {result2['orchestration_pattern']}")
    
    # Display conflict analysis
    if 'conflict_analysis' in result2:
        conflicts = result2['conflict_analysis']
        print(f"Conflicts Detected: {len(conflicts)}")
        for conflict in conflicts[:2]:
            print(f"  - {conflict['type']} between {conflict['agents']}")
            print(f"    Severity: {conflict['severity']}")
    
    if 'intelligence_assessment' in result2:
        intel = result2['intelligence_assessment']
        print(f"Quality Assessment: {intel['quality_metrics']['overall_quality']}")
    
    # Test 3: Quality optimization scenario
    print("\n📊 TEST 3: QUALITY ASSESSMENT & OPTIMIZATION")
    request3 = ConsultationRequest(
        objective="Website conversion optimization with comprehensive analysis",
        context={
            "consultation_type": "conversion_rate_optimization",
            "optimization_scope": "comprehensive_user_experience_and_conversion_analysis",
            "technical_context": {
                "current_performance": "detailed_analytics_available",
                "optimization_goals": "systematic_improvement_approach"
            }
        },
        success_criteria="Data-driven conversion improvement strategy with quality validation"
    )
    
    result3 = await orchestrator.execute_consultation(request3)
    
    print(f"Status: {result3['status']}")
    print(f"Pattern: {result3['orchestration_pattern']}")
    
    if 'intelligence_assessment' in result3:
        intel = result3['intelligence_assessment']
        quality = intel['quality_metrics']
        print(f"Quality Metrics:")
        print(f"  - Overall Quality: {quality['overall_quality']}")
        print(f"  - Methodology Adherence: {quality['methodology_adherence']}")
        print(f"  - User Value Score: {quality['user_value_score']}")
        print(f"  - Orchestration Efficiency: {quality['orchestration_efficiency']}")
        
        print(f"Optimization Suggestions:")
        for suggestion in intel['optimization_suggestions']:
            print(f"  - {suggestion}")
    
    print("\n" + "=" * 60)
    print("✅ ENHANCED ORCHESTRATOR TESTING COMPLETED")
    print("\nIntelligence Engine Features Demonstrated:")
    print("• Advanced overlap detection and agent optimization")
    print("• Sophisticated conflict analysis and resolution")  
    print("• Comprehensive quality assessment with metrics")
    print("• Intelligent optimization suggestions")
    print("• Enhanced result synthesis with methodology validation")

async def test_methodology_validation():
    """Test methodology validation capabilities"""
    print("\n🧠 METHODOLOGY VALIDATION TEST")
    print("-" * 40)
    
    orchestrator = MetaOrchestrator()
    
    request = ConsultationRequest(
        objective="Apply Chris Do value-based selling methodology to enterprise client engagement",
        context={
            "methodology_focus": "chris_do_value_based_selling",
            "client_type": "enterprise_technology_client",
            "sales_challenge": "demonstrate_roi_and_strategic_value"
        },
        success_criteria="Methodology-compliant sales strategy with validated expert framework application"
    )
    
    result = await orchestrator.execute_consultation(request)
    
    print(f"Consultation Status: {result['status']}")
    
    if 'intelligence_assessment' in result:
        intel = result['intelligence_assessment']
        methodology_score = intel['quality_metrics']['methodology_adherence']
        print(f"Methodology Adherence Score: {methodology_score}")
        
        if methodology_score >= 0.9:
            print("✅ Excellent methodology compliance")
        elif methodology_score >= 0.8:
            print("✅ Good methodology compliance")
        else:
            print("⚠️  Methodology compliance needs improvement")

if __name__ == "__main__":
    async def main():
        await test_intelligence_enhanced_orchestration()
        await test_methodology_validation()
    
    asyncio.run(main())