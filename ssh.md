Connect Git Bash With Google Compute Engine

STEP 1: Generate SSH Key

    ssh-keygen -t rsa -f ~/.ssh/gcp_key -C vijaysardulgarh

STEP 2: Add Public Key to GCP VM

Go to Google Cloud Console → Compute Engine → VM Instances

Click your VM (vijaysardulgarh)

Click Edit

Scroll to "SSH Keys"

Paste the output of:

    cat ~/.ssh/gcp_key.pub

STEP 3: Connect Git Bash with Google Compute Engine USing ssh

    ssh -i ~/.ssh/gcp_key vijaysardulgarh@34.131.65.194

