""" Holds superclasses for the model objects """
import numpy as np

class ModelLoader(object):
    """ ModelLoader is meant to be subclassed. Holds basic model info.
    
    Attributes:
        model(object): Object representing the specifics of a model. 
            Typically will involve importing from some external package.
            Because of this specificity, external methods should avoid
            expecting specific attributes or methods in this object.
        epsilons(Array): The current value of each of the model's 
                    adjustable parameters. 
        beta(float): Value of 1/KT for the system.
    
    Example:
            ml = ModelLoader()
            data = ml.load_data(fname)
            hepsilon = ml.get_potentials_epsilons(data)
            Potential_Energy = hepsilon(ModelLoader.epsilons) 
            
    """
    def __init__(self):
        """ initialize the model
        
        Intialization for subclasses will be much more complex.
                    
        """
        self.GAS_CONSTANT_KJ_MOL = 0.0083144621 #kJ/mol*k
        self.model = type('temp', (object,), {})()  
        self.epsilons = []  
        self.beta = 1.0
        self.temperature = 1.0 / (self.beta*self.GAS_CONSTANT_KJ_MOL)
    
    def load_data(self,fname):
        """ Load a data file and format for later use
        
        Args:
            fname(string): Name of a file to load.
        
        Return:
            Array(floats): Default is load using numpy and return.
            
        """
        return np.loadtxt(fname)
        
    def get_model(self):
        return self.model
    
    def get_epsilons(self):
        return self.epsilons
    
    def set_temperature(self, temp):
        """ Set attribute temperature for the loader
        
        Also updates the setting for the attribute beta.
        
        Args:
            temp (float): Temperature in Kelvins
        
        """
        
        self.temperature = temp 
        self.beta = 1.0 / (self.temperature*self.GAS_CONSTANT_KJ_MOL)
        
    def set_beta(self, besta):
        """ Set attribute beta for the loader
        
        Also updates the setting for the attribute temperature.
        
        Args:
            besta (float): Temperature in Kelvins
        
        """
        
        self.beta = besta
        self.temperature = 1.0 / (self.beta*self.GAS_CONSTANT_KJ_MOL)
        
    def get_potentials_epsilon(self, data):
        """ Return PotentialEnergy(epsilons)  
        
        Computes the potential energy for each frame in data. Each 
        ModelLoader subclass should have all the necessary information 
        internally to interpret the inputted data format. 
        
        Args:
            data(array): First index is the frame, rest are coordinates.
            
        Return:
            hepsilon(method): potential energy as a function of 
                epsilons.
                Args:
                    x: Input list of epsilons.
                Return:
                    total(Array): Same length as data, gives the 
                        potential energy of each frame.
                        
        """
        
        def hepsilon(x):
            total = np.array([0.0])
            return total
        
        return hepsilon
    
