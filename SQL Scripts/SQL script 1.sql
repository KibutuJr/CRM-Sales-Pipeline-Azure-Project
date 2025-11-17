CREATE VIEW dbo.vAccounts AS 
SELECT *
FROM OPENROWSET(
    BULK 'https://crmsalespipelinesc.blob.core.windows.net/transformed-data/accounts/part-00000-tid-787264848602467671-92d5f00d-929d-43f8-a027-631c1c86fd3f-26-1-c000.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS rows;

CREATE VIEW dbo.vData_Dictionary AS 
SELECT *
FROM OPENROWSET(
    BULK 'https://crmsalespipelinesc.blob.core.windows.net/transformed-data/data_dictionary/part-00000-tid-4488594506689834481-e5dbee4a-7c34-4250-b4e0-acfeb8b83c1b-27-1-c000.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE,
    FIELDTERMINATOR = ',',
    FIELDQUOTE = ''
) AS rows;


CREATE VIEW dbo.vProducts AS 
SELECT *
FROM OPENROWSET(
    BULK 'https://crmsalespipelinesc.blob.core.windows.net/transformed-data/products/part-00000-tid-3152107885619549837-f08ede2b-29bf-4e8f-9e2f-6de4184fbf0e-28-1-c000.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS rows;


CREATE VIEW dbo.vSales_Pipeline AS 
SELECT *
FROM OPENROWSET(
    BULK 'https://crmsalespipelinesc.blob.core.windows.net/transformed-data/sales_pipeline/part-00000-tid-3598504167674920313-f557ba6d-0d16-4452-99f2-46f664d83932-29-1-c000.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS rows;



CREATE VIEW dbo.vSales_Teams AS 
SELECT *
FROM OPENROWSET(
    BULK 'https://crmsalespipelinesc.blob.core.windows.net/transformed-data/sales_teams/part-00000-tid-2454140839408117665-f6732027-a2b0-4488-8706-a7ae3c8018c8-30-1-c000.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS rows;