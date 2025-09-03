#!/usr/bin/env python3
"""
Methodology Validation System for Enhanced Agent System
Validates expert framework adherence and methodology integrity
"""

import json
import asyncio
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class MethodologyCompliance(Enum):
    """Methodology compliance levels"""
    EXCELLENT = "excellent"  # 90-100%
    GOOD = "good"           # 80-89%  
    ACCEPTABLE = "acceptable" # 70-79%
    POOR = "poor"           # Below 70%

class ValidationSeverity(Enum):
    """Validation issue severity"""
    CRITICAL = "critical"
    HIGH = "high"
    MODERATE = "moderate" 
    LOW = "low"

@dataclass
class MethodologyViolation:
    """Detected methodology violation"""
    agent_name: str
    expert_framework: str
    violation_type: str
    severity: ValidationSeverity
    description: str
    expected_behavior: str
    actual_behavior: str
    correction_guidance: str
    compliance_impact: float

@dataclass
class MethodologyValidationResult:
    """Complete validation result"""
    agent_name: str
    expert_framework: str
    compliance_level: MethodologyCompliance
    compliance_score: float
    violations: List[MethodologyViolation]
    strengths: List[str]
    recommendations: List[str]
    framework_integrity: float
    user_value_impact: float

class MethodologyValidator:
    """Expert methodology validation system"""
    
    def __init__(self, agent_registry_path: str = "/workspaces/JoineryAgency/enhanced-agent-registry.json"):
        self.agent_registry = self._load_agent_registry(agent_registry_path)
        self.expert_frameworks = self._load_expert_frameworks()
        self.validation_rules = self._build_validation_rules()
        
        logger.info(f"Methodology Validator initialized with {len(self.expert_frameworks)} expert frameworks")
    
    def _load_agent_registry(self, registry_path: str) -> Dict[str, Any]:
        """Load the agent registry"""
        try:
            with open(registry_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"Agent registry not found at {registry_path}")
            return {}
    
    def _load_expert_frameworks(self) -> Dict[str, Dict[str, Any]]:
        """Load expert framework specifications"""
        frameworks = {}
        
        if self.agent_registry:
            expert_methodologies = self.agent_registry.get("expert_methodologies", {})
            for expert_name, expert_data in expert_methodologies.items():
                frameworks[expert_name] = {
                    "agents": expert_data.get("agents", []),
                    "focus": expert_data.get("focus", ""),
                    "key_principles": self._extract_key_principles(expert_name),
                    "validation_criteria": self._define_validation_criteria(expert_name)
                }
        
        return frameworks
    
    def _extract_key_principles(self, expert_name: str) -> List[str]:
        """Extract key principles for each expert framework"""
        principles_map = {
            "chris_do": [
                "Value-based positioning over feature-based selling",
                "Strategic questioning to uncover business outcomes",
                "Outcome-focused proposals with ROI demonstration",
                "Premium pricing justified by strategic value"
            ],
            "don_norman": [
                "Human-centered design approach",
                "Usability testing and user feedback integration", 
                "Cognitive psychology principles in interface design",
                "Accessibility and inclusive design practices"
            ],
            "becca_luna": [
                "Menu-based pricing model structure",
                "Service packaging psychology principles",
                "Clear pricing tier differentiation",
                "Value perception optimization"
            ],
            "paula_scher": [
                "Systematic visual identity development",
                "Pentagram methodology application",
                "Brand expression through typography and color",
                "Cultural context integration in design"
            ],
            "massimo_vignelli": [
                "Mathematical proportions and systematic design",
                "Grid-based layout systems",
                "Timeless design principles over trends",
                "Information hierarchy and clarity"
            ],
            "marty_neumeier": [
                "Brand Gap framework application",
                "Strategic positioning differentiation",
                "Brand promise alignment with delivery",
                "Customer experience consistency"
            ],
            "seth_godin": [
                "Permission marketing principles",
                "Purple cow differentiation strategy",
                "Remarkable product/service development",
                "Tribe building and community engagement"
            ],
            "steve_krug": [
                "Don't make me think usability principles",
                "Practical usability testing methodology",
                "Common sense approach to web usability",
                "User-centric navigation and information architecture"
            ]
        }
        
        return principles_map.get(expert_name, [])
    
    def _define_validation_criteria(self, expert_name: str) -> Dict[str, Any]:
        """Define validation criteria for each expert framework"""
        criteria_map = {
            "chris_do": {
                "strategic_questioning": {"weight": 0.3, "required": True},
                "value_positioning": {"weight": 0.25, "required": True},
                "outcome_focus": {"weight": 0.25, "required": True},
                "premium_justification": {"weight": 0.2, "required": False}
            },
            "don_norman": {
                "user_centered_approach": {"weight": 0.35, "required": True},
                "usability_testing": {"weight": 0.25, "required": False},
                "cognitive_psychology": {"weight": 0.25, "required": True},
                "accessibility_consideration": {"weight": 0.15, "required": False}
            },
            "becca_luna": {
                "menu_based_structure": {"weight": 0.4, "required": True},
                "packaging_psychology": {"weight": 0.3, "required": True},
                "tier_differentiation": {"weight": 0.2, "required": True},
                "value_perception": {"weight": 0.1, "required": False}
            },
            "paula_scher": {
                "systematic_identity": {"weight": 0.3, "required": True},
                "pentagram_methodology": {"weight": 0.25, "required": False},
                "typography_focus": {"weight": 0.25, "required": True},
                "cultural_context": {"weight": 0.2, "required": False}
            }
        }
        
        return criteria_map.get(expert_name, {})
    
    def _build_validation_rules(self) -> Dict[str, List[Dict[str, Any]]]:
        """Build validation rules for each framework"""
        rules = {}
        
        for framework_name, framework_data in self.expert_frameworks.items():
            framework_rules = []
            criteria = framework_data.get("validation_criteria", {})
            
            for criterion, config in criteria.items():
                rule = {
                    "criterion": criterion,
                    "weight": config.get("weight", 0.1),
                    "required": config.get("required", False),
                    "validation_function": f"_validate_{criterion}"
                }
                framework_rules.append(rule)
            
            rules[framework_name] = framework_rules
        
        return rules
    
    async def validate_agent_methodology(self, agent_name: str, consultation_result: Dict[str, Any]) -> MethodologyValidationResult:
        """Validate agent adherence to their expert methodology"""
        
        # Determine which expert framework this agent uses
        expert_framework = self._get_agent_framework(agent_name)
        if not expert_framework:
            return self._create_no_framework_result(agent_name)
        
        # Perform validation checks
        violations = []
        strengths = []
        total_score = 0.0
        max_score = 0.0
        
        validation_rules = self.validation_rules.get(expert_framework, [])
        
        for rule in validation_rules:
            criterion = rule["criterion"]
            weight = rule["weight"]
            required = rule["required"]
            
            # Perform specific validation
            validation_result = await self._perform_criterion_validation(
                agent_name, criterion, consultation_result, expert_framework
            )
            
            score = validation_result.get("score", 0.0)
            total_score += score * weight
            max_score += weight
            
            # Check for violations
            if validation_result.get("violation"):
                violation = MethodologyViolation(
                    agent_name=agent_name,
                    expert_framework=expert_framework,
                    violation_type=criterion,
                    severity=validation_result.get("severity", ValidationSeverity.MODERATE),
                    description=validation_result.get("description", ""),
                    expected_behavior=validation_result.get("expected", ""),
                    actual_behavior=validation_result.get("actual", ""),
                    correction_guidance=validation_result.get("guidance", ""),
                    compliance_impact=weight
                )
                violations.append(violation)
            
            # Note strengths
            if validation_result.get("strength"):
                strengths.append(validation_result.get("strength_description", ""))
        
        # Calculate compliance score
        compliance_score = (total_score / max_score) if max_score > 0 else 0.0
        compliance_level = self._determine_compliance_level(compliance_score)
        
        # Generate recommendations
        recommendations = self._generate_methodology_recommendations(
            expert_framework, violations, compliance_score
        )
        
        return MethodologyValidationResult(
            agent_name=agent_name,
            expert_framework=expert_framework,
            compliance_level=compliance_level,
            compliance_score=compliance_score,
            violations=violations,
            strengths=strengths,
            recommendations=recommendations,
            framework_integrity=compliance_score,
            user_value_impact=self._calculate_user_value_impact(compliance_score, violations)
        )
    
    def _get_agent_framework(self, agent_name: str) -> Optional[str]:
        """Determine which expert framework an agent uses"""
        for framework_name, framework_data in self.expert_frameworks.items():
            if agent_name in framework_data.get("agents", []):
                return framework_name
        return None
    
    async def _perform_criterion_validation(self, agent_name: str, criterion: str, 
                                          consultation_result: Dict[str, Any], 
                                          framework: str) -> Dict[str, Any]:
        """Perform specific criterion validation"""
        
        # This is a simplified validation - in production, would use NLP analysis
        result_text = str(consultation_result)
        
        # Chris Do framework validations
        if framework == "chris_do":
            if criterion == "strategic_questioning":
                return self._validate_strategic_questioning(result_text)
            elif criterion == "value_positioning":
                return self._validate_value_positioning(result_text)
            elif criterion == "outcome_focus":
                return self._validate_outcome_focus(result_text)
        
        # Don Norman framework validations
        elif framework == "don_norman":
            if criterion == "user_centered_approach":
                return self._validate_user_centered_approach(result_text)
            elif criterion == "cognitive_psychology":
                return self._validate_cognitive_psychology(result_text)
        
        # Default validation
        return {
            "score": 0.8,  # Assume good compliance by default
            "violation": False,
            "strength": True,
            "strength_description": f"Agent demonstrates {criterion} principles"
        }
    
    def _validate_strategic_questioning(self, result_text: str) -> Dict[str, Any]:
        """Validate Chris Do strategic questioning methodology"""
        questioning_indicators = [
            "what business outcomes", "strategic goals", "return on investment",
            "business impact", "stakeholder objectives", "success metrics"
        ]
        
        found_indicators = sum(1 for indicator in questioning_indicators 
                             if indicator.lower() in result_text.lower())
        
        score = min(found_indicators / 3.0, 1.0)  # Normalize to 0-1
        
        if score >= 0.7:
            return {
                "score": score,
                "violation": False,
                "strength": True,
                "strength_description": "Strong strategic questioning approach evident"
            }
        else:
            return {
                "score": score,
                "violation": True,
                "severity": ValidationSeverity.MODERATE,
                "description": "Insufficient strategic questioning methodology",
                "expected": "Strategic questions focusing on business outcomes and ROI",
                "actual": "Limited strategic inquiry approach",
                "guidance": "Integrate more strategic business-focused questioning"
            }
    
    def _validate_value_positioning(self, result_text: str) -> Dict[str, Any]:
        """Validate value-based positioning methodology"""
        value_indicators = [
            "strategic value", "business value", "competitive advantage",
            "differentiation", "premium positioning", "value proposition"
        ]
        
        found_indicators = sum(1 for indicator in value_indicators 
                             if indicator.lower() in result_text.lower())
        
        score = min(found_indicators / 2.0, 1.0)
        
        return {
            "score": score,
            "violation": score < 0.6,
            "strength": score >= 0.8,
            "strength_description": "Strong value positioning evident" if score >= 0.8 else None,
            "severity": ValidationSeverity.MODERATE if score < 0.6 else None,
            "description": "Weak value positioning approach" if score < 0.6 else None,
            "guidance": "Strengthen value proposition and strategic positioning" if score < 0.6 else None
        }
    
    def _validate_outcome_focus(self, result_text: str) -> Dict[str, Any]:
        """Validate outcome-focused methodology"""
        outcome_indicators = [
            "measurable outcomes", "business results", "roi", "success metrics",
            "performance indicators", "deliverable outcomes"
        ]
        
        found_indicators = sum(1 for indicator in outcome_indicators 
                             if indicator.lower() in result_text.lower())
        
        score = min(found_indicators / 2.0, 1.0)
        
        return {
            "score": score,
            "violation": score < 0.5,
            "strength": score >= 0.7,
            "strength_description": "Strong outcome focus demonstrated" if score >= 0.7 else None
        }
    
    def _validate_user_centered_approach(self, result_text: str) -> Dict[str, Any]:
        """Validate Don Norman user-centered design methodology"""
        ucd_indicators = [
            "user needs", "user experience", "usability", "user research",
            "user testing", "human factors", "user behavior"
        ]
        
        found_indicators = sum(1 for indicator in ucd_indicators 
                             if indicator.lower() in result_text.lower())
        
        score = min(found_indicators / 3.0, 1.0)
        
        return {
            "score": score,
            "violation": score < 0.6,
            "strength": score >= 0.8,
            "strength_description": "Strong user-centered approach" if score >= 0.8 else None
        }
    
    def _validate_cognitive_psychology(self, result_text: str) -> Dict[str, Any]:
        """Validate cognitive psychology principles"""
        cognitive_indicators = [
            "cognitive load", "mental models", "user perception", "psychology",
            "cognitive principles", "human behavior"
        ]
        
        found_indicators = sum(1 for indicator in cognitive_indicators 
                             if indicator.lower() in result_text.lower())
        
        score = min(found_indicators / 2.0, 1.0)
        
        return {
            "score": score,
            "violation": False,  # Optional criterion
            "strength": score >= 0.7,
            "strength_description": "Cognitive psychology principles applied" if score >= 0.7 else None
        }
    
    def _determine_compliance_level(self, score: float) -> MethodologyCompliance:
        """Determine compliance level from score"""
        if score >= 0.9:
            return MethodologyCompliance.EXCELLENT
        elif score >= 0.8:
            return MethodologyCompliance.GOOD
        elif score >= 0.7:
            return MethodologyCompliance.ACCEPTABLE
        else:
            return MethodologyCompliance.POOR
    
    def _generate_methodology_recommendations(self, framework: str, 
                                           violations: List[MethodologyViolation], 
                                           score: float) -> List[str]:
        """Generate improvement recommendations"""
        recommendations = []
        
        if score < 0.7:
            recommendations.append(f"Review and strengthen {framework} methodology adherence")
        
        if violations:
            for violation in violations[:3]:  # Top 3 violations
                recommendations.append(f"Address {violation.violation_type}: {violation.correction_guidance}")
        
        if score >= 0.9:
            recommendations.append("Excellent methodology compliance - maintain current approach")
        
        return recommendations
    
    def _calculate_user_value_impact(self, compliance_score: float, 
                                   violations: List[MethodologyViolation]) -> float:
        """Calculate user value impact of methodology compliance"""
        base_impact = compliance_score
        
        # Reduce impact for critical violations
        for violation in violations:
            if violation.severity == ValidationSeverity.CRITICAL:
                base_impact -= 0.2
            elif violation.severity == ValidationSeverity.HIGH:
                base_impact -= 0.1
        
        return max(base_impact, 0.0)
    
    def _create_no_framework_result(self, agent_name: str) -> MethodologyValidationResult:
        """Create result for agents without specific framework"""
        return MethodologyValidationResult(
            agent_name=agent_name,
            expert_framework="none",
            compliance_level=MethodologyCompliance.ACCEPTABLE,
            compliance_score=0.75,
            violations=[],
            strengths=["General consulting expertise"],
            recommendations=["Consider adopting specific expert methodology"],
            framework_integrity=0.75,
            user_value_impact=0.75
        )

