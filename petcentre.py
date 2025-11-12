class Pet:
    """
    Represents a single pet in the shelter.

    Attributes:
        name (str): The pet's name.
        species (str): The type of animal (e.g., "Dog", "Cat").
        age (int): The pet's age.
        is_adopted (bool): Status flag, True if the pet is adopted, False otherwise.
    """
    def __init__(self, name, species, age):
        """Initializes a new Pet object."""
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False  # All pets start as not adopted

    def display_details(self):
        """Prints the details of the pet."""
        status = "Adopted" if self.is_adopted else "Available"
        print(f"  - Name: {self.name}, Species: {self.species}, Age: {self.age}, Status: {status}")

    def adopt(self):
        """Marks the pet as adopted."""
        if not self.is_adopted:
            self.is_adopted = True
            return True
        return False # Already adopted

    def return_to_shelter(self):
        """Marks the pet as not adopted (returned)."""
        if self.is_adopted:
            self.is_adopted = False
            return True
        return False # Already in shelter


class Adopter:
    """
    Represents a person who can adopt pets.

    Attributes:
        name (str): The adopter's name.
        adopter_id (str): A unique ID for the adopter.
        adopted_pets (list): A list of Pet objects adopted by this person.
    """
    def __init__(self, name, adopter_id):
        """Initializes a new Adopter object."""
        self.name = name
        self.adopter_id = adopter_id
        self.adopted_pets = []  # Starts with an empty list

    def adopt_pet(self, pet_object):
        """Adds a Pet object to the adopter's list of adopted pets."""
        if pet_object not in self.adopted_pets:
            self.adopted_pets.append(pet_object)
            print(f"Success: {self.name} has adopted {pet_object.name}.")
        else:
            print(f"Info: {self.name} has already adopted {pet_object.name}.")

    def return_pet(self, pet_object):
        """Removes a Pet object from the adopter's list."""
        if pet_object in self.adopted_pets:
            self.adopted_pets.remove(pet_object)
            print(f"Success: {self.name} has returned {pet_object.name}.")
        else:
            print(f"Error: {self.name} does not have a pet named {pet_object.name}.")

    def display_details(self):
        """Prints the adopter's details and a list of their adopted pets."""
        print(f"Adopter Name: {self.name}, ID: {self.adopter_id}")
        if not self.adopted_pets:
            print("  Has not adopted any pets yet.")
        else:
            print("  Adopted Pets:")
            for pet in self.adopted_pets:
                print(f"    - {pet.name} ({pet.species})")


class Shelter:
    """
    Manages the pets and adopters in the adoption centre.
    This class handles the main logic of adding, finding, and processing adoptions.
    """
    def __init__(self):
        """Initializes the Shelter with empty lists for pets and adopters."""
        self.pets = []
        self.adopters = []

    def add_pet(self, name, species, age):
        """Creates a new Pet object and adds it to the shelter's pet list."""
        new_pet = Pet(name, species, age)
        self.pets.append(new_pet)
        print(f"Success: Pet '{name}' added to the shelter.")

    def add_adopter(self, name, adopter_id):
        """Creates a new Adopter object and adds it to the shelter's adopter list."""
        # Check for duplicate ID
        if self.find_adopter(adopter_id):
            print(f"Error: Adopter ID '{adopter_id}' already exists.")
            return
        
        new_adopter = Adopter(name, adopter_id)
        self.adopters.append(new_adopter)
        print(f"Success: Adopter '{name}' registered with ID '{adopter_id}'.")

    def find_pet(self, name):
        """
        Finds a Pet object in the shelter by its name.
        Returns the Pet object or None if not found.
        """
        for pet in self.pets:
            if pet.name.lower() == name.lower():
                return pet
        return None  # Pet not found

    def find_adopter(self, adopter_id):
        """
        Finds an Adopter object in the shelter by their ID.
        Returns the Adopter object or None if not found.
        """
        for adopter in self.adopters:
            if adopter.adopter_id.lower() == adopter_id.lower():
                return adopter
        return None  # Adopter not found

    def process_adoption(self, adopter_id, pet_name):
        """Handles the logic for an adopter adopting a pet."""
        adopter = self.find_adopter(adopter_id)
        pet = self.find_pet(pet_name)

        if not adopter:
            print(f"Error: Adopter with ID '{adopter_id}' not found.")
            return
        
        if not pet:
            print(f"Error: Pet with name '{pet_name}' not found.")
            return
        
        if pet.is_adopted:
            print(f"Error: Pet '{pet_name}' is already adopted.")
            return
            
        # If all checks pass, process the adoption
        pet.adopt()  # Mark pet as adopted
        adopter.adopt_pet(pet)  # Add pet to adopter's list

    def process_return(self, adopter_id, pet_name):
        """Handles the logic for an adopter returning a pet."""
        adopter = self.find_adopter(adopter_id)
        pet = self.find_pet(pet_name) # Find pet in the *shelter's* main list

        if not adopter:
            print(f"Error: Adopter with ID '{adopter_id}' not found.")
            return

        if not pet:
            # This case should be rare if pet was adopted from here, but good to check
            print(f"Error: Pet '{pet_name}' not found in shelter records.")
            return

        # Check if the adopter actually has this pet
        if pet not in adopter.adopted_pets:
            print(f"Error: {adopter.name} does not have a pet named {pet_name}.")
            return

        # Process the return
        pet.return_to_shelter() # Mark pet as available
        adopter.return_pet(pet) # Remove pet from adopter's list

    def display_available_pets(self):
        """Prints details for all pets that are not currently adopted."""
        print("\n--- Available Pets ---")
        available_count = 0
        for pet in self.pets:
            if not pet.is_adopted:
                pet.display_details()
                available_count += 1
        
        if available_count == 0:
            print("No pets are currently available for adoption.")
        print("------------------------")

    def display_adopter_details(self, adopter_id):
        """Finds and displays details for a specific adopter."""
        adopter = self.find_adopter(adopter_id)
        if adopter:
            adopter.display_details()
        else:
            print(f"Error: Adopter with ID '{adopter_id}' not found.")


