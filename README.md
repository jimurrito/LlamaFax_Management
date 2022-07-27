![Logo](https://pbs.twimg.com/profile_images/1550147959379021824/EE1vU4LG_400x400.jpg)

# [LlamaFax](https://github.com/jimurrito/LlamaFax) Management UI
Interface used to Administer Llamafax infrastructure.
(This service is not publicly accessible.)

## Overview
- Provides single plane of glass dashboard.
- Allows for instant insights into the LlamaFax Services.
- Can run queries on the Databases and Queues used.
- Provides a clean layout for managing the ticketing system.

## Features
#### Dashboard
Provides insights into the Llamafax Service Databases, and Queues.
- Dash shows current count of the Data Containers.
- Allows Admin to get an idea of the service state, without having to manually query the database.
#### Search
Allows for direct queries into the Llamafax Service Data Containers.
- Queries can be directed at individual Data Containers.
- Optionally, Specific Attributes can be used as search criteria.
- Can configure a limit on the count of query results.
#### Tickets
Provides an interface to manage Tickets. Either Bug-Reports or Account Support Tickets.
- Either Bug-reports, or Support Tickets can be selected for viewing.
- UI will list 'all' results for that ticket type.
- Tickets will be marked as either "Open" or "Closed".
- Each ticket will have its own expanding element, that can be used to reveal more data.
