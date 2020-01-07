SELECT Standby_Time.Facility_ID,Standby_Time.Standby_Time,Standby_Time.Date 
FROM saichann.Standby_Time 
WHERE (Standby_Time.Standby_Time,Standby_Time.Date) 
IN (
SELECT Standby_Time.Standby_Time,Standby_Time.Date 
FROM saichann.Facility 
inner join saichann.Standby_Time 
ON Facility.Facility_ID = Standby_Time.Facility_ID  
group by Facility.Facility_ID 
ORDER BY Standby_Time.Date ASC,Facility.Facility_ID ASC
);