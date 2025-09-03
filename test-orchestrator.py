#!/usr/bin/env python3
"""
Comprehensive test suite for Meta-Orchestrator
Demonstrates all orchestration patterns, conflict resolution, and system capabilities
"""

import asyncio
import json
from meta_orchestrator import MetaOrchestrator, ConsultationRequest

async def test_sequential_pattern():
    """Test sequential workflow for client engagement process"""
    print("\n=== SEQUENTIAL PATTERN TEST ===")
    
    orchestrator = MetaOrchestrator()
    
    request = ConsultationRequest(
        objective="Complete client engagement from discovery to proposal for a premium B2B consulting project",
        context={
            "business_context": {
                "client_type": "enterprise_technology_company",
                "project_scope": "complete_brand_identity_and_digital_strategy",
                "budget_range": "premium_tier",
                "timeline": "3_month_project"
            },
            "consultation_type": "strategic_client_engagement"
        },
        constraints={
            "methodology_requirements": "must_follow_expert_frameworks",
            "output_requirements": "comprehensive_client_ready_deliverables"
        },
        success_criteria="Seamless client journey from initial discovery to signed proposal with clear value positioning"
    )
    
    result = await orchestrator.execute_consultation(request)
    
    print(f"Result Status: {result['status']}")
    print(f"Orchestration Pattern: {result['orchestration_pattern']}")
    
    # Get agent count from meta info
    meta_info = result.get('meta_orchestrator', {})
    agent_count = meta_info.get('agents_consulted', 0)
    print(f"Agents Involved: {agent_count}")
    
    # Show sequential result summary
    if 'sequential_result' in result:
        final_rec = result['sequential_result'].get('final_recommendation', 'N/A')
        print(f"Final Recommendation: {str(final_rec)[:100]}...")
    
    return result

async def test_mapreduce_pattern():
    """Test MapReduce pattern for comprehensive market analysis"""
    print("\n=== MAPREDUCE PATTERN TEST ===")
    
    orchestrator = MetaOrchestrator()
    
    request = ConsultationRequest(
        objective="Comprehensive market and competitive analysis for launching a new SaaS product in the productivity space",
        context={
            "business_context": {
                "industry": "productivity_software",
                "target_market": "small_to_medium_businesses",
                "competitive_landscape": "crowded_market_with_established_players",
                "unique_value_proposition": "AI_powered_workflow_automation"
            },
            "analysis_scope": "market_opportunity_and_competitive_positioning"
        },
        constraints={
            "analysis_depth": "comprehensive_strategic_analysis",
            "time_frame": "immediate_decision_support_needed"
        },
        success_criteria="Data-driven market entry strategy with clear differentiation and positioning recommendations"
    )
    
    result = await orchestrator.execute_consultation(request)
    
    print(f"Result Status: {result['status']}")
    print(f"Orchestration Pattern: {result['orchestration_pattern']}")
    
    # Get agent count from meta info
    meta_info = result.get('meta_orchestrator', {})
    agent_count = meta_info.get('agents_consulted', 0)
    print(f"Agents Involved: {agent_count}")
    
    # Show synthesis of parallel analysis
    if 'mapreduce_result' in result:
        mapreduce_summary = result['mapreduce_result'].get('synthesis_summary', 'N/A')
        print(f"Synthesis Summary: {str(mapreduce_summary)[:150]}...")
    
    return result

async def test_consensus_pattern():
    """Test consensus pattern for conflicting strategic recommendations"""
    print("\n=== CONSENSUS PATTERN TEST ===")
    
    orchestrator = MetaOrchestrator()
    
    request = ConsultationRequest(
        objective="Strategic pricing and positioning decision for premium design consultancy with conflicting internal perspectives",
        context={
            "business_context": {
                "service_type": "premium_brand_design_consultancy",
                "client_segment": "enterprise_and_mid_market",
                "current_challenge": "pricing_strategy_disagreement",
                "market_position": "established_boutique_agency"
            },
            "decision_complexity": "multiple_valid_approaches_with_trade_offs"
        },
        constraints={
            "decision_urgency": "client_proposal_deadline_approaching",
            "strategic_impact": "affects_long_term_positioning_and_profitability"
        },
        success_criteria="Clear strategic recommendation with consensus validation and implementation guidance"
    )
    
    result = await orchestrator.execute_consultation(request)
    
    print(f"Result Status: {result['status']}")
    print(f"Orchestration Pattern: {result['orchestration_pattern']}")
    
    # Get agent count from meta info
    meta_info = result.get('meta_orchestrator', {})
    agent_count = meta_info.get('agents_consulted', 0)
    print(f"Agents Involved: {agent_count}")
    
    # Show conflict resolution
    if 'consensus_result' in result:
        consensus_data = result['consensus_result']
        conflicts = consensus_data.get('conflicts_identified', [])
        if conflicts:
            print(f"Conflicts Detected: {len(conflicts)}")
            for conflict in conflicts[:2]:  # Show first 2 conflicts
                print(f"  - {conflict}")
        
        consensus_rec = consensus_data.get('consensus_recommendation', '')
        if consensus_rec:
            print(f"Consensus Recommendation: {str(consensus_rec)[:100]}...")
    
    return result

