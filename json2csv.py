import json
import csv
import sys

def process_json_to_csv(json_file_path, output_file_path='output.csv'):
    # Load the JSON data
    with open(json_file_path) as f:
        data = json.load(f)

    # Open the CSV file for writing
    with open(output_file_path, 'w', newline='') as f:
        writer = csv.writer(f)

        # Write the header row
        writer.writerow(['Division', 'Conference', 'Conference Alias', 'Team', 'Market'])

        # Iterate over the divisions
        for division in data['divisions']:
            division_name = division['name']

            # Iterate over the conferences in the division
            for conference in division['conferences']:
                conference_name = conference['name']
                conference_alias = conference['alias']

                # Check if the conference has any teams
                if 'teams' in conference:

                    # Iterate over the teams in the conference
                    for team in conference['teams']:
                        team_name = team['name']
                        team_market = team['market']

                        # Write the row to the CSV file
                        writer.writerow([division_name, conference_name, conference_alias, team_name, team_market])
                        
                else:
                    # If the conference has no teams, write a row with empty team and market fields
                    writer.writerow([division_name, conference_name, conference_alias, '', ''])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python json2csv.py <json_file_path> [output_file_path]")
        sys.exit(1)

    json_file_path = sys.argv[1]
    output_file_path = 'output.csv' if len(sys.argv) < 3 else sys.argv[2]

    process_json_to_csv(json_file_path, output_file_path)
