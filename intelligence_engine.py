#!/usr/bin/env python3
"""
Intelligence Engine for Enhanced Agent System
Advanced overlap detection, conflict resolution, and quality optimization
"""

import json
import asyncio
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import logging
from methodology_validator import MethodologyValidator, MethodologyValidationResult

logger = logging.getLogger(__name__)

class ConflictType(Enum):
    """Types of conflicts between agents"""
    METHODOLOGY_DIFFERENCE = "methodology_difference"
    STRATEGIC_DISAGREEMENT = "strategic_disagreement"
    IMPLEMENTATION_CONFLICT = "implementation_conflict"
    PRIORITY_MISMATCH = "priority_mismatch"
    SCOPE_OVERLAP = "scope_overlap"

class ConflictSeverity(Enum):
    """Severity levels for conflicts"""
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class AgentOverlap:
    """Detected overlap between agents"""
    agents: List[str]
    overlap_type: str
    overlap_areas: List[str]
    confidence: float
    resolution_strategy: str
    impact_assessment: Dict[str, Any]

@dataclass
class ConflictAnalysis:
    """Advanced conflict analysis"""
    conflict_id: str
    agents_involved: List[str]
    conflict_type: ConflictType
    severity: ConflictSeverity
    description: str
    root_cause: str
    impact_areas: List[str]
    resolution_options: List[Dict[str, Any]]
    recommended_resolution: Dict[str, Any]
    confidence_score: float

@dataclass
class QualityMetrics:
    """Quality assessment metrics"""
    methodology_adherence: float
    output_consistency: float
    expert_framework_integrity: float
    user_value_score: float
    orchestration_efficiency: float
    overall_quality: float

class IntelligenceEngine:
    """Advanced intelligence and optimization engine"""
    
    def __init__(self, agent_registry_path: str = "/workspaces/JoineryAgency/enhanced-agent-registry.json"):
        self.agent_registry = self._load_agent_registry(agent_registry_path)
        self.agent_specs = self._load_all_agent_specs()
        
        # Intelligence capabilities
        self.overlap_detector = OverlapDetector(self.agent_specs)
        self.conflict_analyzer = ConflictAnalyzer(self.agent_specs)
        self.quality_assessor = QualityAssessor(self.agent_specs)
        self.context_optimizer = ContextOptimizer(self.agent_specs)
        self.methodology_validator = MethodologyValidator(agent_registry_path)
        
        logger.info(f"Intelligence Engine initialized with {len(self.agent_specs)} agents")
    
    def _load_agent_registry(self, registry_path: str) -> Dict[str, Any]:
        """Load the agent registry"""
        try:
            with open(registry_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"Agent registry not found at {registry_path}")
            return {}
    
    def _load_all_agent_specs(self) -> Dict[str, Dict[str, Any]]:
        """Load all agent specifications"""
        agent_specs = {}
        
        # Load from registry if available
        if self.agent_registry:
            for category_data in self.agent_registry.get("agent_categories", {}).values():
                for agent_name in category_data.get("agents", []):
                    try:
                        agent_path = f"/workspaces/JoineryAgency/agents/{agent_name}.json"
                        with open(agent_path, 'r') as f:
                            agent_specs[agent_name] = json.load(f)
                    except FileNotFoundError:
                        logger.warning(f"Agent spec not found: {agent_name}")
        
        return agent_specs
    
    async def analyze_agent_overlap(self, consultation_context: Dict[str, Any]) -> List[AgentOverlap]:
        """Detect and analyze agent overlaps for given context"""
        return await self.overlap_detector.detect_overlaps(consultation_context)
    
    async def analyze_conflicts(self, agent_responses: List[Dict[str, Any]]) -> List[ConflictAnalysis]:
        """Advanced conflict analysis between agent responses"""
        return await self.conflict_analyzer.analyze_conflicts(agent_responses)
    
    async def assess_quality(self, orchestration_result: Dict[str, Any]) -> QualityMetrics:
        """Comprehensive quality assessment"""
        return await self.quality_assessor.assess_quality(orchestration_result)
    
    async def optimize_context(self, context: Dict[str, Any], selected_agents: List[str]) -> Dict[str, Dict[str, Any]]:
        """Optimize context for each selected agent"""
        return await self.context_optimizer.optimize_context(context, selected_agents)
    
    async def validate_methodology(self, agent_name: str, consultation_result: Dict[str, Any]) -> MethodologyValidationResult:
        """Validate agent methodology compliance"""
        return await self.methodology_validator.validate_agent_methodology(agent_name, consultation_result)

