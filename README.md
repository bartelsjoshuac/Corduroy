# Corduroy 
## Executive Summary 
Corduroy is a website/app to collect and publish snowmobile trail condition reports (mainly grooming reports) in the state of Colorado. [Colorado Snowmobile Association (CSAA)](https://www.snowmobilecolo.com/content.aspx?page_id=1980&club_id=45117#search_results) maintains a website hosted by a provider (ClubExpress) who wrote it in ASP code.  Colorado snowmobile trails are groomed by a variety of clubs, private parties, and state/federal land managers, often using 3rd party contractors.  

Currently the CSAA relies on these parties to email grooming information and reports to the club, who then enters them into the current site for display to the general public.  This has lead to reports being published sporadicky or not at all, as well as the usual user errors associated with manual data re-entry.  Basically no one uses it anymore.

In 2023/24 several clubs attempted to adapt an existing application and service called [GroomerTrack](https://www.groomertracker.com/), however it is cost prohibitive to both the club and the end user requring a financial obligation from each end. As a board member for the [Vail Pass Winter Recreation Area](https://www.facebook.com/profile.php?id=100039877668899), I helped evaluate this solution. This application is geared towards non-motorized users (cross county and skate skiing) and contains features unique to that activity, while lacking features desired by motorized users.  As a result it proved to be unpopular and is not currently planned for use by one of the largest organizations for 2024/25.

Corduroy aims to create a simnple interface for these "groomers" to enter their reports directly via a website (or app), allow a CSAA admin to approve and/or modify/approve the report before publishing it for the general public to view in an equally simple website(app).  

The application is written in Python using the Django framework with a PostgreSQL database and runs as a Docker container with just two images (more on that later).  The user interface is mobile friendly HTML and JavaScript utilizing Alpine.JS as the client side framework.  

## Project Details
Project 1 was built of the same concepts we learned in Django with the DogAPI and using all Django code.

For project 2 started to re-design in Ember, as Ember is what I did in the client side lab exercise.  Ember is extremely large (60k files and 325mb) before you write a single line of code.  Ember was also broke mid project with the release of a bad Beta 6 as the LTS version (which can be corrected by forcing 5.8 as 6 was still broke as of 11/27).  Ember made commits extremely time consuming, and build times were extremely long with Ember.  You have to rebuild for every change which meant changing a single line of code would need 10 minutes to test, even on a 16 core machine.  Dynamic testing was impossible (like in the lab) inside of Docker.  That required running Django outside of Docker as well as PostGres, which added to the setup and took a step backwards from the deployment methodology.  

So I tried React which I had limited familiarity with (aka none).  React, while not as cumbersome and large as Ember also proved to be very challenging and even more cumbersome to build as I was never ever to get the hot re-load to work properly in Docker (it works outside of Docker).  Even with a persistant volume it only kinda works in Docker, which is to say sometimes it reloads changes, sometimes it does not, which is more frusterating as it makes it very hard to know what you are actualy testing. Again I found myself waiting 5-10 minutes to test each change as I had to rebuild the React image with each code change to be certain I was testing the changes I had made.

I did two all night sessions with each framework and had far more frusteration than success. I took a step back to my working Project 1 code base and did some research on how to proceed as both Ember and React were looking like I would never get something working like it had in Django, let alone be astetically pleasing.  What I did do was learn a lot about the power of client side frameworks and specically Ember and React.

I was semi-familiar with jQuery but in the name only.  This led me to [Alpine.JS](https://alpinejs.dev/) which calls itself jQuery for the modern web.  After playing with some samples, I was able to determine that it would provide everything I needed for my simple application.  Specificaly it allowed me to do the following:  

1. Load my data in my pages dynamically, and display a nice message while it loaded data as well as handle the possibe data errors (that should never happen)
2. Create nice, dynamic, informational error messages, like if you forgot to select a trail rating, etc.  Without having to submit the form and wait for the server to respond.
3. Display a feedback messages inline with the page in a nice format, vs. submit and wait, AKA tradditional web design.  Again an asteically pleasing user feedback vs fire and forgot, or alert boxes.

Alpine allowed the project to maintain a compact footprint.  For Project 1 had a 4 MB code base, Project 2 (with Alpine) increased that to just 16 MB.  The complete sever and client produced a 1.6 GB server/client and a 600MB database.  Contrasting that to Ember, before development, Ember produced a 325MB code base and a 7 GB docker image.  This is likely because of Ember and React's node.js requirement.

Alpine.js also did not require a seperate application server or Docker image, it worked with my existing Django templates, with relatively minor modifications, but ones I could understand, something I had a very difficult time doing with Ember and React.  In just two long evenings, I was able to get my templates and existing code working semi-nice with Alpine and reusing a significant amount of code between them.  This left a lot of work to still do, but the basic functionality of the app was all working per the use cases and I was left with the fun part.

Lastly, the very name Alpine.js was very fitting to my Coduroy Snowmobile trail report application for the high alpine areas of the Rocky Mountains, although that is merely coincidence.  As a side note, the name Corduroy was dereived from the corduroy pants look left in the surface of the snow after a mechanized snow groomer passes over it.  The term is shared among skiers and snowmobilers alike as a similiar machine is used to produce both.

ChatGPT was used to do some of the heavy lifting and repeitive work to incorperate Alpine into my Django templates. My CSS was courtesy of a CSS website for common simple and readable mobile friendly pages.  It was then customized a tad  Most of ChatGPT's use was in debugging features as I tried to make the application more dynamic.  For example I found I would frequently break an entire template, spend a very long time trying to find an obscure typo that Django allowed (because it does not care what you do in Javascript), but caused a form to not submit or not save the data.  Correlating the developer console errors in the browser with the Javascript can be very time consuming and ChatGPT can often spot the simplest of typos instantly when provided the code and the console error.  It is also very good when you ask it to take code that should be working, but is not and all you want it to do is pack it full of debug statements so that you can then run it see where the problem lies and fix it yourself in the case where your logic was just wrong.  Simiilary, you can then have it remove all those debug statements once it is working, without the risk of breaking something by accdident again.  I found myself manually adding debug statements, that then needed to be manually debugged themselves, or removing debug statements from working code, only to have the absence of debugging statements again break the functionality, which is not only time consuming, but frusterating as well.

For demo purposes I created python scripts that pre-populate the users, groups, etc, to test basic functionality.  Use of these is desribed in the Getting Stated Section.  I also created a script to pre-populate some data to play with, although it is possible to create create your own data, but the pre-populate deployes that all in a functioning demo that makes it look like the app has already been used by an admin and groomer.

Lastly I went ahead and did the Google Cloud hosting as GCS was something I had basic knowledge of already, and quite frankly, I did that when Prject 2 was announced and before it was optional using just the Project 1 code base.  Once everything is working locally in Docker, deploying it with GCS is relatively straight forward if you understand GCS a little.  GCS of course is no place to try and develop code as GCS mini VMs are extremely slow for building.

## Installation

### *** NEW - now with instructions for running on GCS ***
For hosting on Google Cloud with a Compute Engine follow these [instructions](https://github.com/bartelsjoshuac/Corduroy/blob/main/GCS.md).  

NOTES:  
- This assumes some familiarty with GCS and GCS Compute Engines.
- This can take a very long time to build on micro or mini compute instances.  

## Prerequisites  
- Docker verison 27
- Python 3.11.9  // All Python requirements will be pulled  (see requirements.txt for details).  
- PostgresSQL 17 // Pulled from Dockerhub.
- Alpine.js // Included in HTML.  


## Getting Started  
1. Download the latest release from GitHub and *tar -xzvf Source code.tar.gz* or  *unzip Source code.zip*  
2. cd source/CorduroyProject  

<-or->  

1. Clone the repository: *git clone https://github.com/bartelsjoshuac/Corduroy*  
2. *cd /Corduroy/source/corduroyproject*  
3. *docker compose up  -d*  // Starts the webserver and database.  
4. *docker compose exec web bash*   // Starts a shell in the container.  
4. *python manage.py createsuperuser*  // Follow the prompts to create a user called root with a password of password.  
6. *python manage.py populate_users* // Create groomy (groomy account) and corduroyadmin(admin account) and groomers and admins groups.  
7. *python manage.py populate_data* // Populates some sample data.  

NOTES:   
- On OSX, docker sometimes has to be run as sudo (root) or you will get a weird postgres database lock file permissions error.  But this seems random. 
- There are subtle differences between unix and windows commands you will need to familize yourself with.  
- There are several security settings that were disabled to make testing much easier, and to make a deployable application for submission.  Comments are available where these changes were made so that they can be reverted to at 
least defaults or a more secure settings.  Examples include password policies, timeouts, etc.

Normal execution after Getting Stated
- *docker compose up -d*

Access the web interface:  
- Corduroy Interface http://localhost:8000/  
- Django Admin Interface (root only) http://localhost:8000/admin  

NOTES (for testing):   
- Login as root/password for admin access and all functions and the Django admin including raw data.  
- Login as groomy/password for access to create new grooming reports.  
- Login as admin to approve reports or add/delete trails.  You may wish to create new trails first unless you want to only work with the limited sample data. 

## Samples (from Project 1 submission phase, before use of Alpine)  
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
