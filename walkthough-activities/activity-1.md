# ![Digital Futures Academy](https://github.com/digital-futures-academy/DataScienceMasterResources/blob/main/Resources/datascience-notebook-header.png?raw=true)

## ETL Pipeline Project Walkthrough

---

---

## Activity 1: Identify the User Stories

| Epic                                                 | User Requirements                                                                         |
|------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Epic 1: Data Availability, Quality and Trust         | Analysts need a single, clean dataset combining transaction and demographic data.         |
|                                                      | Data scientists need the cleaned dataset stored in a SQL table for analysis.              |
| Epic 2: Customer Insights                            | Analysts want to analyze spending per customer and identify high-value customers.         |
|                                                      | Business stakeholders would like to identify customers who have spent more than **$500**. |
| Epic 3: Demographic Trends                           | Business stakeholders want insights into age and country trends of key customers.         |
| Epic 4: Data Access and Storage                      | Scientists need assurance that the data is clean, consistent, and accurate.               |
|                                                      | Scientists need the cleaned dataset stored in a SQL table for analysis.                   |
|                                                      | Scientists need to be able to reset and update the data for repeat or future analysis     |

Given these epics and their requirements, create user stories for each epic.  There is a hint as to how many stories are needed and the stakeholders involved in it.

### User Stories

#### Epic 1: Data Availability, Quality, Trust and Access

```txt
As a Data Analyst,  
I want to obtain a single, clean dataset combining transantion and demogragraphic data,  
So that I can do further analytics and gather insights

As a Data Scientist,
I want to acquire a cleaned dataset stored in a SQL table,
So that I can carry out further analysis
```

#### Epic 2: Customer Insights

```txt
As a Data Analyst,  
I want to analyze spending per customer and identify high-value customers,  
So that I can gather data insights on customer spending

As a Business Stakeholder,  
I want to identify customers that have spent more than $500,  
So that I can identify key customers
```

#### Epic 3: Demographic Trends

```txt
As a Business Stakeholder,  
I want insights into age and country trends of key customers,  
So that I can identify demographic trends in customers
```

#### Epic 4: Data Storage and Access

```txt
As a Data Scientist,  
I want assurance that the data is clean, consistent, and accurate and stored in a SQL table for analysis,  
So that I can gather insights smoothly, without dealing with errors due to database quality.

As a Data Scientist,
I want to reset and update the data for repeat or future analysis,
So that can further my analysis.
```

---

## Activity 1.2: Acceptance Criteria and Definition of Done

Review this definition of done for the ETL pipeline project with your team.  This has been agreed between the team's Product Owner, Data Analysts, Data Scientists and the Business Stakeholders.

For each of the user stories identified, complete the missing information in Acceptance Criteria that will ensure the story meets the definition of done.

---

## Definition of Done

### Code Quality

- [ ] Code follows the project's coding standards and best practices.
  - ***SQL***:
    - **Query Performance**: Queries should execute in less than 2 seconds for typical operations.
    - **Readability and Maintainability**: Queries should be formatted for readability with consistent indentation, meaningful aliases, and comments.
    - **Use of Best Practices**: Follow best practices such as avoiding `SELECT *`, using `JOINs` appropriately, and ensuring proper *indexing*.
    - **Linting**: SQL code should be linted for syntax errors and compliance with best practices.
  - ***Python***:
    - **PEP 8 Compliance**: Code should follow PEP 8 guidelines. Use a linter (e.g., flake8) to ensure compliance.
    - **Code Readability**: Use meaningful variable names, consistent indentation, and comments to explain complex logic.
    - **Modularity**: Functions and classes should be used to encapsulate logic and promote reuse.
    - **Error Handling**: Use `try-except` blocks to handle exceptions and provide meaningful error messages.
  - ***Pandas***:
    - **Efficient Data Manipulation**: Use vectorised operations instead of loops for data manipulation.
    - **Memory Usage**: Use appropriate data types and avoid loading unnecessary data into memory.
    - D**ata Validation**: Check for missing values, data types, and data ranges before performing operation