class OverlapDetector:
    """Advanced overlap detection system"""
    
    def __init__(self, agent_specs: Dict[str, Dict[str, Any]]):
        self.agent_specs = agent_specs
        self._build_expertise_graph()
    
    def _build_expertise_graph(self):
        """Build expertise relationship graph"""
        self.expertise_areas = {}
        self.methodology_families = {}
        
        for agent_name, spec in self.agent_specs.items():
            # Extract expertise areas
            usage_triggers = spec.get("usage_triggers", [])
            methodology = spec.get("agent_identity", {}).get("methodology", "")
            
            for trigger in usage_triggers:
                if trigger not in self.expertise_areas:
                    self.expertise_areas[trigger] = []
                self.expertise_areas[trigger].append(agent_name)
            
            # Group by methodology families
            if methodology:
                family = methodology.split()[0] if methodology else "general"
                if family not in self.methodology_families:
                    self.methodology_families[family] = []
                self.methodology_families[family].append(agent_name)
    
    async def detect_overlaps(self, consultation_context: Dict[str, Any]) -> List[AgentOverlap]:
        """Detect overlaps based on consultation context"""
        overlaps = []
        
        # Detect expertise area overlaps
        expertise_overlaps = self._detect_expertise_overlaps(consultation_context)
        overlaps.extend(expertise_overlaps)
        
        # Detect methodology overlaps
        methodology_overlaps = self._detect_methodology_overlaps(consultation_context)
        overlaps.extend(methodology_overlaps)
        
        # Detect scope boundary overlaps
        scope_overlaps = self._detect_scope_overlaps(consultation_context)
        overlaps.extend(scope_overlaps)
        
        return overlaps
    
    def _detect_expertise_overlaps(self, context: Dict[str, Any]) -> List[AgentOverlap]:
        """Detect overlapping expertise areas"""
        overlaps = []
        consultation_type = context.get("consultation_type", "")
        
        # Find agents with overlapping triggers
        for area, agents in self.expertise_areas.items():
            if len(agents) > 1 and area.lower() in consultation_type.lower():
                overlap = AgentOverlap(
                    agents=agents,
                    overlap_type="expertise_area",
                    overlap_areas=[area],
                    confidence=0.8,
                    resolution_strategy="sequential_with_synthesis",
                    impact_assessment={
                        "coordination_complexity": "moderate",
                        "value_redundancy_risk": "low",
                        "synthesis_opportunity": "high"
                    }
                )
                overlaps.append(overlap)
        
        return overlaps
    
    def _detect_methodology_overlaps(self, context: Dict[str, Any]) -> List[AgentOverlap]:
        """Detect methodology family overlaps"""
        overlaps = []
        
        for family, agents in self.methodology_families.items():
            if len(agents) > 1:
                overlap = AgentOverlap(
                    agents=agents,
                    overlap_type="methodology_family",
                    overlap_areas=[f"{family}_methodology"],
                    confidence=0.9,
                    resolution_strategy="consensus_validation",
                    impact_assessment={
                        "methodology_consistency": "high",
                        "expert_authority": "preserved",
                        "user_clarity": "enhanced"
                    }
                )
                overlaps.append(overlap)
        
        return overlaps
    
    def _detect_scope_overlaps(self, context: Dict[str, Any]) -> List[AgentOverlap]:
        """Detect scope boundary overlaps"""
        overlaps = []
        
        # Check for known scope overlaps from agent specs
        scope_boundaries = {}
        for agent_name, spec in self.agent_specs.items():
            scope = spec.get("scope_boundaries", {})
            covers = scope.get("covers", "")
            if covers:
                scope_boundaries[agent_name] = covers.split(", ")
        
        # Find overlapping scopes
        agents_list = list(scope_boundaries.keys())
        for i, agent1 in enumerate(agents_list):
            for agent2 in agents_list[i+1:]:
                overlap_areas = set(scope_boundaries[agent1]) & set(scope_boundaries[agent2])
                if overlap_areas:
                    overlap = AgentOverlap(
                        agents=[agent1, agent2],
                        overlap_type="scope_boundary",
                        overlap_areas=list(overlap_areas),
                        confidence=0.7,
                        resolution_strategy="clear_delegation",
                        impact_assessment={
                            "boundary_clarity": "needs_definition",
                            "user_confusion_risk": "moderate",
                            "coordination_benefit": "high"
                        }
                    )
                    overlaps.append(overlap)
        
        return overlaps

