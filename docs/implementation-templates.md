# Implementation Templates & Code Examples
*Practical Templates for Building the Enhanced Agent System*

## Overview

This document provides concrete implementation templates, code examples, and practical guidance for building the enhanced two-tier agent system. These templates serve as blueprints for actual development work.

## Table of Contents

1. [Meta-Orchestrator Implementation](#meta-orchestrator-implementation)
2. [Enhanced Agent Template](#enhanced-agent-template)
3. [Communication Protocol Implementation](#communication-protocol-implementation)
4. [Orchestration Pattern Examples](#orchestration-pattern-examples)
5. [Context Management Implementation](#context-management-implementation)
6. [Error Handling Templates](#error-handling-templates)
7. [Monitoring & Analytics](#monitoring--analytics)
8. [Testing Frameworks](#testing-frameworks)

---

## Meta-Orchestrator Implementation

### Core Meta-Orchestrator Class

```python
from typing import Dict, List, Optional, Union, Any
from dataclasses import dataclass
from enum import Enum
import asyncio
import logging
from datetime import datetime

class OrchestrationPattern(Enum):
    SINGLE_AGENT = "single_agent"
    SEQUENTIAL_PIPELINE = "sequential_pipeline"
    MAPREDUCE_PARALLEL = "mapreduce_parallel"
    CONSENSUS_VALIDATION = "consensus_validation"
    HIERARCHICAL_DELEGATION = "hierarchical_delegation"

class TaskComplexity(Enum):
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"
    VERY_COMPLEX = "very_complex"

@dataclass
class TaskRequest:
    task_id: str
    timestamp: datetime
    user_context: Dict[str, Any]
    objective: str
    success_criteria: List[str]
    constraints: Dict[str, Any]
    priority: str = "medium"
    
@dataclass
class AgentResponse:
    agent_id: str
    task_id: str
    status: str
    confidence: float
    result: Dict[str, Any]
    metadata: Dict[str, Any]
    recommendations: List[str]
    errors: List[str] = None

class MetaOrchestrator:
    """
    Central coordination system for managing multi-agent consultations
    """
    
    def __init__(self, agent_registry: Dict[str, Any], config: Dict[str, Any]):
        self.agent_registry = agent_registry
        self.config = config
        self.active_tasks = {}
        self.performance_tracker = PerformanceTracker()
        self.context_manager = ContextManager()
        self.conflict_resolver = ConflictResolver()
        
    async def process_consultation_request(self, request: TaskRequest) -> Dict[str, Any]:
        """
        Main orchestration method that coordinates the entire consultation process
        """
        try:
            # Task analysis and decomposition
            analysis = await self._analyze_task(request)
            
            # Agent selection and orchestration pattern determination
            orchestration_plan = await self._create_orchestration_plan(analysis)
            
            # Execute orchestration pattern
            result = await self._execute_orchestration(orchestration_plan, request)
            
            # Synthesize and validate results
            final_response = await self._synthesize_results(result, request)
            
            return final_response
            
        except Exception as e:
            return await self._handle_orchestration_error(e, request)
    
    async def _analyze_task(self, request: TaskRequest) -> Dict[str, Any]:
        """
        Analyze task complexity, domain requirements, and orchestration needs
        """
        analysis = {
            "complexity": self._assess_complexity(request),
            "primary_domains": self._identify_primary_domains(request),
            "secondary_domains": self._identify_secondary_domains(request),
            "overlap_risk": self._assess_overlap_risk(request),
            "dependencies": self._analyze_dependencies(request),
            "estimated_agents_needed": 0,
            "recommended_pattern": None
        }
        
        # Domain mapping and agent selection
        relevant_agents = self._map_request_to_agents(request, analysis)
        analysis["relevant_agents"] = relevant_agents
        analysis["estimated_agents_needed"] = len(relevant_agents)
        
        # Pattern recommendation based on analysis
        analysis["recommended_pattern"] = self._recommend_orchestration_pattern(analysis)
        
        return analysis
    
    def _assess_complexity(self, request: TaskRequest) -> TaskComplexity:
        """
        Determine task complexity based on request characteristics
        """
        complexity_indicators = {
            "multiple_domains": len(self._identify_primary_domains(request)) > 1,
            "strategic_implications": any(keyword in request.objective.lower() 
                                       for keyword in ["strategy", "transformation", "roadmap"]),
            "cross_functional": "integration" in request.objective.lower(),
            "high_stakes": request.priority == "urgent" or "critical" in request.objective.lower(),
            "ambiguous_requirements": len(request.success_criteria) < 2
        }
        
        complexity_score = sum(complexity_indicators.values())
        
        if complexity_score <= 1:
            return TaskComplexity.SIMPLE
        elif complexity_score <= 2:
            return TaskComplexity.MODERATE
        elif complexity_score <= 3:
            return TaskComplexity.COMPLEX
        else:
            return TaskComplexity.VERY_COMPLEX
    
    def _recommend_orchestration_pattern(self, analysis: Dict[str, Any]) -> OrchestrationPattern:
        """
        Select optimal orchestration pattern based on task analysis
        """
        complexity = analysis["complexity"]
        agent_count = analysis["estimated_agents_needed"]
        overlap_risk = analysis["overlap_risk"]
        
        if agent_count == 1:
            return OrchestrationPattern.SINGLE_AGENT
        elif complexity == TaskComplexity.SIMPLE and agent_count <= 3:
            return OrchestrationPattern.SEQUENTIAL_PIPELINE
        elif overlap_risk == "low" and agent_count <= 5:
            return OrchestrationPattern.MAPREDUCE_PARALLEL
        elif overlap_risk == "high" or "consensus" in analysis.get("requirements", ""):
            return OrchestrationPattern.CONSENSUS_VALIDATION
        elif complexity == TaskComplexity.VERY_COMPLEX and agent_count > 5:
            return OrchestrationPattern.HIERARCHICAL_DELEGATION
        else:
            return OrchestrationPattern.MAPREDUCE_PARALLEL  # Default fallback

class ContextManager:
    """
    Manages context filtering, compression, and relevance optimization
    """
    
    def __init__(self):
        self.context_cache = {}
        self.relevance_threshold = 0.7
    
    async def prepare_agent_context(self, agent_id: str, full_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Filter and optimize context for specific agent
        """
        agent_profile = self._get_agent_profile(agent_id)
        
        # Context filtering based on agent domain and needs
        filtered_context = self._filter_context_by_relevance(full_context, agent_profile)
        
        # Context compression to stay within token limits
        compressed_context = await self._compress_context(filtered_context, agent_profile)
        
        # Add agent-specific context enhancements
        enhanced_context = self._add_agent_specific_context(compressed_context, agent_id)
        
        return enhanced_context
    
    def _filter_context_by_relevance(self, context: Dict[str, Any], agent_profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Remove irrelevant context based on agent's domain expertise
        """
        relevant_context = {}
        
        for key, value in context.items():
            relevance_score = self._calculate_relevance_score(key, value, agent_profile)
            if relevance_score >= self.relevance_threshold:
                relevant_context[key] = value
        
        return relevant_context
    
    async def _compress_context(self, context: Dict[str, Any], agent_profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Compress context to fit within agent's optimal context window
        """
        max_tokens = agent_profile.get("max_context_tokens", 2000)
        
        # Prioritize context elements by importance
        prioritized_context = self._prioritize_context_elements(context, agent_profile)
        
        # Compress until within token limit
        compressed = {}
        current_tokens = 0
        
        for priority, (key, value) in prioritized_context:
            estimated_tokens = self._estimate_tokens(value)
            if current_tokens + estimated_tokens <= max_tokens:
                compressed[key] = value
                current_tokens += estimated_tokens
            else:
                # Try to include a summary if space allows
                summary = self._create_context_summary(value)
                summary_tokens = self._estimate_tokens(summary)
                if current_tokens + summary_tokens <= max_tokens:
                    compressed[f"{key}_summary"] = summary
                    current_tokens += summary_tokens
        
        return compressed

class ConflictResolver:
    """
    Handles overlap detection and consensus resolution between agents
    """
    
    def __init__(self):
        self.overlap_patterns = self._load_overlap_patterns()
        self.resolution_strategies = self._load_resolution_strategies()
    
    async def detect_overlaps(self, agent_responses: List[AgentResponse]) -> List[Dict[str, Any]]:
        """
        Identify potential conflicts or overlaps between agent responses
        """
        overlaps = []
        
        for i, response_a in enumerate(agent_responses):
            for j, response_b in enumerate(agent_responses[i+1:], i+1):
                overlap = await self._detect_response_overlap(response_a, response_b)
                if overlap:
                    overlaps.append({
                        "agents": [response_a.agent_id, response_b.agent_id],
                        "overlap_type": overlap["type"],
                        "conflict_areas": overlap["areas"],
                        "severity": overlap["severity"],
                        "resolution_strategy": self._select_resolution_strategy(overlap)
                    })
        
        return overlaps
    
    async def resolve_conflicts(self, overlaps: List[Dict[str, Any]], 
                              agent_responses: List[AgentResponse]) -> Dict[str, Any]:
        """
        Resolve identified conflicts using appropriate consensus mechanisms
        """
        resolution_results = {}
        
        for overlap in overlaps:
            strategy = overlap["resolution_strategy"]
            
            if strategy == "consensus_voting":
                resolution = await self._consensus_voting(overlap, agent_responses)
            elif strategy == "expertise_hierarchy":
                resolution = await self._expertise_hierarchy(overlap, agent_responses)
            elif strategy == "synthesis_approach":
                resolution = await self._synthesis_approach(overlap, agent_responses)
            else:
                resolution = await self._default_resolution(overlap, agent_responses)
            
            resolution_results[f"conflict_{len(resolution_results)}"] = resolution
        
        return resolution_results
    
    async def _consensus_voting(self, overlap: Dict[str, Any], 
                               responses: List[AgentResponse]) -> Dict[str, Any]:
        """
        Use weighted voting based on confidence and expertise relevance
        """
        conflict_agents = overlap["agents"]
        relevant_responses = [r for r in responses if r.agent_id in conflict_agents]
        
        # Calculate weighted votes
        weighted_votes = {}
        for response in relevant_responses:
            agent_expertise_weight = self._get_expertise_weight(response.agent_id, overlap)
            confidence_weight = response.confidence
            total_weight = agent_expertise_weight * confidence_weight
            
            weighted_votes[response.agent_id] = {
                "response": response.result,
                "weight": total_weight,
                "rationale": response.metadata.get("methodology_applied", "")
            }
        
        # Determine consensus based on weights
        winner = max(weighted_votes.keys(), key=lambda x: weighted_votes[x]["weight"])
        
        return {
            "resolution_method": "consensus_voting",
            "selected_approach": weighted_votes[winner]["response"],
            "winning_agent": winner,
            "vote_weights": weighted_votes,
            "confidence": weighted_votes[winner]["weight"]
        }

# Performance tracking implementation
class PerformanceTracker:
    """
    Monitors and tracks system and agent performance
    """
    
    def __init__(self):
        self.metrics = {}
        self.alert_thresholds = {
            "response_time": 5.0,  # seconds
            "success_rate": 0.95,
            "user_satisfaction": 4.0
        }
    
    def track_consultation(self, task_id: str, start_time: datetime, 
                          end_time: datetime, success: bool, 
                          user_rating: Optional[float] = None):
        """
        Track metrics for a complete consultation
        """
        duration = (end_time - start_time).total_seconds()
        
        if task_id not in self.metrics:
            self.metrics[task_id] = {
                "response_time": duration,
                "success": success,
                "user_rating": user_rating,
                "timestamp": start_time
            }
    
    def get_performance_summary(self, time_window_hours: int = 24) -> Dict[str, Any]:
        """
        Generate performance summary for specified time window
        """
        cutoff_time = datetime.now() - timedelta(hours=time_window_hours)
        recent_metrics = [m for m in self.metrics.values() 
                         if m["timestamp"] >= cutoff_time]
        
        if not recent_metrics:
            return {"error": "No recent data available"}
        
        avg_response_time = sum(m["response_time"] for m in recent_metrics) / len(recent_metrics)
        success_rate = sum(1 for m in recent_metrics if m["success"]) / len(recent_metrics)
        avg_rating = sum(m["user_rating"] for m in recent_metrics if m["user_rating"]) / \
                    len([m for m in recent_metrics if m["user_rating"]])
        
        return {
            "time_window_hours": time_window_hours,
            "total_consultations": len(recent_metrics),
            "average_response_time": avg_response_time,
            "success_rate": success_rate,
            "average_user_rating": avg_rating,
            "alerts": self._check_performance_alerts(avg_response_time, success_rate, avg_rating)
        }
```

---

## Enhanced Agent Template

### Base Enhanced Agent Implementation

```python
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from datetime import datetime
import json
import logging

@dataclass
class AgentInputSchema:
    required_fields: List[str]
    optional_fields: List[str]
    validation_rules: Dict[str, Any]

@dataclass
class AgentOutputSchema:
    status: str
    primary_result: Dict[str, Any]
    confidence_score: float
    methodology_applied: str
    recommendations: List[str]
    follow_up_suggestions: List[str]
    metadata: Dict[str, Any]
    errors: List[str] = None

class EnhancedAgentBase(ABC):
    """
    Base class for all enhanced stateless agents
    """
    
    def __init__(self, agent_config: Dict[str, Any]):
        self.agent_id = agent_config["agent_id"]
        self.version = agent_config["version"]
        self.category = agent_config["category"]
        self.expert_methodology = agent_config["expert_methodology"]
        self.complexity_rating = agent_config["complexity_rating"]
        
        self.input_schema = self._define_input_schema()
        self.output_schema = self._define_output_schema()
        self.performance_metrics = {}
        
    @abstractmethod
    def _define_input_schema(self) -> AgentInputSchema:
        """Define the structured input requirements for this agent"""
        pass
    
    @abstractmethod
    def _define_output_schema(self) -> AgentOutputSchema:
        """Define the structured output format for this agent"""
        pass
    
    @abstractmethod
    async def _process_request(self, validated_input: Dict[str, Any]) -> Dict[str, Any]:
        """Core processing logic using expert methodology"""
        pass
    
    async def execute_consultation(self, request: Dict[str, Any]) -> AgentOutputSchema:
        """
        Main execution method that handles the complete consultation process
        """
        start_time = datetime.now()
        
        try:
            # Input validation
            validated_input = await self._validate_input(request)
            
            # Core processing using expert methodology
            result = await self._process_request(validated_input)
            
            # Output structuring and validation
            structured_output = await self._structure_output(result, validated_input)
            
            # Performance tracking
            self._track_performance(start_time, True, structured_output.confidence_score)
            
            return structured_output
            
        except Exception as e:
            error_output = await self._handle_processing_error(e, request)
            self._track_performance(start_time, False, 0.0)
            return error_output
    
    async def _validate_input(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate input against schema and business rules
        """
        # Check required fields
        for field in self.input_schema.required_fields:
            if field not in request:
                raise ValueError(f"Required field '{field}' missing from request")
        
        # Apply validation rules
        for field, rules in self.input_schema.validation_rules.items():
            if field in request:
                await self._apply_validation_rule(field, request[field], rules)
        
        return request
    
    async def _structure_output(self, result: Dict[str, Any], 
                               input_data: Dict[str, Any]) -> AgentOutputSchema:
        """
        Structure the processing result into standardized output format
        """
        return AgentOutputSchema(
            status="success",
            primary_result=result,
            confidence_score=self._calculate_confidence(result, input_data),
            methodology_applied=self.expert_methodology,
            recommendations=result.get("recommendations", []),
            follow_up_suggestions=self._generate_follow_up_suggestions(result),
            metadata={
                "agent_id": self.agent_id,
                "processing_time": datetime.now().isoformat(),
                "input_complexity": self._assess_input_complexity(input_data),
                "methodology_confidence": self._assess_methodology_fit(input_data)
            }
        )
    
    def _calculate_confidence(self, result: Dict[str, Any], 
                            input_data: Dict[str, Any]) -> float:
        """
        Calculate confidence score based on result quality and input completeness
        """
        base_confidence = 0.7  # Base confidence for methodology application
        
        # Input completeness factor
        completeness_factor = len([f for f in self.input_schema.required_fields 
                                 if f in input_data and input_data[f]]) / len(self.input_schema.required_fields)
        
        # Result richness factor
        richness_factor = min(len(result.get("recommendations", [])) / 3, 1.0)
        
        # Methodology fit factor
        fit_factor = self._assess_methodology_fit(input_data)
        
        confidence = base_confidence * completeness_factor * (1 + richness_factor * 0.2) * fit_factor
        return min(confidence, 1.0)
    
    @abstractmethod
    def _assess_methodology_fit(self, input_data: Dict[str, Any]) -> float:
        """
        Assess how well the agent's methodology fits the specific request
        """
        pass
    
    def _generate_follow_up_suggestions(self, result: Dict[str, Any]) -> List[str]:
        """
        Generate suggestions for additional expertise that might be helpful
        """
        # Default implementation - override in specific agents
        return [
            f"Consider consulting with complementary agents for {self.category} optimization",
            "Validate recommendations through user testing or stakeholder feedback",
            "Monitor implementation results and iterate based on outcomes"
        ]

# Example: Enhanced Sales Specialist Implementation
class EnhancedSalesSpecialist(EnhancedAgentBase):
    """
    Enhanced Sales Specialist using Chris Do's value-based selling methodology
    """
    
    def _define_input_schema(self) -> AgentInputSchema:
        return AgentInputSchema(
            required_fields=["client_situation", "sale_objective", "objections_encountered"],
            optional_fields=["budget_parameters", "decision_timeline", "competition"],
            validation_rules={
                "client_situation": {"min_length": 10, "type": "string"},
                "sale_objective": {"min_length": 5, "type": "string"},
                "objections_encountered": {"type": "list"}
            }
        )
    
    def _define_output_schema(self) -> AgentOutputSchema:
        # Schema is handled by parent class structure
        pass
    
    async def _process_request(self, validated_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply Chris Do's value-based selling methodology
        """
        client_situation = validated_input["client_situation"]
        sale_objective = validated_input["sale_objective"]
        objections = validated_input.get("objections_encountered", [])
        
        # Apply Chris Do's framework
        value_analysis = await self._analyze_client_value_opportunity(client_situation)
        positioning_strategy = await self._develop_value_positioning(sale_objective, value_analysis)
        objection_responses = await self._create_objection_responses(objections, positioning_strategy)
        relationship_strategy = await self._design_relationship_approach(client_situation, positioning_strategy)
        
        return {
            "sales_strategy": {
                "value_positioning": positioning_strategy,
                "relationship_approach": relationship_strategy,
                "objection_handling": objection_responses
            },
            "action_plan": {
                "immediate_steps": self._generate_immediate_steps(positioning_strategy),
                "conversation_flow": self._design_conversation_flow(positioning_strategy),
                "follow_up_strategy": self._create_follow_up_strategy(relationship_strategy)
            },
            "success_indicators": {
                "positive_signals": self._identify_positive_signals(),
                "risk_factors": self._identify_risk_factors(objections),
                "decision_criteria": self._extract_decision_criteria(client_situation)
            },
            "recommendations": self._generate_sales_recommendations(positioning_strategy, objections)
        }
    
    async def _analyze_client_value_opportunity(self, client_situation: str) -> Dict[str, Any]:
        """
        Analyze client situation to identify value creation opportunities
        """
        # Implementation of Chris Do's value analysis framework
        pain_points = self._extract_pain_points(client_situation)
        business_impact = self._assess_business_impact(pain_points)
        transformation_opportunity = self._identify_transformation_potential(client_situation)
        
        return {
            "pain_points": pain_points,
            "business_impact": business_impact,
            "transformation_opportunity": transformation_opportunity,
            "value_multiplier": self._calculate_value_multiplier(business_impact)
        }
    
    async def _develop_value_positioning(self, sale_objective: str, 
                                       value_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create value-based positioning using Chris Do's methodology
        """
        return {
            "outcome_focus": self._frame_outcome_benefits(sale_objective, value_analysis),
            "transformation_story": self._create_transformation_narrative(value_analysis),
            "roi_framework": self._develop_roi_justification(value_analysis),
            "differentiation": self._establish_unique_value_proposition(sale_objective)
        }
    
    def _assess_methodology_fit(self, input_data: Dict[str, Any]) -> float:
        """
        Assess how well Chris Do's methodology fits this specific sales situation
        """
        # Higher fit for consultative, high-value sales
        situation = input_data.get("client_situation", "").lower()
        
        fit_indicators = [
            "consulting" in situation,
            "strategic" in situation,
            "transformation" in situation,
            "investment" in situation,
            any(obj for obj in input_data.get("objections_encountered", []) 
                if "price" in str(obj).lower() or "cost" in str(obj).lower())
        ]
        
        base_fit = 0.8  # Chris Do's methodology is broadly applicable
        indicator_bonus = sum(fit_indicators) * 0.05
        
        return min(base_fit + indicator_bonus, 1.0)
```

---

## Communication Protocol Implementation

### Message Schema and Validation

```python
from typing import Dict, Any, List, Optional, Union
from pydantic import BaseModel, Field, validator
from datetime import datetime
from enum import Enum

class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"

class ResponseStatus(str, Enum):
    SUCCESS = "success"
    PARTIAL = "partial"
    FAILED = "failed"

class TaskSpecification(BaseModel):
    """
    Structured task specification schema for agent communication
    """
    task_id: str = Field(..., description="Unique identifier for the task")
    timestamp: datetime = Field(default_factory=datetime.now)
    priority: TaskPriority = Field(default=TaskPriority.MEDIUM)
    estimated_complexity: str = Field(..., regex="^(simple|moderate|complex)$")
    
    objective: str = Field(..., min_length=10, description="Clear, specific task description")
    success_criteria: List[str] = Field(..., min_items=1, description="Measurable completion indicators")
    output_format: str = Field(..., description="Expected result structure")
    
    user_background: Optional[str] = Field(None, description="Relevant user information")
    business_context: Optional[str] = Field(None, description="Industry and company details")
    technical_constraints: Optional[Dict[str, Any]] = Field(None, description="Limitations and requirements")
    reference_materials: Optional[List[str]] = Field(None, description="Supporting documents or data")
    
    time_limit: Optional[int] = Field(None, description="Maximum processing time in seconds")
    resource_limits: Optional[Dict[str, Any]] = Field(None, description="Computational boundaries")
    privacy_requirements: Optional[List[str]] = Field(None, description="Data handling restrictions")
    
    primary_agents: Optional[List[str]] = Field(None, description="Main expertise required")
    secondary_agents: Optional[List[str]] = Field(None, description="Supporting capabilities needed")
    orchestration_pattern: Optional[str] = Field(None, description="Coordination strategy")
    overlap_risk: Optional[str] = Field(None, description="Potential conflict areas")
    
    @validator('success_criteria')
    def validate_success_criteria(cls, v):
        if not v:
            raise ValueError('At least one success criterion must be provided')
        return v

class AgentResponse(BaseModel):
    """
    Structured response schema for agent communication
    """
    agent_id: str = Field(..., description="Responding agent identifier")
    task_id: str = Field(..., description="Corresponding request ID")
    response_timestamp: datetime = Field(default_factory=datetime.now)
    processing_duration: float = Field(..., description="Execution time in seconds")
    
    execution_status: ResponseStatus = Field(..., description="Completion status")
    confidence_level: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    completeness: float = Field(..., ge=0.0, le=1.0, description="Percentage of task completed")
    
    deliverable: Dict[str, Any] = Field(..., description="Main task output")
    methodology_applied: str = Field(..., description="Frameworks and approaches used")
    key_insights: List[str] = Field(default_factory=list, description="Important findings")
    actionable_recommendations: List[str] = Field(default_factory=list, description="Specific next steps")
    
    model_type: Optional[str] = Field(None, description="AI model utilized")
    token_count: Optional[int] = Field(None, description="Computational resources consumed")
    processing_complexity: Optional[str] = Field(None, description="Actual vs estimated complexity")
    
    self_assessment: Optional[float] = Field(None, ge=0.0, le=1.0, description="Agent's confidence in output")
    validation_checks: Optional[List[str]] = Field(None, description="Internal quality controls passed")
    edge_cases_considered: Optional[List[str]] = Field(None, description="Boundary conditions addressed")
    
    related_expertise: Optional[List[str]] = Field(None, description="Other agents that could help")
    unanswered_questions: Optional[List[str]] = Field(None, description="Areas requiring additional research")
    potential_conflicts: Optional[List[str]] = Field(None, description="Areas where other agents might disagree")
    
    encountered_issues: Optional[List[str]] = Field(None, description="Problems during processing")
    workarounds_applied: Optional[List[str]] = Field(None, description="How issues were addressed")
    limitations: Optional[List[str]] = Field(None, description="What couldn't be accomplished")
    retry_suggestions: Optional[List[str]] = Field(None, description="How to improve next attempt")

class InterAgentMessage(BaseModel):
    """
    Schema for communication between agents during orchestration
    """
    message_id: str = Field(..., description="Unique message identifier")
    from_agent: str = Field(..., description="Sending agent ID")
    to_agent: str = Field(..., description="Recipient agent ID")
    message_type: str = Field(..., regex="^(consultation_request|consensus_voting|result_validation)$")
    timestamp: datetime = Field(default_factory=datetime.now)
    
    content: Dict[str, Any] = Field(..., description="Message payload")
    context_summary: Optional[str] = Field(None, description="Relevant background")
    response_required: bool = Field(default=True, description="Whether response is expected")
    timeout: Optional[int] = Field(None, description="Response timeout in seconds")

# Protocol validation and serialization functions
class CommunicationProtocol:
    """
    Handles validation, serialization, and routing of agent communications
    """
    
    @staticmethod
    def validate_task_specification(data: Dict[str, Any]) -> TaskSpecification:
        """
        Validate incoming task specification against schema
        """
        try:
            return TaskSpecification(**data)
        except Exception as e:
            raise ValueError(f"Invalid task specification: {str(e)}")
    
    @staticmethod
    def validate_agent_response(data: Dict[str, Any]) -> AgentResponse:
        """
        Validate agent response against schema
        """
        try:
            return AgentResponse(**data)
        except Exception as e:
            raise ValueError(f"Invalid agent response: {str(e)}")
    
    @staticmethod
    def serialize_for_agent(task: TaskSpecification, agent_id: str, 
                           context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Serialize task specification for specific agent with filtered context
        """
        serialized = {
            "task_id": task.task_id,
            "timestamp": task.timestamp.isoformat(),
            "objective": task.objective,
            "success_criteria": task.success_criteria,
            "output_format": task.output_format,
            "priority": task.priority.value,
            "time_limit": task.time_limit,
            "agent_specific_context": context
        }
        
        # Add optional fields if present
        if task.business_context:
            serialized["business_context"] = task.business_context
        if task.technical_constraints:
            serialized["technical_constraints"] = task.technical_constraints
        if task.reference_materials:
            serialized["reference_materials"] = task.reference_materials
            
        return serialized
    
    @staticmethod
    def deserialize_agent_response(response_data: Dict[str, Any]) -> AgentResponse:
        """
        Deserialize and validate agent response
        """
        # Convert timestamp string back to datetime if needed
        if isinstance(response_data.get("response_timestamp"), str):
            response_data["response_timestamp"] = datetime.fromisoformat(
                response_data["response_timestamp"]
            )
        
        return AgentResponse(**response_data)

# Message routing and queuing
import asyncio
from asyncio import Queue
from typing import Callable

class MessageRouter:
    """
    Routes messages between agents and handles communication protocols
    """
    
    def __init__(self):
        self.agent_queues: Dict[str, Queue] = {}
        self.message_handlers: Dict[str, Callable] = {}
        self.active_conversations: Dict[str, List[InterAgentMessage]] = {}
    
    async def register_agent(self, agent_id: str, handler: Callable):
        """
        Register an agent and its message handler
        """
        self.agent_queues[agent_id] = Queue()
        self.message_handlers[agent_id] = handler
    
    async def send_message(self, message: InterAgentMessage) -> Optional[InterAgentMessage]:
        """
        Send message to target agent and optionally wait for response
        """
        target_agent = message.to_agent
        
        if target_agent not in self.agent_queues:
            raise ValueError(f"Agent {target_agent} not registered")
        
        # Add to conversation history
        conversation_key = f"{message.from_agent}_{message.to_agent}"
        if conversation_key not in self.active_conversations:
            self.active_conversations[conversation_key] = []
        self.active_conversations[conversation_key].append(message)
        
        # Queue message for target agent
        await self.agent_queues[target_agent].put(message)
        
        # If response required, wait for it
        if message.response_required:
            timeout = message.timeout or 30  # Default 30 second timeout
            try:
                response = await asyncio.wait_for(
                    self._wait_for_response(message.message_id, target_agent),
                    timeout=timeout
                )
                return response
            except asyncio.TimeoutError:
                return None
        
        return None
    
    async def _wait_for_response(self, original_message_id: str, from_agent: str) -> InterAgentMessage:
        """
        Wait for response to a specific message
        """
        while True:
            # Check conversation history for response
            for conversation in self.active_conversations.values():
                for msg in conversation:
                    if (msg.from_agent == from_agent and 
                        msg.content.get("response_to") == original_message_id):
                        return msg
            
            # Wait a bit before checking again
            await asyncio.sleep(0.1)
```

---

## Orchestration Pattern Examples

### Sequential Pipeline Implementation

```python
import asyncio
from typing import List, Dict, Any, Optional

class SequentialPipeline:
    """
    Implements sequential agent orchestration with dependency management
    """
    
    def __init__(self, orchestrator_config: Dict[str, Any]):
        self.config = orchestrator_config
        self.context_manager = ContextManager()
        self.error_handler = PipelineErrorHandler()
    
    async def execute_pipeline(self, task: TaskSpecification, 
                             agent_sequence: List[str]) -> Dict[str, Any]:
        """
        Execute agents in sequence, passing context between stages
        """
        pipeline_context = await self._initialize_pipeline_context(task)
        stage_results = []
        
        for stage_num, agent_id in enumerate(agent_sequence):
            try:
                # Prepare stage-specific context
                stage_context = await self._prepare_stage_context(
                    pipeline_context, stage_results, stage_num
                )
                
                # Execute agent
                stage_result = await self._execute_pipeline_stage(
                    agent_id, task, stage_context
                )
                
                # Validate stage output
                validation_result = await self._validate_stage_output(
                    stage_result, stage_num, len(agent_sequence)
                )
                
                if not validation_result["valid"]:
                    # Handle stage failure
                    recovery_result = await self.error_handler.handle_stage_failure(
                        agent_id, stage_result, stage_num, pipeline_context
                    )
                    if recovery_result["recovered"]:
                        stage_result = recovery_result["result"]
                    else:
                        return await self._handle_pipeline_failure(
                            f"Stage {stage_num} failed validation", 
                            stage_results, pipeline_context
                        )
                
                stage_results.append({
                    "stage": stage_num,
                    "agent_id": agent_id,
                    "result": stage_result,
                    "validation": validation_result
                })
                
                # Update pipeline context with stage results
                pipeline_context = await self._update_pipeline_context(
                    pipeline_context, stage_result, stage_num
                )
                
            except Exception as e:
                return await self._handle_pipeline_error(e, stage_num, stage_results)
        
        # Synthesize final result
        final_result = await self._synthesize_pipeline_results(stage_results, pipeline_context)
        return final_result
    
    async def _prepare_stage_context(self, pipeline_context: Dict[str, Any], 
                                   previous_results: List[Dict[str, Any]], 
                                   stage_num: int) -> Dict[str, Any]:
        """
        Prepare context for specific pipeline stage
        """
        stage_context = {
            "pipeline_objective": pipeline_context["original_objective"],
            "stage_number": stage_num,
            "total_stages": pipeline_context["total_stages"],
            "previous_results": previous_results[-2:] if previous_results else [],  # Last 2 results
            "accumulated_insights": pipeline_context.get("accumulated_insights", [])
        }
        
        # Add stage-specific requirements
        if stage_num == 0:
            # First stage gets full context
            stage_context["full_context"] = pipeline_context["original_context"]
        else:
            # Subsequent stages get filtered context plus previous results
            stage_context["relevant_context"] = await self.context_manager.filter_context_for_stage(
                pipeline_context["original_context"], stage_num, previous_results
            )
        
        return stage_context
    
    async def _execute_pipeline_stage(self, agent_id: str, task: TaskSpecification, 
                                    stage_context: Dict[str, Any]) -> AgentResponse:
        """
        Execute a single pipeline stage
        """
        # Get agent instance
        agent = self._get_agent_instance(agent_id)
        
        # Prepare agent-specific task specification
        stage_task = self._adapt_task_for_stage(task, stage_context)
        
        # Execute agent consultation
        result = await agent.execute_consultation(stage_task)
        
        return result

# MapReduce Pattern Implementation
class MapReduceOrchestration:
    """
    Implements MapReduce pattern for parallel agent execution with result aggregation
    """
    
    def __init__(self, orchestrator_config: Dict[str, Any]):
        self.config = orchestrator_config
        self.conflict_resolver = ConflictResolver()
        self.result_synthesizer = ResultSynthesizer()
    
    async def execute_mapreduce(self, task: TaskSpecification, 
                               map_agents: List[str],
                               reduce_strategy: str = "synthesis") -> Dict[str, Any]:
        """
        Execute MapReduce orchestration pattern
        """
        # Map Phase: Parallel execution
        map_results = await self._execute_map_phase(task, map_agents)
        
        # Conflict Detection
        conflicts = await self.conflict_resolver.detect_overlaps(map_results)
        
        # Reduce Phase: Result aggregation
        if conflicts:
            reduced_result = await self._execute_reduce_with_conflicts(
                map_results, conflicts, reduce_strategy
            )
        else:
            reduced_result = await self._execute_reduce_phase(
                map_results, reduce_strategy
            )
        
        return reduced_result
    
    async def _execute_map_phase(self, task: TaskSpecification, 
                               map_agents: List[str]) -> List[AgentResponse]:
        """
        Execute multiple agents in parallel (Map phase)
        """
        # Prepare context for each agent
        agent_contexts = {}
        for agent_id in map_agents:
            agent_contexts[agent_id] = await self._prepare_agent_context(task, agent_id)
        
        # Create tasks for parallel execution
        agent_tasks = []
        for agent_id in map_agents:
            agent = self._get_agent_instance(agent_id)
            agent_task = self._create_agent_task(task, agent_contexts[agent_id])
            agent_tasks.append(agent.execute_consultation(agent_task))
        
        # Execute all agents in parallel
        results = await asyncio.gather(*agent_tasks, return_exceptions=True)
        
        # Process results and handle any exceptions
        processed_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                # Handle agent execution failure
                error_result = await self._create_error_result(
                    map_agents[i], str(result), task.task_id
                )
                processed_results.append(error_result)
            else:
                processed_results.append(result)
        
        return processed_results
    
    async def _execute_reduce_with_conflicts(self, map_results: List[AgentResponse],
                                           conflicts: List[Dict[str, Any]],
                                           reduce_strategy: str) -> Dict[str, Any]:
        """
        Execute reduce phase with conflict resolution
        """
        # Resolve conflicts first
        conflict_resolutions = await self.conflict_resolver.resolve_conflicts(
            conflicts, map_results
        )
        
        # Apply conflict resolutions to results
        resolved_results = await self._apply_conflict_resolutions(
            map_results, conflict_resolutions
        )
        
        # Proceed with normal reduce phase
        return await self._execute_reduce_phase(resolved_results, reduce_strategy)
    
    async def _execute_reduce_phase(self, map_results: List[AgentResponse], 
                                  reduce_strategy: str) -> Dict[str, Any]:
        """
        Aggregate results from map phase (Reduce phase)
        """
        if reduce_strategy == "synthesis":
            return await self.result_synthesizer.synthesize_results(map_results)
        elif reduce_strategy == "consensus":
            return await self._consensus_reduce(map_results)
        elif reduce_strategy == "best_result":
            return await self._best_result_reduce(map_results)
        else:
            return await self._default_reduce(map_results)

# Consensus Validation Pattern
class ConsensusValidation:
    """
    Implements consensus-based validation and decision making
    """
    
    def __init__(self, orchestrator_config: Dict[str, Any]):
        self.config = orchestrator_config
        self.voting_mechanisms = {
            "simple_majority": self._simple_majority_vote,
            "weighted_expertise": self._weighted_expertise_vote,
            "confidence_weighted": self._confidence_weighted_vote
        }
    
    async def execute_consensus(self, task: TaskSpecification,
                              consensus_agents: List[str],
                              voting_mechanism: str = "weighted_expertise") -> Dict[str, Any]:
        """
        Execute consensus validation pattern
        """
        # Phase 1: Independent analysis
        independent_results = await self._independent_analysis_phase(task, consensus_agents)
        
        # Phase 2: Structured comparison
        comparison_results = await self._structured_comparison_phase(independent_results)
        
        # Phase 3: Consensus building
        if comparison_results["consensus_achieved"]:
            final_result = comparison_results["consensus_result"]
        else:
            # Phase 4: Voting mechanism
            voting_result = await self.voting_mechanisms[voting_mechanism](
                independent_results, comparison_results
            )
            final_result = voting_result
        
        return final_result
    
    async def _independent_analysis_phase(self, task: TaskSpecification,
                                        agents: List[str]) -> List[AgentResponse]:
        """
        Have each agent analyze independently without seeing others' work
        """
        # Similar to MapReduce map phase but with isolation emphasis
        isolated_contexts = {}
        for agent_id in agents:
            isolated_contexts[agent_id] = await self._create_isolated_context(task, agent_id)
        
        # Execute agents in parallel with isolated contexts
        agent_tasks = []
        for agent_id in agents:
            agent = self._get_agent_instance(agent_id)
            agent_task = self._create_agent_task(task, isolated_contexts[agent_id])
            agent_tasks.append(agent.execute_consultation(agent_task))
        
        results = await asyncio.gather(*agent_tasks, return_exceptions=True)
        return [r for r in results if not isinstance(r, Exception)]
    
    async def _weighted_expertise_vote(self, independent_results: List[AgentResponse],
                                     comparison_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Vote based on expertise relevance and confidence
        """
        weighted_votes = {}
        
        for result in independent_results:
            # Calculate expertise weight for this specific task
            expertise_weight = await self._calculate_expertise_weight(
                result.agent_id, comparison_results["task_analysis"]
            )
            
            # Calculate confidence weight
            confidence_weight = result.confidence_level
            
            # Calculate total weight
            total_weight = expertise_weight * confidence_weight
            
            weighted_votes[result.agent_id] = {
                "result": result,
                "weight": total_weight,
                "expertise_weight": expertise_weight,
                "confidence_weight": confidence_weight
            }
        
        # Select result with highest weight
        winner = max(weighted_votes.keys(), key=lambda x: weighted_votes[x]["weight"])
        
        return {
            "consensus_method": "weighted_expertise_vote",
            "selected_result": weighted_votes[winner]["result"],
            "vote_details": weighted_votes,
            "consensus_confidence": weighted_votes[winner]["weight"]
        }
```

<function_calls>
<invoke name="TodoWrite">
<parameter name="todos">[{"content": "Create implementation code examples and templates", "status": "completed", "activeForm": "Creating implementation code examples and templates"}]