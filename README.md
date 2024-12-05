# Corduroy 

## Executive Summary 
Corduroy is a website/app to collect and publish snowmobile trail condition reports (mainly grooming reports) in the state of Colorado. [Colorado Snowmobile Association (CSAA)](https://www.snowmobilecolo.com/content.aspx?page_id=1980&club_id=45117#search_results) maintains a website hosted by a provider (ClubExpress) who wrote it in ASP code.  Colorado snowmobile trails are groomed by a variety of clubs, private parties, and state/federal land managers, often using 3rd party contractors.  

Currently the CSAA relies on these parties to email grooming information and reports to the club, who then enters them into the current site for display to the general public.  This has lead to reports being published sporadically or not at all, as well as the usual user errors associated with manual data re-entry.  Basically no one (groomers or the public) uses it anymore.  [Here](https://github.com/bartelsjoshuac/Corduroy/blob/main/html_images/Old1.jpg) is a sample of the current page, with a hard to read map because it is cluttered with topo information that is not relevant.  You need to click on one of the little snowflakes to get to trail reports for any area.  Most people know the names of the areas near them that are interested in.  Tourists we be told which area (by name) they would be at.  [Here](https://github.com/bartelsjoshuac/Corduroy/blob/main/html_images/Old2.jpg) is an example of current trail reports, which have no updates since last January, or in other cases since 2021.  

In 2023/24 several clubs attempted to adapt an existing application and service called [GroomerTrack](https://www.groomertracker.com/), however it is cost prohibitive to both the club and the end user requiring a financial obligation from each end. As a board member for the [Vail Pass Winter Recreation Area](https://www.facebook.com/profile.php?id=100039877668899), I helped evaluate this solution. This application is geared towards non-motorized users (cross county and skate skiing) and contains features unique to that activity, while lacking features desired by motorized users.  As a result it proved to be unpopular and is not currently planned for use by one of the largest organizations for 2024/25.  

Corduroy aims to create a simple interface for these "groomers" to enter their reports directly via a website (or app), allow a CSAA admin to approve and/or modify/approve the report before publishing it for the general public to view in an equally simple website(app).  Something that both groomers would actually use, and the public would use that is also free.  Grooming information is especially relevant to tourists who tend to stick to trails vs. backcountry exploration as tourists rent trail capable only machines.  

This application is written in Python using the Django framework with a PostgreSQL database and runs as a Docker container with just two images (more on that later).  The user interface is mobile friendly HTML and JavaScript utilizing Alpine.JS as the client side framework.  While it is not complete, it is a good starting point.  

I used Visual Studio code with several extensions; including ones for Draw.io, Python, Docker, GitHub, and a spell checker.  When I did the first assignment for this class, I was using vi :-).  

## Project Details
Project 1 was built off the same concepts we learned in Django with the DogAPI and using all Django code.  

For project 2 started to re-design in Ember, as Ember is what I did in the client side lab exercise.  Ember is extremely large (60k files and 325mb) before you write a single line of code.  Ember was also broke mid project with the release of a bad Beta 6 as the LTS version (which can be corrected by forcing 5.8 as 6 was still broke as of 11/27).  Ember made commits extremely time consuming, and build times were extremely long with Ember.  You have to rebuild for every change which meant changing a single line of code would need 10 minutes to test, even on a 16 core machine.  Dynamic testing was impossible (like in the lab) inside of Docker.  That required running Django outside of Docker as well as PostGres, which added to the setup and took a step backwards from the deployment methodology. In general Ember was just to cumbersome and slow to work with for a project with this timeline.  

So I tried React which I had limited familiarity with (aka none).  React, while not as cumbersome and large as Ember also proved to be very challenging and even more cumbersome to build as I was never ever to get the hot re-load to work properly in Docker (it works outside of Docker).  Even with a persistent volume it only kind of works in Docker, which is to say sometimes it reloads changes, sometimes it does not, which is more frustrating as it makes it very hard to know what you are actually testing. Again I found myself waiting 5-10 minutes to test each change as I had to rebuild the React image with each code change to be certain I was testing the changes I had made.  

I did two very long (all night) sessions with each framework and had far more frustration than success. I took a step back to my working Project 1 code base and did some research on how to proceed as both Ember and React were looking like I would never get something working like it had in Django, let alone be ascetically pleasing.  I had a significant time investment in Ember and React, with less to show for it than when I started.  What I did do was learn a lot about the power of client side frameworks and especially Ember and React.

I was semi-familiar with jQuery but in the name only.  This led me to [Alpine.JS](https://alpinejs.dev/) which calls itself jQuery for the modern web.  After playing with some samples, I was able to determine that it would provide everything I needed for my simple application.  Specifically it allowed me to do the following:  

1. Load my data in my pages dynamically, and display a nice message while it loaded data as well as handle the possible data errors (that should never happen).  
2. Create nice, dynamic, and informational error messages, like if you forgot to select a trail rating, etc.  Without having to submit the form and wait for the server to respond like Django alone required.
3. Display a feedback messages inline with the page in a nice format, vs. submit and wait, AKA traditional web design.  Again an ascetically pleasing user feedback vs fire and forgot, or alert boxes.
4. Integrate weather information, which I am not really sure is even needed.  There are 1000's of more popular ways to get current weather conditions.  But it let me experiment with using Alpine to call an external API securely. And #3 allowed me to handle the lack of a weather API Key in the deployment version. 

Alpine allowed the project to maintain a compact footprint.  For Project 1 had a 4 MB code base, Project 2 (with Alpine) increased that to just 16 MB.  The complete sever and client produced a 1.6 GB server/client and a 600MB database.  Contrasting that to Ember, before development, Ember produced a 325MB code base and a 7 GB docker image.  This is likely because of Ember and React's node.js requirements.  

Alpine.js also did not require a separate application server or Docker image, it worked with my existing Django templates, with relatively minor modifications, but ones I could understand, something I had a very difficult time doing with Ember and React.  In just two long evenings, I was able to get my templates and existing code working semi-nice with Alpine and reusing a significant amount of code between the templates.  This left a lot of work to still do, but the basic functionality of the app was all working per the use cases and I was left with the fun part.  This also allowed me to use many of the out of box Django security features to meet the project requirements.  

Lastly, the very name Alpine.js was very fitting to my Corduroy Snowmobile trail report application for the high alpine areas of the Rocky Mountains, although that is merely coincidence.  As a side note, the name Corduroy was derived from the corduroy pants look left in the surface of the snow after a mechanized snow groomer passes over it.  The term is shared among skiers (both alpine and x-country) and snowmobilers alike as a similar machine is used to produce the same groomed corduroy surface in the snow.  

ChatGPT was used to do some of the heavy lifting and repetitive work to incorporate Alpine into my Django templates. My CSS was courtesy of a CSS website for common simple and readable mobile friendly pages.  But then I also took some stuff from Tailwind I wanted.  It was then customized a tad more as it wasn't great and I always wanted to learn CSS. I let ChatGPT clean it up for me, which it did nicely.  Most of ChatGPT's use was in debugging features as I tried to make the application more dynamic and I kept breaking it.  For example I found I would frequently break an entire template, spend a very long time trying to find an obscure typo that Django allowed (because it does not care what you do in JavaScript tags), but caused a form to not submit or not save the data.  Correlating the developer console errors in the browser with the JavaScript can be very time consuming and ChatGPT can often spot the simplest of typos instantly when provided the code and the console error.  Just don't ask it to fix it as it will, while at the same time breaking other things it wasn't asked to even touch :-)  It is also very good when you ask it to take code that should be working, but is not and all you want it to do is pack it full of debug statements (console.log()) so that you can then run it see where the problem lies and fix it yourself in the case where your logic was just wrong but the syntax was correct.  Similarly, you can then have it remove all those debug statements once it is working, without the risk of breaking something by accident again.  I found myself manually adding debug statements, that then needed to be manually debug the debug statements themselves, or removing debug statements from working code, only to have the absence of debugging statements again break the functionality, which is not only time consuming, but frustrating as well.  I also used it to clean up code, so that you don't import the same thing 5 times each time you decide to use it and did not look back.

<img src="https://github.com/bartelsjoshuac/Corduroy/blob/main/html_images/dog-sled.jpg" alt="DogApi goes wild" width="200" height="200"> -> <img src="https://github.com/bartelsjoshuac/Corduroy/blob/main/html_images/dogapi.webp" alt="DogApi goes wild" width="200" height="200">  


AI is far from perfect....  In fact it is not even close. It gets the concept, but it gets key things wrong and you have to help it get it right, the same thing a human does when you debug code.     All I asked for was a cartoon drawing of my original picture which I had planned to use the cartoon instead of the sled.  Now my dog is going the wrong way and has no googles.  I did not end up using this image for my intended purpose after-all.  I did try to get it to fix it and it added an airplane overhead, then my groomer was replaced with a snowplow????  It can lead you to disaster pretty quickly but it can also pull you out of a dead end.  It was sometimes very helpful and other times made so mad, that reading doc and doing it myself was much easier.  


.....  

For demo purposes I created python scripts that pre-populate the users, groups, etc., to test basic functionality.  Use of these is described in the Getting Stated Section.  I also created a script to pre-populate some data to play with, although it is possible to create just create your own data to test as well, but the pre-populate data deploys that all in a functioning demo that makes it look like the app has already been used by an admin and groomer.  I did not know what was expected yet for the presentation portion and wanted something that I could rehearse with and use for repeatable testing.

The current weather works with a valid Openweather.org API key in settings.py, but only if user updates that key manually.  Instead, I made the code gracefully handle the failure of the weather API call, so if you don't have a valid key, you simply won't have the weather feature and will see a message load and disappear very quickly when it fails to load the weather.  

Lastly I went ahead and did the Google Cloud hosting as GCS was something I had basic knowledge of already, and quite frankly, I did that when Project 2 was announced and before it was optional using just the Project 1 code base.  Once everything is working locally in Docker, deploying it with GCS is relatively straight forward if you understand GCS a little.  GCS of course is no place to try and develop code as GCS mini VMs are extremely slow for building.  Details on this are noted in *** New  sections at the end.  You can either build your own image to test, or use the running GCS image as it is the same release.

## Installation
- Follow the getting started  

## Prerequisites  
- Docker verison 27
- Docker Compose // If not included with your Docker install
- Python 3.11.9  // All Python requirements will be pulled  (see requirements.txt for details).  
- PostgresSQL 17 // Pulled from DockerHub.
- Alpine.js // Included in HTML.  


## Getting Started  
1. Download the latest Project 2 release(tag) from GitHub and *tar -xzvf Source code.tar.gz* or  *unzip Source code.zip*  
2. cd source/CorduroyProject  

<-or (preferred)->  

1. Clone the repository: *git clone https://github.com/bartelsjoshuac/Corduroy*  
2. *cd Corduroy/source/corduroyproject*  

<-continue->  

3. Run *docker compose build* to install everything from requirements.txt.   // This seems to occur automatically with the up command on Windows but not on *nix.  May require sudo on OSX.
4. *docker compose up  -d*  // Starts the webserver and database.  
5. *docker compose exec corduroyserver bash*   // Starts a shell in the container.  Not you need to "exit" the container shell to return to you local machine if needed later.  
6. *python manage.py createsuperuser*  // Follow the prompts to create a user called root with a password of password.  
7. *python manage.py populate_users* // Create groomy (groomy account) and admin(Corduroy admin account) and the groomers and admins groups.  
8. *python manage.py populate_data* // Populates some sample data.  
9. If you wish to have current weather data displayed, you need to manually insert a valie OpenWeatherMap.org API key at the end of the settings.py file.  If you contact the author, he might give you one :-) 
10. Access the Corduroy Interface http://localhost:8000/.    

NOTES:   
- On OSX, Docker sometimes has to be run as sudo (root) or you will get a weird postgres database lock file permissions error.  But this seems random. 
- There are subtle differences between Unix and Windows commands you will need to familiarize yourself with.  This is especially true for Docker docker-compose vs. docker compose for example.  
- There are several security settings that were disabled to make testing much easier, and to make a deployable application for submission.  Comments are available where these changes were made so that they can be reverted to at least defaults or a more secure setting.  Examples include password policies, timeouts, etc.  I tried to put comments everywhere I did something that seemed less secure that would be done differently in a true production environment.  

Normal execution after Getting Stated
- *docker compose up -d*  // Not needed if already running.

Access the web interface:  
- Corduroy Interface http://localhost:8000/  
- Django Admin Interface (root only) http://localhost:8000/admin  

NOTES (for testing):   
- Login as root/password for admin access and all functions and the Django admin including raw data.  
- Login as groomy/password for access to create new grooming reports.  
- Login as admin/password to approve reports or add/delete trails.  You may wish to create new trails first unless you want to only work with the limited sample data.  

- Sample test scenario
1. Click on Manage Trails, login as admin/password.  Create a new trail.  Make note of the trail name you chose and the location, as you will need to reference this later.
2. Return the homepage and logout (different user context).  
3. Click on Enter Grooming Report, login as groomy/password.  Under location select the location from Step 1 so that you see the new trail you created in Step 1.  Enter something in the report field.  If you don't select a trail name, you will get a nice message generated by Alpine, or some other errors depending on what you did wrong.
4. Return to the homepage, and note that your report does not appear.   This is because it is not yet approved by an admin.  Logout.  It does not appear to the public user for the same reason.
5. Click on Approve Pending Reports and login again as admin/password (changing user context again).  You will see other data there that was loaded as sample data, but you will also see the new report for the new trail you created in Step 3.  Make sure to check the approved box and submit the form. You can also approve sample reports if desired. Or un-approve on of the sample data reports. 
6.  Return to the homepage.  Now that your report is approved, it appears.  But you are still an admin.  You can logout and become a public user again and it also appears as expected.  

### *** NEW  - Live GCS Demo instance ***
 - As of project submission on 12/02/24 a running instance is available on GCS at http://35.202.122.99:8000. This will remaining running through course completion, and can be restarted at request if it is not available (I am out of education credits so its costs real money to leave running).  
 - Use the same usernames, passwords as if testing as a local instance.  This site has the same test data but may have additional test data depending on how I left it.  Same code, same sample test scenario. You get the idea...  

### *** NEW - Specific instructions for installing and running on GCS ***
NOTES:  
- This assumes some familiarty with GCS and GCS Compute Engines.
- This can take a very long time to build on micro or mini compute instances so should only be done once when ready for deployment.  

For hosting on Google Cloud with a Compute Engine follow these [instructions](https://github.com/bartelsjoshuac/Corduroy/blob/main/GCS.md).  

## Samples (from Project 1 submission phase, before use of Alpine - historical)   
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
