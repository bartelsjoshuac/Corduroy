# Corduroy 
## Executive Summary 
Corduroy is a website/app to collect and publish snowmobile trail condition reports (mainly grooming reports) in the state of Colorado. [Colorado Snowmobile Association (CSAA)](https://www.snowmobilecolo.com/content.aspx?page_id=1980&club_id=45117#search_results) maintains a website hosted by a provider (ClubExpress) who wrote it in ASP code.  Colorado snowmobile trails are groomed by a variety of clubs, private parties, and state/federal land managers, often using 3rd party contractors.  

Currently the CSAA relies on these parties to email grooming information and reports to the club, who then enters them into the current site for display to the general public.  This has lead to reports being published sporadicky or not at all, as well as the usual user errors associated with manual data re-entry.  Basically no one uses it anymore.

In 2023/24 several clubs attempted to adapt an existing application and service called [GroomerTrack](https://www.groomertracker.com/), however it is cost prohibitive to both the club and the end user requring a financial obligation from each end. As a board member for the [Vail Pass Winter Recreation Area](https://www.facebook.com/profile.php?id=100039877668899), I helped evaluate this solution. This application is geared towards non-motorized users (cross county and skate skiing) and contains features unique to that activity, while lacking features desired by motorized users.  As a result it proved to be unpopular and is not currently planned for use by one of the largest organizations for 2024/25.

Corduroy aims to create a simnple interface for these "groomers" to enter their reports directly via a website (or app), allow a CSAA admin to approve and/or modify/approve the report before publishing it for the general public to view in an equally simple website(app).  

The application will be written in Python using the Django framework with a PostgreSQL database and run as a Docker container.  The user interface will be mobile friendly HTML.

## Installation

### *** NEW - now with instructions for running on GCS ***
For hosting on Google Cloud with a Compute Engine  these [instructions](https://github.com/bartelsjoshuac/Corduroy/blob/main/GCS.md).  

## Prerequisites  
- Docker verison 27
- Python 3.11.9  // All Python requirements will be pulled  (see requirements.txt for details)
- PostgresSQL 17 // Pulled from Dockerhub  
- tar -xzvf Source code.tar.gz or  unzip Source code.zip  

## Getting Started
First time to create the superuser for Django Admin
- docker compose up  -d  // Starts the webserver and database  
- docker compose exec web bash   // Starts a shell in the container  
- python manage.py createsuperuser  // Follow the prompts to create a user called root with a password of password   
- python manage.py populate_users // Create groomy (groomy account) and corduroyadmin(admin account) and groomers and admins groups  
- python manage.py populate_data // Populates some sample data  

NOTES:   
- On OSX, docker sometimes has to be run as sudo (root) or you will get a weird postgres database lock file permissions error.  But this seems random.  


Normall execution after Getting Stated
- docker compose up -d

Access the web interface:  
- Corduroy Interface http://localhost:8000/  
- Django Admin Interface http://localhost:8000/admin   

NOTES:   
- Login as root/password for admin access and all functions and the Django admin
- Login as groomy/password for access to create new grooming reports  
- Login as admin to approve reports or add/delete trails  



## Samples  
[Homepage](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/samples/homepage.png) &nbsp;&nbsp;&nbsp;
[Groomers Admin ](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/samples/groomers.png) &nbsp;&nbsp;&nbsp;
[Trails Admin ](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/samples/trailsadmin.png) &nbsp;&nbsp;&nbsp;
[Approval Admin ](https://github.com/bartelsjoshuac/Corduroy/blob/main/docs/samples/admin.png) &nbsp;&nbsp;&nbsp;


## License
The MIT License (MIT)

Copyright (c) Joshua C. Bartels 2024

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
