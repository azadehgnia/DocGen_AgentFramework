Populate section 3 of the attached BRD template only.

Inputs:

- The BRD markdown template
- Attached project context files provided by the user

Instructions:

- Read all attached files first.
- Fill only section 3 of the BRD.
- Preserve the exact markdown structure shown below.
- Replace placeholders and blank cells only where the attached files support the content.
- Draft business requirements from a business perspective, not an implementation-design perspective, unless the source explicitly states a design constraint.
- Do not invent process IDs, owners, priorities, authors, assumptions, or business rules.
- If the source files support only one process, populate one process section well and leave the other section mostly in template form.
- Return markdown only.
- Return only the completed content for the section below.

Use this exact markdown format:

```markdown
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
```