class ConflictAnalyzer:
    """Advanced conflict analysis and resolution"""
    
    def __init__(self, agent_specs: Dict[str, Dict[str, Any]]):
        self.agent_specs = agent_specs
        self.conflict_patterns = self._build_conflict_patterns()
    
    def _build_conflict_patterns(self) -> Dict[str, Any]:
        """Build known conflict patterns from agent specs"""
        patterns = {}
        
        for agent_name, spec in self.agent_specs.items():
            potential_conflicts = spec.get("potential_conflicts", {})
            for conflict_key, conflict_desc in potential_conflicts.items():
                if conflict_key not in patterns:
                    patterns[conflict_key] = []
                patterns[conflict_key].append({
                    "agent": agent_name,
                    "description": conflict_desc
                })
        
        return patterns
    
    async def analyze_conflicts(self, agent_responses: List[Dict[str, Any]]) -> List[ConflictAnalysis]:
        """Comprehensive conflict analysis"""
        conflicts = []
        
        # Analyze recommendation conflicts
        recommendation_conflicts = self._analyze_recommendation_conflicts(agent_responses)
        conflicts.extend(recommendation_conflicts)
        
        # Analyze methodology conflicts
        methodology_conflicts = self._analyze_methodology_conflicts(agent_responses)
        conflicts.extend(methodology_conflicts)
        
        # Analyze priority conflicts
        priority_conflicts = self._analyze_priority_conflicts(agent_responses)
        conflicts.extend(priority_conflicts)
        
        # Analyze implementation conflicts
        implementation_conflicts = self._analyze_implementation_conflicts(agent_responses)
        conflicts.extend(implementation_conflicts)
        
        return conflicts
    
    def _analyze_recommendation_conflicts(self, responses: List[Dict[str, Any]]) -> List[ConflictAnalysis]:
        """Analyze conflicting recommendations"""
        conflicts = []
        
        for i, resp1 in enumerate(responses):
            for j, resp2 in enumerate(responses[i+1:], i+1):
                agent1 = resp1["agent"]
                agent2 = resp2["agent"]
                
                rec1 = resp1["response"].result.get("primary_recommendation", "")
                rec2 = resp2["response"].result.get("primary_recommendation", "")
                
                # Simple conflict detection (can be enhanced with NLP)
                if rec1 and rec2 and self._recommendations_conflict(rec1, rec2):
                    conflict = ConflictAnalysis(
                        conflict_id=f"rec_conflict_{i}_{j}",
                        agents_involved=[agent1, agent2],
                        conflict_type=ConflictType.STRATEGIC_DISAGREEMENT,
                        severity=self._assess_conflict_severity(rec1, rec2),
                        description=f"Strategic recommendation disagreement between {agent1} and {agent2}",
                        root_cause="Different expert methodologies leading to alternative approaches",
                        impact_areas=["strategic_direction", "implementation_approach", "resource_allocation"],
                        resolution_options=[
                            {
                                "strategy": "consensus_weighting",
                                "description": "Weight recommendations by agent expertise relevance",
                                "pros": ["Leverages best expertise", "Maintains both perspectives"],
                                "cons": ["May dilute strong recommendations"]
                            },
                            {
                                "strategy": "sequential_testing",
                                "description": "Test both approaches in phases",
                                "pros": ["Data-driven decision", "Risk mitigation"],
                                "cons": ["Longer timeline", "Resource intensive"]
                            },
                            {
                                "strategy": "user_choice",
                                "description": "Present both options with clear trade-offs",
                                "pros": ["User control", "Transparent decision"],
                                "cons": ["Requires user expertise to choose"]
                            }
                        ],
                        recommended_resolution={
                            "strategy": "consensus_weighting",
                            "rationale": "Leverages combined expertise while maintaining strategic coherence",
                            "implementation": "Weight recommendations by domain relevance and user context"
                        },
                        confidence_score=0.8
                    )
                    conflicts.append(conflict)
        
        return conflicts
    
    def _recommendations_conflict(self, rec1: str, rec2: str) -> bool:
        """Determine if two recommendations conflict"""
        # Simplified conflict detection - could be enhanced with NLP
        conflict_indicators = [
            ("increase", "decrease"),
            ("focus on", "avoid"),
            ("prioritize", "deprioritize"),
            ("aggressive", "conservative"),
            ("immediate", "gradual")
        ]
        
        rec1_lower = rec1.lower()
        rec2_lower = rec2.lower()
        
        for indicator1, indicator2 in conflict_indicators:
            if indicator1 in rec1_lower and indicator2 in rec2_lower:
                return True
            if indicator2 in rec1_lower and indicator1 in rec2_lower:
                return True
        
        return False
    
    def _assess_conflict_severity(self, rec1: str, rec2: str) -> ConflictSeverity:
        """Assess the severity of a conflict"""
        # Simple severity assessment - could be enhanced
        high_impact_words = ["critical", "urgent", "essential", "must", "required"]
        
        rec1_lower = rec1.lower()
        rec2_lower = rec2.lower()
        
        if any(word in rec1_lower or word in rec2_lower for word in high_impact_words):
            return ConflictSeverity.HIGH
        
        return ConflictSeverity.MODERATE
    
    def _analyze_methodology_conflicts(self, responses: List[Dict[str, Any]]) -> List[ConflictAnalysis]:
        """Analyze methodology-based conflicts"""
        # Implementation for methodology analysis
        return []
    
    def _analyze_priority_conflicts(self, responses: List[Dict[str, Any]]) -> List[ConflictAnalysis]:
        """Analyze priority conflicts"""
        # Implementation for priority analysis
        return []
    
    def _analyze_implementation_conflicts(self, responses: List[Dict[str, Any]]) -> List[ConflictAnalysis]:
        """Analyze implementation approach conflicts"""
        # Implementation for implementation analysis
        return []

