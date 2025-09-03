#!/usr/bin/env python3
"""
Meta-Orchestrator for Enhanced Agent System

Implements the "Primary Agent" pattern from agentic AI best practices:
- Maintains conversation context and user state
- Handles task planning and decomposition  
- Manages subagent coordination and results synthesis
- Implements error handling and fallback strategies

Following the article's two-tier architecture exactly.
"""

import json
import yaml
import asyncio
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
import logging
from intelligence_engine import IntelligenceEngine, QualityMetrics, ConflictAnalysis, AgentOverlap
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OrchestrationPattern(Enum):
    """Orchestration patterns from the article"""
    SEQUENTIAL = "sequential"
    MAPREDUCE = "mapreduce" 
    CONSENSUS = "consensus"
    HIERARCHICAL = "hierarchical"

class TaskStatus(Enum):
    """Task execution status"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    PARTIAL = "partial"

@dataclass
class ConsultationRequest:
    """Structured consultation request following article's communication protocol"""
    objective: str
    context: Dict[str, Any] = field(default_factory=dict)
    constraints: Dict[str, Any] = field(default_factory=dict)
    output_format: str = "consultation"
    success_criteria: str = ""
    
    def to_yaml(self) -> str:
        """Convert to YAML format as specified in article"""
        data = {
            "consultation_request": {
                "objective": self.objective,
                "context": self.context,
                "constraints": self.constraints,
                "output_format": self.output_format,
                "success_criteria": self.success_criteria
            }
        }
        return yaml.dump(data, default_flow_style=False)

@dataclass
class AgentResponse:
    """Structured agent response following article's protocol"""
    status: str
    result: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    recommendations: Dict[str, Any] = field(default_factory=dict)
    scope_boundaries: Dict[str, Any] = field(default_factory=dict)
    potential_conflicts: Dict[str, Any] = field(default_factory=dict)
    errors: str = ""
    
    @classmethod
    def from_yaml(cls, yaml_str: str) -> 'AgentResponse':
        """Parse agent response from YAML"""
        data = yaml.safe_load(yaml_str)
        response_data = data.get('response', {})
        return cls(
            status=response_data.get('status', 'failed'),
            result=response_data.get('result', {}),
            metadata=response_data.get('metadata', {}),
            recommendations=response_data.get('recommendations', {}),
            scope_boundaries=response_data.get('scope_boundaries', {}),
            potential_conflicts=response_data.get('potential_conflicts', {}),
            errors=response_data.get('errors', '')
        )

