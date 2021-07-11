def encode1(Loan_Status):
        
        """
        This function encodes a loan status to either 1 or 0.
        """
        if Loan_Status == 'Y':
            return 1
        else:
            return 0

def encode2(Gender):
        
        """
        This function encodes a loan status to either 1 or 0.
        """
        if Gender == 'Male':
            return 1
        else:
            return 0   

def encode3(Married):
        
        """
        This function encodes a loan status to either 1 or 0.
        """
        if Married == 'Yes':
            return 1
        else:
            return 0  

def encode4(Education):
        
        """
        This function encodes a loan status to either 1 or 0.
        """
        if Education == 'Graduate':
            return 1
        else:
            return 0  

def encode5(Self_Employed):
        
        """
        This function encodes a loan status to either 1 or 0.
        """
        if Self_Employed == 'Yes':
            return 1
        else:
            return 0  

def encode6(Property_Area):
        
        """
        This function encodes a loan status to either 1 or 0.
        """
        if Property_Area == 'Urban':
            return 1
        elif Property_Area == 'Rural':
            return 0
        else:
            return 2
        