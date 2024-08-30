from typing import Dict, List

hardcoded_data: dict[str, list[str] | list[float]] = {
    'Account_Number': [
        'ACC00001', 'ACC00002', 'ACC00003', 'ACC00004', 'ACC00005',
        'ACC00006', 'ACC00007', 'ACC00008', 'ACC00009', 'ACC00010'
    ],
    'Account_Holder': [
        'John', 'Jane Smith', 'Alice Johnson', 'Robert Brown', 'Emily Davis',
        'Michael Wilson', 'Mary Clark', 'David Martinez', 'Linda Rodriguez', 'James Lewis'
    ],
    'Balance': [
        5023.45, 6345.32, 7534.23, 1290.54, 8453.34,
        2345.76, 9876.54, 1250.78, 6745.12, 4589.67
    ],
    'Account_Type': [
        'Savings', 'Checking', 'Business', 'Savings', 'Checking',
        'Business', 'Savings', 'Checking', 'Business', 'Savings'
    ],
    'Last_Transaction_Date': [
        '2023-01-31', '2023-02-28', '2023-03-31', '2023-04-30', '2023-05-31',
        '2023-06-30', '2023-07-31', '2023-08-31', '2023-09-30', '2023-10-31'
    ]
}