- [ ] Code is reviewed and approved by at least one other team member.
- [ ] Code is free of critical and high-severity bugs.

---

### Testing

- [ ] **Unit tests** are written and cover all new functionality.
- [ ] **Integration tests** are written and cover interactions between components.
- [ ] **Component tests** are written and validate individual parts of the system.
- [ ] All tests pass successfully.
- [ ] ***Test coverage*** meets the the ***90%*** threshold for the project.

---

### Documentation

- [ ] Code is documented with clear and concise comments.
- [ ] User-facing documentation is updated to reflect new or changed functionality.
- [ ] Any relevant diagrams or flowcharts are updated.

---

### Performance

- [ ] Performance benchmarks are met (e.g., data extraction and cleaning times are within acceptable limits).
  - **Database Extraction**: *Less than 1 minute* for *10,500 rows* with *4 fields*.
  - **CSV Extraction**: *Less than 30 seconds* for *5,200 rows* with *5 columns*.
  - **Data Cleaning**: *Less than 1 second* per *1,000 rows*.
  - **Data Transformation**: *Joins* and *aggregations* take *less than 5 seconds* per *10,000 rows*.
  - **Data Loading**: *Less than 5 seconds* per *10,000 rows*.
  - **End-to-End Processing**: The entire ETL process *completes within 30 minutes* for a full dataset.
  - [ ] No significant performance regressions are introduced.

---

### Data Quality

- [ ] Data is validated for accuracy, completeness, and consistency.
  - **Accuracy**: *99%* of records are accurate.
  - **Completeness**: *100%* of expected columns and rows are present.
  - **Consistency**: *100%* of records have consistent formats and values.
  - **Integrity**: *100%* of records maintain integrity constraints.
  - **Error Rate**: *Less than 1%* error rate.
  - **Validation Time**: *Less than 1 second* per *1,000 rows*.
- [ ] Data cleaning rules are applied, and logs are generated for any issues encountered.
  - **Duplicate Removal Rate**: *100%* of duplicates removed (e.g., 0% duplicates remain).
  - **Null Handling Rate**: *100%* of missing or invalid fields resolved.
  - **Data Completeness**: *100%* of *expected* *columns* and *rows* are present.
  - **Data Consistency**: *100%* of records have consistent formats.
  - **Cleaning Time**: *Less than 1 second* per *1,000 rows*.
  - **Error Rate**: *Less than 1%* error rate.
- [ ] Data transformation logic is verified and tested.

---

### Deployment

- [ ] Code is deployed to the appropriate environment (e.g., staging, production).
- [ ] Deployment scripts and configurations are updated as needed.
- [ ] Deployment is verified and tested in the target environment.

---

### Acceptance Criteria

- [ ] All acceptance criteria for the user story are met.
- [ ] The user story is demonstrated to and accepted by the product owner or relevant stakeholders.

---

### Metrics and Monitoring

- [ ] Relevant metrics (e.g., record count accuracy, extraction performance) are collected and reviewed.
- [ ] Monitoring and alerting are set up for critical components.

---

### Compliance

- [ ] All work complies with relevant legal, regulatory, and security requirements.

---

---

### Activity 1.2 - Complete Acceptance Criteria

Certain metrics for each user story's Acceptance Criteria have been identified.  Complete the missing information (signified by ***...***) for each user story.

#### For Epic 1: Data Availability, Quality, and Trust

```txt
As a Data Analyst,  
I want access to a single, clean, and accurate dataset combining customer demographics and transaction data,  
So that I can analyse customer behaviour without worrying about data inconsistencies and can rely on it for analysis without manual checks.
```

***Acceptance Criteria***

- **Data Extraction**
  - [ ] Given the database contains  ***...*** rows with  ***...*** fields, when the data is extracted, then it should complete in less than  ***...*** minute.
  - [ ] Given the CSV file contains  ***...*** rows with  ***...*** columns, when the data is extracted, then it should complete in less than  ***...*** seconds.