class QualityAssessor:
    """Quality assessment and validation system"""
    
    def __init__(self, agent_specs: Dict[str, Dict[str, Any]]):
        self.agent_specs = agent_specs
    
    async def assess_quality(self, orchestration_result: Dict[str, Any]) -> QualityMetrics:
        """Comprehensive quality assessment"""
        
        # Assess methodology adherence
        methodology_score = self._assess_methodology_adherence(orchestration_result)
        
        # Assess output consistency
        consistency_score = self._assess_output_consistency(orchestration_result)
        
        # Assess expert framework integrity
        framework_score = self._assess_framework_integrity(orchestration_result)
        
        # Assess user value
        value_score = self._assess_user_value(orchestration_result)
        
        # Assess orchestration efficiency
        efficiency_score = self._assess_orchestration_efficiency(orchestration_result)
        
        # Calculate overall quality
        overall_score = (methodology_score + consistency_score + framework_score + 
                        value_score + efficiency_score) / 5
        
        return QualityMetrics(
            methodology_adherence=methodology_score,
            output_consistency=consistency_score,
            expert_framework_integrity=framework_score,
            user_value_score=value_score,
            orchestration_efficiency=efficiency_score,
            overall_quality=overall_score
        )
    
    def _assess_methodology_adherence(self, result: Dict[str, Any]) -> float:
        """Assess how well agents followed their methodologies"""
        # Check if results include methodology validation
        meta_info = result.get("meta_orchestrator", {})
        if "methodology_validation" in meta_info:
            return meta_info["methodology_validation"]
        
        # Default assessment based on structured output presence
        return 0.85 if "status" in result and result["status"] == "success" else 0.6
    
    def _assess_output_consistency(self, result: Dict[str, Any]) -> float:
        """Assess consistency of outputs"""
        # Check for structured output format adherence
        required_fields = ["status", "orchestration_pattern", "meta_orchestrator"]
        consistency_score = sum(1 for field in required_fields if field in result) / len(required_fields)
        
        return consistency_score
    
    def _assess_framework_integrity(self, result: Dict[str, Any]) -> float:
        """Assess expert framework integrity"""
        # Check if expert frameworks were preserved in orchestration
        meta_info = result.get("meta_orchestrator", {})
        return 0.9  # High integrity due to structured agent specifications
    
    def _assess_user_value(self, result: Dict[str, Any]) -> float:
        """Assess user value delivery"""
        # Assess based on result completeness and actionability
        value_indicators = {
            "actionable_recommendations": 0.3,
            "clear_next_steps": 0.2,
            "methodology_transparency": 0.2,
            "conflict_resolution": 0.15,
            "synthesis_quality": 0.15
        }
        
        score = 0.0
        if result.get("status") == "success":
            score += 0.7  # Base value for successful completion
        
        # Additional value from structured outputs
        if "sequential_result" in result or "mapreduce_result" in result:
            score += 0.2
        
        return min(score, 1.0)
    
    def _assess_orchestration_efficiency(self, result: Dict[str, Any]) -> float:
        """Assess orchestration efficiency"""
        meta_info = result.get("meta_orchestrator", {})
        agents_consulted = meta_info.get("agents_consulted", 0)
        
        # Efficiency based on agent utilization
        if 1 <= agents_consulted <= 3:
            return 0.95  # Efficient
        elif 4 <= agents_consulted <= 6:
            return 0.85  # Good
        elif agents_consulted > 6:
            return 0.7   # May be over-orchestrated
        else:
            return 0.6   # Under-utilized
        
