Uniprot
-

Use this script to pull protein sequences and their domains from https://www.uniprot.org

Inputs:
- inEnzymeName: name your enzyme.

- inOrganism: what organism is your protein found in?
  - If you want all variants: you have two options
  
        inOrganism = ''
        inOrganism = None
    
- inGetAASequence:
  - To display the AA sequences

        inGetAASequence = True
  - To quickly inspect the search results 

        inGetAASequence = False
