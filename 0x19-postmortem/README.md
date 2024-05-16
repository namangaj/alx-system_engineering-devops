0x19. Postmortem: 
 Postmortem: Web Stack Outage
Issue Summary:
•	Duration:
•	Start Time: May 11, 2024, 14:00 UTC
•	End Time: May 11, 2024, 16:30 UTC
•	Impact:
•	The web application experienced intermittent downtime, affecting 30% of users. Users reported slow response times and occasional error messages during the outage.
Root Cause:
The root cause of the outage was identified as a misconfiguration in the load balancer settings, leading to improper distribution of incoming traffic to backend servers.
Timeline:
•	14:00 UTC:
•	Issue detected through monitoring alerts indicating increased latency.
•	14:05 UTC:
•	Engineering team notified about the outage.
•	14:10 UTC:
•	Initial investigation focused on backend server health and database performance.
•	14:30 UTC:
•	Misleading assumption made that the database was the bottleneck.
•	14:45 UTC:
•	Increased error rates led to suspicion of networking issues.
•	15:00 UTC:
•	Incident escalated to the infrastructure team for further analysis.
•	15:15 UTC:
•	Load balancer logs reviewed, revealing misconfigurations.
•	15:30 UTC:
•	Load balancer settings adjusted to properly distribute traffic.
•	16:30 UTC:
•	Full service restoration confirmed.
Root Cause and Resolution:
•	Root Cause:
•	Misconfigured load balancer settings caused improper distribution of incoming traffic, leading to performance degradation and intermittent downtime.
•	Resolution:
•	Load balancer settings were corrected to evenly distribute traffic among backend servers, resolving the performance issues and restoring service stability.
Corrective and Preventative Measures:
•	Improvements/Fixes:
•	Regular audits of load balancer configurations to prevent similar misconfigurations.
•	Implementation of automated alerts for load balancer health and performance metrics.
•	Tasks to Address the Issue:
•	Conduct thorough review of load balancer configurations to identify and correct any remaining misconfigurations.
•	Develop and implement automated testing procedures to validate load balancer functionality after configuration changes.
•	Enhance monitoring and alerting systems to provide more granular visibility into web stack performance and health.
https://github.com/namangaj/alx-system_engineering-devops/blob/main/Web%20downtime%20image.JPG
