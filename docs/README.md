# User Stories

## Stories  
1. As a **snowmobiler**, I want to be able to **view** the most recent grooming report for a chosen trail so I can **decide if conditions are approproate for my skill level.**  
2. As a **groomer**, I want to be able to **create** a grooming status report for a trail I am responsible for so that **admins** can **approve and publish my reports.**
3. As an **admin**, I want to be able to **view/edit and approve/publish reports** from groomers so that **snowmobilers can view them.**   

## Acceptance criteria
1.  All reports contain all three attributes from groomers.  
2.  The report must contain the date/time, groomer's ID(name).  
3.  All reports contain at a minimum the date/time, trail name, and a yes/no on grooming.  

## Mis-user stories
1.  Snowmobilers (non-registered users) should not be able to submit reports or create trails  
2.  Groomers must submit a minimum of all fields with the conditions being 4+ chars.    
3.  Admins must not be able to change the date of trail name of the submission when approving.  
4.  Only Admins can change the approved attribute

## Mitigation  
1.  Only authenticated user can submit or publish reports and they will be members of groups with access to the appropriate views
2.  Error checking in models of date, and char limits
3.  Seperate this attribute from the view so that only the groomer has access
4.  Security on the view


# Diagrams  

## Mockups  
### Homepage
![Homepage](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/mockups/mockup-homepage.png)  

### Groomers Report Page
![Groomer Page](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/mockups/mockup-groomers.png)  

### Reports Admin Page
![Admin Page](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/mockups/mockup-admin.png)  

### Trails Admin Page
![Admin Page](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/mockups/mockup-trailsadmin.png)      

## Architecture Diagrams

### Contexts
![Context](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/C4/Context-C4.png)  

---

### Containers
![Containers](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/C4/containers-C4.png)  

### Components  
Django Component  
![Django Component](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/C4/djangocomponent-C4.png)    

Postgres Component  
![Postgres Component](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/C4/postgresomponent-C4.png)    



