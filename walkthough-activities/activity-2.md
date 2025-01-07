# ![Digital Futures Academy](https://github.com/digital-futures-academy/DataScienceMasterResources/blob/main/Resources/datascience-notebook-header.png?raw=true)

## ETL Pipeline Project Walkthrough

## Activity 2 ETL Pipeline High-Level Plan and Subprocesses

### Activity 2.1 - High-Level Flowchart

Identify the missing steps in the high-level flowchart.  Preview the document to see flowchart, edit the `label` key to add the missing steps.

```mermaid
flowchart TD
    A@{ shape: stadium, label: "Start: Data Sources"} --> B@{ shape: tri, label: "Extract Data"}
    B --> C1@{ shape: cyl, label: "Source 1: Database"}
    B --> C2@{shape: doc, label: "Source 2: CSV file"}
    C1 --> D[Data Cleaning]
    C2 --> D[Data Transformation]
    D --> E[Data Quality]
    E --> F[Testing]
    F --> G([Deploy Pipeline])
    

```

---

### Activity 2.2 - ??? Subprocesses

Identify the missing subprocesses in the data cleaning flowchart.  Preview the document to see flowchart, edit the `label` key to add the missing subprocesses.

```mermaid

flowchart LR
    A[???*] --> B1@{shape: subproc, label: "???"}
    B1 --> B2@{shape: subproc, label: "???"}
    B2 --> B3@{shape: subproc, label: "???"}
    B3 --> B4@{shape: subproc, label: "???"}
    B4 --> B5@{ shape: lean-r, label: "Cleaned Data" }
```

---

## Activity 2.3 - Data Transformation Subprocesses

Identify the missing subprocesses in the data transformation flowchart.  Preview the document to see flowchart, edit the `label` key to add the missing subprocesses.

```mermaid
flowchart LR
    A[???**] --> B1@{shape: subproc, label: "???"}
    B1 --> B2@{shape: subproc, label: "???"}
    B2 --> B3@{shape: subproc, label: "???"}
    B3 --> B4@{shape: subproc, label: "???"}
    B4 --> B5@{ shape: lean-r, label: "Transformed Data" }
```

---

## Activity 2.3 - Loading Subprocesses

Identify the missing subprocesses in the loading flowchart.  Preview the document to see flowchart, edit the `label` key to add the missing subprocesses.

```mermaid
flowchart LR
    A[???***] --> B1@{shape: subproc, label: "???"}
    B1 --> B2@{shape: subproc, label: "???"}
    B2 --> B3@{shape: subproc, label: "???"}
    B3 --> B4@{shape: subproc, label: "???"}
    B4 --> B5@{shape: subproc, label: "???"}
    B5 --> B6@{shape: subproc, label: "???"}
    B6 --> B7@{shape: lean-r, label: "Final Dataset in SQL Table"}
```

---

## Deployment Subprocesses

This will be covered later in the project walkthrough.

---

---
