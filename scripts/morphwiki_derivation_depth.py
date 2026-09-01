"""Field-independent schema for mechanism-page derivation depth.

Field builders supply the physics.  This module fixes only the evidence
classes and the optional sections that turn a role assignment into a local
derivation with consequences, transfer tests, and a stated domain.
"""

from __future__ import annotations

from typing import Any, Mapping


DERIVATION_DEPTH_SECTIONS = (
    ("forced_consequences", "Consequences Forced By The Relation"),
    ("transfer_relations", "Transformations To Other Physical Realizations"),
    ("scope_conditions", "Domain Of The Construction"),
)


def classify_derivation_basis(
    *,
    topic_model: bool,
    source_grounded: bool,
    identifier_linked: bool,
    annotation: bool,
) -> str:
    if annotation:
        return "annotation"
    if source_grounded and topic_model:
        return "source_grounded_topic_model"
    if source_grounded:
        return "source_grounded_placement"
    if identifier_linked and topic_model:
        return "identifier_linked_topic_model"
    if identifier_linked:
        return "identifier_linked_placement"
    if topic_model:
        return "topic_model"
    return "branch_template"


def validate_derivation_template(template: Mapping[str, Any]) -> list[str]:
    """Return schema errors without imposing field vocabulary."""
    errors: list[str] = []
    for key, _ in DERIVATION_DEPTH_SECTIONS:
        value = template.get(key)
        if value is not None and not isinstance(value, (list, tuple)):
            errors.append(f"{key} must be a list of statements")
    equations = template.get("equations")
    if equations is not None and not isinstance(equations, (list, tuple)):
        errors.append("equations must be a list")
    return errors
