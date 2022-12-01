# used this script to consolidate scan centers with multiple scanningcenter ids in the metadata into one scan center 
# created the count_per_center_per_month.csv file
from creates_csv_map import csv_to_dict, makes_results_csv
def scanid_to_scan_center_name():
    # adds the counts for each scan center id per month together to get total scans per center
    # per month
    center_counts = csv_to_dict("path to file with center counts")
    centers = csv_to_dict("locations_file.csv")
    names_list = []
    for center in centers:
        center['scan_center_ids'] = center['scan_center_ids'].split(' || ')
        names_list.append(center['name'])
    refac_count = []
    for this_count in center_counts:
        entry = set_entry(this_count['year'],  this_count['month'])
        these_centers_counts = this_count.keys()
        for this_center_count in these_centers_counts:
            if this_center_count == 'year':
                pass
            elif this_center_count == 'month':
                pass
            else:
                for a_center in centers:
                    if this_center_count in a_center['scan_center_ids']:
                        print(entry[a_center['name']])
                        try:
                            entry[a_center['name']] = entry[a_center['name']] + float(this_count[this_center_count])
                        except ValueError:
                            pass
        refac_count.append(entry)

    print(refac_count)
    makes_results_csv(refac_count, 'refac_count.csv')

def set_entry(this_year, this_month):
    return  {'year': this_year,
                 'month': this_month, 'Innodata Knowledge Services, Inc.': 0,
'Hong Kong': 0,
'University of Alberta': 0,
'Internet Archive Headquarters': 0,
'Datum Data Co. Ltd.': 0,
'University of Toronto': 0,
'Allen County Public Library Geneaology Center': 0,
'British Library': 0,
'UCLA': 0,
'Princeton University': 0,
'Boston Public Library': 0,
'National Agricultural Library': 0,
'Library of Congress': 0,
'Columbia University': 0,
'UNC Chapel Hill': 0,
'Internt Archive Physical Archive': 0,
'UIUC': 0,
'National Library of Scotland': 0,
'San Francisco Public Library': 0,
'University of Maryland, College Park': 0,
'North Carolina State University': 0,
'BYU, Provo': 0,
'Smithsonian Libraries and Archives': 0,
'Georgetown University': 0,
'Internet Archive Sheridan Headquarters ': 0,
'Duke University': 0,
'Brown University': 0,
'Natural History Museum Library, London': 0,
'The Archive of Contemporary Music': 0,
'BYU, Hawaii': 0,
'BYU, Idaho Family History Library': 0,
'Getty Research Institute Valencia Warehouse': 0,
'University of Florida': 0,
'The Ohio State University': 0,
'American Numismatic Society': 0,
'Getty Research Institute': 0,
'Ernst Mayr Library of the Museum of Comparative Zoology': 0,
'University of Pretoria': 0,
'The Servants of Knowledge': 0,
'International Institute of Information Technology Hyderabad': 0,
'California State Library': 0,
'University of Chinese Academy of Sciences': 0,
'Servants of Knowledge': 0,
'Trent University': 0,
'Universidad Francisco Marroquín': 0,
'Analysis and Policy Observatory (APO)': 0,
'BookScanUS': 0,
'American Museum of Natural History': 0,
'State Library of Pennsylvania': 0,
'Yiddish Book Center': 0,
'Stanford University': 0,
'Peabody Essex Museum': 0,
'California Acaddemy of Sciences': 0,
'Centre for Strategic and International Studies, Jakarta': 0,
'Zhejiang University': 0,
'Clemson University': 0,
'Osmania University': 0,
'Kahle/Austin Foundation': 0,
'John Hopkins University Library Offsite Storage': 0,
'University of Victoria': 0,
'Hopewell Junction': 0,
'University of Warwick': 0,
'Research Institute of Korean Studies': 0,
'1 Dollar Scan': 0,
                 }


scanid_to_scan_center_name()
