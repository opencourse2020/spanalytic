# Graph Report - .  (2026-08-10)

## Corpus Check
- Corpus is ~12,542 words - fits in a single context window. You may not need a graph.

## Summary
- 131 nodes · 167 edges · 19 communities (16 shown, 3 thin omitted)
- Extraction: 77% EXTRACTED · 22% INFERRED · 1% AMBIGUOUS · INFERRED: 37 edges (avg confidence: 0.8)
- Token cost: 0 input · 134,167 output

## Community Hubs (Navigation)
- Product Positioning & Frontend Rules
- Core Data Model & Measurement Pipeline
- Claims Safety & Regulatory Review
- ReportRequest Django App
- Engagement Deliverables & Agent Pipeline
- Engine Adapter & Metering Layer
- Hard Rules & Compliance Constraints
- Prompt Set Design
- Core App Config
- manage.py Entrypoint
- Prompts App

## God Nodes (most connected - your core abstractions)
1. `Data Model` - 12 edges
2. `ReportRequest` - 9 edges
3. `The Claims Filter (Seven Checks)` - 8 edges
4. `Deliverable 2: Remediation Package` - 8 edges
5. `Response Model` - 8 edges
6. `Spa Analytic Marketing Landing Page` - 8 edges
7. `Austin Botox Study (573 Responses)` - 7 edges
8. `Design Token System (tokens.css)` - 7 edges
9. `Spa Analytic (Product)` - 6 edges
10. `Hard Rules` - 6 edges

## Surprising Connections (you probably didn't know these)
- `Django==6.1 dependency` --conceptually_related_to--> `Spa Analytic (Product)`  [AMBIGUOUS]
  requierments.txt → CLAUDE.md
- `apps/remediation` --conceptually_related_to--> `2.2 Schema Package (lumen-schema.jsonld)`  [INFERRED]
  CLAUDE.md → docs/ENGAGEMENT_SPEC.md
- `Source Citation Bars (Yelp/GBP/RealSelf/etc.)` --semantically_similar_to--> `Deliverable 1: Source Citation Frequency Table`  [INFERRED] [semantically similar]
  spanalytic/templates/index.html → docs/ENGAGEMENT_SPEC.md
- `Claims Filter Ships-With-Copy Rule` --references--> `The Claims Filter (Seven Checks)`  [EXTRACTED]
  CLAUDE.md → .claude/skills/answer-block-authoring/SKILL.md
- `anthropic SDK dependency` --conceptually_related_to--> `apps.core.metering.MeteredClient`  [INFERRED]
  requierments.txt → CLAUDE.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Claims Safety Review Pipeline** — claude_skills_answer_block_authoring_skill_claims_filter, docs_engagement_spec_claims_safety_pass, docs_run_book_claims_filter_mandatory_stage, claude_claims_filter_rule, docs_system_design_review_queue_bottleneck [INFERRED 0.85]
- **Five-Agent Delivery Pipeline** — docs_run_book_agentic_delivery_pipeline, docs_run_book_prompt_set_builder_agent, docs_run_book_measurement_agent, docs_run_book_diagnosis_agent, docs_run_book_remediation_agent, docs_run_book_reporting_agent [EXTRACTED 1.00]
- **Measurement Domain Data Model Cluster** — docs_system_design_data_model, docs_system_design_response_model, docs_system_design_mention_model, docs_system_design_citation_model, docs_system_design_source_model [EXTRACTED 1.00]

## Communities (19 total, 3 thin omitted)

### Community 0 - "Product Positioning & Frontend Rules"
Cohesion: 0.12
Nodes (19): apps/billing, apps/reports, Spa Analytic (Product), Accessibility Floor, Brass/Clinical Colour Semantics, Design Token System (tokens.css), PDF Template Rules, Typography System (Newsreader/Instrument Sans/IBM Plex Mono) (+11 more)

### Community 1 - "Core Data Model & Measurement Pipeline"
Cohesion: 0.19
Nodes (19): apps/clinics, apps/diagnosis, apps/measurement, apps/remediation, Stage 3: Diagnosis Agent, AnswerBlock Model, Citation Model, CitationTarget Model (+11 more)