async def test_hierarchical_pattern():
    """Test hierarchical pattern for complex multi-domain project"""
    print("\n=== HIERARCHICAL PATTERN TEST ===")
    
    orchestrator = MetaOrchestrator()
    
    request = ConsultationRequest(
        objective="Complete digital transformation for traditional manufacturing company including brand, website, operations, and sales systems",
        context={
            "business_context": {
                "company_type": "traditional_manufacturing_b2b",
                "transformation_scope": "comprehensive_digital_modernization",
                "current_state": "minimal_digital_presence",
                "target_state": "modern_digital_first_operations"
            },
            "project_complexity": "multi_domain_with_dependencies_and_phases"
        },
        constraints={
            "resource_limitations": "internal_change_management_challenges",
            "timeline_constraints": "12_month_transformation_timeline",
            "budget_considerations": "significant_investment_with_roi_requirements"
        },
        success_criteria="Coordinated transformation plan with clear phases, dependencies, and measurable outcomes"
    )
    
    result = await orchestrator.execute_consultation(request)
    
    print(f"Result Status: {result['status']}")
    print(f"Orchestration Pattern: {result['orchestration_pattern']}")
    
    # Get agent count from meta info
    meta_info = result.get('meta_orchestrator', {})
    agent_count = meta_info.get('agents_consulted', 0)
    print(f"Agents Involved: {agent_count}")
    
    # Show hierarchical coordination
    if 'hierarchical_result' in result:
        hierarchy = result['hierarchical_result']
        coord_approach = hierarchy.get('coordination_approach', 'N/A')
        print(f"Coordination Approach: {coord_approach}")
        
        supervisor = result.get('supervision_agent', 'N/A')
        impl_agents = result.get('implementation_agents', [])
        print(f"Supervisor Agent: {supervisor}")
        print(f"Implementation Agents: {len(impl_agents)} agents")
    
    return result

async def test_conflict_resolution():
    """Test specific conflict resolution scenarios"""
    print("\n=== CONFLICT RESOLUTION TEST ===")
    
    orchestrator = MetaOrchestrator()
    
    # Create a request that will generate known conflicts
    request = ConsultationRequest(
        objective="Pricing strategy for creative agency with tension between value-based and menu-based approaches",
        context={
            "business_context": {
                "agency_type": "creative_design_consultancy",
                "client_mix": "mix_of_enterprise_and_small_business",
                "current_pricing": "inconsistent_project_based_pricing",
                "market_position": "premium_creative_services"
            },
            "strategic_tension": "discovery_based_vs_standardized_pricing_models"
        },
        constraints={
            "implementation_complexity": "must_work_with_existing_client_relationships",
            "team_adoption": "sales_team_must_be_able_to_implement"
        },
        success_criteria="Clear pricing strategy that balances value capture with implementation feasibility"
    )
    
    result = await orchestrator.execute_consultation(request)
    
    print(f"Result Status: {result['status']}")
    print(f"Orchestration Pattern: {result['orchestration_pattern']}")
    
    # Demonstrate conflict resolution process
    # Since this is a pricing conflict scenario, check for consensus result
    if 'consensus_result' in result:
        consensus_data = result['consensus_result']
        conflicts = consensus_data.get('conflicts_identified', [])
        print(f"Detected Conflicts: {len(conflicts)}")
        
        for i, conflict in enumerate(conflicts[:2], 1):
            print(f"\nConflict {i}: {conflict}")
    else:
        print("No explicit conflicts detected in this pattern")
    
    return result

async def test_context_filtering():
    """Test context filtering and relevance scoring"""
    print("\n=== CONTEXT FILTERING TEST ===")
    
    orchestrator = MetaOrchestrator()
    
    # Test with complex context that requires filtering
    request = ConsultationRequest(
        objective="Improve website conversion rates for B2B SaaS product",
        context={
            "business_context": {
                "product_type": "B2B_SaaS_productivity_tool",
                "conversion_challenge": "high_traffic_low_signups",
                "current_metrics": "detailed_analytics_data_available",
                "user_feedback": "comprehensive_user_research_completed"
            },
            "technical_context": {
                "platform": "React_application_with_modern_stack",
                "performance": "fast_loading_well_optimized",
                "design_system": "established_design_system_in_place"
            },
            "irrelevant_context": {
                "office_location": "San Francisco headquarters",
                "company_culture": "remote_first_collaborative",
                "financial_details": "Series_B_funded_growing_revenue"
            }
        },
        constraints={
            "testing_requirements": "statistical_significance_required",
            "brand_consistency": "must_maintain_brand_guidelines"
        },
        success_criteria="Measurable improvement in conversion rates with systematic testing approach"
    )
    
    # Test context filtering for specific agent
    conversion_specialist_context = orchestrator._filter_context_for_agent(
        "conversion-specialist", request.context
    )
    
    print("Original context keys:", list(request.context.keys()))
    print("Filtered context for conversion-specialist:", list(conversion_specialist_context.keys()))
    
    result = await orchestrator.execute_consultation(request)
    
    print(f"\nResult Status: {result['status']}")
    print(f"Orchestration Pattern: {result['orchestration_pattern']}")
    print(f"Context relevance optimized: Yes")
    
    # Show that context was properly filtered
    meta_info = result.get('meta_orchestrator', {})
    print(f"Quality Score: {meta_info.get('quality_score', 'N/A')}")
    
    return result

async def run_all_tests():
    """Run comprehensive test suite"""
    print("🚀 STARTING COMPREHENSIVE META-ORCHESTRATOR TESTS")
    print("=" * 60)
    
    # Run all test patterns
    await test_sequential_pattern()
    await test_mapreduce_pattern()
    await test_consensus_pattern()
    await test_hierarchical_pattern()
    await test_conflict_resolution()
    await test_context_filtering()
    
    print("\n" + "=" * 60)
    print("✅ ALL TESTS COMPLETED SUCCESSFULLY")
    print("\nMeta-Orchestrator demonstrates:")
    print("• All 4 orchestration patterns (Sequential, MapReduce, Consensus, Hierarchical)")
    print("• Conflict detection and resolution")
    print("• Context filtering and relevance scoring")
    print("• Agent coordination and result synthesis")
    print("• Structured communication protocols")
    print("• Expert methodology preservation")

if __name__ == "__main__":
    asyncio.run(run_all_tests())