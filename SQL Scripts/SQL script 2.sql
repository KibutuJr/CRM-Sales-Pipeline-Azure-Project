SELECT sales_agent, close_value
FROM dbo.vSales_Pipeline
WHERE close_value > 2000
ORDER BY close_value DESC;

SELECT product, close_value 
FROM dbo.vSales_Pipeline 
ORDER BY close_value DESC;