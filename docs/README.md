# User Stories

## Stories  
1. As a **snowmobiler**, I want to be able to **view** the most recent grooming report for a chosen trail so I can **decide if conditions are approproate for my skill level.**  
2. As a **groomer**, I want to be able to **create** a grooming status report for a trail I am responsible for so that **admins** can **approve and publish my reports.**
3. As an **admin**, I want to be able to **view/edit and approve/publish reports** from groomers so that **snowmobilers can view them.**   

## Acceptance criteria
1. The homepage will only display the most recent approved two reports for a trail.  
2. Users will not be required to register or authenticate to view reports.  
3. All reports contain the date, name of the trail, and at least 10 characters in "report" (current conditions) vs. groomed/non-groomed (not acceptible).  
4. The admin approval must display the date, groomer's ID(name).  The date and time shall auto populate to current time and the groomer name will come from the authenticated user (groomer).  These values can not be chosen by the user.  
5. The application should dynamically resize and be mobile friendy, eliminating the need for a mobile app.  
6. Reports come from approved groomers, and have further been approved by an approval admin before being published and not from unvetted users.  

## Mis-user stories  
1. A groomer approves their own report.  
2. A groomer modifies a trail (difficulty, location, etc.)  
3. An admin approver admin deletes a report without approving or dis-approving (data loss).  
4. An admin approver creates a report and approves it (their own report).  
5. A non authenticated user (snowmobiler) creates a trail or report, or approves a report.
6. A groomer enters HTML or inapproriate chars in the report field.  

## Mitigation  
1. Groomers and admins are members of different groups and not given access to the same views.  
2. Create multiple views for the same model.  
3. Use Django user and groups provided framework to secure views.  
4. Views will support only the functions required (Create, Update, Delete).  
5. When doing group verification on the view call (in the template), insure that an admin (not admin approver) has not added the same user to both groups and handle exception.  
6. Data validation on the models, with appropriate exception handling to insure acceptence criteria on data is met and that groomer understand the error.
7. Set date and groomerID on the view and not in the html form via hidden fields.  

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
