#!/bin/bash

# ===== CONFIGURABLE VARIABLES =====
PEM_FILE_PATH="$HOME/path"  # Full path to your AWS .pem file
USERNAME="ubuntu"           # EC2 instance user
PUBLIC_IPS=(
    <ip_address>
    # Add more public IPs here
)

# ===== COPY SSH KEY TO EACH MANAGED NODE =====
for IP in "${PUBLIC_IPS[@]}"; do
    echo "📡 Copying SSH key to $IP..."

    ssh-copy-id -f "-o IdentityFile $PEM_FILE_PATH" $USERNAME@$IP

    if [ $? -eq 0 ]; then
        echo "✅ Key successfully copied to $IP"
    else
        echo "❌ Failed to copy key to $IP"
    fi
done

echo "🎉 Passwordless SSH setup complete."

