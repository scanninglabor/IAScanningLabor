# creates a csv file for scans per center per year to be uploaded to keplergl
import calendar
def main():
    records_to_map = []
    centers_per_month_file = input('input absolute path to the centers_per_month csv file: ')
    centers_per_month = csv_to_dict(centers_per_month_file)
    locations_file = input('input absolute path to locations csv file: ')
    geocoder = makes_geocoder(locations_file)
    for item in centers_per_month:
        map_dicts = create_records(item, geocoder)
        for entry in map_dicts:
                records_to_map.append(entry)
    makes_results_csv(records_to_map, 'scans_center_per_month.csv')


def create_records(count, geocoder):
    records = []
    the_year = count['year']
    the_month = count['month']
    for center in count.keys():
        if center == 'year' or center == 'month':
            pass
        else:
            try:
                geocoded = geocodes_centers(center, geocoder)
                if count[center] == '0':
                    pass
                else:
                    records.append(
                        {'name':geocoded['name'],
                         'lat': geocoded['lat'],
                         'long': geocoded['long'],
                         'count': count[center],
                         'date': formats_date(the_year, the_month),
                         'certainty_index' : geocoded['certainty_index']
                         }
                    )
            except TypeError:
                 pass
    return records


def geocodes_centers(scan_center, the_geocoder):
    for location in the_geocoder:
        if scan_center == location['name'].lower():
            return {'lat': location['lat'], 'long': location['long'], 'name': location['name'], 'certainty_index': location['certainty_index']}
        else:
            pass

def makes_geocoder(locations_file):
    locations = csv_to_dict(locations_file)
    print(locations)
    geocoder = []
    for location in locations:
        location['scan_center_ids'] = location['scan_center_ids'].split(' || ')
        try:
            location['lat'] = float(location['lat'].replace(',', ''))
            location['long'] = float(location['long'].replace(',', ''))
            geocoder.append(location)
        except ValueError:
            pass

    return geocoder


def make_records(this_center_per_year, year, month, the_geocoder):
    the_date = formats_date(year, month)
    print(the_date)
    the_records = []
    the_keys = this_center_per_year.keys()
    for this_key in the_keys:
        if this_key == "year" or this_key == "month":
            pass
        else:
            if this_center_per_year[this_key] != '':
                center = geocodes_centers(this_key, the_geocoder)
                print(center)
                if center != None:
                    the_records.append({'scanning_center': this_key,
                                        'name' : center['name'],
                                        'book_count': (this_center_per_year[this_key]),
                                        'date': the_date,
                                        'lat': center['lat'],
                                        'long': center['long']})
                else:

                     pass
    print(the_records)
    return the_records


def formats_date(year, month):
    year = str(year).split('.')[0]
    month = str(month).split('.')[0]
    if len(month) == 1:
        month = '0' + month
    day = calendar.monthrange(int(year), int(month))[1]
    the_date = year + '-' + month + '-' + str(day) + ' 00:00:00'
    return the_date

def get_scan_years(records):
    for record in records:
        record['scan_date'] = record['scan_date'].split('-')[0]
    scan_years = []
    for record in records:
        if record['scan_date'] not in scan_years:
            scan_years.append(record['scan_date'])
        else:
            pass
    scans_by_years = []
    for this_year in scan_years:
        scans = []
        for record in records:
            if record['scan_date'] == this_year:
                scans.append(record)
            else: pass
        scans_by_years.append({"year": this_year, "records": scans})

    return scans_by_years


def get_scans_by_center(records):
    centers = []
    for record in records:
        if record['scanning_center'] not in centers:
            centers.append(record['scanning_center'])
        else:
            pass
    scans_by_centers = []
    for this_center in centers:
        the_records = []
        for record in records:
            if record['scanning_center'] == this_center:
                the_records.append(record)
            else: pass
        scans_by_centers.append({"center": this_center, "records": the_records})

    return scans_by_centers

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




main()
