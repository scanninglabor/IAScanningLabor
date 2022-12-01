# used to create maps based on per center stats 
import csv


def scan_center_stats():
#     insert complete path to per_center_stats.csv file
    center_stats = csv_to_dict("per_center_stats.csv")
#     insert complete path to "locations_file.csv"
    geocoder = csv_to_dict("locations_file.csv")
    center_report = makes_centers_report(geocoder)
    for this_stat in center_stats:
        for center in geocoder:
            if this_stat['name'] == center['name']:
                this_stat['lat'] = center['lat']
                this_stat['long'] = center['long']
            else: pass
        print(this_stat)
    print(center_stats)
    makes_results_csv(center_stats, 'scans_stats_map.csv')


def scans_total_report():
    these_centers_counts = csv_to_dict("/Users/elizabethschwartz/Documents/fall_2022/pythonProject/data/scans_per_center_per_month.csv")
    geocoder = csv_to_dict("/Users/elizabethschwartz/Documents/fall_2022/pythonProject/data/geocoder.csv")
    center_report = makes_centers_report(geocoder)
    for this_center_count in these_centers_counts:
        for this_center_report in center_report:
            if this_center_count['name'] == this_center_report['name']:
                this_center_report['total_scans'] += int(this_center_count['count'])
                this_center_report['months'] += 1
                if int(get_date(this_center_count['date'])[0]) <= int(get_date(this_center_report['start_date'])[0]):
                    if int(get_date(this_center_count['date'])[1]) <= int(get_date(this_center_report['start_date'])[1]):
                        this_center_report['start_date'] = this_center_count['date']
                    else: pass
                elif int(get_date(this_center_count['date'])[0]) >= int(get_date(this_center_report['end_date'])[0]):
                    if int(get_date(this_center_count['date'])[1]) >= int(get_date(this_center_report['end_date'])[1]):
                        this_center_report['end_date'] = this_center_count['date']
                    else: pass
                else: pass
    print(center_report)
    makes_results_csv(center_report, 'total_scans_per_center.csv')



def makes_results_csv(records, outfile_name):
    headers = records[0].keys()
    rows = records

    with open(outfile_name, 'w', encoding='UTF-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            try:
                writer.writerow(row)
            except AttributeError:
                pass

def get_date(a_date):
    return a_date.split('-')


def makes_centers_report(geocoder):
    center_report = []
    for center in geocoder:
        center_report.append({'name': center['name'], 'alt_names': center['scan_center_ids'].split('||'), 'lat' :center['lat'], 'long': center['long'], 'total_scans': 0, 'start_date': '2023-12-00', 'end_date': '0000-00-00', 'months':0})
    return center_report


def csv_to_dict(csv_file_name):
    results = []
    with open(csv_file_name, 'r', newline='', encoding='utf-8') as infile:
        csvin = csv.reader(infile)
        headers = next(csvin)
        # Make headers str.lower
        headers = [header.strip().lower() for header in headers]
        # Save dictionary of header:value for each row of data
        for row in csvin:
            n = 0
            your_dict = {}
            for column in row:
                your_dict[headers[n]] = column
                n += 1
            results.append(your_dict)
    return results


scan_center_stats()
