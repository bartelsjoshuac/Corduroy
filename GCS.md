# Google Cloud (Compute Engine) Deployment Steps w/Docker

## Create GCS Project and Compute Engine  
1. Install the [Google Cloud SDK](https://cloud.google.com/sdk/?hl=en)  
2. Open a Google Cloud SDK Shell.   
3. Create a new project: *gcloud projects create corduroy-project*  
4. Install the API: *gcloud services enable compute.googleapis.com*  
5. Create a micro instance: *gcloud compute instances create corduroy-vm --machine-type=e2-micro  --image-family=debian-11 --image-project=debian-cloud --tags=http-server,https-server* 
6. Open the firewall to allow access to port 8000: *gcloud compute firewall-rules create allow-port-8000 --allow tcp:8000 --source-ranges 0.0.0.0/0 --target-tags http-server*  
7. Find your *EXTERNAL_IP* as you will use this to access your server: *gcloud compute instances list*  

## Setting up your Compute Engine for Docker
1. Connect to your install *gcloud compute ssh corduroy-vm* //Note you need to have a default SSH client installed like PuTTY  
2. Switching to the new SSH terminal update the package listing: *sudo apt update*  
3. Install Docker: *sudo apt install -y docker.io*  
4. Get Docker Compose: *sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose*  
5. Change permissions: *sudo chmod +x /usr/local/bin/docker-compose*  
6. Add yourself to the Docker Group: *sudo usermod -aG docker $USER*  
7. Refresh the shell: *newgrp docker*  

## Setting up Coduroy
1. Navigate to the /source directory and transfer your files to GCS *gcloud compute scp --recurse source*    corduroy-vm:.* // As an alternative tranfer the zip or tar image and extract it remotely.    
2. Return to the SSH Engine *gcloud compute ssh corduroy-vm*.  
3. Navigate to */source/corduroyproject*  
4. Start the container *docker-compose up -d*  // This will take a long time the first time.  
5. Start a shell and create the Django SuperUser *docker-compose exec web bash*.  
6. Populate the demo user *python manage.py populate_users*      
7. Populate some sample data *python manage.py populate_data*    
8. Access your server using the IP address from Step 7 above at http://<EXTERNAL_IP>:8000  

## Going back to GCS  
1. gcloud compute instances list // Follow prompts to reconnect
2. 