- **Data Cleaning**
  - [ ] Given the extracted data, when duplicates are removed, ***...***
  - [ ] Given the extracted data, when missing values are handled, then ***...*** of missing should be resolved.
  - [ ] Given the extracted data, when invalid values are handled, then ***...*** of invalid fields should be resolved.
  - [ ] Given the extracted data, when data cleaning is performed,  ***...***
- **Data Transformation**
  - [ ] Given the cleaned data, when the customer demographics dataset (CSV) and transaction dataset (database) are merged, then the merge should be performed correctly using the  ***...***` field as the key.
  - [ ] Given the cleaned data, when calculating the total amount spent by each customer, then the  ***...*** field should be accurate and reflect the sum of all amount values for each  ***...***.
  - [ ] Given the cleaned data, when filtering for active customers, then only customers with  ***...*** set to  ***...*** should be included.
- **Data Quality**
  - [ ] Given the transformed dataset, when data validation is performed, then 99% of records should be accurate.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of expected columns and rows should be present.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of records should have consistent formats and values.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of records should maintain integrity constraints.
  - [ ] Given the transformed dataset, when data validation is performed, then the error rate should be less than 1%.
  - [ ] Given the transformed dataset, when data validation is performed, then it should complete in less than 1 second per 1,000 rows.
- **Documentation**
  - [ ] Code should be documented with clear and concise comments.
  - [ ] User-facing documentation should be updated to reflect new or changed functionality.
- **Testing**
  - [ ] Unit tests should cover all new functionality.
  - [ ] Integration tests should cover interactions between components.
  - [ ] All tests should pass successfully.
  - [ ] Test coverage should meet the project's required threshold of 90%.

---

#### For Epic 2: Customer Insights

```txt
As a Data Analyst,  
I want to know how much each customer has spent and their average transaction value,  
So that I can identify high-value customers for further analysis
```

***Acceptance Criteria***

- **Data Transformation**
  - [ ] Given the cleaned data, when calculating the total amount spent by each customer, then the  ***...*** field should be accurate and reflect the sum of all amount values for each  ***...***.
  - [ ] Given the cleaned data, when calculating the average transaction value for each customer, then the  ***...*** field should be accurate and reflect the average of all amount values for each  ***...***.
  - [ ] Given the cleaned data, when filtering for high-value customers, then only customers with a  ***...*** greater than  ***...*** should be included.
- **Data Quality**
  - [ ] Given the transformed dataset, when data validation is performed, then 99% of records should be accurate.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of expected columns and rows should be present.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of records should have consistent formats and values.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of records should maintain integrity constraints.
  - [ ] Given the transformed dataset, when data validation is performed, then the error rate should be less than 1%.
- **Documentation**
  - [ ] Code should be documented with clear and concise comments.
  - [ ] User-facing documentation should be updated to reflect new or changed functionality.
- **Testing**
  - [ ] Unit tests should cover all new functionality.
  - [ ] Integration tests should cover interactions between components.
  - [ ] All tests should pass successfully.
  - [ ] Test coverage should meet the project's required threshold of 90%.

```txt
As a Business Stakeholder,  
I want to identify high-value customers who have spent more than $500,  
So that we can target them for loyalty rewards
```

***Acceptance Criteria***

- **Data Transformation**
  - [ ] Given the cleaned data, when calculating the total amount spent by each customer, then the  ***...*** field should be accurate and reflect the sum of all  ***...*** values for each  ***...***.
  - [ ] Given the cleaned data, when filtering for high-value customers, then only customers with a  ***...*** greater than  ***...*** should be included.
- **Data Quality**
  - [ ] Given the transformed dataset, when data validation is performed, then 99% of records should be accurate.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of expected columns and rows should be present.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of records should have consistent formats and values.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of records should maintain integrity constraints.
  - [ ] Given the transformed dataset, when data validation is performed, then the error rate should be less than 1%.
- **Documentation**
  - [ ] Code should be documented with clear and concise comments.
  - [ ] User-facing documentation should be updated to reflect new or changed functionality.
- **Testing**
  - [ ] Unit tests should cover all new functionality.
  - [ ] Integration tests should cover interactions between components.
  - [ ] All tests should pass successfully.
  - [ ] Test coverage should meet the project's required threshold of 90%.

---

#### For Epic 3: Demographic Trends

```txt
As a Business Stakeholder,  
I want to analyse demographic trends, such as customer age and country, among high-value customers,  
So that I can tailor our marketing campaigns to reach them effectively
```

***Acceptance Criteria***

- **Data Transformation**
  - [ ] Given the cleaned data, when identifying high-value customers, then only customers with a  ***...*** greater than  ***...*** should be included.
  - [ ] Given the high-value customers, when analysing demographic trends, then the analysis should include  ***...*** and  ***...*** fields.
- **Data Analysis**
  - [ ] Given the high-value customers, when calculating demographic trends, then the average  ***...*** and distribution by  ***...*** should be accurately calculated.
  - [ ] Given the high-value customers, when generating demographic reports, then the reports should include visualizations (e.g., charts, graphs) of  ***...*** and  ***...*** distributions.
- **Data Quality**
  - [ ] Given the demographic analysis, when data validation is performed, then 99% of records should be accurate.
  - [ ] Given the demographic analysis, when data validation is performed, then 100% of expected columns and rows should be present.
  - [ ] Given the demographic analysis, when data validation is performed, then 100% of records should have consistent formats and values.
  - [ ] Given the demographic analysis, when data validation is performed, then 100% of records should maintain integrity constraints.
  - [ ] Given the demographic analysis, when data validation is performed, then the error rate should be less than 1%.
- **Documentation**
  - [ ] Code should be documented with clear and concise comments.
  - [ ] User-facing documentation should be updated to reflect new or changed functionality.
- **Testing**
  - [ ] Unit tests should cover all new functionality.
  - [ ] Integration tests should cover interactions between components.
  - [ ] All tests should pass successfully.
  - [ ] Test coverage should meet the project's required threshold of 90%.

---

#### For Epic 4: Data Storage and Access

```txt
As a Data Scientist,  
I want the cleaned and enriched data to be stored in a SQL table,  
So that I can query it directly for advanced analysis
```

***Acceptance Criteria***

- **Data Loading**
  - [ ] Given the cleaned and enriched data, when the data is loaded into the target SQL table, then it should complete in less than  ***...*** seconds per  ***...*** rows.
  - [ ] Given the cleaned and enriched data, when the data is loaded into the target SQL table, then the row counts should match expectations.
- **Data Quality**
  - [ ] Given the loaded data, when data validation is performed, then 99% of records should be accurate.
  - [ ] Given the loaded data, when data validation is performed, then 100% of expected columns and rows should be present.
  - [ ] Given the loaded data, when data validation is performed, then 100% of records should have consistent formats and values.
  - [ ] Given the loaded data, when data validation is performed, then 100% of records should maintain integrity constraints.
  - [ ] Given the loaded data, when data validation is performed, then the error rate should be less than 1%.
  - [ ] Given the loaded data, when data validation is performed, then it should complete in less than 1 second per 1,000 rows.
- **Performance**
  - [ ] Given the entire ETL process, when it is executed, then it should complete within 30 minutes for a full dataset.
  - [ ] Given the entire ETL process, when it is executed, then no significant performance regressions should be introduced.
- **Documentation**
  - [ ] Given the ETL process, when it is completed, then the code should be documented with clear and concise comments.
  - [ ] Given the ETL process, when it is completed, then user-facing documentation should be updated to reflect new or changed functionality.
- **Testing**
  - [ ] Given the ETL process, when it is completed, then unit tests should cover all new functionality.
  - [ ] Given the ETL process, when it is completed, then integration tests should cover interactions between components.
  - [ ] Given the ETL process, when it is completed, then all tests should pass successfully.
  - [ ] Given the ETL process, when it is completed, then test coverage should meet the project's required threshold of 90%.

```txt
As a Data Scientist,
I want to be able to refresh the data set, perhaps with new data,
So that I can keep my analysis up to date
```

***Acceptance Criteria***

- **Data Extraction**
  - [ ] Given new data is available in the source systems, when the ETL pipeline is executed, then the new data should be extracted successfully.
  - [ ] Given the database contains new rows, when the data is extracted, then it should complete in less than ***...*** minute for ***...***rows with ***...*** fields.
  - [ ] Given the CSV file contains new rows, when the data is extracted, then it should complete in less than ***...*** seconds for ***...*** rows with ***...*** columns.
- **Data Cleaning**
  - [ ] Given the extracted data, when duplicates are removed, then ***...***% of duplicates should be removed.
  - [ ] Given the extracted data, when missing or invalid values are handled, then ***...***% of missing or invalid fields should be resolved.
  - [ ] Given the extracted data, when data cleaning is performed, then it should complete in less than ***...*** second per ***...*** rows.
- **Data Transformation**
  - [ ] Given the cleaned data, when the customer demographics dataset (CSV) and transaction dataset (database) are merged, then the merge should be performed correctly using the ***...*** field as the key.
  - [ ] Given the cleaned data, when calculating the total amount spent by each customer, then the ***...*** field should be accurate and reflect the sum of all ***...*** values for each ***...***.
  - [ ] Given the cleaned data, when calculating the average transaction value for each customer, then the ***...*** field should be accurate and reflect the average of all ***...*** values for each `***...***.
  - [ ] Given the cleaned data, when filtering for active customers, then only customers with ***...*** set to ***...*** should be included.