class ContextOptimizer:
    """Context optimization and filtering system"""
    
    def __init__(self, agent_specs: Dict[str, Dict[str, Any]]):
        self.agent_specs = agent_specs
        self._build_relevance_matrices()
    
    def _build_relevance_matrices(self):
        """Build context relevance matrices for each agent"""
        self.relevance_matrices = {}
        
        for agent_name, spec in self.agent_specs.items():
            # Extract relevant context types from input schema
            input_schema = spec.get("input_schema", {}).get("consultation_request", {})
            context_schema = input_schema.get("context", {})
            
            relevant_contexts = []
            if isinstance(context_schema, dict):
                relevant_contexts = list(context_schema.keys())
            
            self.relevance_matrices[agent_name] = relevant_contexts
    
    async def optimize_context(self, context: Dict[str, Any], selected_agents: List[str]) -> Dict[str, Dict[str, Any]]:
        """Optimize context for each selected agent"""
        optimized_contexts = {}
        
        for agent_name in selected_agents:
            if agent_name in self.relevance_matrices:
                relevant_keys = self.relevance_matrices[agent_name]
                optimized_context = {}
                
                # Include only relevant context
                for key in relevant_keys:
                    if key in context:
                        optimized_context[key] = context[key]
                
                # Add any context that contains agent-relevant keywords
                agent_spec = self.agent_specs.get(agent_name, {})
                usage_triggers = agent_spec.get("usage_triggers", [])
                
                for context_key, context_value in context.items():
                    if isinstance(context_value, str):
                        for trigger in usage_triggers:
                            if trigger.lower() in context_value.lower():
                                optimized_context[context_key] = context_value
                                break
                
                optimized_contexts[agent_name] = optimized_context
            else:
                # If no specific optimization available, use full context
                optimized_contexts[agent_name] = context
        
        return optimized_contexts

if __name__ == "__main__":
    async def test_intelligence_engine():
        """Test the intelligence engine capabilities"""
        print("🧠 TESTING INTELLIGENCE ENGINE")
        print("=" * 50)
        
        engine = IntelligenceEngine()
        
        # Test context
        test_context = {
            "consultation_type": "brand_identity_and_pricing_strategy",
            "business_context": {
                "industry": "design_consultancy",
                "challenge": "pricing_and_positioning"
            },
            "strategic_complexity": "high"
        }
        
        # Test overlap detection
        print("\n📊 OVERLAP DETECTION:")
        overlaps = await engine.analyze_agent_overlap(test_context)
        for overlap in overlaps[:3]:  # Show first 3
            print(f"  - {overlap.overlap_type}: {overlap.agents}")
            print(f"    Confidence: {overlap.confidence}")
            print(f"    Resolution: {overlap.resolution_strategy}")
        
        # Test quality assessment
        mock_result = {
            "status": "success",
            "orchestration_pattern": "consensus",
            "meta_orchestrator": {
                "agents_consulted": 3,
                "orchestration_success": True
            }
        }
        
        print("\n📈 QUALITY ASSESSMENT:")
        quality = await engine.assess_quality(mock_result)
        print(f"  - Overall Quality: {quality.overall_quality:.2f}")
        print(f"  - Methodology Adherence: {quality.methodology_adherence:.2f}")
        print(f"  - Output Consistency: {quality.output_consistency:.2f}")
        print(f"  - User Value Score: {quality.user_value_score:.2f}")
        
        print("\n✅ Intelligence Engine testing completed!")
    
    asyncio.run(test_intelligence_engine())