### Community 2 - "Claims Safety & Regulatory Review"
Cohesion: 0.13
Nodes (18): The Claims Filter (Seven Checks), claims_status (PASS/REWRITTEN/ESCALATED), Corporate Practice of Medicine Rules, Good Faith Exam (GFE) Requirement, Medical Director Requirement, Writing for Extraction, MedSpaScout.com (national directory), Finding: at most 1.9% of Responses Named a Clinic With a Price (+10 more)

### Community 3 - "ReportRequest Django App"
Cohesion: 0.16
Nodes (9): CreateView, register, ReportRequestAdmin, Meta, ReportRequestForm, Meta, A prospect asking for the free AI-visibility report — not yet a paying Client., ReportRequest (+1 more)

### Community 4 - "Engagement Deliverables & Agent Pipeline"
Cohesion: 0.18
Nodes (14): Source Citation Share Table, Deliverable 1: Baseline Visibility Report, 2.4 Citation-Source Targeting Plan, Deliverable 3: Delta Report, 2.3 Google Business Profile Field Sheet, Deliverable 4: Monthly Retainer ($499), Deliverable 2: Remediation Package, 2.2 Schema Package (lumen-schema.jsonld) (+6 more)

### Community 5 - "Engine Adapter & Metering Layer"
Cohesion: 0.24
Nodes (10): apps/core, EngineAdapter (base class), ENGINE_REGISTRY, apps.core.metering.MeteredClient, Response Model (reference), EngineAdapter Protocol, MeteredClient (Budget Enforcement), anthropic SDK dependency (+2 more)

### Community 6 - "Hard Rules & Compliance Constraints"
Cohesion: 0.29
Nodes (8): Claims Filter Ships-With-Copy Rule, Hard Rules, Never Fabricate Measurement Data Rule, No PHI Ever Rule, Official APIs Only Rule, Record Method Metadata Rule, Part 1c: What We Never Ask For (No PHI), No PHI Enforcement (CI Grep Check)

### Community 7 - "Prompt Set Design"
Cohesion: 0.38
Nodes (7): Prompt Set Versioned/Immutable Rule, Prompt.intent Enum, Price Prompts Over-Weighted Rationale, Prompt Set — Austin Metro v1 (48 prompts), Stage 1: Prompt-Set Builder Agent, Prompt / PromptSet Models, Animated Console Demo (typed prompt/answer)

## Ambiguous Edges - Review These
- `Spa Analytic (Product)` → `Django==6.1 dependency`  [AMBIGUOUS]
  requierments.txt · relation: conceptually_related_to
- `Lumen Aesthetics & Wellness (worked example client)` → `Austin Botox Study (573 Responses)`  [AMBIGUOUS]
  docs/austin-study-published.md · relation: conceptually_related_to

## Knowledge Gaps
- **20 isolated node(s):** `Meta`, `claims_status (PASS/REWRITTEN/ESCALATED)`, `Medical Director Requirement`, `Corporate Practice of Medicine Rules`, `ENGINE_REGISTRY` (+15 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Spa Analytic (Product)` and `Django==6.1 dependency`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Lumen Aesthetics & Wellness (worked example client)` and `Austin Botox Study (573 Responses)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `The Claims Filter (Seven Checks)` connect `Claims Safety & Regulatory Review` to `Hard Rules & Compliance Constraints`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Why does `Spa Analytic Marketing Landing Page` connect `Product Positioning & Frontend Rules` to `Claims Safety & Regulatory Review`, `Engagement Deliverables & Agent Pipeline`, `Prompt Set Design`?**
  _High betweenness centrality (0.130) - this node is a cross-community bridge._
- **Why does `Design Token System (tokens.css)` connect `Product Positioning & Frontend Rules` to `Core Data Model & Measurement Pipeline`?**
  _High betweenness centrality (0.114) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `ReportRequest` (e.g. with `ReportRequestAdmin` and `Meta`) actually correct?**
  _`ReportRequest` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `The Claims Filter (Seven Checks)` (e.g. with `Claims Filter as Mandatory Stage` and `'What We Don't Promise' List`) actually correct?**
  _`The Claims Filter (Seven Checks)` has 2 INFERRED edges - model-reasoned connections that need verification._