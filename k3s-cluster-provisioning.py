

# Refactored to use the new package and classes
import os
from k3sprovision import ClusterProvisioner 

def main() -> int:
    config = {
        "cluster": os.getenv("CLUSTER", default = "k3s1"),
        "inventory": os.getenv("INVENTORY", default = "/home/adminstack/workplace/k3sverse/inventory/inventory.yml"),
        "k3s_version": None,
        "kube_vip_version": None,
        "kubectl_config": "/home/adminstack/.kube/config",
        "ssh_key": "/home/adminstack/.ssh/id_rsa",
    }
    provisioner = ClusterProvisioner(config)
    return provisioner.run()

if __name__ == '__main__':
    exit(main())
