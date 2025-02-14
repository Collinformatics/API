import requests


inEnzymeName = 'Fyn'
inOrganism = 'human'
inGetAASequence = False


def searchUniprot(enzyme, limit=5):
    url = 'https://rest.uniprot.org/uniprotkb/search'
    params = {
        'query': enzyme,
        'format': 'json',
        'size': limit}

    try:
        # Get data from uniprot
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        import sys
        print(f'Error: {e}\n\n')
        sys.exit()


# Search for enzyme
searchResults = searchUniprot(enzyme=inEnzymeName)
if searchResults['results']:
    if inOrganism == '' or inOrganism is None:
        for entry in searchResults.get("results", []):
            print(f"Enzyme: {entry['uniProtkbId']}, "
                  f"Protein ID: {entry['primaryAccession']}")
            proteinName = entry['proteinDescription']['recommendedName']['fullName']
            accession = entry['primaryAccession']
            urlUniprot = f"https://www.uniprot.org/uniprotkb/{accession}"
            print(f"     Name: {proteinName['value']}\n"
                  f"     Uniprot URL: {urlUniprot}\n")

            if inGetAASequence:
                # Get protein sequence
                sequence = entry.get("sequence", {}).get("value", "")
                print(f"     Full Sequence ({len(sequence)} AA): {sequence}\n")

                # Get protein features
                features = entry.get("features", [])

                # Extract domain sequences from the features
                for feature in features:
                    if feature.get("type") == "Domain":
                        print()
                        start = int(feature["location"]["start"]["value"]) - 1
                        end = int(feature["location"]["end"]["value"])
                        domainSequence = sequence[start:end]
                        print(f"     Domain: "
                              f"{feature['description']} ({start + 1}-{end})"
                              f"{domainSequence}")
                print('')
    else:
        for entry in searchResults.get("results", []):
            print(f"Enzyme: {entry['uniProtkbId']}, "
                  f"Protein ID: {entry['primaryAccession']}")
            if inOrganism.lower() in entry['uniProtkbId'].lower():
                proteinName = entry['proteinDescription']['recommendedName']['fullName']
                accession = entry['primaryAccession']
                urlUniprot = f"https://www.uniprot.org/uniprotkb/{accession}"
                print(f"     Name: {proteinName['value']}\n"
                      f"     Uniprot URL: {urlUniprot}\n")

                if inGetAASequence:
                    # Get protein sequence
                    sequence = entry.get("sequence", {}).get("value", "")
                    print(f"     Full Sequence ({len(sequence)} AA): {sequence}\n")

                    # Get protein features
                    features = entry.get("features", [])

                    # Extract domain sequences from the features
                    for feature in features:
                        if feature.get("type") == "Domain":
                            print()
                            start = int(feature["location"]["start"]["value"]) - 1
                            end = int(feature["location"]["end"]["value"])
                            domainSequence = sequence[start:end]
                            print(f"     Domain: "
                                  f"{feature['description']} ({start + 1}-{end})"
                                  f"{domainSequence}")
                    print('')
else:
    print(f'The protein {inEnzymeName} was not found.')