class MetaOrchestrator:
    """
    Primary Agent implementing the article's orchestrator pattern
    
    Core responsibilities:
    - Task analysis and decomposition (vertical/horizontal)
    - Agent coordination and routing
    - Context management and filtering
    - Result synthesis and conflict resolution
    - Error handling and fallback strategies
    """
    
    def __init__(self, agents_directory: str = "agents"):
        self.agents_directory = Path(agents_directory)
        self.agents_registry = {}
        self.conversation_context = {}
        self.active_tasks = {}
        self.load_agent_registry()
        
        # Initialize Intelligence Engine for advanced capabilities
        try:
            self.intelligence_engine = IntelligenceEngine()
            logger.info("Intelligence Engine integrated successfully")
        except Exception as e:
            logger.warning(f"Intelligence Engine initialization failed: {e}")
            self.intelligence_engine = None
        
        logger.info(f"Meta-Orchestrator initialized with {len(self.agents_registry)} agents")
    
    def load_agent_registry(self):
        """Load enhanced agent specifications from registry"""
        registry_path = Path("enhanced-agent-registry.json")
        if registry_path.exists():
            with open(registry_path, 'r') as f:
                registry_data = json.load(f)
                self.agents_registry = registry_data
        
        # Load individual agent specs
        self.agent_specs = {}
        for agent_file in self.agents_directory.glob("enhanced-*.json"):
            with open(agent_file, 'r') as f:
                agent_data = json.load(f)
                agent_name = agent_data['agent_identity']['name']
                self.agent_specs[agent_name] = agent_data
    
    def analyze_consultation_request(self, request: ConsultationRequest) -> Dict[str, Any]:
        """
        Analyze consultation request to determine orchestration approach
        
        Following article's task decomposition strategies:
        - Vertical Decomposition: Sequential multi-step tasks
        - Horizontal Decomposition: Parallel tasks with aggregation
        """
        analysis = {
            "complexity": self._assess_complexity(request),
            "domains": self._identify_domains(request),
            "agent_candidates": self._identify_candidate_agents(request),
            "orchestration_pattern": self._select_orchestration_pattern(request),
            "decomposition_strategy": self._plan_task_decomposition(request)
        }
        
        logger.info(f"Request analysis: {analysis['orchestration_pattern'].value} pattern with {len(analysis['agent_candidates'])} agents")
        return analysis
    
    def _assess_complexity(self, request: ConsultationRequest) -> str:
        """Assess consultation complexity to inform orchestration approach"""
        objective = request.objective.lower()
        context_size = len(str(request.context))
        
        # Multiple domain indicators
        domain_keywords = [
            "brand", "design", "marketing", "sales", "pricing", "strategy", 
            "website", "technical", "user", "content", "social", "email"
        ]
        domain_count = sum(1 for keyword in domain_keywords if keyword in objective)
        
        if domain_count >= 3 or context_size > 1000:
            return "complex"
        elif domain_count >= 2 or context_size > 500:
            return "moderate"
        else:
            return "simple"
    
    def _identify_domains(self, request: ConsultationRequest) -> List[str]:
        """Identify which agent domains are relevant to the request"""
        objective = request.objective.lower()
        context_text = str(request.context).lower()
        full_text = f"{objective} {context_text}"
        
        domains = []
        
        # Business Strategy & Sales
        if any(word in full_text for word in ["pricing", "sales", "proposal", "client", "business"]):
            domains.append("business_strategy_sales")
            
        # Design & Visual  
        if any(word in full_text for word in ["design", "visual", "brand", "logo", "website", "ui", "ux"]):
            domains.append("design_visual")
            
        # Technical & Architecture
        if any(word in full_text for word in ["technical", "performance", "seo", "accessibility", "responsive"]):
            domains.append("technical_architecture")
            
        # Content & Communication
        if any(word in full_text for word in ["content", "copy", "marketing", "social", "email"]):
            domains.append("content_communication")
            
        # Analysis & Operations
        if any(word in full_text for word in ["research", "analysis", "operations", "project", "conversion"]):
            domains.append("analysis_operations")
        
        return domains if domains else ["business_strategy_sales"]  # Default fallback
    
    def _identify_candidate_agents(self, request: ConsultationRequest) -> List[str]:
        """Identify specific agents that could handle this request"""
        objective = request.objective.lower()
        context_text = str(request.context).lower()
        full_text = f"{objective} {context_text}"
        
        candidates = []
        
        # Check each agent's usage triggers
        for agent_name, agent_spec in self.agent_specs.items():
            usage_triggers = agent_spec.get('usage_triggers', [])
            
            # Check if any trigger keywords match the request
            for trigger in usage_triggers:
                trigger_words = trigger.lower().split()
                if any(word in full_text for word in trigger_words if len(word) > 3):
                    candidates.append(agent_name)
                    break
        
        return candidates if candidates else ["sales-specialist"]  # Fallback
    
    def _select_orchestration_pattern(self, request: ConsultationRequest) -> OrchestrationPattern:
        """Select appropriate orchestration pattern based on request analysis"""
        complexity = self._assess_complexity(request)
        domain_count = len(self._identify_domains(request))
        candidate_count = len(self._identify_candidate_agents(request))
        
        # Pattern selection logic from article
        if "compare" in request.objective.lower() or "validate" in request.objective.lower():
            return OrchestrationPattern.CONSENSUS
        elif candidate_count > 3 and domain_count > 2:
            return OrchestrationPattern.MAPREDUCE
        elif complexity == "complex" and domain_count > 1:
            return OrchestrationPattern.SEQUENTIAL
        else:
            return OrchestrationPattern.SEQUENTIAL  # Default for single agent or simple cases
    
    def _plan_task_decomposition(self, request: ConsultationRequest) -> Dict[str, Any]:
        """Plan how to decompose the task based on article's strategies"""
        pattern = self._select_orchestration_pattern(request)
        candidates = self._identify_candidate_agents(request)
        
        if pattern == OrchestrationPattern.SEQUENTIAL:
            # Vertical decomposition - sequential steps
            return {
                "type": "vertical",
                "steps": [{"agent": agent, "depends_on": candidates[i-1] if i > 0 else None} 
                         for i, agent in enumerate(candidates[:3])]  # Limit to 3 for efficiency
            }
        
        elif pattern == OrchestrationPattern.MAPREDUCE:
            # Horizontal decomposition - parallel with aggregation
            return {
                "type": "horizontal", 
                "parallel_agents": candidates[:4],  # Limit to 4 for efficiency
                "aggregation": "synthesis"
            }
        
        elif pattern == OrchestrationPattern.CONSENSUS:
            # Multiple agents for validation
            return {
                "type": "consensus",
                "agents": candidates[:3],  # 3 agents for consensus
                "resolution": "user_choice"
            }
        
        else:
            # Hierarchical - rarely used as per article
            return {
                "type": "hierarchical",
                "supervisor": candidates[0] if candidates else "sales-specialist",
                "workers": candidates[1:3]
            }
    
    async def execute_consultation(self, request: ConsultationRequest) -> Dict[str, Any]:
        """
        Execute consultation following article's orchestration patterns
        Enhanced with Intelligence Engine capabilities
        
        Main orchestration logic implementing the primary agent responsibilities
        """
        logger.info(f"Executing consultation: {request.objective}")
        
        # Step 1: Enhanced analysis with overlap detection
        analysis = self.analyze_consultation_request(request)
        
        # Step 1.5: Intelligence Engine - Detect agent overlaps
        overlaps = []
        if self.intelligence_engine:
            try:
                overlaps = await self.intelligence_engine.analyze_agent_overlap(request.context)
                if overlaps:
                    logger.info(f"Intelligence Engine detected {len(overlaps)} agent overlaps")
                    # Optimize agent selection based on overlaps
                    analysis = self._optimize_agent_selection(analysis, overlaps)
            except Exception as e:
                logger.warning(f"Overlap detection failed: {e}")
        
        # Step 2: Execute based on orchestration pattern
        if analysis["orchestration_pattern"] == OrchestrationPattern.SEQUENTIAL:
            result = await self._execute_sequential(request, analysis)
        elif analysis["orchestration_pattern"] == OrchestrationPattern.MAPREDUCE:
            result = await self._execute_mapreduce(request, analysis)
        elif analysis["orchestration_pattern"] == OrchestrationPattern.CONSENSUS:
            result = await self._execute_consensus(request, analysis)
        else:
            result = await self._execute_hierarchical(request, analysis)
        
        # Step 2.5: Intelligence Engine - Advanced conflict analysis
        conflicts = []
        if self.intelligence_engine and result.get("results"):
            try:
                conflicts = await self.intelligence_engine.analyze_conflicts(result["results"])
                if conflicts:
                    logger.info(f"Intelligence Engine detected {len(conflicts)} conflicts")
                    # Enhance result with conflict analysis
                    result["conflict_analysis"] = [
                        {
                            "conflict_id": c.conflict_id,
                            "agents": c.agents_involved,
                            "type": c.conflict_type.value,
                            "severity": c.severity.value,
                            "recommended_resolution": c.recommended_resolution
                        } for c in conflicts
                    ]
            except Exception as e:
                logger.warning(f"Conflict analysis failed: {e}")
        
        # Step 3: Enhanced synthesis with quality assessment
        final_result = await self._synthesize_results(result, analysis)
        
        # Step 4: Intelligence Engine - Quality assessment
        if self.intelligence_engine:
            try:
                quality_metrics = await self.intelligence_engine.assess_quality(final_result)
                final_result["intelligence_assessment"] = {
                    "overlaps_detected": len(overlaps),
                    "conflicts_analyzed": len(conflicts),
                    "quality_metrics": {
                        "overall_quality": round(quality_metrics.overall_quality, 3),
                        "methodology_adherence": round(quality_metrics.methodology_adherence, 3),
                        "user_value_score": round(quality_metrics.user_value_score, 3),
                        "orchestration_efficiency": round(quality_metrics.orchestration_efficiency, 3)
                    },
                    "optimization_suggestions": self._generate_optimization_suggestions(quality_metrics)
                }
            except Exception as e:
                logger.warning(f"Quality assessment failed: {e}")
        
        logger.info(f"Consultation completed with status: {final_result.get('status', 'unknown')}")
        return final_result
    
    async def _execute_sequential(self, request: ConsultationRequest, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Execute sequential pipeline pattern from article"""
        logger.info("Executing sequential pipeline pattern")
        
        steps = analysis["decomposition_strategy"]["steps"]
        results = []
        context = request.context.copy()
        
        for step in steps:
            agent_name = step["agent"]
            logger.info(f"Consulting {agent_name}")
            
            # Create agent-specific request with filtered context
            agent_request = ConsultationRequest(
                objective=request.objective,
                context=self._filter_context_for_agent(context, agent_name),
                constraints=request.constraints,
                output_format=request.output_format,
                success_criteria=request.success_criteria
            )
            
            # Simulate agent consultation (in real implementation, this would call actual agent)
            agent_response = await self._consult_agent(agent_name, agent_request)
            results.append({
                "agent": agent_name,
                "response": agent_response
            })
            
            # Add agent result to context for next agent
            if agent_response.status in ["success", "partial"]:
                context.update(agent_response.result)
        
        return {
            "pattern": "sequential",
            "results": results,
            "final_context": context
        }
    
    async def _execute_mapreduce(self, request: ConsultationRequest, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Execute MapReduce parallel pattern from article"""
        logger.info("Executing MapReduce parallel pattern")
        
        parallel_agents = analysis["decomposition_strategy"]["parallel_agents"]
        
        # Map phase - parallel agent consultation
        tasks = []
        for agent_name in parallel_agents:
            agent_request = ConsultationRequest(
                objective=request.objective,
                context=self._filter_context_for_agent(request.context, agent_name),
                constraints=request.constraints,
                output_format=request.output_format,
                success_criteria=request.success_criteria
            )
            tasks.append(self._consult_agent(agent_name, agent_request))
        
        # Execute parallel consultations
        agent_responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Reduce phase - aggregate results
        results = []
        for i, response in enumerate(agent_responses):
            if not isinstance(response, Exception):
                results.append({
                    "agent": parallel_agents[i],
                    "response": response
                })
            else:
                logger.error(f"Agent {parallel_agents[i]} failed: {response}")
        
        return {
            "pattern": "mapreduce",
            "results": results,
            "aggregation": "parallel_synthesis"
        }
    
    async def _execute_consensus(self, request: ConsultationRequest, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Execute consensus pattern from article"""
        logger.info("Executing consensus pattern")
        
        consensus_agents = analysis["decomposition_strategy"]["agents"]
        
        # Get responses from all consensus agents
        tasks = []
        for agent_name in consensus_agents:
            agent_request = ConsultationRequest(
                objective=request.objective,
                context=self._filter_context_for_agent(request.context, agent_name),
                constraints=request.constraints,
                output_format=request.output_format,
                success_criteria=request.success_criteria
            )
            tasks.append(self._consult_agent(agent_name, agent_request))
        
        agent_responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Analyze for consensus and conflicts
        valid_responses = []
        for i, response in enumerate(agent_responses):
            if not isinstance(response, Exception):
                valid_responses.append({
                    "agent": consensus_agents[i],
                    "response": response
                })
        
        # Detect conflicts between agents
        conflicts = self._detect_conflicts(valid_responses)
        
        return {
            "pattern": "consensus",
            "results": valid_responses,
            "conflicts": conflicts,
            "resolution": "user_choice" if conflicts else "consensus_reached"
        }
    
    async def _execute_hierarchical(self, request: ConsultationRequest, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Execute hierarchical delegation pattern (limited use as per article)"""
        logger.info("Executing hierarchical pattern")
        
        supervisor = analysis["decomposition_strategy"]["supervisor"]
        workers = analysis["decomposition_strategy"]["workers"]
        
        # First consult supervisor for high-level guidance
        supervisor_request = ConsultationRequest(
            objective=f"Provide high-level guidance for: {request.objective}",
            context=request.context,
            constraints=request.constraints,
            output_format="strategic_guidance",
            success_criteria=request.success_criteria
        )
        
        supervisor_response = await self._consult_agent(supervisor, supervisor_request)
        
        # Then consult workers for detailed implementation
        worker_tasks = []
        for worker in workers:
            worker_request = ConsultationRequest(
                objective=request.objective,
                context={**request.context, "supervisor_guidance": supervisor_response.result},
                constraints=request.constraints,
                output_format=request.output_format,
                success_criteria=request.success_criteria
            )
            worker_tasks.append(self._consult_agent(worker, worker_request))
        
        worker_responses = await asyncio.gather(*worker_tasks, return_exceptions=True)
        
        return {
            "pattern": "hierarchical",
            "supervisor_result": {"agent": supervisor, "response": supervisor_response},
            "worker_results": [
                {"agent": workers[i], "response": resp}
                for i, resp in enumerate(worker_responses)
                if not isinstance(resp, Exception)
            ]
        }
    
    async def _consult_agent(self, agent_name: str, request: ConsultationRequest) -> AgentResponse:
        """
        Consult individual agent (simulated for now)
        
        In full implementation, this would:
        1. Load agent specification
        2. Apply agent's methodology 
        3. Generate structured response
        4. Validate against agent's framework
        """
        logger.info(f"Consulting {agent_name}")
        
        # Simulate agent processing time
        await asyncio.sleep(0.1)
        
        # Get agent specification
        agent_spec = self.agent_specs.get(agent_name, {})
        methodology = agent_spec.get('agent_identity', {}).get('methodology', 'Generic methodology')
        
        # Simulate agent response (in real implementation, this would use the agent's actual logic)
        simulated_response = AgentResponse(
            status="success",
            result={
                "primary_recommendation": f"Strategic recommendation from {agent_name} using {methodology}",
                "methodology_applied": methodology,
                "specific_guidance": f"Detailed guidance based on {methodology} framework"
            },
            metadata={
                "confidence": 0.85,
                "methodology_applied": methodology,
                "agent_name": agent_name,
                "processing_time": "0.1s"
            },
            recommendations={
                "complementary_consultations": self._get_complementary_agents(agent_name),
                "implementation_approach": "Follow methodology-specific implementation steps"
            },
            scope_boundaries=agent_spec.get('scope_boundaries', {}),
            potential_conflicts=agent_spec.get('potential_conflicts', {})
        )
        
        return simulated_response
    
    def _filter_context_for_agent(self, context: Dict[str, Any], agent_name: str) -> Dict[str, Any]:
        """Filter and optimize context for specific agent (following article's context management)"""
        # In full implementation, this would:
        # 1. Apply context relevance scoring
        # 2. Compress context for agent-specific needs
        # 3. Remove irrelevant information
        # 4. Apply privacy controls
        
        # For now, return filtered context based on agent domain
        agent_spec = self.agent_specs.get(agent_name, {})
        agent_domain = self._get_agent_domain(agent_name)
        
        # Simple filtering - keep relevant context only
        filtered_context = {}
        for key, value in context.items():
            if any(domain_word in key.lower() for domain_word in self._get_domain_keywords(agent_domain)):
                filtered_context[key] = value
        
        # Always include basic business context
        for key in ["business_goals", "target_audience", "budget_constraints", "timeline"]:
            if key in context:
                filtered_context[key] = context[key]
        
        return filtered_context if filtered_context else context
    
    def _get_agent_domain(self, agent_name: str) -> str:
        """Get the domain category for an agent"""
        for category, info in self.agents_registry.get("agent_categories", {}).items():
            if f"enhanced-{agent_name}" in info.get("agents", []):
                return category
        return "business_strategy_sales"  # Default
    
    def _get_domain_keywords(self, domain: str) -> List[str]:
        """Get relevant keywords for domain-based context filtering"""
        domain_keywords = {
            "business_strategy_sales": ["business", "sales", "pricing", "strategy", "client"],
            "design_visual": ["design", "visual", "brand", "logo", "color", "typography"],
            "technical_architecture": ["technical", "performance", "seo", "accessibility", "code"],
            "content_communication": ["content", "copy", "marketing", "social", "email"],
            "analysis_operations": ["research", "analysis", "operations", "project", "data"]
        }
        return domain_keywords.get(domain, ["business", "strategy"])
    
    def _get_complementary_agents(self, agent_name: str) -> List[str]:
        """Get complementary agents based on orchestration patterns"""
        # Get from agent spec if available
        agent_spec = self.agent_specs.get(agent_name, {})
        orchestration = agent_spec.get('orchestration_integration', {})
        
        complementary = []
        
        # Parallel collaboration agents
        parallel_collabs = orchestration.get('parallel_collaboration', [])
        for collab in parallel_collabs:
            if 'agent' in collab:
                complementary.append(collab['agent'])
        
        # Sequential workflow next steps
        next_steps = orchestration.get('sequential_workflow', {}).get('next_steps', [])
        complementary.extend(next_steps)
        
        return complementary[:3]  # Limit to 3 suggestions
    
    def _detect_conflicts(self, agent_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect conflicts between agent responses"""
        conflicts = []
        
        # Compare agent responses for conflicts
        for i, result1 in enumerate(agent_results):
            for j, result2 in enumerate(agent_results[i+1:], i+1):
                agent1_name = result1["agent"]
                agent2_name = result2["agent"]
                response1 = result1["response"]
                response2 = result2["response"]
                
                # Check for explicit potential conflicts
                conflicts1 = response1.potential_conflicts
                conflicts2 = response2.potential_conflicts
                
                # Simple conflict detection based on different recommendations
                if (response1.result.get("primary_recommendation", "").lower() != 
                    response2.result.get("primary_recommendation", "").lower()):
                    
                    conflicts.append({
                        "agents": [agent1_name, agent2_name],
                        "conflict_type": "methodology_difference",
                        "agent1_approach": response1.result.get("primary_recommendation", ""),
                        "agent2_approach": response2.result.get("primary_recommendation", ""),
                        "resolution_needed": True
                    })
        
        return conflicts
    
    async def _synthesize_results(self, execution_result: Dict[str, Any], analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Synthesize results from multiple agents (article's result synthesis)"""
        pattern = execution_result["pattern"]
        results = execution_result["results"]
        
        if pattern == "sequential":
            # For sequential, use the final result with full context
            final_result = results[-1]["response"] if results else None
            synthesis = {
                "status": "success" if final_result and final_result.status == "success" else "partial",
                "orchestration_pattern": pattern,
                "primary_result": final_result.result if final_result else {},
                "agent_chain": [r["agent"] for r in results],
                "methodology_synthesis": self._synthesize_methodologies([r["response"] for r in results])
            }
        
        elif pattern == "mapreduce":
            # For MapReduce, aggregate all successful results
            successful_results = [r["response"] for r in results if r["response"].status in ["success", "partial"]]
            synthesis = {
                "status": "success" if successful_results else "failed",
                "orchestration_pattern": pattern,
                "aggregated_results": {
                    "combined_recommendations": self._combine_recommendations(successful_results),
                    "methodology_consensus": self._find_methodology_consensus(successful_results),
                    "implementation_synthesis": self._synthesize_implementation_guidance(successful_results)
                },
                "contributing_agents": [r["agent"] for r in results],
                "agent_count": len(results)
            }
        
        elif pattern == "consensus":
            # For consensus, present agreement and conflicts
            conflicts = execution_result.get("conflicts", [])
            consensus_items = self._find_consensus_items(results)
            
            synthesis = {
                "status": "success" if results else "failed",
                "orchestration_pattern": pattern,
                "consensus_result": {
                    "agreed_recommendations": consensus_items,
                    "conflicting_advice": conflicts,
                    "resolution_required": len(conflicts) > 0,
                    "user_decision_points": self._create_decision_framework(conflicts)
                },
                "expert_perspectives": [{
                    "agent": r["agent"],
                    "methodology": r["response"].metadata.get("methodology_applied", ""),
                    "confidence": r["response"].metadata.get("confidence", 0.0)
                } for r in results]
            }
        
        else:  # hierarchical
            supervisor_result = execution_result.get("supervisor_result", {})
            worker_results = execution_result.get("worker_results", [])
            
            synthesis = {
                "status": "success" if supervisor_result else "failed",
                "orchestration_pattern": pattern,
                "hierarchical_result": {
                    "strategic_guidance": supervisor_result.get("response", {}).result,
                    "implementation_details": [w["response"].result for w in worker_results],
                    "coordination_approach": "hierarchical_delegation"
                },
                "supervision_agent": supervisor_result.get("agent", ""),
                "implementation_agents": [w["agent"] for w in worker_results]
            }
        
        # Add meta-information
        synthesis.update({
            "meta_orchestrator": {
                "analysis": analysis,
                "agents_consulted": len(results) if isinstance(results, list) else 1,
                "total_processing_time": "simulated",
                "orchestration_success": True,
                "quality_score": self._calculate_quality_score(synthesis)
            }
        })
        
        return synthesis
    
    def _optimize_agent_selection(self, analysis: Dict[str, Any], overlaps: List[AgentOverlap]) -> Dict[str, Any]:
        """Optimize agent selection based on detected overlaps"""
        optimized_analysis = analysis.copy()
        
        for overlap in overlaps:
            if overlap.overlap_type == "methodology_family":
                # For methodology family overlaps, prefer primary expert
                primary_agents = overlap.agents[:1]  # Keep primary agent
                logger.info(f"Optimized agent selection for {overlap.overlap_type}: keeping {primary_agents}")
            elif overlap.overlap_type == "scope_boundary":
                # For scope overlaps, use resolution strategy
                if overlap.resolution_strategy == "clear_delegation":
                    # Keep most relevant agent based on context
                    logger.info(f"Applying clear delegation for scope overlap: {overlap.agents}")
        
        return optimized_analysis
    
    def _generate_optimization_suggestions(self, quality_metrics: QualityMetrics) -> List[str]:
        """Generate optimization suggestions based on quality assessment"""
        suggestions = []
        
        if quality_metrics.methodology_adherence < 0.8:
            suggestions.append("Consider validating agent methodology adherence")
        
        if quality_metrics.orchestration_efficiency < 0.8:
            suggestions.append("Review agent selection for optimal coordination")
        
        if quality_metrics.user_value_score < 0.7:
            suggestions.append("Enhance result synthesis for improved user value")
        
        if quality_metrics.output_consistency < 0.9:
            suggestions.append("Improve output format consistency across agents")
        
        if not suggestions:
            suggestions.append("System performing optimally - no improvements needed")
        
        return suggestions
    
    def _synthesize_methodologies(self, responses: List[AgentResponse]) -> Dict[str, Any]:
        """Synthesize different expert methodologies"""
        methodologies = {}
        for response in responses:
            if response and hasattr(response, 'metadata'):
                methodology = response.metadata.get("methodology_applied", "Unknown")
                confidence = response.metadata.get("confidence", 0.0)
                
                if methodology not in methodologies:
                    methodologies[methodology] = {
                        "confidence": confidence,
                        "recommendations": []
                    }
                
                if hasattr(response, 'result'):
                    methodologies[methodology]["recommendations"].append(
                        response.result.get("primary_recommendation", "")
                    )
        
        return methodologies
    
    def _combine_recommendations(self, responses: List[AgentResponse]) -> List[str]:
        """Combine recommendations from multiple agents"""
        recommendations = []
        for response in responses:
            if response and hasattr(response, 'result'):
                rec = response.result.get("primary_recommendation", "")
                if rec and rec not in recommendations:
                    recommendations.append(rec)
        return recommendations
    
    def _find_methodology_consensus(self, responses: List[AgentResponse]) -> Dict[str, Any]:
        """Find consensus across different methodologies"""
        # Simple consensus detection - in full implementation would be more sophisticated
        common_themes = {}
        for response in responses:
            if response and hasattr(response, 'result'):
                rec = response.result.get("primary_recommendation", "").lower()
                words = rec.split()
                for word in words:
                    if len(word) > 4:  # Focus on meaningful words
                        common_themes[word] = common_themes.get(word, 0) + 1
        
        # Find most common themes
        consensus_themes = {k: v for k, v in common_themes.items() if v > 1}
        
        return {
            "common_themes": consensus_themes,
            "consensus_strength": len(consensus_themes),
            "methodology_agreement": len(consensus_themes) > 2
        }
    
    def _synthesize_implementation_guidance(self, responses: List[AgentResponse]) -> Dict[str, Any]:
        """Synthesize implementation guidance from multiple responses"""
        implementation_steps = []
        timeline_suggestions = []
        resource_requirements = []
        
        for response in responses:
            if response and hasattr(response, 'recommendations'):
                impl_approach = response.recommendations.get("implementation_approach", "")
                if impl_approach:
                    implementation_steps.append(impl_approach)
        
        return {
            "combined_steps": implementation_steps,
            "timeline_synthesis": "Coordinate parallel implementation where possible",
            "resource_optimization": "Leverage agent expertise efficiently"
        }
    
    def _find_consensus_items(self, results: List[Dict[str, Any]]) -> List[str]:
        """Find areas of agreement between agents"""
        if len(results) < 2:
            return []
        
        # Simple consensus detection
        recommendations = []
        for result in results:
            response = result.get("response")
            if response and hasattr(response, 'result'):
                rec = response.result.get("primary_recommendation", "")
                if rec:
                    recommendations.append(rec.lower())
        
        # Find common words/themes
        consensus_items = []
        if len(recommendations) > 1:
            words_sets = [set(rec.split()) for rec in recommendations]
            common_words = set.intersection(*words_sets)
            consensus_items = [word for word in common_words if len(word) > 3]
        
        return consensus_items
    
    def _create_decision_framework(self, conflicts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Create user decision framework for conflicts"""
        decision_points = []
        
        for conflict in conflicts:
            decision_points.append({
                "decision_required": f"Choose approach for {conflict.get('conflict_type', 'methodology difference')}",
                "option_1": {
                    "agent": conflict.get("agents", ["", ""])[0],
                    "approach": conflict.get("agent1_approach", ""),
                    "methodology": "See agent methodology details"
                },
                "option_2": {
                    "agent": conflict.get("agents", ["", ""])[1], 
                    "approach": conflict.get("agent2_approach", ""),
                    "methodology": "See agent methodology details"
                },
                "recommendation": "Consider business context and expert methodology alignment"
            })
        
        return decision_points
    
    def _calculate_quality_score(self, synthesis: Dict[str, Any]) -> float:
        """Calculate overall quality score for orchestration result"""
        base_score = 0.7
        
        # Bonus for successful orchestration
        if synthesis.get("status") == "success":
            base_score += 0.2
        
        # Bonus for multiple agents contributing
        agents_count = synthesis.get("meta_orchestrator", {}).get("agents_consulted", 1)
        if agents_count > 1:
            base_score += 0.1
        
        return min(base_score, 1.0)

# Example usage and testing
if __name__ == "__main__":
    async def test_orchestrator():
        """Test the meta-orchestrator with sample requests"""
        orchestrator = MetaOrchestrator()
        
        # Test 1: Simple single-domain request
        simple_request = ConsultationRequest(
            objective="Help me price my design services",
            context={
                "business_type": "design agency",
                "current_pricing": "hourly rates",
                "market_position": "mid-market"
            },
            constraints={
                "budget_limitations": "startup budget"
            },
            success_criteria="Clear pricing strategy that improves profitability"
        )
        
        print("=== Test 1: Simple Pricing Request ===")
        result1 = await orchestrator.execute_consultation(simple_request)
        print(f"Pattern: {result1.get('orchestration_pattern')}")
        print(f"Status: {result1.get('status')}")
        print(f"Agents: {result1.get('meta_orchestrator', {}).get('agents_consulted')}")
        
        # Test 2: Complex multi-domain request
        complex_request = ConsultationRequest(
            objective="Launch a complete brand identity and website for a tech startup that builds trust with enterprise clients",
            context={
                "business_type": "B2B SaaS startup",
                "target_audience": "enterprise clients",
                "competitive_landscape": "crowded market",
                "timeline": "3 months to launch"
            },
            constraints={
                "budget_limitations": "Series A funding available",
                "technical_constraints": "modern web stack preferred"
            },
            success_criteria="Professional brand identity and high-converting website that builds enterprise trust"
        )
        
        print("\n=== Test 2: Complex Brand + Website Request ===")
        result2 = await orchestrator.execute_consultation(complex_request)
        print(f"Pattern: {result2.get('orchestration_pattern')}")
        print(f"Status: {result2.get('status')}")
        print(f"Agents: {result2.get('meta_orchestrator', {}).get('agents_consulted')}")
        
        # Test 3: Consensus-requiring request
        consensus_request = ConsultationRequest(
            objective="Evaluate whether to use value-based pricing or package-based pricing for our agency",
            context={
                "business_type": "creative agency",
                "current_challenges": "inconsistent pricing, client objections",
                "team_concerns": "pricing confidence"
            },
            success_criteria="Clear recommendation on pricing approach with expert validation"
        )
        
        print("\n=== Test 3: Pricing Strategy Consensus Request ===")
        result3 = await orchestrator.execute_consultation(complex_request)
        print(f"Pattern: {result3.get('orchestration_pattern')}")
        print(f"Status: {result3.get('status')}")
        if 'consensus_result' in result3:
            conflicts = result3['consensus_result'].get('conflicting_advice', [])
            print(f"Conflicts detected: {len(conflicts)}")
    
    # Run tests
    asyncio.run(test_orchestrator())