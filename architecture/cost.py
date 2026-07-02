def estimate_cost(
    services,
    shape="VM.Standard.E4.Flex",
    ocpu=2,
    memory=8,
    db_storage=100,
    object_storage=100
):

    OCI_PRICING = {

        "VM.Standard.E4.Flex": {
            "ocpu": 850,
            "memory": 90
        },

        "VM.Standard.A1.Flex": {
            "ocpu": 420,
            "memory": 45
        },

        "Autonomous Database": {
            "storage": 18
        },

        "Object Storage": {
            "storage": 2.5
        },

        "Load Balancer": {
            "fixed": 600
        },

        "VCN": {
            "fixed": 200
        }
    }

    breakdown = []
    total = 0

    if "OCI Compute" in services:
        compute = (
            OCI_PRICING[shape]["ocpu"] * ocpu +
            OCI_PRICING[shape]["memory"] * memory
        )

        breakdown.append({
            "service": "OCI Compute",
            "price": round(compute)
        })

        total += compute

    if "Oracle Autonomous Database" in services:
        database = OCI_PRICING["Autonomous Database"]["storage"] * db_storage

        breakdown.append({
            "service": "Oracle Autonomous Database",
            "price": round(database)
        })

        total += database

    if "OCI Object Storage" in services:
        storage = OCI_PRICING["Object Storage"]["storage"] * object_storage

        breakdown.append({
            "service": "OCI Object Storage",
            "price": round(storage)
        })

        total += storage

    if "OCI Load Balancer" in services:
        lb = OCI_PRICING["Load Balancer"]["fixed"]

        breakdown.append({
            "service": "OCI Load Balancer",
            "price": lb
        })

        total += lb

    if "Virtual Cloud Network (VCN)" in services:
        vcn = OCI_PRICING["VCN"]["fixed"]

        breakdown.append({
            "service": "Virtual Cloud Network (VCN)",
            "price": vcn
        })

        total += vcn

    return breakdown, round(total)