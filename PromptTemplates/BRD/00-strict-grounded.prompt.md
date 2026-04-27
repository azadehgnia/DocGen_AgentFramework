Populate the attached BRD template end to end using the attached project context files.

This variant is optimized for minimal hallucination and maximum evidence discipline.

Inputs:

- The BRD markdown template
- All attached project context files provided by the user

Core operating rules:

- Do not guess.
- Do not fill gaps with plausible business language.
- Do not infer names, dates, process IDs, owners, priorities, risks, controls, rules, or metrics unless the source files explicitly support them.
- If a detail is not directly supported, leave it blank or write `[To be confirmed]`.
- It is better to produce an incomplete but trustworthy BRD than a polished but speculative BRD.

Required workflow:

1. Read every attached file before writing any BRD content.
2. Build an internal evidence inventory using only explicit statements from the source files.
3. Populate the BRD using the exact markdown structure below.
4. For each BRD section, fill only fields that are supported by that evidence inventory.
5. If a section has insufficient evidence, preserve the structure and leave most of it blank.
6. Keep image, diagram, and document placeholders when the user did not attach the underlying artifact.
7. Return markdown only.
8. Return the completed BRD followed by a final section titled `Evidence Gaps And Missing Inputs`.

Use this exact markdown format for the BRD body:

See the exact scaffold below and preserve it verbatim when drafting.