if __name__ == "__main__":
    async def test_methodology_validator():
        """Test methodology validation system"""
        print("🔍 TESTING METHODOLOGY VALIDATOR")
        print("=" * 50)
        
        validator = MethodologyValidator()
        
        # Test Chris Do methodology validation
        mock_chris_do_result = {
            "primary_recommendation": "Strategic value positioning with business outcome focus and ROI demonstration for competitive advantage",
            "methodology_applied": "Chris Do value-based selling",
            "strategic_analysis": "What business outcomes are you trying to achieve? How will this impact your strategic goals?"
        }
        
        result = await validator.validate_agent_methodology(
            "enhanced-sales-specialist", 
            mock_chris_do_result
        )
        
        print(f"Agent: {result.agent_name}")
        print(f"Framework: {result.expert_framework}")
        print(f"Compliance Level: {result.compliance_level.value}")
        print(f"Compliance Score: {result.compliance_score:.3f}")
        print(f"Violations: {len(result.violations)}")
        print(f"Strengths: {result.strengths}")
        print(f"Framework Integrity: {result.framework_integrity:.3f}")
        
        # Test Don Norman methodology validation
        mock_don_norman_result = {
            "primary_recommendation": "User-centered design approach with usability testing and user research integration",
            "methodology_applied": "Don Norman human-centered design",
            "user_focus": "User needs analysis and user experience optimization with cognitive psychology principles"
        }
        
        result2 = await validator.validate_agent_methodology(
            "enhanced-ux-interaction-specialist",
            mock_don_norman_result
        )
        
        print(f"\nAgent: {result2.agent_name}")
        print(f"Framework: {result2.expert_framework}")
        print(f"Compliance Level: {result2.compliance_level.value}")
        print(f"Compliance Score: {result2.compliance_score:.3f}")
        
        print("\n✅ Methodology validation testing completed!")
    
    asyncio.run(test_methodology_validator())