- **Data Loading**
  - [ ] Given the transformed data, when the data is loaded into the target SQL database, then it should complete in less than ***...*** seconds per ***...*** rows.
  - [ ] Given the transformed data, when the data is loaded into the target SQL database, then the row counts should match expectations.
- **Data Quality**
  - [ ] Given the final dataset, when data validation is performed, then 99% of records should be accurate.
  - [ ] Given the final dataset, when data validation is performed, then 100% of expected columns and rows should be present.
  - [ ] Given the final dataset, when data validation is performed, then 100% of records should have consistent formats and values.
  - [ ] Given the final dataset, when data validation is performed, then 100% of records should maintain integrity constraints.
  - [ ] Given the final dataset, when data validation is performed, then the error rate should be less than 1%.
  - [ ] Given the final dataset, when data validation is performed, then it should complete in less than 1 second per 1,000 rows.
- **Performance**
  - [ ] Given the entire ETL process, when it is executed, then it should complete within 30 minutes for a full dataset.
  - [ ] Given the entire ETL process, when it is executed, then no significant performance regressions should be introduced.
- **Deployment**
  - [ ] Given the ETL pipeline, when it is deployed, then it should be scheduled to run at regular intervals (e.g., daily, weekly) to refresh the dataset with new data.
  - [ ] Given the ETL pipeline, when it is deployed, then it should support manual triggers to refresh the dataset on-demand.
  - [ ] Given the ETL pipeline, when it is deployed, then it should include monitoring and alerting for successful and failed runs.
- **Documentation**
  - [ ] Given the ETL process, when it is completed, then the code should be documented with clear and concise comments.
  - [ ] Given the ETL process, when it is completed, then user-facing documentation should be updated to reflect new or changed functionality.
- **Testing**
  - [ ] Given the ETL process, when it is completed, then unit tests should cover all new functionality.
  - [ ] Given the ETL process, when it is completed, then integration tests should cover interactions between components.
  - [ ] Given the ETL process, when it is completed, then all tests should pass successfully.
  - [ ] Given the ETL process, when it is completed, then test coverage should meet the project's required threshold of 90%.

---