def print_menu():
    """Prints the main menu options to the console."""
    print("\n===== Pet Adoption Centre Menu =====")
    print("1. Add New Pet to Shelter")
    print("2. Register New Adopter")
    print("3. Process an Adoption")
    print("4. Process a Pet Return")
    print("5. View Available Pets")
    print("6. View Adopter Details")
    print("7. Exit")
    print("====================================")

# --- Main Program ---
if __name__ == "__main__":
    
    # 1. Create the main shelter object
    happy_paws_shelter = Shelter()

    # 2. Pre-populate with some data
    happy_paws_shelter.add_pet("Buddy", "Dog", 5)
    happy_paws_shelter.add_pet("Whiskers", "Cat", 2)
    happy_paws_shelter.add_adopter("Alice", "A001")
    
    # 3. Start the main menu loop
    while True:
        print_menu()
        choice = input("Enter your choice 1-7: ")

        if choice == '1':
            # Add New Pet
            print("\n--- Add New Pet ---")
            name = input("Enter pet's name: ")
            species = input("Enter pet's species (e.g., Dog, Cat): ")
            try:
                age = int(input("Enter pet's age: "))
                happy_paws_shelter.add_pet(name, species, age)
            except ValueError:
                print("Error: Age must be a number.")

        elif choice == '2':
            # Register New Adopter
            print("\n--- Register New Adopter ---")
            name = input("Enter adopter's name: ")
            adopter_id = input("Enter a unique Adopter ID (e.g., A002): ")
            happy_paws_shelter.add_adopter(name, adopter_id)

        elif choice == '3':
            # Process an Adoption
            print("\n--- Process Adoption ---")
            adopter_id = input("Enter Adopter ID: ")
            pet_name = input("Enter Pet Name: ")
            happy_paws_shelter.process_adoption(adopter_id, pet_name)

        elif choice == '4':
            # Process a Pet Return
            print("\n--- Process Pet Return ---")
            adopter_id = input("Enter Adopter ID: ")
            pet_name = input("Enter Pet Name: ")
            happy_paws_shelter.process_return(adopter_id, pet_name)

        elif choice == '5':
            # View Available Pets
            happy_paws_shelter.display_available_pets()

        elif choice == '6':
            # View Adopter Details
            print("\n--- View Adopter Details ---")
            adopter_id = input("Enter Adopter ID: ")
            happy_paws_shelter.display_adopter_details(adopter_id)

        elif choice == '7':
            # Exit
            print("Thank you for using the Pet Adoption Centre system. Goodbye!")
            break

        else:
            print("Error: Invalid choice. Please enter a number between 1 and 7.")