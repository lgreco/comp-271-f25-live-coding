class Restaurant:

    def __init__(self, name, address, style="sushi"):
        self.name = name
        self.address = address # big mistake
        self.style = style
    
    def __str__(self):
        return f"Restaurant {self.name} serves {self.style} at {self.address}"