class CompleteLease:
    def __init__(self, info):
        # Initialize with lease info (e.g., partitionId, owner, etc.)
        self.epoch = info["epoch"]

    def incrementEpoch(self):
        # Increment the epoch value by 1
        self.epoch += 1
        return self.epoch

# Example usage:
lease_info = {"epoch": 42}  # Replace with actual lease info
lease = CompleteLease(lease_info)
new_epoch = lease.incrementEpoch()
print(f"New epoch value: {new_epoch}")
