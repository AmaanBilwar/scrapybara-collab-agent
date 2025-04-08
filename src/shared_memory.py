class SharedMemory:
    """Shared memory space for agents to communicate"""
    
    def __init__(self):
        self.data = {}
        
    def save(self, key, value):
        """Save data to shared memory"""
        self.data[key] = value
        return True
        
    def load(self, key):
        """Load data from shared memory"""
        return self.data.get(key)
    
    def exists(self, key):
        """Check if key exists in shared memory"""
        return key in self.data
    
    def get_all(self):
        """Get all data in shared memory"""
        return self.data