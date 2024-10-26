# User Stories

## Stories  
1. As a **snowmobiler**, I want to be able to **view** the most recent grooming report for a chosen trail so I can **decide if conditions are approproate for my skill level.**  
2. As a **groomer**, I want to be able to **create** a grooming status report for a trail I am responsible for trail so that **admins** can **moderate my reports.**
3. As an **admin**, I want to be able to **view/edit and publish reports** from groomers so that **snowmobilers can view them.**   

## Acceptance criteria
1.  All reports contain complete all three attributes.  
2.  The report must contain the date/time, trail name, and conditions.  
3.  All reports contain at a minimum the date/time, trail name, and a yes/no on grooming.  

## Mis-user stories
1.  Snowmobilers (non-registered users) should not be able to submit reports.  
2.  Groomers must submit a minimum of all field with the conditions being 4+ chars.  
3.  Admins must not be able to change the date of trail name of the submission when approving.  

## Mitigation  
1.  Only authenticated user can submit or publish reports
2.  Error checking in models of date, and char limits
3.  Possibly attribute level security


# Diagrams  

## Mockups  
### Homepage
![Homepage](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/mockups/mockup-homepage.png)  

### Groomer Page
![Groomer Page](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/mockups/mockup-groomers.png)  

### Admin Page
![Admin Page](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/mockups/mockup-admin.png)   

## Architecture Diagrams

### Contexts
![Context](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/C4/Context-C4.png)  

---

### Containers
![Containers](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/C4/containers-C4.png)  

### Components  
Web Component
![Web Component](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/C4/webcomponent-C4.png)  

Popstgres Component
![Web Component](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/C4/dbcomponent-C4.png)  



