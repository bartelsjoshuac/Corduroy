# Google Cloud (Compute Engine) Deployment Steps w/Docker

## Create GCS Project and Compute Engine with Billing  
1. Install the [Google Cloud SDK](https://cloud.google.com/sdk/?hl=en) on your location machine
2. Open a Google Cloud SDK Shell.  
3. Create a new project: *gcloud projects create corduroy-project*  
4. Install the API: *gcloud services enable compute.googleapis.com*  
5. Create a micro instance: *gcloud compute instances create corduroy-vm --machine-type=e2-micro  --image-family=debian-11 --image-project=debian-cloud --tags=http-server,https-server* 
6. Open the firewall to allow access to port 8000: *gcloud compute firewall-rules create allow-port-8000 --allow tcp:8000 --source-ranges 0.0.0.0/0 --target-tags http-server*  
7. Find your *EXTERNAL_IP* as you will use this to access your server: *gcloud compute instances list*  
8.  In the GCS console setup billing.  Even with free credits, GCS will disable console access on the second connection attempt if you do not have valid billing information.  [Privacy.com](https://privacy.com/) can be used to create a virtual credit card number and protect your real credit card number.  This is also recommended for the openweather.org API key, which is also free to a certain limit.

## Setting up your Compute Engine for Docker
1. Connect to your install *gcloud compute ssh corduroy-vm* //Note you need to have a default SSH client installed like PuTTY  
2. Switching to the new SSH terminal update the package listing: *sudo apt update*  
3. Install Docker: *sudo apt install -y docker.io*  
4. Get Docker Compose: *sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose*  
5. Change permissions the Docker Compose: *sudo chmod +x /usr/local/bin/docker-compose*  
6. Add yourself to the Docker Group: *sudo usermod -aG docker $USER*  
7. Create the docker groups: *sudo newgrp docker*  

## Setting up Coduroy (using Git)
1. Clone the repository: *git clone https://github.com/bartelsjoshuac/Corduroy*  
2. *cd ~/Corduroy/source/corduroyproject*  
3. Proceed from Step 3 below.  

## Setting up Coduroy (with scp)
1. Navigate to the /source directory locally and transfer your files to GCS *gcloud compute scp --recurse source corduroy-vm:.* 
2. Navigate to */source/corduroyproject* on your GCS image.  
3. Start the container: *docker-compose up -d*  // This will take a long time the first time.  
4. Start a shell: *docker-compose exec corduroyserver bash*
5. create the Django SuperUser: *python manage.py createsuperuser*  
6. Populate the demo user: *python manage.py populate_users*  
7. Populate some sample data: *python manage.py populate_data* 
8. If you wish to have current weather data displayed, you need to manually insert a valid OpenWeatherMap.org API key at the end of the settings.py file.  If you contact the author, he might give you one :-)  
9. Access your server using the IP address from Step 7 above at http://<EXTERNAL_IP>:8000

## Going back to GCS  
1. Set your project *gcloud config set project corduroy-project3*  
2. List your instances and addresses: *gcloud compute instances list*  // See if your EXTERNAL_IP changed  
3. Open a SSH window to your computer engine: *gcloud compute ssh corduroy-vm* // You can also start a SSH session from the console.  
4. Find your *EXTERNAL_IP* as you will use this to access your server: *gcloud compute instances list*.  
5. Return to your work.  

NOTES:
- Your public and private IPs can change under a basic GCS plan, check that and make note of them and update accordingly.  For this reason, some security features were disabled in Django to avoid constant updates.  You would also need to update the URL you use to access the web interface remotely.  Likely there is free Google DNS that can eliminate this issue, but it would be better to just get a static public IP in a production environment and setup DNS for that.

### *** Live GCS Demo instance ***
 - As of project submission on 12/08/24 a running instance is available on GCS at http://35.30.34.210:8000 (as of 11/30/2024).  This will remaining running through course completion, and can be restart at request if it is not available (out of education credits so it costs real money).  
 - Use the same usernames, passwords a testing a local instance.  This site has the same test data but may have additional test data from verification I did after deployment.  It is the Project 2 Release (tag).  




