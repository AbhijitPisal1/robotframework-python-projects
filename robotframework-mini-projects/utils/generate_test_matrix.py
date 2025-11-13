import xml.etree.ElementTree as ET
import csv
from datetime import datetime

# Parse Robot Framework output.xml
tree = ET.parse('output.xml')
root = tree.getroot()

# Create CSV
with open('test_matrix.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Feature', 'Test Case', 'Priority', 'Status', 'Execution Time'])

    for test in root.iter('test'):
        test_name = test.attrib.get('name')
        status = test.attrib.get('status')
        feature = None
        priority = None

        # Extract tags from the <tags> section
        for tag in test.iter('tag'):
            if 'Feature:' in tag.text:
                feature = tag.text.split(':')[1]
            elif 'Priority:' in tag.text:
                priority = tag.text.split(':')[1]

        # Extract start/end time (optional)
        starttime = test.attrib.get('starttime', '')
        endtime = test.attrib.get('endtime', '')
        exec_time = ''
        if starttime and endtime:
            try:
                start = datetime.strptime(starttime, "%Y%m%d %H:%M:%S.%f")
                end = datetime.strptime(endtime, "%Y%m%d %H:%M:%S.%f")
                exec_time = f"{(end - start).seconds}s"
            except:
                pass

        writer.writerow([feature, test_name, priority, status, exec_time])

print("Test Matrix updated: test_matrix.csv")
