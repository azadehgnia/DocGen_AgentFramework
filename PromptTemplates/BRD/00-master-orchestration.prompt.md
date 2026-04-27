Populate the attached BRD template end to end using the attached project context files.

Inputs:

- The BRD markdown template
- All attached project context files provided by the user

Instructions:

1. Read all attached files carefully before drafting.
2. Extract a fact base from the source files before writing.
3. Populate the BRD using the exact markdown structure below.
4. Replace placeholders and blank cells only where the attached files support the content.
5. If information is missing, leave table cells blank or write `[To be confirmed]` in prose.
6. Do not fabricate project names, dates, stakeholder names, owners, process IDs, priorities, business rules, compliance obligations, or performance thresholds.
7. Keep placeholders for diagrams or images if the user did not provide those assets.
8. Keep requirement statements business-oriented, concise, and testable where possible.
9. Return markdown only.
10. Return the completed BRD followed by a final section titled `Missing Inputs Needed From User`.

Use this exact markdown format for the BRD body:

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
| Rule ref # | *This is only relevant to Reform/Rule change delivery projects*.|
| Traceability | Traceability is the ability to look at a requirement to which it is related, linking business requirements to stakeholder and solution requirements, to artefacts and to solution components. Traceability help identifies and documents the lineage of each requirement, including its backward traceability (derivation), forward traceability (allocation) and its relationship to other requirements. Relationships used in the project are:  1. **Derive**: Is used when one requirement is derived from another e.g., stakeholder requirements may be derived from the Final Rule or the Business Requirements, and then solution requirements (functional / non-functional) are derived from stakeholder requirements, and so on.   2. **Depend**: Is used when one requirement has a dependency on another requirement, where the requirement precedes or succeeds another, i.e. can only be implemented if other related requirements are also implemented at the same time.  3. **Satisfy**: Is used when a requirement satisfies another requirement or implementation element (often something technical e.g., config item).  4. **Validate**: Is used when a requirement validates whether the solution fulfils the requirement (e.g., solution requirement) via another requirement, a test case or another implementation element. |

Format of business requirements in this
document is:

| **BR ID#** | **Priority (MoSCoW)** | **Business Requirement** | **Dependencies/** **Assumptions** | **Business Rule** | **Process ID** |
| --- | --- | --- | --- | --- | --- |
| **BR1.** |  |  | • | • |  |
| **BR2.** |  |  |  |  |  |

A1.2     Requirements Traceability