```markdown
|  |
| --- |
| Business Requirements Document – <P0XXXX Insert Project Name> |
| April 2026 |
|  |

---

Table 0   Version control

| **Version** | **Release date** | **Changes** | **Name** |
| --- | --- | --- | --- |
| 0.1 |  |  |  |
|  |  |  |  |


Table 1   Document acceptance

Written confirmation not required

| **Name** | **Title** | **Version #** | **Signature/email confirmation** | **Date** |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Table 2   Document Reviewers

| **Name** | **Title** | **Purpose** |
| --- | --- | --- |
|  |  |  |
|  |  |  |



---

# 1        Introduction

## 1.1     Project context

## 1.2     Project purpose

## 1.3     Definitions

## 1.4     Audience
## 1.5     Document objective

## 1.6     Stakeholders

### 1.6.1      Requirement stakeholders

The table below identifies people who
contributed to the process of defining or reviewing the requirements for the
<<*project/workstream>>*.

| **SN#** | **Contributor** | **Role** |
| --- | --- | --- |
| 1. |  |  |
| 2. |  |  |
| 3. |  |  |
| 4. |  |  |

### 1.6.2      Impacted participant categories

*(If known)*

| **Participant category** | **Potential impact description** |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |

### 1.6.3      Impacted business units

*(If known)*

| **Business unit** | **Potential impact description** |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |

## 1.7         Reference documents

Table 3   List of reference documents

| **Ref#** | **Version** | **Document name** | **Owner** | **Comments** |
| --- | --- | --- | --- | --- |
| 1. |  |  |  |  |
| 2. |  |  |  |  |
| 3. |  |  |  |  |

## 1.8     Scope

### 1.8.1      In scope

### 1.8.2      Out of scope

## 1.9     Facts

The following facts have been identified
(or made) with respect to this stakeholder requirement analysis:

1.

2.

3.

## 1.10 Assumptions

The following assumptions have been
identified (or made) with respect to this stakeholder requirement analysis:

1.

2.

3.

## 1.11 Risks

The following dependencies are identified
with respect to this this stakeholder requirement analysis:

1.

2.

3.

## 1.12  Dependencies

The following dependencies are identified
with respect to this this stakeholder requirement analysis:

1.

2.

## 1.13  Unknowns

The following unknowns are identified
with respect to this this stakeholder requirement analysis:

1.

2.

# 2        Context for business requirements

Business requirements are written to
enable forward traceability which maps Project Drivers to their relevant
benefits, and each benefit to their respective business requirements. Business Requirements are derived from the
Impacted Level 3 Capability from BCM and scope that is defined by Value chain
and Process Catalogue.

## 2.1     Business Capability Model (BCM)

The Business
Capability Model provides a high-level overview of the organisation's business capabilities
and their relation, outlining the core business functions in a
hierarchical manner. It is the blueprint of the organisation which encapsulates
what the business is doing currently as well as what it needs to do to fulfil
its mission or meet future challenges.​​​​​​​​​​​​​​​​​​​​​​​​​​​

### 2.1.1      Impacted Business Capabilities

Mapping below indicates which business
capbilities are fully impacted (green) and partially impacted (yellow) as part
of this project.

<insert impacted Business Capability
Model Figure (ensure correct resolution e.g. GIF)>

Figure 1
Business Capability Model

| **BCM Level 3** | **Capability Description** | **Impact (Fully/Partially /Leveraged)** | **Impact Description (Optional)** | **Systems Impacted (if known)** |
| --- | --- | --- | --- | --- |
| X.X.X Xxxx |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## 2.2     Value Chain and Process Catalogue

A Value Chain is an
end-to-end set of activities which collectively create value for stakeholders.

<Insert image of Value Chain or link of
the pack that is endorsed>

### 2.2.1      Value Chain Descriptions

| **Value Chain Activity** | **High-level description** | **Linked BCM Level 3** |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

### 2.2.2      Process Catalogue

<Insert image
of  Value Chain and Process Catalogue>

| **Value Chain Activity** | **Process name** | **Process  description** | **Linked BCM Level 3** | **Process available in Repository (Y/N)** |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## 2.3     Business Process

<insert as-is Process Map diagram. *If
High level current available*>

Figure 2
Current State Process Map

---

# 3        Business requirements

This section covers the high-level business
requirements and user stories for each of the processes identified in the
process catalogue.

## 3.1     [Process 1/ Value chain Function 1 requirements]

<Process 1 Description> (Insert
current state available)

### 3.1.1      Basic flow

(optional)

<insert as-is Level 4 catalogue flow
diagram>

### 3.1.2      Sub-processes

The following sub-processes defines
business requirements related to [process ID and name] processes.

*If Applicable*

|  |  |  |  |
| --- | --- | --- | --- |
| **Process ID** | **Sub-Process No.#** | **Sub-Process Name** | **Process Description** |
|  | 1. |  |  |
|  | 2. |  |  |

### 3.1.3      Requirements

#### 3.1.3.1      Use Case Description

| **Use case 1.** | **Priority (M/D):** | **Process ID:** | **Req. Owner:** | **Req. Author:** |
| --- | --- | --- | --- | --- |
| **Goal** |  | | | |
| **Business Scenarios** |  | | | |
| **Actors** |  | | | |
| **Interaction** |  | | | |
| **Assumption** |  | | | |
| **Pre-conditions** |  | | | |
| **Post-conditions** |  | | | |
| **Note** |  | | | |

#### 3.1.3.2      Use Case 1 Requirements

*Or Extract of JIRA requirements*

Table 4   [Process 1 Use Case 1] Business Requirements

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **BR ID#** | **Priority (MoSCoW)** | **Business Requirement** | **Dependencies/**  **Assumptions** | **Business Rule** | **Process ID** |
| **BR1.** |  |  | • | • |  |
| **BR2.** |  |  |  |  |  |

## 3.2     [Process 2/ Value chain Function 2 requirements]

<Process 1 Description> (Insert
current state available)

### 3.2.1      Basic flow

(optional)

<insert as-is Level 4 catalogue flow
diagram>

### 3.2.2      Sub-processes

The following sub-processes defines
business requirements related to [process ID and name] processes.

*If Applicable*

|  |  |  |  |
| --- | --- | --- | --- |
| **Process ID** | **Sub-Process No.#** | **Sub-Process Name** | **Process Description** |
|  |  |  |  |
|  | 3. |  |  |

### 3.2.3      Requirements

#### 3.2.3.1      Use Case Description

| **Use case 2.** | **Priority (M/D):** | **Process ID:** | **Req. Owner:** | **Req. Author:** |
| --- | --- | --- | --- | --- |
| **Goal** |  | | | |
| **Business Scenarios** |  | | | |
| **Actors** |  | | | |
| **Interaction** |  | | | |
| **Assumption** |  | | | |
| **Pre-conditions** |  | | | |
| **Post-conditions** |  | | | |
| **Note** |  | | | |

#### 3.2.3.2      Use Case 2 Requirements

*Or Extract of JIRA requirements*

Table 5   [Process 2 Use Case 1] Business Requirements

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **BR ID#** | **Priority (MoSCoW)** | **Business Requirement** | **Dependencies/**  **Assumptions** | **Business Rule** | **Process ID** |
| **BR3.** |  |  | • | • |  |
| **BR4.** |  |  |  |  |  |

---

# 4        Non-functional requirements

For business non-functional
requirement field definitions see [A1.2](#NFRGlossary).

| **NFR ID#** | **Priority (MoSCoW)** | **Category** | **Requirement rationale (optional)** | **Non-functional requirement statement** |
| --- | --- | --- | --- | --- |
| PXXXX\_NFR001 |  |  |  |  |
| PXXXX\_NFR002 |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

---

# 5            Documentation

The
following documentation requires creating or updating and uploading to the participant-facing website or the organisation's internal knowledge pages.

| **Doc ref.** | **Document name (if known)** | **Type** | **Audience** | **New/existing** | | **Consultation required?** | **Responsible** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **1.** |  |  |  |  |  | | |
| **2.** |  |  |  |  |  | | |
| **3.** |  |  |  |  |  | | |
|  |  |  |  |  |  |  |  |

---

Appendix

A1.1
Requirement template field
definitions

Business requirements representation of
goals, objectives and outcomes that describe why a change has been initiated
and how success will be assessed.

Each requirement in this document has at
least one of the following prioritiesassigned:

**M – Must have** (all the requirements necessary for successful completion of the
project)
**S – Should have** (requirements that are important for project completion
but not necessary)
**C – Could have** (requirements that are nice to have, but not necessary
for project completion)
**W – Will not have** (all the requirements that have been recognised as not
a priority for the project)

To clarify, there are two levels of
prioritisation, stakeholder requirements will be the first level of
prioritisation, and functional requirements will form the second level of
prioritisation.

Requirements Structure

The structure of
the business requirements is as follows:

| **Field** | **Definition** |
| --- | --- |
| BR ID # | Every business requirement defined in this document will have a unique Business Requirement Identity (BR ID). A BR ID will be a unique ID across all business requirements documents prepared for the WDER project. This unique BR ID is used for  a. Identification of the requirement;  b. Estimation;  c. Traceability; and   d. Review |
| Business Requirement | The business requirement statement |
| Dependencies/ Assumptions |  |
| Business Rule |  |
| Process ID | Process maps are documented in the Level 4 Process Catalogue, which can be used to derive business requirements. Requirements are broken up by each process impacted by the project. The Process ID # refers to the Level 4 process map ID requirements are being written for. |
|  |  |
| Business unit | Defines responsibility for ongoing maintenance and support of this process once implemented. |
| Rule ref # | *This is only relevant to Reform/Rule change delivery projects*. This is a reference ID used for traceability of clauses to business requirements and ensures that all clauses are covered as part of BR analysis.|
| Traceability | Traceability is the ability to look at a requirement to which it is related, linking business requirements to stakeholder and solution requirements, to artefacts and to solution components. Traceability help identifies and documents the lineage of each requirement, including its backward traceability (derivation), forward traceability (allocation) and its relationship to other requirements. Relationships used in the project are:  1. **Derive**: Is used when one requirement is derived from another e.g., stakeholder requirements may be derived from the Final Rule or the Business Requirements, and then solution requirements (functional / non-functional) are derived from stakeholder requirements, and so on.   2. **Depend**: Is used when one requirement has a dependency on another requirement, where the requirement precedes or succeeds another, i.e. can only be implemented if other related requirements are also implemented at the same time.  3. **Satisfy**: Is used when a requirement satisfies another requirement or implementation element (often something technical e.g., config item).  4. **Validate**: Is used when a requirement validates whether the solution fulfils the requirement (e.g., solution requirement) via another requirement, a test case or another implementation element. |

Format of business requirements in this
document is:

| **BR ID#** | **Priority (MoSCoW)** | **Business Requirement** | **Dependencies/** **Assumptions** | **Business Rule** | **Process ID** |
| --- | --- | --- | --- | --- | --- |
| **BR1.** |  |  | • | • |  |
| **BR2.** |  |  |  |  |  |

A1.2     Requirements Traceability

Business requirements are written to
enable forward traceability which maps Project Drivers to their
relevant business requirements. The same business requirements will then
be used to further map to stakeholder requirements or user stories, functional
requirements, technical design, and other requirements as the project forms.

Constraints

Potential constraints to this analysis
are:

1.     **Implicit Requirements**: The analysis conducted as part of the identification of business
requirements process, it is understood that various system and business
processes will leverage existing organisational processes. To avoid any implicit
requirements being missed the analysis explicitly assumes ‘implied’
requirements and has documented them where possible. However, while measures
have been taken to prevent implicit requirements being missed, there is still a
possibility that some requirements may still be missed. Therefore, it is strongly
recommended for document reviewers and approvers to identify such missing
implied requirements and ensure they are added in this document.

2.     **Integrated Functions:** The implementation of the requirements include integration of
processes and systems for the relevant business units within the context
of the project.
---

A1.3     Non-functionalcategory
definitions

Non-functional requirements (also known
as quality attributes or quality of service requirements) are often associated
with system solutions, but they also apply more broadly to both process and
people aspects of solutions. They augment the functional requirements of a
solution, identify constraints on those requirements, or describe quality
attributes a solution must exhibit when based on those functional requirements.

| **Term** | **Definition** |
| --- | --- |