Business requirements are written to
enable forward traceability which maps Project Drivers to their relevant business requirements. The same business requirements will then
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
| Alerting | Describes the requirements for alerts. Alerts are brief, usually human-readable, technical notification regarding current vulnerabilities, exploits, and other security issues. |
| Access Management | To identify, track, control and manage authorized or specified users' access to a system or application.   Any member of the concerned team can access and run the report as they see fit. |
| Auditability | The degree to which the platform supports an examination of the management controls within the IT infrastructure. The ability to log and monitor events that occur on the platform. Include the watermark used for screenshots and prints for audit purposes. Also often independent certification. |
| Availability | Degree to which the solution is operable and accessible when required for use   - percentage of time the solution is available    The solution must be available during the organisation's business hours (e.g. 8am-6pm) or extended business hours of operation (e.g. 8am-9pm) depending on the business criticality  - Maximum acceptance Outage  - Metrics can be determined for the solution as a whole, for components of the solution or on a process basis as best suits the scope and nature of each project   - It must also be verified that upstream and downstream systems which have functional implications on the solution have aligned availability |
| Backup & Recovery | All system data must be backed up and stored so that can be used to protect organizations against data loss. The solution must be able to be restored from backup |
| Capacity | The solution must be able to handle concurrent users without any noticeable impact to services. (E.g.: Ability to have 4-5 users to run and use the report at the same time.) |
| Compatibility | The characteristics of the platform which can operate satisfactorily together on the same computer, or on different computers linked by a computer network. Or the degree to which the solution operates effectively with other components in the environment. |
| Compliance | Regulatory, financial, or legal constraints which can vary based on the context or jurisdiction. |
| Data Quality & Integrity | Data quality refers to the condition of a set of values of qualitative or quantitative variables. Data is generally considered high quality if it is fit for its intended uses in operations, decision making and planning. Or the degree to which the data maintained by the software system are accurate, authentic, and without corruption. |
| Data Retention | Relates to the ability of a solution to safely store and retrieve data from previous periods in a readily accessible format |
| Disaster Recovery | The process, policies and procedures that are related to preparing for recovery or continuation of technology infrastructure and Business in an instance of a disaster. |
| Documentation | The solution must have the appropriate documentation related to the software delivery lifecycle documented in the organisation's standard repository tool (e.g. Confluence and/or SharePoint) |
| Error Handling | Error handling refers to the response and recovery procedures from error conditions present in a software application. In other words, it is the process comprised of anticipation, detection and resolution of application errors, programming errors or communication errors. Error handling helps in maintaining the normal flow of program execution. |
| Localisation | Requirements dealing with local languages, laws, currencies, cultures, spellings and other characteristics of users which requires attention to the context.    - Ability to be adapted to suit a particular business operating environment  - Capacity for the system to be adapted to needs relating to one or more geographical/economic location  - Coping with international operation eg: multi-currency, different languages, keyboard configurations etc.    Remember that even for solutions which operate only in Australia that there are three different time-zones and hence there is a need to consider regionalism |
| Logging & Monitoring | The ability to log and monitor events that occur on the platform. The solution must align with the organisation's enterprise architecture strategy and current standard logging and monitoring tool. (All system errors must be logged and accessible for support staff for troubleshooting) |
| Integrability | Integrity is the degree to which the data maintained by the software system are accurate, authentic, and without corruption. |
| Maintainability & Serviceability | The ability of technical support personnel to install, configure, and monitor the platform, identify exceptions or faults, debug, or isolate faults to root cause analysis, and provide hardware or software maintenance in pursuit of solving a problem and restoring the platform into service.    The solution must ensure that the application can not only be maintained once delivered into production but meets any regulatory requirements in the future. |
| Performance & Response Time | The amount of work accomplished by the platform. Degree to which a solution or component performs its designated functions with minimum consumption of resources. How quickly should the system respond to a request from the user / system?   Can be defined based on the context or period, such as high-peak, mid-peak or off-peak usage    The length of time taken for a person or system to react to a given stimulus or event.  e.g. response time when the ‘submit’ button on application creation screen is clicked it should take less than 2 seconds to create relevant records |
| Reliability | The ability of the platform to function under stated conditions for a specified period of time. E.g.  - mean time to failure of a device  - calculation of mathematical formula and returning results within a specific period of time |
| Reporting | The areas and parameters a platform must report on. |
| Scalability | The capability of the platform to handle a growing amount of work, or its potential to be enlarged to accommodate that growth. Or the  ability for the solution to grow or evolve (horizontally and vertically) to handle increased amounts of work    - Horizontal = Horizontal scalability is the ability to increase capacity by connecting multiple hardware or software entities so that they all work as a single logical unit  - Vertical = Vertical scalability is the ability to increase the capacity of existing hardware or software by adding resource. |
| Security | Aspects of the solution that protect solution content or solution components from accidental or malicious access, use, modification , destruction or disclosure |
| Service Level Agreements (SLAs) | A Service Level Agreement (SLA) is an agreement between an IT service provider and a customer. The content of an SLA is about quality standards that are assigned to products, processes and services. An example of an SLA standard for an application is: availability of 99,9% with a maximum of 3 incidents per year and a maximum of 3 hours outage. Service may sometimes be swapped out for product in this context. |
| Throttling | The process of limiting the number of requests a user or application can make in a certain period |
| Training & Support | Necessary training to be provided to system users through the Change Management Plan.    Support must be available during business hours of operation (8am-6pm) or extended business hours of operation (8am-9pm). |
| Usability | The degree to which the platform can be used by specified consumers to achieve quantified objectives with effectiveness, efficiency, and satisfaction in a quantified context of use. Or the ease with which a user can learn to use the solution |

---

A1.4     Glossary

*Update this glossary where acronyms
from your project aren’t listed, or to shorten the list to acronyms only
relevant to your project*


| **Term** | **Definition** |
| --- | --- |
